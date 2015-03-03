
.. index::
   pair: C# ; Endianness


.. _endianness_sharp:

==================================
Csharp Endianness tutorials
==================================

.. contents::
   :depth: 3


IsLittleEndian
==============

.. seealso::

   - http://msdn.microsoft.com/en-us/library/system.bitconverter.aspx
   - http://msdn.microsoft.com/en-us/library/system.bitconverter.islittleendian.aspx


Indicates the byte order ("endianness") in which data is stored in this computer
architecture

Example of the BitConverter.IsLittleEndian field
-------------------------------------------------

::

    using System;

    class LittleEndDemo
    {
        public static void Main( )
        {
            Console.WriteLine(
                "This example of the BitConverter.IsLittleEndian field " +
                "generates \nthe following output when run on " +
                "x86-class computers.\n");
            Console.WriteLine( "IsLittleEndian:  {0}",
                BitConverter.IsLittleEndian );
        }
    }

    /*
    This example of the BitConverter.IsLittleEndian field generates
    the following output when run on x86-class computers.

    IsLittleEndian:  True
    */



DecodeHex
=========

::

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


ConvertIntegerToBinaryHexaBytes
===============================


::

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


Source
======

.. literalinclude:: Convertion.cs
   :linenos:

