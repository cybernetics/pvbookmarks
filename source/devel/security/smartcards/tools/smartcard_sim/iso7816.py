#!/usr/bin/env python

#################################
# Python library to work on
# smartcard defined with ISO 7816
#
# Specially designed SIM and USIM class
# for ETSI / 3GPP cards
#
# needs pyscard from:
# http://pyscard.sourceforge.net/
#################################

# classic python modules
import os,re
from time import sleep

# smartcard python modules from pyscard
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnection import CardConnection
from smartcard.util import toHexString, toBytes
from smartcard.ATR import ATR
from smartcard.sw.SWExceptions import SWException
from smartcard.Exceptions import CardConnectionException


# generic functions
def byteToBit(byte):
    '''
    byteToBit(0xAB) -> [1, 0, 1, 0, 1, 0, 1, 1]

    convert a byte integer value into a list of bits
    '''
    bit = [0,0,0,0,0,0,0,0]
    for i in range(8):
        if byte % pow(2,i+1):
            bit[7-i] = 1
            byte = byte - pow(2,i)
    return bit

def stringToByte(s):
    '''
    strinToByte('test') -> [116, 101, 115, 116]
    convert a string into a list of bytes
    '''
    bytes = []
    for c in s:
        bytes.extend( toBytes(c.encode('hex')) )
    return bytes

def byteToString(bytelist):
    '''
    strinToByte([116, 101, 115, 116]) -> 'test')
    convert a list of bytes into a string
    '''
    string = ''
    for b in bytelist:
        string += chr(b)
    return string

def LV_parser(bytes):
    '''
    LV_parser([0x02, 0xAB, 0xCD, 0x01, 0x12, 0x34]) -> [[171, 205], [18], []]

    parse Length-Value records in a bytes list
    return a list of list of bytes

    length coded on 1 byte
    '''
    values = []
    while len(bytes) > 0:
        l = bytes[0]
        values.append( bytes[1:1+l] )
        bytes = bytes[1+l:]
    return values

def first_TLV_parser(bytes):
    '''
    first_TLV_parser([0xAA, 0x02, 0xAB, 0xCD, 0xFF, 0x00]) -> (170, 2, [171, 205])

    parse first TLV format record in a list of bytes
    return a 3-Tuple: Tag, Length, Value
    Value is a list of bytes

    parsing of length is ETSI'style 101.220
    '''
    Tag = bytes[0]
    if bytes[1] == 0xFF:
        Len = bytes[2]*256 + bytes[3]
        Val = bytes[4:4+Len]
    else:
        Len = bytes[1]
        Val = bytes[2:2+Len]
    return (Tag, Len, Val)

def first_BERTLV_parser(bytes):
    '''
    first_BERTLV_parser([0xAA, 0x02, 0xAB, 0xCD, 0xFF, 0x00]) -> ([1, 'contextual', 'constructed', 10], [1, 2], [2, [171, 205]])

    parse first BER-TLV format record in a list of bytes
    return a 3-Tuple: Tag, Length, Value
        Tag: [Tag length, Tag class, Tag DO, Tag number]
        Length: [Length length, Length value]
        Value: [Value Length, Value bytes list]

    parsing of length is ETSI'style 101.220
    '''
    # Tag class and DO
    byte0 = byteToBit(bytes[0])
    if byte0[0:2] == [0,0]:
        Tag_class = 'universal'
    elif byte0[0:2] == [0,1]:
        Tag_class = 'applicative'
    elif byte0[0:2] == [1,0]:
        Tag_class = 'contextual'
    elif byte0[0:2] == [1,1]:
        Tag_class = 'private'
    if byte0[2:3] == [0]:
        Tag_DO = 'primitive'
    elif byte0[2:3] == [1]:
        Tag_DO = 'constructed'

    # Tag coded with more than 1 byte
    i = 0
    if byte0[3:8] == [1,1,1,1,1]:
        Tag_bits = byteToBit(bytes[1])[1:8]
        i += 1
        while byteToBit(bytes[i])[0] == 1:
            i += 1
            Tag_bits += byteToBit(bytes[i])[1:8]

    # Tag coded with 1 byte
    else:
        Tag_bits = byte0[3:8]

    # Tag number calculation
    Tag_num = 0
    for j in range(len(Tag_bits)):
        Tag_num += Tag_bits[len(Tag_bits)-j-1]*pow(2,j)

    # Length coded with more than 1 byte
    if bytes[i+1] > 0x50:
        Len_num = bytes[i+1] - 0x50
        Len_bytes = bytes[i+2:i+1+Len_num]
        Len = 0
        for j in range(len(Len_bytes)):
            Len += bytes[i+1+Len_num-j]*pow(256,j)
        Val = bytes[i+1+Len_num:i+1+Len_num+Len]

    # Length coded with 1 byte
    else:
        Len_num = 1
        Len = bytes[i+1]
        Val = bytes[i+2:i+2+Len]

    return ([i+1, Tag_class, Tag_DO, Tag_num],[Len_num, Len],[len(Val), Val])


##################################################################################################
# ISO7816 class with attributes and methods as defined by ISO-7816 part 4 standard for smartcard #
##################################################################################################

