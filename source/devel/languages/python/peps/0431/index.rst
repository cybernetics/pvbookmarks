
.. index::
   pair: PEP; 0431
   pair: Time; PEP 431

.. _python_pep_0431:

============================================================================
pep 0431 Time zone support improvements
============================================================================

.. seealso::

   - http://www.python.org/dev/peps/pep-0431/
   - :ref:`python_time_libraries`


.. contents::
   :depth: 3


Abstract
========

This PEP proposes the implementation of concrete time zone support in 
the Python standard library, and also improvements to the time zone API 
to deal with ambiguous time specifications during DST changes.

Conferences
===========

.. seealso:: http://regebro.wordpress.com/2013/03/25/pycon-us-2013-wrap-up-ambitions-and-results/


I have also the last few months been writing a Python Enhancement Proposal 
on getting full time zone support into Python 3.4. 

It was important to get that PEP reasonably finished before PyCon, as I 
intended to implement it during the sprints. 

The idea here was that I would more or less merge pytz into the standard 
library, with just a bit of refactoring. And this is the ambition that 
I failed to achieve. Mostly the failure is related to the way pytz works 
around some limitations in the datetime library. 

Since we are now enhancing the datetime library, we don’t want to work 
around those limitations, but we want to instead fix them. 
Doing that the simple way turned out to be impossible, and the result 
is instead that timezone support needs to be more or less reimplemented 
from scratch. The three days I was sprinting ended up with me diving 
deep into both pytz and also dateutil.tz, comparing them and deciding 
what needed to be done, so that I now have a plan.

An implementation of the time zone support for Python 3.4 will therefore 
have to wait a bit, although I still aim to have it done by the first 
Python 3.4 alpha, which is planned for August.


