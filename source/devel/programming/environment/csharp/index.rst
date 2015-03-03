

.. index::
   pair: C# ; Dossiers spéciaux
   pair: Dossiers ; spéciaux
   pair: SpecialFolder ; GetFolderPath
   pair: SpecialFolder ; MyDocuments
   pair: SpecialFolder ; ApplicationData


.. _csharp_environment:

======================
C# system Environment
======================


.. contents::
   :depth: 3

Environment.SpecialFolder
=========================


.. seealso:: http://msdn.microsoft.com/fr-fr/library/system.environment.specialfolder.aspx

Spécifie les constantes énumérées utilisées pour récupérer les chemins d'accès
des dossiers spéciaux du système.


- Environment.SpecialFolder.System
- Environment.SpecialFolder.MyDocuments
- Environment.SpecialFolder.ApplicationData
- ...

GetFolderPath
-------------

::

    // Sample for the Environment.GetFolderPath method
    using System;

    class Sample
    {
        public static void Main()
        {
        Console.WriteLine();
        Console.WriteLine("GetFolderPath: {0}", Environment.GetFolderPath(Environment.SpecialFolder.System));
        }
    }

