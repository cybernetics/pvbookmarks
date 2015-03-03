

.. index::
   pair: StackTrace; Exceptions



.. _csharp_exception_3:

============================================
3) Program that shows exception properties
============================================

Next, we see examples of some of the exception type's properties in the C#
programming language.

These properties include:

- HelpLink, 
- Message, 
- Source, 
- StackTrace, 
- and TargetSite.

This program creates an exception by dividing by zero.

Then, it catches the exception instance and writes five properties to the Console.


::

    using System;

    class Program
    {
        static void Main()
        {
            try
            {
                int value = 1 / int.Parse("0");
            }
            catch (Exception ex)
            {
                Console.WriteLine("HelpLink = {0}", ex.HelpLink);
                Console.WriteLine("Message = {0}", ex.Message);
                Console.WriteLine("Source = {0}", ex.Source);
                Console.WriteLine("StackTrace = {0}", ex.StackTrace);
                Console.WriteLine("TargetSite = {0}", ex.TargetSite);
            }
        }
    }

Output
-------

::


    (StackTrace was abbreviated for display.)

    HelpLink =
    Message = Attempted to divide by zero.
    Source = ConsoleApplication1
    StackTrace =    at Program.Main() in C:\...\Program.cs:line 9
    TargetSite = Void Main()



