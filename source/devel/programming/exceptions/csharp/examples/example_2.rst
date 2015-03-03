



.. _csharp_exception_2:

==========================================
Example2 Program that uses Data property
==========================================

.. seealso:: 

   - http://www.dotnetperls.com/exception


.. contents::
   :depth: 3

Description
============


It is possible to store structured data on an exception that is thrown in one
part of your program, and then later read in this data.

Using the Data dictionary on the Exception instance, you can store associative
keys and values.



Exemple
=======

::

    using System;
    using System.Collections;

    class Program
    {
        static void Main()
        {
            try
            {
                // Create new exception.
                var ex = new DivideByZeroException("Message");
                // Set the data dictionary.
                ex.Data["Time"] = DateTime.Now;
                ex.Data["Flag"] = true;
                
                // Throw it!
                throw ex;
            }
            catch (Exception ex)
            {
                // Display the exception's data dictionary.
                foreach (DictionaryEntry pair in ex.Data)
                {
                Console.WriteLine("{0} = {1}", pair.Key, pair.Value);
                }
            }
        }
    }

Output::

    Time = 6/21/2010 11:17:41 AM
    Flag = True



Program that shows exception properties
========================================

Next, we see examples of some of the exception type's properties in the C#
programming language.

These properties include HelpLink, Message, Source, StackTrace, and TargetSite.

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



