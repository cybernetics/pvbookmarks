

.. index::
   c♯ (classes)



.. _csharp_static_class:

================
c♯ static class
================


.. seealso::

   - http://www.dotnetperls.com/static


What does the static modifier do in the C# programming language? Here, we answer
this question and also dive into the concept of the singleton design pattern,
which also allows you to restrict the number of instances of an object.

Through the example sets, we learn about the static modifier and the
singleton pattern.

::

    A static field identifies exactly one storage location to be shared by all
    instances of a given closed class type. Hejlsberg et al., p. 434


Example
=======

As an introduction, this program shows a static class, a static field, and also
a static method. The Main method is a special case of a static method because it
is invoked as the entry point when the program begins execution.

You can see that the static field is incremented and displayed.


::

    using System;

    static class Perls
    {
        public static int _value = 5;
    }

    class Program
    {
        static void Main()
        {
        Console.WriteLine(++Perls._value);
        }
    }






