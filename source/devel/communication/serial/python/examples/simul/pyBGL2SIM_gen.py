# -*- coding: utf-8 -*-
"""
This module simulates the input of case frames by reading a file of records
captured by the `Beagle USB Protocol Analyzer <http://www.totalphase.com/support/product/beagle_ism/>`_

- the fake frames are sent to a COM5 port.
- the reader (not provided here) reads a COM1 port.

"""

from __future__ import print_function

# Import standard modules
import string
import csv
import binascii
import time

# Import addons modules
import serial

## COM port number
# Please defines here the correct COM port number.
COMPortNumber = 5

from collections import namedtuple

BeagleRecord = namedtuple('BeagleRecord', 'Index, Time, Dur ,Len ,Err ,Dev ,Ep ,Level , Record, Data')


def beagle_records(filename):
    print('opening the ' ,  filename , 'beagle file')
    try:
        for beagle_record in map(BeagleRecord._make, csv.reader(open(filename, "rb"))):
            yield beagle_record
    except Exception as e:
       print('can t open file', filename)
        
#beagle_file = "essai_touche_gen.csv"
# beagle_file = "bug2_gen.csv"
# beagle_file = "CR_t2009_11_09_small_gen.csv"
nb_max_records = 100000000000
beagle_file = "CR_beagle_2009_11_09_all_gen.csv"
 
if __name__ == '__main__':
    try:
        print("Opening serial port ...")
        ser = serial.Serial(COMPortNumber-1, 115200)

        try :
            Table                   = string.maketrans('','')
            RemoveNonHexCharsTable  = string.translate(Table, Table, string.hexdigits)
            CheckBadCharTable       = string.translate(Table, Table, string.punctuation)
            UniformSepTable         = string.maketrans(string.punctuation,' '.ljust(len(string.punctuation)))

            LastTime = time.clock()
            PreviousTimeStamp = None

            nb_records=0;
            for beagle_record in beagle_records(beagle_file):
                nb_records=nb_records+1
                print("." , end = "")
                if ((nb_records % 200) == 0):
                    print("\n", nb_records, " beagle records")
                if (nb_records > nb_max_records):
                    break;
                SplittedTime = string.translate(beagle_record.Time, UniformSepTable).split()
                Minutes, Secondes, Millisecondes = int(SplittedTime[0]), int(SplittedTime[1]), int(SplittedTime[2])
                Microsecondes , Nanosecondes = int(SplittedTime[3]), int(SplittedTime[4])
                CurrentTimeStamp = (Minutes * 60) + Secondes + (Millisecondes / 1000.0) + (Microsecondes / 1000000.0) + (Nanosecondes / 1000000000.0)

                # to comment if no delay between frames.
                if PreviousTimeStamp is not None :
                   if CurrentTimeStamp > PreviousTimeStamp :
                       time.sleep(CurrentTimeStamp-PreviousTimeStamp)
                   else:
                       PreviousTimeStamp = CurrentTimeStamp
                else:
                    PreviousTimeStamp = CurrentTimeStamp

                if len(string.translate(beagle_record.Data, Table, CheckBadCharTable)) == 0 :
                    try :
                        RawData = binascii.a2b_hex(string.translate(beagle_record.Data, Table, RemoveNonHexCharsTable))
                        ser.write(RawData)
                    except TypeError :
                        pass
                PreviousTimeStamp = CurrentTimeStamp
        finally :
            print("\n" , nb_records, "records processed")
            print("Closing serial port ...")
            ser.close()
    except serial.SerialException, e :
        print("Unable to open COM port %d, please check port number" % COMPortNumber)



