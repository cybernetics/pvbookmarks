

.. index::
   pair: C♯ ; mask computing


.. _csharp_mask_computing:

==================================
C# Mask computing
==================================


.. seealso::

   - http://en.wikipedia.org/wiki/Mask_%28computing%29


.. contents::
   :depth: 3


Introduction
============

::

    static UInt32 MasqueLongueurChampNom = 0xFFFFFFF0;
    static UInt32 SetLongueurChampNom    = 0x0000000F;     // binaire : 0000 0000 0000 0000 0000 0000 0000 1111 4 bits => 16 nom de 0 à 15 caractères
    static public UInt32 LongueurChampNomProduit
    {
        get
        {
            UInt32 val = LongueursChamps & SetLongueurChampNom;
            return val;
        }

        set
        {
            LongueursChamps &= MasqueLongueurChampNom;          // nettoie valeur précédente
            LongueursChamps |= (value & SetLongueurChampNom);   // met la nouvelle valeur
        }
    }
