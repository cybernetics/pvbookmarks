

.. index::
   c♯ (bytearray type)



.. _csharp_bytearray_type:

===================
c♯ bytearray type
===================


.. seealso:: http://www.dotnetperls.com/convert-string-byte-array


You want to convert your string into a byte array, using the C# programming
language.

Because strings in the C# language are stored with two bytes per character, and
ASCII only allows one byte per character, this can cause data loss if the string
is not actually ASCII-encoded. However, if the string is ASCII, you can store
it in a byte array for reduced memory usage.

The :func:`Encoding.ASCII.GetBytes()` method is demonstrated here.

Example
=======

First off, we look at a program written in the C# language that uses a constant
string literal and then converts that to a byte array.

Please note that the :func:`GetBytes()` method will cause an incorrect
conversion if the input string is not actually ASCII.

In the final loop, we examine each byte of the resulting byte array and see its
numeric and also character-based representation; this demonstrates correctness.


::

    using System;
    using System.Text;

    class Program
    {
        static void Main()
        {
            // Input string.
            const string input = "Dot Net Perls";

            // Invoke GetBytes method.
            // ... You can store this array as a field!
            byte[] array = Encoding.ASCII.GetBytes(input);

            // Loop through contents of the array.
            foreach (byte element in array)
            {
                Console.WriteLine("{0} = {1}", element, (char)element);
            }
        }
    }


Output
------

::

    68 = D
    111 = o
    116 = t
    32 =
    78 = N
    101 = e
    116 = t
    32 =
    80 = P
    101 = e
    114 = r
    108 = l
    115 = s

Examining the output. The character representations from the input string were
first converted to fit in one byte elements each. Then, we see that the integer
68 corresponds to the uppercase letter 'D'; this is the standard.



