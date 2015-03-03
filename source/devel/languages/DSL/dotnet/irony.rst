

.. index::
   DSL (Domain Specific Language Irony)


.. _DSL_dot_net_irony:

==========================================
DSL (Domain specific language) with Irony
==========================================

Irony
=====

.. seealso::

   - http://irony.codeplex.com/
   - http://www.hanselman.com/blog/TheWeeklySourceCode59AnOpenSourceTreasureIronyNETLanguageImplementationKit.aspx


Irony is a development kit for implementing languages on .NET platform. Unlike 
most existing yacc/lex-style solutions Irony does not employ any scanner or 
parser code generation from grammar specifications written in a specialized 
meta-language. In Irony the target language grammar is coded directly in c# 
using operator overloading to express grammar constructs. 

Irony's scanner and parser modules use the grammar encoded as c# class to 
control the parsing process. See the expression grammar sample for an example 
of grammar definition in c# class, and using it in a working parser. 

Download
========

.. seealso:: 

   - http://irony.codeplex.com/SourceControl/list/changesets#

Introduction
============

.. seealso: http://www.codeproject.com/KB/recipes/Irony.aspx

The goal of Irony, a new open source project, is to build a complete set of 
libraries and tools for language implementations in the .NET platform. 
It is currently in its first phase, which includes building the two compiler 
front-end modules - scanner and parser. This article provides an overview of 
the technology, and focuses on parser implementation with Irony. The project 
is hosted at CodePlex.

Irony brings several principal innovations into the field of compiler 
construction. Like many parser-building tools in use today, Irony produces 
a working parser from grammar specifications. However, unlike the existing 
parser builders, Irony does not use a separate meta-language for encoding 
the target grammar. In Irony, the grammar is encoded directly in C# using 
BNF-like expressions over grammatical elements represented by .NET objects. 

Additionally, no code generation is employed - Irony's universal LALR parser 
uses the information derived from C#-encoded grammar to control the parsing 
process.

Irony samples
=============

Mini-python
-----------

.. seealso:: http://irony.codeplex.com/SourceControl/changeset/view/6829bcd964f2#Irony.Samples%2fMiniPython%2fMiniPython.cs

::

  namespace Irony.Samples.MiniPython {
  // The grammar for a very small subset of Python. This is work in progress, 
  // I will be adding more features as we go along, bringing it closer to real python.
  // Current version: expressions, assignments, indented code blocks, function defs, function calls
  // Full support for Python line joining rules: line continuation symbol "\", automatic line joining when 
  //  line ends in the middle of expression, with unbalanced parenthesis
  // Python is important test case for Irony as an indentation-sensitive language.
  [Language("MiniPython", "0.2", "Micro-subset of Python, work in progress")]


Examples
========

.. seealso:: http://www.codeproject.com/KB/recipes/YourFirstDSL.aspx


   