class ISO7816:
    '''
    define attributes, methods and facilities for ISO-7816-4 standard smartcard

    use self.dbg = 1 or more to print live debugging information
    '''

    dbg = 0

    def __init__(self, CLA=0x00):
        '''
        smartcard connection initialization and class CLA code definition

        use "pyscard" library services
        '''
        cardtype = AnyCardType()
        cardrequest = CardRequest(timeout=1, cardType=cardtype)
        self.cardservice = cardrequest.waitforcard()
        self.cardservice.connection.connect()
        self.reader = self.cardservice.connection.getReader()
        self.ATR = self.cardservice.connection.getATR()

        self.CLA = CLA
        self.INS_dic = {0xA4 : 'SELECT FILE',\
                        0xF2 : 'STATUS',\
                        0xB0 : 'READ BINARY',\
                        0xD6 : 'UPDATE BINARY',\
                        0xB2 : 'READ RECORD',\
                        0xDC : 'UPDATE RECORD',\
                        0xA2 : 'SEARCH RECORD',\
                        0x32 : 'INCREASE',\
                        0xCB : 'RETRIEVE DATA',\
                        0xDB : 'SET DATA',\
                        0x20 : 'VERIFY',\
                        0x24 : 'CHANGE PIN',\
                        0x26 : 'DISABLE PIN',\
                        0x28 : 'ENABLE PIN',\
                        0x2C : 'UNBLOCK PIN',\
                        0x04 : 'DEACTIVATE FILE',\
                        0x44 : 'ACTIVATE FILE',\
                        0x88 : 'AUTHENTICATE',\
                        0x89 : 'AUTHENTICATE',\
                        0x84 : 'GET CHALLENGE',\
                        0xAA : 'TERMINAL CAPABILITY',\
                        0x10 : 'TERMINAL PROFILE',\
                        0xC2 : 'ENVELOPE',\
                        0x12 : 'FETCH',\
                        0x14 : 'TERMINAL RESPONSE',\
                        0x70 : 'MANAGE CHANNEL',\
                        0x73 : 'MANAGE SECURE CHANNEL',\
                        0x75 : 'TRANSACT DATA',\
                        0xC0 : 'GET RESPONSE'}

    def disconnect(self):
        '''
        disconnect smartcard: stops the session
        '''
        self.cardservice.connection.disconnect()

    def define_class(self, CLA=0x00):
        '''
        define smartcard class attribute for APDU command
        override CLA value defined in class initialization
        '''
        self.CLA = CLA

    def ATR_scan(self, smlist_file='/usr/share/pcsc/smartcard_list.txt'):
        '''
        print smartcard info retrieved from AnswerToReset

        if pcsc_scan is installed,
        use the signature file for guessing the card
        '''
        print '\nsmartcard reader: ', self.reader
        if self.ATR != None:
            print "\nsmart card ATR is: %s" % toHexString(self.ATR)
            print 'ATR analysis: '
            print ATR(self.ATR).dump()
            print '\nhistorical bytes: ', toHexString(ATR(self.ATR).getHistoricalBytes())
            ATRcs = ATR(self.ATR).getChecksum()
            if ATRcs :
                print 'checksum: ', "0x%X" % ATRcs
            else:
                print 'no ATR checksum'
            print "\nusing pcsc_scan ATR list file: %s" % smlist_file
            if os.path.exists(smlist_file):
                smlist = open(smlist_file).readlines()
                ATRre = re.compile('(^3[BF]){1}.{1,}$')
                ATRfinger = ''
                j = 1
                for i in range(len(smlist)):
                    if ATRre.match(smlist[i]):
                        if re.compile(smlist[i][:len(smlist[i])-1]).match(toHexString(self.ATR)):
                            while re.compile('\t.{1,}').match(smlist[i+j]):
                                ATRfinger += smlist[i+j][1:]
                                j += j
                if ATRfinger == '' :
                    print "no ATR fingerprint found in file: %s" % smlist_file
                else:
                    print "smartcard ATR fingerprint:\n%s" % ATRfinger
            else:
                print "%s file not found" % smlist_file

    def sw_status(self, sw1, sw2):
        '''
        self.sw_status(sw1=int, sw2=int) -> string

        SW status bytes interpretation as defined in ISO-7816 part 4 standard
        helps to speak with the smartcard!
        '''
        status = 'undefined status'
        if sw1 == 0x90 and sw2 == 0x00: status = 'normal processing: command accepted: no further qualification'
        elif sw1 == 0x61: status = 'normal processing: %i bytes still available' % sw2
        elif sw1 == 0x62:
            status = 'warning processing: state of non-volatile memory unchanged'
            if sw2 == 0x00: status += ': no information given'
            elif sw2 == 0x81: status += ': part of returned data may be corrupted'
            elif sw2 == 0x82: status += ': end of file/record reached before reading Le bytes'
            elif sw2 == 0x83: status += ': selected file invalidated'
            elif sw2 == 0x84: status += ': FCI not formatted'
            else: status += ': undefined SW2 code: 0x%s' % toHexString([sw2])
        elif sw1 == 0x63:
            status = 'warning processing: state of non-volatile memory changed'
            if sw2 == 0x00: status += ': no information given'
            elif sw2 == 0x81:status += ': file filled up by the last write'
            elif 0xC0 <= sw2 <= 0xCF: status += ': counter provided by %s' % toHexString([sw2])[1]
            else: status += ': undefined SW2 code: 0x%s' % toHexString([sw2])
        elif sw1 == 0x64:
            status = 'execution error: state of non-volatile memory unchanged'
            if sw2 != 0x00:  status += ': SW2 code 0x%s is RFU' % toHexString([sw2])
        elif sw1 == 0x65:
            status = 'execution error: state of non-volatile memory changed'
            if sw2 == 0x00: status += ': no information given'
            elif sw2 == 0x81: status += ': memory failure'
            else: status += ': undefined SW2 code: 0x%s' % toHexString([sw2])
        elif sw1 == 0x66: status = 'execution error: reserved for security-related issues'
        elif sw1 == 0x67 and sw2 == 0x00: status = 'checking error: wrong length (P3 parameter)'
        elif sw1 == 0x68:
            status = 'checking error: functions in CLA not supported'
            if sw2 == 0x00: status += ': no information given'
            elif sw2 == 0x81: status += ': logical channel not supported'
            elif sw2 == 0x82: status += ': secure messaging not supported'
            else: status += ': undefined SW2 code: 0x%s' % toHexString([sw2])
        elif sw1 == 0x69:
            status = 'checking error: command not allowed'
            if sw2 == 0x00: status += ': no information given'
            elif sw2 == 0x81: status += ': command incompatible with file structure'
            elif sw2 == 0x82: status += ': security status not satisfied'
            elif sw2 == 0x83: status += ': authentication method blocked'
            elif sw2 == 0x84: status += ': referenced data invalidated'
            elif sw2 == 0x85: status += ': conditions of use not satisfied'
            elif sw2 == 0x86: status += ': command not allowed (no current EF)'
            elif sw2 == 0x87: status += ': expected SM data objects missing'
            elif sw2 == 0x88: status += ': SM data objects incorrect'
            else: status += ': undefined SW2 code: 0x%s' % toHexString([sw2])
        elif sw1 == 0x6A:
            status = 'checking error: wrong parameter(s) P1-P2'
            if sw2 == 0x00: status += ': no information given'
            if sw2 == 0x80: status += ': incorrect parameters in the data field'
            if sw2 == 0x81: status += ': function not supported'
            if sw2 == 0x82: status += ': file not found'
            if sw2 == 0x83: status += ': record not found'
            if sw2 == 0x84: status += ': not enough memory space in the file'
            if sw2 == 0x85: status += ': Lc inconsistent with TLV structure'
            if sw2 == 0x86: status += ': incorrect parameters P1-P2'
            if sw2 == 0x87: status += ': Lc inconsistent with P1-P2'
            if sw2 == 0x88: status += ': referenced data not found'
            else: status += ': undefined SW2 code: 0x%s' % toHexString([sw2])
        elif sw1 == 0x6B and sw2 == 0x00: status = 'checking error: wrong parameter(s) P1-P2'
        elif sw1 == 0x6C: status = 'checking error: wrong length Le: exact length is %s' % toHexString([sw2])
        elif sw1 == 0x6D and sw2 == 0x00: status = 'checking error: instruction code not supported or invalid'
        elif sw1 == 0x6E and sw2 == 0x00: status = 'checking error: class not supported'
        elif sw1 == 0x6F and sw2 == 0x00: status = 'checking error: no precise diagnosis'
        return status

    def sr_apdu(self, apdu):
        '''
        self.sr_apdu(apdu=[0x.., 0x.., ...]) ->
            4-Tuple( string(apdu sent information),
                     string(SW codes interpretation),
                     2-tuple(sw1, sw2),
                     list(response bytes) )

        generic function to send apdu, receive and interpret response

        force card reconnection if pyscard transmission fails
        '''
        try: data, sw1, sw2 = self.cardservice.connection.transmit(apdu)
        except CardConnectionException:
            ISO7816.__init__(self, CLA = self.CLA)
            data, sw1, sw2 = self.cardservice.connection.transmit(apdu)
        if apdu[1] in self.INS_dic.keys(): apdu_name =  self.INS_dic[apdu[1]] + ' '
        else: apdu_name = ''
        sw_stat = self.sw_status(sw1,sw2)
        return ['%sapdu: %s' % (apdu_name, toHexString(apdu)), \
                'sw1, sw2: %s - %s' % ( toHexString([sw1, sw2]), sw_stat ), \
                (sw1, sw2), \
                data ]

    def bf_cla(self, start=0, param=[0xA4, 0x00, 0x00, 0x02, 0x3F, 0x00]):
        '''
        self.bf_cla( start=int(starting CLA), param=list(bytes for selecting file 0x3F, 0x00) ) ->
            list( CLA which could be supported )

        try all classes CLA codes to check the supported ones
        print CLA suspected to be supported

        WARNING: can block the card definitively
        Do not do it with your own VISA card
        '''
        list = []
        for i in range(start, 256):
            ret = self.sr_apdu([i] + param)
            if ret[2] != (0x6E, 0x00):
                print ret
                list.append(i)
        return list

    def bf_ins(self, start=0):
        '''
        self.bf_cla( start=int(starting INS) ) -> list( INS which could be supported )

        try all instructions INS codes to check the supported ones
        print INS suspected to be supported

        WARNING: can block the card definitively
        Do not do it with your own VISA card
        '''
        list = []
        for i in range(start, 256):
            print 'DEBUG: testing %d for INS code with %d CLA code' % (i, self.CLA)
            ret = self.sr_apdu([self.CLA, i, 0x00, 0x00])
            if ret[2] != (0x6D, 0x00):
                print ret
                list.append(i)
        return list

    def READ_BINARY(self, P1=0x00, P2=0x00, Le=0x01):
        '''
        APDU command to read the content of EF file with transparent structure
        Le: length of data bytes to be read

        call sr_apdu method
        '''
        READ_BINARY = [self.CLA, 0xB0, P1, P2, Le]
        return self.sr_apdu(READ_BINARY)

    def WRITE_BINARY(self, P1=0x00, P2=0x00, Data=[]):
        '''
        APDU command to write the content of EF file with transparent structure

        Data: list of data bytes to be written
        call sr_apdu method
        '''
        WRITE_BINARY = [self.CLA, 0xD0, P1, P2, len(Data)] + Data
        return self.sr_apdu(WRITE_BINARY)

    def UPDATE_BINARY(self, P1=0x00, P2=0x00, Data=[]):
        '''
        APDU command to update the content of EF file with transparent structure

        Data: list of data bytes to be written
        call sr_apdu method
        '''
        UPDATE_BINARY = [self.CLA, 0xD6, P1, P2, len(Data)] + Data
        return self.sr_apdu(UPDATE_BINARY)

    def ERASE_BINARY(self, P1=0x00, P2=0x00, Lc=None, Data=[]):
        '''
        APDU command to erase the content of EF file with transparent structure

        Lc: 'None' or '0x02'
        Data: list of data bytes to be written
        call sr_apdu method
        '''
        if Lc is None: ERASE_BINARY = [self.CLA, 0x0E, P1, P2]
        else: ERASE_BINARY = [self.CLA, 0x0E, P1, P2, 0x02] + Data
        return self.sr_apdu(ERASE_BINARY)

    def READ_RECORD(self, P1=0x00, P2=0x00, Le=0x00):
        '''
        APDU command to read the content of EF file with record structure

        P1: record number
        P2: reference control
        Le: length of data bytes to be read
        call sr_apdu method
        '''
        READ_RECORD = [self.CLA, 0xB2, P1, P2, Le]
        return self.sr_apdu(READ_RECORD)

    def WRITE_RECORD(self, P1=0x00, P2=0x00, Data=[]):
        '''
        APDU command to write the content of EF file with record structure

        P1: record number
        P2: reference control
        Data: list of data bytes to be written in the record
        call sr_apdu method
        '''
        WRITE_RECORD = [self.CLA, 0xD2, P1, P2, len(Data)] + Data
        return self.sr_apdu(WRITE_RECORD)

    def APPEND_RECORD(self, P2=0x00, Data=[]):
        '''
        APDU command to append a record on EF file with record structure

        P2: reference control
        Data: list of data bytes to be appended on the record
        call sr_apdu method
        '''
        APPEND_RECORD = [self.CLA, 0xE2, 0x00, P2, len(Data)] + Data
        return self.sr_apdu(APPEND_RECORD)

    def UPDATE_RECORD(self, P1=0x00, P2=0x00, Data=[]):
        '''
        APDU command to update the content of EF file with record structure

        P1: record number
        P2: reference control
        Data: list of data bytes to update the record
        call sr_apdu method
        '''
        APPEND_RECORD = [self.CLA, 0xDC, P1, P2, len(Data)] + Data
        return self.sr_apdu(APPEND_RECORD)

    def GET_DATA(self, P1=0x00, P2=0x00, Le=0x01):
        '''
        APDU command to retrieve data object

        P1 and P2: reference control for data object description
        Le: number of bytes expected in the response
        call sr_apdu method
        '''
        GET_DATA = [self.CLA, 0xCA, P1, P2, Le]
        return self.sr_apdu(GET_DATA)

    def PUT_DATA(self, P1=0x00, P2=0x00, Data=[]):
        '''
        APDU command to store data object

        P1 and P2: reference control for data object description
        Data: list of data bytes to put in the data object structure
        call sr_apdu method
        '''
        if len(Data) == 0: PUT_DATA = [self.CLA, 0xDA, P1, P2]
        elif 1 <= len(Data) <= 255: PUT_DATA = [self.CLA, 0xDA, P1, P2, len(Data)] + Data
        else: PUT_DATA = [self.CLA, 0xDA, P1, P2, 0xFF] + Data[0:255]
        return self.sr_apdu(PUT_DATA)

    def SELECT_FILE(self, P1=0x00, P2=0x00, Data=[0x3F, 0x00]):
        '''
        APDU command to select file

        P1 and P2: selection control
        Data: list of bytes describing the file identifier or address
        call sr_apdu method
        '''
        if len(Data) == 0: SELECT_FILE = [self.CLA, 0xA4, P1, P2]
        elif 1 <= len(Data) <= 255: SELECT_FILE = [self.CLA, 0xA4, P1, P2, len(Data)] + Data
        else: SELECT_FILE = [self.CLA, 0xA4, P1, P2, 0xFF] + Data[0:255]
        return self.sr_apdu(SELECT_FILE)

    def VERIFY(self, P2=0x00, Data=[]):
        '''
        APDU command to verify user PIN, password or security codes

        P2: reference control
        Data: list of bytes to be verified by the card
        call sr_apdu method
        '''
        if len(Data) == 0: VERIFY = [self.CLA, 0x20, 0x00, P2]
        elif 1 <= len(Data) <= 255: VERIFY = [self.CLA, 0x20, 0x00, P2, len(Data)] + Data
        else: VERIFY = [self.CLA, 0x20, 0x00, P2, 0xFF] + Data[0:255]
        return self.sr_apdu(VERIFY)

    def INTERNAL_AUTHENTICATE(self, P1=0x00, P2=0x00, Data=[]):
        '''
        APDU command to run internal authentication algorithm

        P1 and P2: reference control (algo, secret key selection...)
        Data: list of bytes containing the authentication challenge
        call sr_apdu method
        '''
        INTERNAL_AUTHENTICATE = [self.CLA, 0x88, P1, P2, len(Data)] + Data
        return self.sr_apdu(INTERNAL_AUTHENTICATE)

    def EXTERNAL_AUTHENTICATE(self, P1=0x00, P2=0x00, Data=[]):
        '''
        APDU command to conditionally update the security status of the card after getting a challenge from it

        P1 and P2: reference control (algo, secret key selection...)
        Data: list of bytes containing the challenge response
        call sr_apdu method
        '''
        if len(Data) == 0: EXTERNAL_AUTHENTICATE = [self.CLA, 0x82, P1, P2]
        elif 1 <= len(Data) <= 255: EXTERNAL_AUTHENTICATE = [self.CLA, 0x82, P1, P2, len(Data)] + Data
        else: EXTERNAL_AUTHENTICATE = [self.CLA, 0x82, P1, P2, 0xFF] + Data[0:255]
        return self.sr_apdu(INTERNAL_AUTHENTICATE)

    def GET_CHALLENGE(self):
        '''
        APDU command to get a challenge for external entity authentication to the card

        call sr_apdu method
        '''
        GET_CHALLENGE = [self.CLA, 0x84, 0x00, 0x00]
        return self.sr_apdu(GET_CHALLENGE)

    def MANAGE_CHANNEL(self, P1=0x00, P2=0x00):
        '''
        APDU to open and close supplementary logical channels

        P1=0x00 to open, 0x80 to close
        P2=0x00, 1, 2 or 3 to ask for logical channel number
        call sr_apdu method
        '''
        if (P1, P2) == (0x00, 0x00): MANAGE_CHANNEL = [self.CLA, 0x70, P1, P2, 0x01]
        else:  MANAGE_CHANNEL = [self.CLA, 0x70, P1, P2]
        return self.sr_apdu(MANAGE_CHANNEL)

    def GET_RESPONSE(self, Le=0x01):
        '''
        APDU command to retrieve data after selection or other kind of request that should get an extensive reply

        Le: expected length of data
        call sr_apdu method
        '''
        GET_RESPONSE = [self.CLA, 0xC0, 0x00, 0x00, Le]
        return self.sr_apdu(GET_RESPONSE)

    def ENVELOPPE(self, Data=[]):
        '''
        APDU command to encapsulate data (APDU or other...)
        check ETSI TS 102.221 for some examples...

        Data: list of bytes
        call sr_apdu method
        '''
        if len(Data) == 0: ENVELOPPE = [self.CLA, 0xC2, 0x00, 0x00]
        elif 1 <= len(Data) <= 255: ENVELOPPE = [self.CLA, 0xC2, 0x00, 0x00, len(Data)] + Data
        return self.sr_apdu(ENVELOPPE)

    def SEARCH_RECORD(self, P1=0x00, P2=0x00, Data=[]):
        '''
        APDU command to seach pattern in the current EF file with record structure

        P1: record number
        P2: type of search
        Data: list of bytes describing a pattern to search for
        call sr_apdu method
        '''
        SEARCH_RECORD = [self.CLA, 0xA2, P1, P2, len(Data)] + Data
        return self.sr_apdu(SEARCH_RECORD)

    def DISABLE_CHV(self, P1=0x00, P2=0x00, Data=[]):
        '''
        APDU command to disable CHV verification (such as PIN or password...)

        P1: let to 0x00... or read ISO and ETSI specifications
        P2: type of CHV to disable
        Data: list of bytes for CHV value
        call sr_apdu method
        '''
        DISABLE_CHV = [self.CLA, 0x26, P1, P2, len(Data)] + Data
        return self.sr_apdu(DISABLE_CHV)

    def UNBLOCK_CHV(self, P2=0x00, Lc=None, Data=[]):
        '''
        APDU command to unblock CHV code (e.g. with PUK for deblocking PIN)

        P2: type of CHV to unblock
        Lc: Empty or 0x10
        Data: if Lc=0x10, UNBLOCK_CHV value and new CHV value to set
        call sr_apdu method
        '''
        if Lc is None: UNBLOCK_CHV = [self.CLA, 0x2C, 0x00, P2]
        else: UNBLOCK_CHV = [self.CLA, 0x2C, 0x00, P2, 0x10] + Data
        return self.sr_apdu(UNBLOCK_CHV)


