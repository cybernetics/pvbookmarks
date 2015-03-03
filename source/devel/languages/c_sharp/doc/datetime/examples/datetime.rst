
.. index::
   pair: C♯ datetime  ; interval


=====================
C♯ datetime examples
=====================





::

    using System;

    class Program
    {
        static void Main()
        {
        // This DateTime is constructed with an instance constructor.
        // ... We write it to the console.
        // ... If this is today, the second line will be "True".
        DateTime value = new DateTime(2010, 1, 18);
        Console.WriteLine(value);
        Console.WriteLine(value == DateTime.Today);
        }
    }




