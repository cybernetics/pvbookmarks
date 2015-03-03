

.. index::
   pair: c♯ collections; array list


.. _csharp_arraylist:

================
C♯ array list
================

.. seealso::


   - http://www.dotnetperls.com/arraylist
   - :ref:`csharp_collections`
   - :ref:`csharp_array`
   - :ref:`array_blockcopy`


.. contents::
   :depth: 3


Introduction
============

Implémente l'interface ``IList`` à l'aide d'un tableau dont la taille est
augmentée de manière dynamique.


Méthodes
========

AddRange
--------

Ajoute les éléments de ``ICollection`` à la fin de ArrayList.


toArray
-------

.. seealso:: http://msdn.microsoft.com/fr-fr/library/fcyyh2hb.aspx

::

    using System;
    using System.Collections;

    public class SamplesArrayList  {

       public static void Main()  {

          // Creates and initializes a new ArrayList.
          ArrayList myAL = new ArrayList();
          myAL.Add( "The" );
          myAL.Add( "quick" );
          myAL.Add( "brown" );
          myAL.Add( "fox" );
          myAL.Add( "jumped" );
          myAL.Add( "over" );
          myAL.Add( "the" );
          myAL.Add( "lazy" );
          myAL.Add( "dog" );

          // Displays the values of the ArrayList.
          Console.WriteLine( "The ArrayList contains the following values:" );
          PrintIndexAndValues( myAL );

          // Copies the elements of the ArrayList to a string array.
          String[] myArr = (String[]) myAL.ToArray( typeof( string ) );

          // Displays the contents of the string array.
          Console.WriteLine( "The string array contains the following values:" );
          PrintIndexAndValues( myArr );

       }

       public static void PrintIndexAndValues( ArrayList myList )  {
          int i = 0;
          foreach ( Object o in myList )
             Console.WriteLine( "\t[{0}]:\t{1}", i++, o );
          Console.WriteLine();
       }

       public static void PrintIndexAndValues( String[] myArr )  {
          for ( int i = 0; i < myArr.Length; i++ )
             Console.WriteLine( "\t[{0}]:\t{1}", i, myArr[i] );
          Console.WriteLine();
       }
    }



Combine
=======

There are different ways to add one ArrayList to another, but the best way is
using AddRange.

Internally, AddRange uses the Array.Copy or CopyTo methods, which have better
performance than some loops.

Example
-------

::


    using System;
    using System.Collections;

    class Program
    {
        static void Main()
        {
            //
            // Create an ArrayList with two values.
            //
            ArrayList list = new ArrayList();
            list.Add(5);
            list.Add(7);
            //
            // Second ArrayList.
            //
            ArrayList list2 = new ArrayList();
            list2.Add(10);
            list2.Add(13);
            //
            // Add second ArrayList to first.
            //
            list.AddRange(list2);
            //
            // Display the values.
            //
            foreach (int i in list)
            {
                Console.WriteLine(i);
            }
        }
    }

Output::

    5
    7
    10
    13


