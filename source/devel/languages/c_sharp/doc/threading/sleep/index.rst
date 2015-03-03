
.. index::
   pair: sleep; C♯




.. _csharp_sleep:

================
sleep
================

.. seealso:: http://www.dotnetperls.com/sleep

You are developing a program in the C# language targeting the .NET Framework
that must wait on an external process or procedure for some period of
milliseconds to ensure correct execution of the application.

The Thread.Sleep method in the .NET Framework and the System.Threading namespace
provides a way to suspend your program.

Here we look at how you can use ``Thread.Sleep``.


Example
=======

::

    using System;
    using System.Diagnostics;
    using System.Threading;

    class Program
    {
        static void Main()
        {
            //
            // Demonstrates three different ways of calling Sleep.
            //
            var stopwatch = Stopwatch.StartNew();
            Thread.Sleep(0);
            stopwatch.Stop();
            Console.WriteLine(stopwatch.ElapsedMilliseconds);
            Console.WriteLine(DateTime.Now.ToLongTimeString());

            stopwatch = Stopwatch.StartNew();
            Thread.Sleep(5000);
            stopwatch.Stop();
            Console.WriteLine(stopwatch.ElapsedMilliseconds);
            Console.WriteLine(DateTime.Now.ToLongTimeString());

            stopwatch = Stopwatch.StartNew();
            System.Threading.Thread.Sleep(1000);
            stopwatch.Stop();
            Console.WriteLine(stopwatch.ElapsedMilliseconds);

            //
            // Bonus: shows SpinWait method.
            //
            stopwatch = Stopwatch.StartNew();
            Thread.SpinWait(100000 * 10000);
            stopwatch.Stop();
            Console.WriteLine(stopwatch.ElapsedMilliseconds);
        }
    }


Output
======

::


    0              ElapsedMilliseconds after Sleep(0)
    8:14:43 AM     Time after Sleep(0)
    4999           ElapsedMilliseconds after Sleep(5000)
    8:14:48 AM     Time after Sleep(5000)
    999            ElapsedMilliseconds after Sleep(1000)
    3144           ElapsedMilliseconds after SpinWait(Int32)




