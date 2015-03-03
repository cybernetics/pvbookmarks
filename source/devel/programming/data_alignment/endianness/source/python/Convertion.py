## @cond -*- coding: UTF-8 -*- @endcond
# @file			Convertion.py
# @author		$Author: pbourgault $
# @version		$Revision: 354 $
# @date			$Date: 2011-12-05 17:25:31 +0100 (Mon, 05 Dec 2011) $
# @brief		Miscellaneous convertion functions module
# @par Module dependencies:
#	None.
# @par Copyright 2008-2011 id3 Semiconductors.

## @package     id3.CL1356APlus.CL1356.Utils.Convertion
# @brief		Miscellaneous convertion functions package.
# @copydetails	Convertion.py

# Standard modules
import sys
import binascii

def convertBytesListToInteger(BytesList, LittleEndian = True) :
    """
    Converts a bytes list to an integer.
    @param	BytesList
        the bytes list as a list of bytes.
    @param	LittleEndian
        the endianess format used during convert :
        - @b True if bytes list represents an integer coded using little endian format.
        - @b False if bytes list represents an integer coded using big endian format.
    @return the integer as an int if it is possible or as a long otherwise.
    """
    Integer = 0L
    Shift = 0

    if LittleEndian :
        for byte in BytesList :
            Integer += (long(byte) << Shift)
            Shift += 8
    else :
        for byte in reversed(BytesList) :
            Integer += (long(byte) << Shift)
            Shift += 8

    return int(Integer)

def convertIntegerToBytesList(Integer, Size = 4, LittleEndian = True) :
    """
    Converts an integer as a bytes list.
    @param Integer
        the integer as an int or as a long.
    @param Size
        the size of the bytes list.
    @param LittleEndian
        the endianess format used during convert :
        - @b True if bytes list represents an integer coded using little endian format.
        - @b False if bytes list represents an integer coded using big endian format.
    @return the bytes list as a list of bytes.
    """
    BytesList = list()

    if LittleEndian :
        Shift = 0
        for i in range(Size) :
            BytesList.append(int((Integer >> Shift) & 0xFF))
            Shift += 8
    else :
        Shift = 8 * (Size-1)
        for i in range(Size) :
            BytesList.append(int((Integer >> Shift) & 0xFF))
            Shift -= 8

    return BytesList

def convertBytesListToString(BytesList) :
    """
    Converts a bytes list to a string.
    @param	BytesList
        the bytes list as a list of bytes.
    @return the string.
    """
    s = ""

    for byte in BytesList :
        s += chr(byte)

    return s

def convertStringToBytesList(String) :
    """
    Converts a string as a bytes list.
    @param String
        the string.
    @return the bytes list as a list of bytes.
    """
    BytesList = list()

    for char in String :
        BytesList.append(ord(char))

    return BytesList

def convertStringToInteger(String, LittleEndian = True) :
    """
    Converts a string to an integer.
    @param	String
        the String to convert.
    @param	LittleEndian
        the endianess format used during convert :
        - @b True if bytes list represents an integer coded using little endian format.
        - @b False if bytes list represents an integer coded using big endian format.
    @return the integer as an int if it is possible or as a long otherwise.
    """
    Integer = 0L
    Shift = 0

    if LittleEndian :
        for char in String :
            num_ord = ord(char)
            Integer += num_ord * (1 << Shift)
            Shift += 8
    else :
        for char in reversed(String) :
            Integer += ord(char) * (1 << Shift)
            Shift += 8

    return int(Integer)

def convertIntegerToString(Integer, Size = 2, LittleEndian = True) :
    """
    Converts an integer as a string.
    @param Integer
        the integer as an int or as a long.
    @param Size
        the size of the string. Size is the expected number of converted byte(s).
        - If Size == 4 and Integer == 0, the converted string will be "\x00\x00\x00\x00".
        - If Size == 2 and Integer == 0xAABBCCDD and LittleEndian == False, the converted string will be "\xCC\xDD".
        - If Size == 2 and Integer == 0xAABBCCDD and LittleEndian == True, the converted string will be "\xDD\xCC".
    @param LittleEndian
        the endianess format used during convert :
        - @b True if bytes list represents an integer coded using little endian format.
        - @b False if bytes list represents an integer coded using big endian format.
    @return the string.
    """
    AsciiHexString = "%0*X" % (Size*2, Integer)

    # Handles when Integer don't fit in the expected size and generates an odd string.
    if len(AsciiHexString) % 2 :
        AsciiHexString = '0' + AsciiHexString

    String = binascii.a2b_hex(AsciiHexString)

    # Reduces string size if needed.
    if len(String) > Size :
        String = String[-Size:]

    if LittleEndian :
        LEString = ""
        for char in reversed(String) :
            LEString += char
        return LEString
    else :
        return String

