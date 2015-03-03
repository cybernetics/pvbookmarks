

.. index::
   pair: C♯ collections; List


.. _csharp_list:

================
C♯ list
================

.. seealso::

   - http://www.dotnetperls.com/list

Unlike :ref:`arrays <csharp_array>` , the List collection type resizes
dynamically: you do not need to manage its size on your own.

The List type is ideal for linear collections not accessed by a key.

It provides many methods and properties you can use in your C# program



Example
=======

::


    using System.Collections.Generic;

    class Program
    {
        static void Main()
        {
        List<int> list = new List<int>();
        list.Add(2);
        list.Add(3);
        list.Add(5);
        list.Add(7);
        }
    }


