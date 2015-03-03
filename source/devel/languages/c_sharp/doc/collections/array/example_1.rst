



=================
Int array example
=================

As an introduction to the C# array type, let's look at a simple example program
that allocates and initializes an integer array of three elements.

Please notice how the elements can be assigned to or read from using the same
syntax (values[int]).

The array is zero-based; we also demonstrate the foreach loop upon it.


::


    using System;

    class Program
    {
        static void Main()
        {
            // Use an array.
            int[] values = new int[3];
            values[0] = 5;
            values[1] = values[0] * 2;
            values[2] = values[1] * 2;

            foreach (int value in values)
            {
                Console.WriteLine(value);
            }
        }
    }

Output
======


::

    5
    10



