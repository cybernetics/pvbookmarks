

.. index::
   pair: Integer; Binary


.. _convert_integer_to_hexa_bytes:

==================================
Convert integer to hexa bytes
==================================


.. seealso::

   - :ref:`convert_between_binary_and_ascii`


.. contents::
   :depth: 3



Python code
===========

.. seealso::

   - http://docs.python.org/library/binascii.html


Conversion d'un entier en une suite de données binaires.


.. code-block:: python


    import binascii

    def convertIntegerToHexaBytes(Integer, Size = 2, LittleEndian = True) :
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

        >>> AsciiHexString = "%0*X" % (2*2, 10)
        >>> AsciiHexString
        '000A'
        """
        AsciiHexString = "%0*X" % (Size*2, Integer)

        # Handles when Integer don't fit in the expected size and generates an odd string.
        if len(AsciiHexString) % 2 :
            AsciiHexString = '0' + AsciiHexString

        # passage de l'ascii au binaire
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


Examples
--------

.. code-block:: python

    >>> convertIntegerToHexaBytes(20,2)
    '\x14\x00'



C#
===

.. seealso::

   - http://msdn.microsoft.com/fr-fr/library/s8s7t687%28v=vs.80%29.aspx



Code
-----

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



    /// <summary>
    /// Conversion d'un entier en une suite de bytes binaires.
    /// </summary>
    public static byte[] ConvertIntegerToBinaryHexaBytes(int l_integer, int size = 2, bool littleEndian = true)
    {
        string format = String.Format("X{0}", size * 2);

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