class SIM(ISO7816):
    '''
    define attributes, methods and facilities for ETSI / 3GPP SIM card
    check SIM specifications in ETSI TS 102.221 and 3GPP TS 51.011

    inherit methods and objects from ISO7816 class
    use self.dbg = 1 or more to print live debugging information
    '''

    def __init__(self, type='SIM'):
        '''
        initialize like an ISO7816-4 card with CLA=0xA0

        can also be used for USIM working in SIM mode, with <type='USIM'>
        e.g. when you put your new USIM in your old 2G handset
        '''
        if type == 'USIM':
            ISO7816.__init__(self, CLA=0x00)
            self.type = 'USIM'
            self.AID = None
        else:
            ISO7816.__init__(self, CLA=0xA0)
            self.type = 'SIM'
        if self.dbg:
            print '[DBG] type definition: %s' % self.type
            print '[DBG] CLA definition: %s' % hex(self.CLA)

    def sw_status(self, sw1, sw2):
        '''
        self.sw_status(sw1=int, sw2=int) -> string

        extends SW status bytes interpretation from ISO7816 with ETSI / 3GPP SW codes
        helps to speak with the smartcard!
        '''
        status = ISO7816.sw_status(self, sw1, sw2)
        if sw1 == 0x91: status = 'normal processing, with extra info containing a command for the terminal: length of the response data %d' % sw2
        elif sw1 == 0x9E: status = 'normal processing, SIM data download error: length of the response data %d' % sw2
        elif sw1 == 0x9F: status = 'normal processing: length of the response data %d' % sw2
        elif (sw1, sw2) == (0x93, 0x00): status = 'SIM application toolkit busy, command cannot be executed at present'
        elif sw1 == 0x92 :
            status = 'memory management'
            if sw2 < 16: status += ': command successful but after %d retry routine' % sw2
            elif sw2 == 0x40: status += ': memory problem'
        elif sw1 == 0x94:
            status = 'referencing management'
            if sw2 == 0x00: status += ': no EF selected'
            elif sw2 == 0x02: status += ': out of range (invalid address)'
            elif sw2 == 0x04: status += ': file ID or pattern not found'
            elif sw2 == 0x08: status += ': file inconsistent with the command'
        elif sw1 == 0x98:
            status = 'security management'
            if sw2 == 0x02: status += ': no CHV initialized'
            elif sw2 == 0x04: status += ': access condition not fulfilled, at least 1 attempt left'
            elif sw2 == 0x08: status += ': in contradiction with CHV status'
            elif sw2 == 0x10: status += ': in contradiction with invalidation status'
            elif sw2 == 0x40: status += ': unsuccessful CHV verification, no attempt left'
            elif sw2 == 0x50: status += ': increase cannot be performed, max value reached'
            elif sw2 == 0x62: status += ': authentication error, application specific'
            elif sw2 == 0x63: status += ': security session expired'
        return status

    def verify_pin(self, pin_type=1, pin=''):
        '''
        verify CHV1 (PIN code) or CHV2 with VERIFY APDU command

        call VERIFY method
        '''
        if pin_type in [1,2] and type(pin) is str and len(pin) == 4 and 0 <= int(pin) < 10000:
            PIN = [0x30+int(pin[0]), 0x30+int(pin[1]), 0x30+int(pin[2]), 0x30+int(pin[3]), 0xFF, 0xFF, 0xFF, 0xFF]
            return self.VERIFY(P2=pin_type, Data=PIN)
        else: return self.VERIFY()

    def disable_pin(self, pin_type=1, pin=''):
        '''
        disable CHV1 (PIN code) or CHV2 with DISABLE_CHV APDU command
        tip: do it as soon as you can when you are working with a SIM / USIM card for which youu know the PIN!

        call DISABLE method
        '''
        if pin_type in [1,2] and type(pin) is str and len(pin) == 4 and 0 <= int(pin) < 10000:
            PIN = [0x30+int(pin[0]), 0x30+int(pin[1]), 0x30+int(pin[2]), 0x30+int(pin[3]), 0xFF, 0xFF, 0xFF, 0xFF]
            return self.DISABLE_CHV(P2=pin_type, Data=PIN)
        else: return self.DISABLE()

    def unblock_pin(self, pin_type=1, unblock_pin=''):
        '''
        unblock CHV1 (PIN code) or CHV2 with UNBLOCK_CHV APDU command and set 0000 value for new PIN

        call UNBLOCK_CHV method
        '''
        if pin_type == 1: pin_type = 0
        if pin_type in [0,2] and type(unblock_pin) is str and len(unblock_pin) == 4 and 0 <= int(unblock_pin) < 10000:
            UNBL_PIN = [0x30+int(unblock_pin[0]), 0x30+int(unblock_pin[1]), 0x30+int(unblock_pin[2]), 0x30+int(unblock_pin[3]), 0xFF, 0xFF, 0xFF, 0xFF]
            return self.UNBLOCK_CHV(P2=pin_type, Lc=0x10, Data=PIN + [0x30, 0x30, 0x30, 0x30, 0xFF, 0xFF, 0xFF, 0xFF])
        else: return self.UNBLOCK_CHV(P2=pin_type)

    def parse_file_SIM(self, Data=[]):
        '''
        parse_file_SIM(Data=[0x12, 0x34, 0x56, 0x89]) -> dict(file)

        parse a list of bytes returned when selecting a file
        interpret the content of some informative bytes for right accesses, type / format of file...
        work over the SIM file structure
        '''
        file = {}
        file['size'] = Data[2]*0xFF00 + Data[3]
        file['ID'] = Data[4:6]
        file['type'] = ('RFU', 'MF', 'DF', '', 'EF')[Data[6]]
        file['length'] = Data[12]
        if file['type'] == 'MF' or file['type'] == 'DF':
            file['DF_num'] = Data[14]
            file['EF_num'] = Data[15]
            file['codes_num'] = Data[16]
            file['CHV1'] = ('not initialized','initialized')[(Data[18] & 0x80) / 0x80]\
                         + ': %d attempts remain' % (Data[18] & 0x0F)
            file['unblock_CHV1'] = ('not initialized','initialized')[(Data[19] & 0x80) / 0x80]\
                                 + ': %d attempts remain' % (Data[19] & 0x0F)
            file['CHV2'] = ('not initialized','initialized')[(Data[20] & 0x80) / 0x80]\
                         + ': %d attempts remain' % (Data[20] & 0x0F)
            file['unblock_CHV2'] = ('not initialized','initialized')[(Data[21] & 0x80) / 0x80]\
                                 + ': %d attempts remain' % (Data[21] & 0x0F)
            if len(Data) > 23: file['adm'] = Data[23:]
        elif file['type'] == 'EF':
            cond = ('ALW','CHV1','CHV2','RFU','ADM_4','ADM_5','ADM_6','ADM_7','ADM_8','ADM_9','ADM_A','ADM_B','ADM_C','ADM_D','ADM_E','NEW')
            file['UPDATE'] = cond[Data[8] & 0x0F]
            file['READ'] = cond[Data[8] >> 4]
            file['INCREASE'] = cond[Data[9] >> 4]
            file['INVALIDATE'] = cond[Data[10] & 0x0F]
            file['REHABILITATE'] = cond[Data[10] >> 4]
            file['status'] = ('not read/updatable when invalidated', 'read/updatable when invalidated')[byteToBit(Data[11])[5]]\
                           + (': invalidated',': not invalidated')[byteToBit(Data[11])[7]]
            file['structure'] = ('transparent', 'linear fixed', '', 'cyclic')[Data[13]]
            if file['structure'] == 'cyclic': file['INCREASE'] = byteToBit(Data[7])[1]
            if len(Data) > 14: file['rec_length'] = Data[14]
        return file

    def parse_file_USIM(self, Data=[]):
        '''
        parse_file_USIM(Data=[0x12, 0x34, 0x56, 0x89]) -> dict(file)

        parse a list of bytes returned when selecting a file
        interpret the content of some informative bytes for right accesses, type / format of file...
        work over the USIM file structure (quite different from the SIM one)
        '''
        file = {}
        tags = {0x80 : 'size',\
                0x81 : 'length',\
                0x82 : 'fd',\
                0x83 : 'ID',\
                0x84 : 'AID',\
                0x88 : 'SFI',\
                0x8A : 'LCSI',\
                0x8B : 'SecAtt',\
                0x8C : 'SecAtt',\
                0xA5 : 'proprietary',\
                0xAB : 'SecAtt',\
                0xC6 : 'PIN_status'\
                }
        if Data[0] == 0x62:
            toProcess = Data[2:]
            assert( len(toProcess) == Data[1] )
            while len(toProcess) > 0:
                [T, L, V] = first_TLV_parser(toProcess)
                if T in tags.keys(): T = tags[T]
                file[T] = V
                toProcess = toProcess[L+2:]
            fd_byte = byteToBit(file['fd'][0])
            if fd_byte[0:1]+fd_byte[2:5] == [0,0,0,0]: file['type'] = 'EF working'
            elif fd_byte[0:1]+fd_byte[2:5] == [0,0,0,1]: file['type'] = 'EF internal'
            elif fd_byte[0:1]+fd_byte[2:8] == [0,1,1,1,0,0,1]: file['type'] = 'EF with BER-TLV'
            elif fd_byte[0:1]+fd_byte[2:8] == [0,1,1,1,0,0,0]: file['type'] = 'DF or ADF'
            else: file['type'] = 'RFU'
            if file['type'][0:2] == 'EF' :
                if fd_byte[5:8] == [0,0,0]: file['structure'] = 'no information'
                elif fd_byte[2:8] == [1,1,1,0,0,1]: file['structure'] = 'BER-TLV'
                elif fd_byte[5:8] == [0,0,1]: file['structure'] = 'transparent'
                elif fd_byte[5:8] == [0,1,0]: file['structure'] = 'linear fixed'
                elif fd_byte[5:8] == [1,1,0]: file['structure'] = 'cyclic'
                else: file['structure'] = 'RFU'
            else: file['type'] == 'RFU'
            if len(file['fd']) == 5: file['rec_length'],file['req_num'] = file['fd'][3],file['fd'][4]
            if 'size' in file.keys():
                #print 'DEBUG:', file['size']
                size = 0
                for i in range(len(file['size'])): size += file['size'][i] * pow(256,len(file['size'])-i-1)
                file['size'] = size
        if self.dbg: print '[DBG] file:\n', file
        return file

    def select(self, Data=[0x3F, 0x00]):
        '''
        self.select(Data=[0x.., 0x..]) -> dict(file) on success, None on error

        select the file
        if processing correct: get response with info on the file
        if processing correct and EF file: reads the data in the file
        works in SIM and USIM fashion

        if error, returns None
        else returns the data dictionnary: check parse_file_(U)SIM methods
        last apdu available from the attribute self.last_response
        '''

        # select file and check SW; if error, returns None, else get response
        if self.type == 'SIM':
            self.last_response = self.SELECT_FILE(Data=Data)
            type_res = 0x9F
        elif self.type == 'USIM':
            self.last_response = self.SELECT_FILE(P2=0x04, Data=Data)
            type_res = 0x61

        if self.last_response[2][0] != type_res:
            if self.dbg: print '[DBG] %s' % self.last_response
            return None

        # get response and check SW: if error, return None, else parse file info
        self.last_response = self.GET_RESPONSE(Le=self.last_response[2][1])
        if self.last_response[2] != (0x90, 0x00):
            if self.dbg: print '[DBG] %s' % self.last_response
            return None

        data = self.last_response[3]
        if self.type == 'SIM': file = self.parse_file_SIM(data)
        elif self.type == 'USIM': file = self.parse_file_USIM(data)

        if file['type'][0:2] == 'EF':
            # read EF transparent data
            if file['structure'] == 'transparent':
                self.last_response = self.READ_BINARY(Le=file['size'])
                if self.last_response[2] != (0x90, 0x00):
                    if self.dbg: print '[DBG] %s' % self.last_response
                    return None
                file['data'] = self.last_response[3]
            # read EF cyclic / linear all records data
            elif file['structure'] != 'transparent':
                file['data'] = []
                # for record data: need to check the number of recordings stored in the file, and iterate for each
                for i in range( (file['size'] / file['rec_length']) ):
                #for i in range( (file['size'] / file['rec_length']) + 1 ):
                    self.last_response = self.READ_RECORD(P1=i+1, P2=0x04, Le=file['rec_length'])
                    #self.last_response = self.READ_RECORD(P1=i, P2=0x04, Le=file['rec_length'])
                    if self.last_response[2] != (0x90, 0x00):
                        print '[WNG] error in iterating the RECORD parsing at iteration %s' % i
                        if self.dbg: print '[DBG] %s' % self.last_response
                    file['data'].append(self.last_response[3])

        # finally returns the whole file dictionnary, containing the ['data'] key for EF file
        return file


    def run_gsm_alg(self, RAND=16*[0x00]):
        '''
        self.run_gsm_alg( RAND ) -> ( SRES, Kc )
            RAND : list of bytes, length 16
            SRES : list of bytes, length 4
            Kc : list of bytes, length 8

        run GSM authentication algorithm: accepts any kind of RAND (old GSM fashion!)
        feed with RAND 16 bytes value
        return a 2-tuple with SRES and Kc, or None on error
        '''
        if len(RAND) != 16:
            print '[WNG] needs a 16 bytes input RAND value'
            return None
        # select DF_GSM directory
        DF_GSM = self.select([0x7F, 0x20])
        if self.last_response[2] != (0x90, 0x00):
            if self.dbg: print '[DBG] %s' % self.last_response
            return None
        # run authentication
        self.last_response = self.INTERNAL_AUTHENTICATE(P1=0x00, P2=0x00, Data=RAND)
        if self.last_response[2][0] != 0x9F:
            if self.dbg: print '[DBG] %s' % self.last_response
            return None
        # get authentication response
        self.last_response = self.GET_RESPONSE(Le=self.last_response[2][1])
        if self.last_response[2] != (0x90, 0x00):
            if self.dbg: print '[DBG] %s' % self.last_response
            return None
        SRES, Kc = self.last_response[3][0:4], self.last_response[3][4:]
        return [ SRES, Kc ]

    def get_imsi(self):
        '''
        self.get_imsi() -> string(IMSI)

        read IMSI value at address [0x6F, 0x07]
        return IMSI string on success or None on error
        '''
        # select DF_GSM for SIM card
        if self.type == 'SIM':
            DF_GSM = self.select([0x7F, 0x20])
            if self.last_response[2] != (0x90, 0x00):
                if self.dbg: print '[DBG] %s' % self.last_response
                return None
        # select appropriate USIM application directory for USIM card
        if self.type == 'USIM' and self.AID:
            EF_DIR = self.select([0x2F, 0x00])
            if EF_DIR:
                self.AID = EF_DIR['data'][0][4:4+EF_DIR['data'][0][3]]

        # select IMSI file
        imsi = self.select([0x6F, 0x07])
        if self.last_response[2] != (0x90, 0x00):
            if self.dbg: print '[DBG] %s' % self.last_response
            return None
        # and parse the received data into the IMSI structure
        if 'data' in imsi.keys() and len(imsi['data']) == 9:
            imsi_str=''
            imsi_str += str(imsi['data'][1] >> 4)
            for i in range(2,9):
                imsi_str += str(imsi['data'][i] & 0x0F )
                imsi_str += str(imsi['data'][i] >> 4 )
            return imsi_str

        # if issue with the content of the DF_IMSI file
        if self.dbg: print '[DBG] %s' % self.last_response
        return None


