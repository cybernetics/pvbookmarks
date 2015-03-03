


.. _grampg:

=================================================================
Python grampg  : Simple and flexible password generation library
=================================================================


.. seealso::

   - http://pypi.python.org/pypi/grampg



.. contents::
   :depth: 3

ABOUT
======

The grampg (cue to Grumpy Admin Password Generator, and pronounced "grummpeegee")
is a small python2 library which allows to generate passwords according to
(possibly complicated) user specs.

The idea is simple: build an instance, feed it your desired specifications, then
generate as many passwords as you want.

Each password generated will be independent of the others, except from the fact
that all of them will comply with the specs.

The objectives for the grampg are flexibility and easy of use. grampg fulfills
by providing a kind interface to the user:

When building the password generator the user writes the spec as if it were
being pronounced.

In this fashion, a set of complex rules is expressed in a declarative line.