def convert32bitsSignedIntegerToUnsignedInteger(SignedInteger) :
    """
    Converts a 32-bit signed integer to a unsigned integer.
    @param SignedInteger
        the integer as an int or as a long.
    @return the unsigned integer as a int or a long.
    @exception	ValueError if integer does not fit on 32bits.
    """
    if (SignedInteger > 2147483647) or (SignedInteger < -2147483648) :
        raise ValueError("Integer does not fit on 32bits")

    if SignedInteger > 0 :
        return SignedInteger
    else :
        return SignedInteger + 0x100000000L

## This table speeds up bits swapping inside bytes.
_SwapBitsTable = 	"\x00\x80\x40\xC0\x20\xA0\x60\xE0\x10\x90\x50\xD0\x30\xB0\x70\xF0" +	\
                    "\x08\x88\x48\xC8\x28\xA8\x68\xE8\x18\x98\x58\xD8\x38\xB8\x78\xF8" +	\
                    "\x04\x84\x44\xC4\x24\xA4\x64\xE4\x14\x94\x54\xD4\x34\xB4\x74\xF4" +	\
                    "\x0C\x8C\x4C\xCC\x2C\xAC\x6C\xEC\x1C\x9C\x5C\xDC\x3C\xBC\x7C\xFC" +	\
                    "\x02\x82\x42\xC2\x22\xA2\x62\xE2\x12\x92\x52\xD2\x32\xB2\x72\xF2" +	\
                    "\x0A\x8A\x4A\xCA\x2A\xAA\x6A\xEA\x1A\x9A\x5A\xDA\x3A\xBA\x7A\xFA" +	\
                    "\x06\x86\x46\xC6\x26\xA6\x66\xE6\x16\x96\x56\xD6\x36\xB6\x76\xF6" +	\
                    "\x0E\x8E\x4E\xCE\x2E\xAE\x6E\xEE\x1E\x9E\x5E\xDE\x3E\xBE\x7E\xFE" +	\
                    "\x01\x81\x41\xC1\x21\xA1\x61\xE1\x11\x91\x51\xD1\x31\xB1\x71\xF1" +	\
                    "\x09\x89\x49\xC9\x29\xA9\x69\xE9\x19\x99\x59\xD9\x39\xB9\x79\xF9" +	\
                    "\x05\x85\x45\xC5\x25\xA5\x65\xE5\x15\x95\x55\xD5\x35\xB5\x75\xF5" +	\
                    "\x0D\x8D\x4D\xCD\x2D\xAD\x6D\xED\x1D\x9D\x5D\xDD\x3D\xBD\x7D\xFD" +	\
                    "\x03\x83\x43\xC3\x23\xA3\x63\xE3\x13\x93\x53\xD3\x33\xB3\x73\xF3" +	\
                    "\x0B\x8B\x4B\xCB\x2B\xAB\x6B\xEB\x1B\x9B\x5B\xDB\x3B\xBB\x7B\xFB" +	\
                    "\x07\x87\x47\xC7\x27\xA7\x67\xE7\x17\x97\x57\xD7\x37\xB7\x77\xF7" +	\
                    "\x0F\x8F\x4F\xCF\x2F\xAF\x6F\xEF\x1F\x9F\x5F\xDF\x3F\xBF\x7F\xFF"

def swapBits(Bytes) :
    """
    Swaps most significant bits and least significant bits inside 8bit bytes.<br>
    For each bytes, bit 0 is exchanged with bit 7, bit 1 is exchanged with bit 6,
    bit 2 is exchanged with bit and bit 3 is exchanged with bit 4.
    @param Bytes
        the bytes as string of bytes.
    @return the bytes with MSBits<>LSBits swapped.
    """
    return string.translate(Bytes, _SwapBitsTable)
