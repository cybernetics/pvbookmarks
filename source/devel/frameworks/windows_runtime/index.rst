

.. index::
   pair: Windows ; Runtime
   ! WinRT


.. _windows_runtime:

==================================
Windows Runtime WinRT
==================================

.. seealso::

   - https://fr.wikipedia.org/wiki/Windows_Runtime   

.. contents::
   :depth: 3

Description
===========

Windows Runtime ou WinRT est l'Interface de programmation (API) proposée par 
Microsoft pour le développement d'application sur Windows 8 et Windows RT. 

WinRT permet le développement d'application en C++/CX (Component Extensions, un 
langage basé sur le C++), et en langages managés en utilisant le C# ou VB.NET. 

Il est aussi possible d'utiliser JavaScript ou TypeScript. 

Les applications WinRT supportent les architectures x86 et ARM, de plus 
celles-ci fonctionnent dans une Sandbox ce qui apporte une plus grande 
sécurité et stabilité.

**WinRT est en grande partie une API non managée**. 

Celle-ci est essentiellement basée sur des API COM, de ce fait, celle-ci peut 
s'interfacer assez facilement avec différents langages. Cependant à la manière 
de .NET, les définitions de l'API sont stockées dans des fichiers ".winmd" 
utilisant le format de métadonnées ECMA 335 moyennant quelques modifications.

Ce format de meta-données permet une simplification des appels WinRT depuis .NET 
en comparaison avec la relative complexité des P/Invoke pour Win32.

Applications Metro-style était le nom utilisé par Microsoft pour parler des 
applications développées pour WinRT, mais depuis aout 2012, suite à un potentiel 
litige avec une société du même nom, Microsoft utilise et pousse les développeurs 
à faire de même, les appellations suivantes:

- Style Windows 8, 
- Style Modern UI 
- Applications Windows Store.

WinRT est aussi utilisé pour le développement d'applications Windows Phone 8, 
via Windows Phone Runtime, un sous ensemble de Windows Runtime.


WinRT demystified, 15 Sep 2011 by Miguel de Icaza 
==================================================

.. seealso::

   - http://tirania.org/blog/archive/2011/Sep-15.html
   
   
Windows 8 as introduced at Build is an exciting release as it has important 
updates to how Microsoft envisions users will interact with their computers, 
to **a fresh new user interface to a new programming model and a lot more**.

If you build software for end-users, you should watch Jensen Harris discuss 
the Metro principles in Windows 8. I find myself wanting to spend time using 
Windows 8.

But the purpose of this post is to share what I learned at the conference 
specifically about WinRT and .NET. 

   


Qt support
===========

.. seealso::

   - :ref:`qt_5_3`
   
   
   
