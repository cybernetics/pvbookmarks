

.. index::
   pair: C♯ ; exceptions



.. _csharp_exceptions:

================
C♯ exceptions
================

.. seealso::

   - http://www.dotnetperls.com/exception
   - :ref:`csharp_exceptions_bis`


.. contents::
   depth: 3

Introduction
=============

A powerful mechanism for catching errors in your code, exception handling is a
major improvement over using result codes. Because it isolates error handling
in a separate part of your program, it makes the control flow simpler.

Handling exceptions correctly is one of the most important parts of critical applications.

::

    Exceptions in C# provide a structured, uniform, and type-safe way of handling
    both system-level and application-level error conditions. Hejlsberg et al., p. 599



Examples
========


In the C# programming language, you can throw exceptions with a throw statement.
Just as important, exceptions can be thrown automatically by the runtime because
of the values of the variables in your code. In this program, we divide by zero;
this results in a DivideByZeroException, which is reported.

Program that throws an exception
--------------------------------

::

    using System;

    class Program
    {
        static void Main()
        {
            try
            {
                int value = 1 / int.Parse("0");
                Console.WriteLine(value);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }


.. index::
   pair: double ; parsing
   pair: culture; parsing


Parsing a double by using a culture
-----------------------------------

Use to parse the following numbers:

- 4.6 4.8


If the numbers have a different form (ex: 4,7) an exception will be raised.


::

    CultureInfo culture_en = new CultureInfo("en-Gb");

    try
    {
        String seuil = parser.GetSetting("conf", "seuil");
        IniFile.Seuil = Convert.ToDouble(seuil, culture_en);
    }
    catch (Exception ex)
    {
        throw new Exception("seuil exception", ex);
    }
