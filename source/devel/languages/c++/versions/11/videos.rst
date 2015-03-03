


.. _cplusplus_11_videos:

=============
C++11 videos
=============


.. contents::
   :depth: 3


Day 1 Keynote - Bjarne Stroustrup: C++11 Style (February 2, 2012 from 9:30AM to 11:00AM)
=========================================================================================

.. seealso::

   - http://channel9.msdn.com/Events/GoingNative/GoingNative-2012/Keynote-Bjarne-Stroustrup-Cpp11-Style


We know how to write bad code: litter our programs with casts, macros, pointers,
naked new and deletes, and complicated control structures.

Alternatively (or additionally), we could obscure every design decision in a mess
of deeply nested abstractions using the latest object-oriented programming and
generic programming tricks.

Then, for good measure, we might complicate our algorithms with interesting
special cases. Such code is incomprehensible, unmaintainable, usually inefficient,
and not uncommon.

But how do we write good code? What principles, techniques, and idioms can we
exploit to make it easier to produce quality code? In this presentation, I make
an argument for type-rich interfaces, compact data structures, integrated resource
management and error handling, and highly-structured algorithmic code.
I illustrate my ideas and guidelines with a few idiomatic code examples.

I use C++11 freely.

Examples include:

- auto
- general constant expressions,
- uniform initialization,
- type aliases,
- type safe threading,
- and user-defined literals.

``C++11 features`` are only just starting to appear in production compilers, so some
of my suggestions are conjecture. Developing a "modern style," however, is essential
if we don't want to maintain newly-written 1970s and 1980s style code in 2020.

This presentation reflects my thoughts on what "Modern C++" should mean in the
2010s: a language for programming based on light-weight abstraction with direct
and efficient mapping to hardware, suitable for infrastructure code.


