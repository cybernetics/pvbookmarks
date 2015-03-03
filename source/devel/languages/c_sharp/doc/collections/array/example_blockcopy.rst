
.. index::
   pair: array; blockcopy
   pair: buffer; blockcopy



.. _array_blockcopy:

===================
Int array blockcopy
===================


.. seealso::

   - http://www.dotnetperls.com/buffer
   - :ref:`csharp_arraylist`
   - :ref:`csharp_array`


The Buffer type handles ranges of bytes. It includes the optimized Buffer.

BlockCopy method—this copies a range of bytes from one array to another.

It provides too the ByteLength method, which counts bytes in a value type array.

And it offers the GetByte and SetByte methods: these act upon individual bytes
in any value type array.

There is another way to allocate an array in your C# program and fill it with
values.



::

    using System;

    class Program
    {
        static void Main()
        {
            byte[] arr1 = new byte[] { 1, 2, 3, 4, 5 };
            byte[] arr2 = new byte[10];

            // Copy the first five bytes from arr1 to arr2
            Buffer.BlockCopy(arr1, 0, arr2, 0, 5);

            Display(arr2);

            static void Display(byte[] arr)
            {
                for (int i = 0; i < arr.Length; i++)
                {
                    Console.Write(arr[i]);
                }
                Console.WriteLine();
            }
        }
    }

Output
======

::

    1234500000



