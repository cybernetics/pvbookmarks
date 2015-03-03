

.. index::
   ! Conversion
   pair: binary ; ascii


.. _convert_between_binary_and_ascii:

==================================
Convert between binary and ascii
==================================


.. seealso::

   - http://www.dotnetperls.com/hex


.. contents::
   :depth: 3



Python
======

.. seealso:: http://docs.python.org/library/binascii.html



.. _binary2ascii_hex:

binascii.b2a_hex   Binary to Ascii
-----------------------------------

**Return the hexadecimal representation of the binary data**.

Every byte of data is converted into the corresponding 2-digit hex representation.

**The resulting string is therefore twice as long as the length of data**.



.. _ascii2binary_hex:

binascii.a2b_hex(hexstr) binascii.unhexlify(hexstr) -> Ascii to Binary
-----------------------------------------------------------------------

**Return the binary data represented by the hexadecimal string hexstr**.

This function is the inverse of :ref:`binary2ascii_hex`.

**hexstr must contain an even number of hexadecimal digits** (which can be upper
or lower case), otherwise a TypeError is raised.


Example
-------

.. code-block:: python

    >>> AsciiHexString = "%0*X" % (2*2, 20)
    >>> AsciiHexString
    '0014'
    >>> String = binascii.a2b_hex(AsciiHexString)
    >>> String
    '\x00\x14'


C#
===

.. seealso::

   - http://msdn.microsoft.com/fr-fr/library/s8s7t687%28v=vs.80%29.aspx


Example
-------

.. code-block:: c

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
