



===================
Int array example 2
===================

There is another way to allocate an array in your C# program and fill it with
values.

You can use the curly brackets { } to assign element values in one line.

The length of the array is automatically determined when you compile your program.


::

    using System;

    class Program
    {
        static void Main()
        {
            // Create an array of three ints.
            int[] array = { 10, 30, 50 };

            foreach (int value in array)
            {
                Console.WriteLine(value);
            }
        }
    }

Output
======

::

    10
    30
    50


