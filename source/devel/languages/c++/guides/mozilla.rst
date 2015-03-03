

.. index::
   pair: C++ ; programming guide mozilla



.. _coding_styles_mozilla:

=======================
Coding styles (mozilla)
=======================

.. seealso:: https://developer.mozilla.org/En/Developer_Guide/Coding_Style


https://developer.mozilla.org/index.php?title=en/C%2b%2b_Portability_Guide
==========================================================================


What follows is a set of rules, guidelines, and tips that we have found to be
useful in making C++ code portable across many machines and compilers.

This information is the result of porting large amounts of code across about
25 different machines, and at least a dozen different C++ compilers.

Some of these things will frustrate you and make you want to throw your hands
up and say, "well, that's just a stupid compiler if it doesn't do
<insert favorite C++ feature>."

**But this is the reality of portable code.**

If you play by the rules, your code will seamlessly work on all of the Mozilla
platforms and will be easy to port to newer machines.


