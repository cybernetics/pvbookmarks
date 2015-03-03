

.. index::
   pair: MSVC; 2010


.. _visual_c_2010:

=================================================================
Visual C++ 2010 , April 12, 2010
=================================================================

.. contents::
   :depth: 3


Introduction
============


Visual C++ 2010 was released on April 12, 2010. 

It uses a SQL Server Compact database to store information about the 
source code, including IntelliSense information, for better IntelliSense 
and code-completion support. (However, Visual C++ 2010 does not support 
Intellisense for C++/CLI.) 

This version adds a modern C++ parallel computing library called the 
Parallel Patterns Library, partial support for C++11, significantly 
improved IntelliSense based on the Edison Design Group front end, and 
performance improvements to both the compiler and generated code. 

This version is built around .NET 4.0, but supports compiling to 
machine code. 

The partial C++11 support mainly consists of six compiler features:
(lambdas, rvalue references, auto, decltype, static_assert, nullptr), 
and some library features (e.g. moving the TR1 components from std::tr1 
namespace directly to std namespace). Variadic templates were also 
considered, but delayed until some future version due to lower priority 
which stemmed from the fact that unlike other costly-to-implement features 
(lambda, rvalue references), this one would benefit only a minority of 
library writers than the majority of compiler end users. 

By default, all applications compiled against the Visual C++ 2010 Runtimes 
will only work under Windows XP SP2 and later.


Runtime components for running C++ applications built with Visual Studio 2010
===============================================================================

.. seealso::

   - http://support.microsoft.com/kb/2019667


The Microsoft Visual C++ 2010 SP1 Redistributable Package installs runtime 
components of Visual C++ Libraries required to run applications developed 
with Visual C++ 2010 SP1 on a computer that does not have Visual C++ 2010 
SP1 installed.