#################################
# DOCUMENTATION  TO BE CONTINUED HERE !!!!!

class USIM(SIM):
    '''
    define attributes, methods and facilities for ETSI / 3GPP USIM card
    check USIM specifications in ETSI TS 102.221 and 3GPP TS 31.102

    inherit methods and objects from SIM class
    use self.dbg = 1 or more to print live debugging information
    '''
    AID_RID = [
        ([0xA0, 0x00, 0x00, 0x00, 0x09], 'GSM'),
        ([0xA0, 0x00, 0x00, 0x00, 0x87], '3G'),
        ]
    AID_app_code = [
        ([0x00, 0x00], 'Reserved'),
        ([0x00, 0x01], ''),
        ([0x00, 0x02], 'SIM Toolkit'),
        ([0x00, 0x03], 'SIM API for JavaCard'),
        ([0x00, 0x04], 'Tetra'),
        ([0x10, 0x01], 'UICC'),
        ([0x10, 0x02], 'USIM'),
        ([0x10, 0x03], 'USIM Toolkit'),
        ]
    AID_country_code = [
        ([0xFF, 0x33], 'France'),
        ([0xFF, 0x44], 'United Kingdom'),
        ([0xFF, 0x49], 'Germany'),
        ]


    def __init__(self, type='USIM'):
        '''
        initialize like an ISO7816-4 card with CLA=0x00
        and then select the 1st AID (Application ID) available
        read from the EF_DIR file:
        >>> should be the USIM one

        can also be used for USIM working in SIM mode, with <type='SIM'>
        e.g. when you put your new USIM in your old 2G handset
        '''
        self.type = type
        if type == 'SIM': ISO7816.__init__(self, CLA=0xA0)
        elif type == 'USIM': ISO7816.__init__(self, CLA=0x00)
        if self.dbg:
            print '[DBG] type definition: %s' % self.type
            print '[DBG] CLA definition: %s' % hex(self.CLA)
            print '[DBG] EF_DIR file selection and reading...'

        EF_DIR = None
        self.AID = []

        EF_DIR = self.select([0x2F, 0x00])
        if self.dbg:
            print '[DBG] EF_DIR: %s' % EF_DIR

        if EF_DIR is not None:
            AID_value = None

            # loop to parse AID address and AID data referenced in EF_DIR
            for d in EF_DIR['data']:
                if len(d) > 6 \
                and d[0] == 0x61 \
                and d[2] == 0x4F:
                    AID_value = d[4:4+d[3]]
                    if self.dbg: print '[DBG] found AID value in EF_DIR: %s' % AID_value

                    self.AID.append( AID_value )
                    # parse AID and select the right one for 3G USIM
                    # then:
                    self.last_response = self.SELECT_FILE(P1=0x04, P2=0x04, Data=AID_value)
                    if self.last_response[2][0] != 0x61:
                        print '[ERR] unable to select file at AID value: %s' % AID_value
                        if self.dbg: print '[DBG] %s' % self.last_response
                    else:
                        self.last_response = self.GET_RESPONSE(Le=self.last_response[2][1])
                        if self.last_response[2] != (0x90, 0x00):
                            print '[ERR] unable to get response correctly from AID value: %s' % value
                            if self.dbg: print '[DBG] %s' % self.last_response
                        else:
                            self.AID.append( self.last_response[3] )

            if len(self.AID) == 0:
                print '[ERR] no AID found from AID address in EF_DIR'
            else:

                print '[+] USIM AID selection: %s' % self.AID
        else:
            print '[ERR] unable to select EF_DIR\n%s' % self.last_response



    def get_CS_keys(self):
        '''
        self.get_CS_keys() -> [KSI, CK, IK]

        read CS UMTS keys at address [0x6F, 0x08]
        return list of 3 keys, each are list of bytes, on success (or eventually the whole file dict if the format is strange)
        or None on error
        '''
        EF_KEYS = self.select( [0x6F, 0x08] )
        if self.last_response[2] == (0x90, 0x00):
            if len(EF_KEYS['data']) == 33:
                KSI, CK, IK = EF_KEYS['data'][0:1], EF_KEYS['data'][1:17], EF_KEYS['data'][17:33]
                print '[+] Successful CS keys selection: Get [KSI, CK, IK]'
                return [KSI, CK, IK]
            else: return EF_KEYS
        else: return None

    def get_PS_keys(self):
        '''
        self.get_PS_keys() -> [KSI, CK_PS, IK_PS]

        read PS UMTS keys at address [0x6F, 0x09]
        return list of 3 keys, each are list of bytes, on success (or eventually the whole file dict if the format is strange)
        or None on error
        '''
        EF_KEYSPS = self.select( [0x6F, 0x09] )
        if self.last_response[2] == (0x90, 0x00):
            if len(EF_KEYSPS['data']) == 33:
                KSI, CK, IK = EF_KEYSPS['data'][0:1], EF_KEYSPS['data'][1:17], EF_KEYSPS['data'][17:33]
                print '[+] Successful PS keys selection: Get [KSI, CK, IK]'
                return [KSI, CK, IK]
            else: return EF_KEYSPS
        else: return None

    def get_GBA_BP(self):
        '''
        self.get_GBA_BP() -> [[RAND, B-TID, KeyLifetime], ...] , Length-Value parsing style

        read EF_GBABP file at address [0x6F, 0xD6], containing RAND and associated B-TID and KeyLifetime
        return list of list of bytes on success (or eventually the whole file dict if the format is strange)
        or None on error
        '''
        EF_GBABP = self.select( [0x6F, 0xD6] )
        if self.last_response[2] == (0x90, 0x00):
            if len(EF_GBABP['data']) > 2:
                #RAND, B_TID, Lifetime = LV_parser( EF_GBABP['data'] )
                print '[+] Successful GBA_BP selection: Get list of [RAND, B-TID, KeyLifetime]'
                #return (RAND, B_TID, Lifetime)
                return LV_parser( EF_GBABP['data'] )
            else: return EF_GBABP
        else: return None

    def update_GBA_BP(self, RAND, B_TID, key_lifetime):
        '''
        self.get_GBA_BP() -> void (or EF_GBABP file dict if RAND not found)

        read EF_GBABP file at address [0x6F, 0xD6],
        check if RAND provided is referenced, and update the file structure with provided B-TID and KeyLifetime
        return nothing (or eventually the whole file dict if the RAND is not found)
        '''
        GBA_BP = self.get_GBA_BP()
        for i in GBA_BP:
            if i == RAND:
                print '[+] RAND found in GBA_BP'
                # update transparent file with B_TID and key lifetime
                self.last_response = self.UPDATE_BINARY( P2=len(RAND)+1, Data=[len(B_TID)]+B_TID+[len(key_lifetime)]+key_lifetime )
                if self.dbg: print '[DBG] %s' % self.last_response
                if self.last_response[2] == 0x90:
                    print '[+] Successful GBA_BP update with B-TID and key lifetime'
                if self.dbg: print '[DBG] new value of EF_GBA_BP:\n%s' % self.get_GBA_BP()
            else:
                '[+] RAND not found in GBA_BP'
                return GBA_BP

    def get_GBA_NL(self):
        '''
        self.get_GBA_NL() -> [[NAF_ID, B-TID], ...] , Tag-Length-Value parsing style

        read EF_GBANL file at address [0x6F, 0xDA], containing NAF_ID and B-TID
        return list of list of bytes vector on success (or eventually the whole file dict if the format is strange)
        or None on error
        '''
        EF_GBANL = self.select( [0x6F, 0xDA] )
        if self.last_response[2] == (0x90, 0x00):
            if len(EF_GBANL['data'][0]) > 2:
                # This is Tag-Length-Value parsing, with 0x80 for NAF_ID and 0x81 for B-TID
                values = []
                for rec in EF_GBANL['data']:
                    NAF_ID, B_TID = [], []

                    while len(rec) > 0:
                        tlv = first_TLV_parser( rec )
                        if tlv[1] > 0xFF:
                            rec = rec[ tlv[1]+4 : ]
                        else:
                            rec = rec[ tlv[1]+2 : ]
                        if tlv[0] == 0x80: NAF_ID = tlv[2]
                        elif tlv[0] == 0x81: B_TID = tlv[2]

                    values.append( [NAF_ID, B_TID] )
                print '[+] Successful GBA_NL selection: Get list of [NAF_ID, B-TID]'
                #return (NAF_ID, B_TID)
                return values
            else: return EF_GBANL
        else: return None

    def authenticate(self, RAND=[], AUTN=[], ctx='3G'):
        '''
        self.authenticate(RAND, AUTN, ctx='3G') -> [key1, key2...] , Length-Value parsing style

        run the INTERNAL AUTHENTICATE command in the USIM with the right context:
            ctx = '2G', '3G', 'GBA' (MBMS or other not supported at this time)
            RAND and AUTN are list of bytes; for '2G' context, AUTN is not used
        return a list containing the keys (list of bytes) computed in the USIM, on success:
            [RES, CK, IK (, Kc)] or [AUTS] for '3G'
            [RES] or [AUTS] for 'GBA'
            [RES, Kc] for '2G'
        or None on error
        '''
        # prepare input data for authentication
        if ctx in ('3G', 'VGCS', 'GBA', 'MBMS') and len(RAND) != 16 and len(AUTN) != 16:
            return 'needs a 16 bytes input for RAND and AUTN values'

        if ctx == 'GBA': input = [0xDD]
        else: input = []
        input.extend( [len(RAND)] + RAND + [len(AUTN)] + AUTN )

        if ctx == '3G':
            P2 = 0x81
        elif ctx == 'VGCS':
            P2 = 0x82
            print '[+] Not implemented. Exit.'
            return -1
        elif ctx == 'MBMS':
            print '[+] Not implemented. Exit.'
            return -1
        elif ctx == 'GBA':
            P2 = 0x84
        else: # and also, if ctx == '2G'
            P2 = 0x80
            if len(RAND) != 16: return 'needs a 16 bytes input for RAND value'
            # override input value for 2G authent
            input = [len(RAND)] + RAND

        self.last_response = self.INTERNAL_AUTHENTICATE(P2=P2, Data=input)

        if self.last_response[2][0] in (0x9F, 0x61):
            self.last_response = self.GET_RESPONSE(Le=self.last_response[2][1])

            if self.last_response[2] == (0x90, 0x00):
                val = self.last_response[3]
                if P2 == 0x80:
                    print '[+] Successful 2G authentication. Get [RES, Kc]'
                    values = LV_parser(val)
                    # returned values are (RES, Kc)
                    return values
                if val[0] == 0xDB: # not adapted to 2G context with Kc, RES
                    if P2 == 0x81: print '[+] Successful 3G authentication. Get [RES, CK, IK(, Kc)]'
                    elif P2 == 0x84: print '[+] Successful GBA authentication. Get [RES]'
                    values = LV_parser(val[1:])
                    # returned values can be (RES, CK, IK) or (RES, CK, IK, Kc)
                    return values
                elif val[0] == 0xDC:
                    print '[+] Synchronization failure. Get [AUTS]'
                    values = val[2:val[1]]
                    return values
                else : return None

            return None
        return None

    def GBA_derivation(self, NAF_ID=[], IMPI=[]):
        '''
        self.GBA_derivation(NAF_ID, IMPI) -> [Ks_ext_naf]

        run the INTERNAL AUTHENTICATE command in the USIM with the GBA derivation context:
            NAF_ID is a list of bytes (use stringToByte())
                "NAF domain name"||"security protocol id", eg: "application.org"||"0x010001000a" (> TLS with RSA and SHA)
            IMPI is a list of bytes
                "IMSI@ims.mncXXX.mccYYY.3gppnetwork.org" if no IMS IMPI is specifically defined in the USIM
        return a list with GBA ext key (list of bytes) computed in the USIM:
            [Ks_ext_naf]
            Ks_int_naf remains available in the USIM for further GBA_U key derivation
        or None on error
        '''
        # need to run 1st an authenicate command with 'GBA' context, so to have the required keys in the USIM
        P2 = 0x84
        input = [0xDE] + [len(NAF_ID)] + NAF_ID + [len(IMPI)] + IMPI

        self.last_response = self.INTERNAL_AUTHENTICATE(P2=P2, Data=input)

        if self.last_response[2][0] in (0x9F, 0x61):
            self.last_response = self.GET_RESPONSE(Le=self.last_response[2][1])

            if self.last_response[2] == (0x90, 0x00):
                val = self.last_response[3]
                if val[0] == 0xDB: # not adapted to 2G context with Kc, RES
                    print '[+] Successful GBA derivation. Get [Ks_EXT_NAF]'
                    values = LV_parser(val[1:])
                    return values
                else : return None
            return None
        return None



