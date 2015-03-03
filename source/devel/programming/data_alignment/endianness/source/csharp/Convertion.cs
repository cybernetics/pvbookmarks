/**
@file       Convertion.cs
@author     $Author: pvergain $
@version    $Revision: 732 $
@date       $Date: 2012-09-24 16:11:42 +0200 (Mon, 24 Sep 2012) $
@brief      Experiment management.
@details
 *

*/

/** @addtogroup Convertion
 *  @{
 */


using System;
using System.Text;

namespace VideoCell
{
        public static class Convertion
        {
            public static object EncodeHex(string data)
            {
                StringBuilder sb = new StringBuilder(data.Length * 2);
                for (int i = 0; i < data.Length; i++)
                {
                    sb.AppendFormat("{0:x2}", (int)data[i]);
                }
                return sb.ToString();
            }

            public static object Hexlify(string data)
            {
                return EncodeHex(data);
            }

            public static byte[] DecodeHex(string data)
            {
                // if (data == null) throw Ops.TypeError("expected string, got NoneType");
                // if ((data.Length & 0x01) != 0) throw Ops.ValueError("string must be even lengthed");
                byte[] bytes_array = new byte[data.Length / 2];

                int j = 0;
                for (int i = 0; i < data.Length; i += 2)
                {
                    byte b1, b2;
                    if (Char.IsDigit(data[i])) b1 = (byte)(data[i] - '0');
                    else b1 = (byte)(Char.ToUpper(data[i]) - 'A' + 10);

                    if (Char.IsDigit(data[i + 1])) b2 = (byte)(data[i + 1] - '0');
                    else b2 = (byte)(Char.ToUpper(data[i + 1]) - 'A' + 10);

                    bytes_array[j] = (byte)(b1 * 16 + b2);
                    j += 1;
                }

                return bytes_array;
            }



            /// <summary>
            /// Conversion d'un entier en une suite de bytes binaires suivant le boutisme.
            /// </summary>
            public static byte[] ConvertIntegerToBinaryHexaBytes(int l_integer, int size = 2, bool littleEndian = true)
            {
                string format = String.Format("X{0}", size*2);

                string AsciiHexString = l_integer.ToString(format);

                byte[] binary_hexa_bytes = DecodeHex(AsciiHexString);

                if (littleEndian)
                {
                    byte[] little_binary_hexa_bytes = new byte[binary_hexa_bytes.Length];
                    int i_byte = binary_hexa_bytes.Length - 1;
                    int j=0;
                    while (i_byte >= 0)
                    {
                        little_binary_hexa_bytes[j] = binary_hexa_bytes[i_byte];
                        i_byte--;
                        j++;
                    }

                    return little_binary_hexa_bytes;
                }
                else
                {
                    return binary_hexa_bytes;
                }
            }


            /// <summary>
            /// Conversion d'un entier en une suite de bytes binaire suivant 
            /// </summary>
            public static void test_ConvertIntegerToBinaryHexaBytes32bits()
            {
                int value = 20;

                byte[] res = ConvertIntegerToBinaryHexaBytes(value, 4, true);

                foreach (byte elem in res)
                {
                    Console.WriteLine(elem);
                }
            }

            public static void test_ConvertIntegerToBinaryHexaBytes16bits(UInt16 value)
            {
                byte[] res = ConvertIntegerToBinaryHexaBytes(value, 2, true);

                foreach (byte elem in res)
                {
                    Console.WriteLine(elem);
                }
            }

            /*
             * 
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
                        Integer += ord(char) * (1 << Shift)
                        Shift += 8
                else :
                    for char in reversed(String) :
                        Integer += ord(char) * (1 << Shift)
                        Shift += 8

                return int(Integer)
             */


            public static int ConvertBinaryHexaBytesToInteger(byte[] binary_data_bytes, bool littleEndian = true)
            {
                int Integer = 0;
                int Shift = 0;

                if (littleEndian)
                {
                    foreach (byte elem in binary_data_bytes)
                    {
                        Integer += elem * (1 << Shift);
                        Shift += 8;
                    }
                }
                else
                {
                    int j = binary_data_bytes.Length - 1;
                    while (j >= 0)
                    {
                        Integer += binary_data_bytes[j] * (1 << Shift);
                        j -= 1;
                        Shift += 8;
                    }

                }

                return Integer;
            }


            public static void test_ConvertBinaryHexaBytesToInteger_2()
            {
                byte[] binary_data_bytes = new byte[] { 0x20, 0xD6, 0x1d, 0x00 };

                int value_integer = ConvertBinaryHexaBytesToInteger(binary_data_bytes, true);

                string message = string.Format("Value={0}", value_integer);

                Console.Write(message); ;
            }

            public static void test_ConvertBinaryHexaBytesToInteger()
            {
                int value = 3126;

                byte[] binary_data_bytes = ConvertIntegerToBinaryHexaBytes(value, 4, true);


                int value2 = ConvertBinaryHexaBytesToInteger(binary_data_bytes, true);

                if (value == value2)
                    Console.Write("OK");
                else
                    Console.Write("PB");
            }


            /// <summary>
            /// http://www.csharp-examples.net/reverse-bytes/
            /// This example shows how to reverse byte order in integer numbers. This can be used to change between little-endian and big-endian.
            /// // reverse byte order (16-bit) 
            /// </summary>
            public static UInt16 ReverseBytes(UInt16 value)
            {
                return (UInt16)((value & 0xFFU) << 8 | (value & 0xFF00U) >> 8);
            }

            /// <summary>
            /// reverse byte order (32-bit) 
            /// </summary>
            public static UInt32 ReverseBytes(UInt32 value)
            {
              return (value & 0x000000FFU) << 24 | (value & 0x0000FF00U) << 8 |
                     (value & 0x00FF0000U) >> 8 | (value & 0xFF000000U) >> 24;
            }

            /// <summary>
            /// reverse byte order (64-bit) 
            /// </summary>
            public static UInt64 ReverseBytes(UInt64 value)
            {
                return (value & 0x00000000000000FFUL) << 56 | (value & 0x000000000000FF00UL) << 40 |
                       (value & 0x0000000000FF0000UL) << 24 | (value & 0x00000000FF000000UL) << 8 |
                       (value & 0x000000FF00000000UL) >> 8 | (value & 0x0000FF0000000000UL) >> 24 |
                       (value & 0x00FF000000000000UL) >> 40 | (value & 0xFF00000000000000UL) >> 56;
            }
        } // class Convertion

} // VideoCell

/**
    fin Convertion

@}

*/
