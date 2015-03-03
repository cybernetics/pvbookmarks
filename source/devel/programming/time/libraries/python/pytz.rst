

.. index::
   pair: DateTime; pytz

.. _pytz:

===============
pytz
===============

.. seealso::

   -  http://pypi.python.org/pypi/pytz
   - :ref:`delorean`


.. contents::
   :depth: 3



Introduction
============

World timezone definitions, modern and historical


pytz brings the Olson tz database into Python. This library allows accurate and
cross platform timezone calculations using Python 2.4 or higher.

It also solves the issue of ambiguous times at the end of daylight savings,
which you can read more about in the Python Library Reference (datetime.tzinfo).

Almost all of the Olson timezones are supported.

Note that this library differs from the documented Python API for tzinfo
implementations; if you want to create local wallclock times you need to use the
localize() method documented in this document.

In addition, if you perform date arithmetic on local times that cross DST
boundaries, the result may be in an incorrect timezone (ie. subtract 1 minute
from 2002-10-27 1:00 EST and you get 2002-10-27 0:59 EST instead of the
correct 2002-10-27 1:59 EDT).

A normalize() method is provided to correct this.

Unfortunately these issues cannot be resolved without modifying the Python
datetime implementation.


PEP TimeZone
============

.. seealso::

   - https://github.com/regebro/tz-pep/blob/master/pep-04tz.txt

Abstract
---------

This PEP proposes the implementation of concrete time zone support in the
Python standard library, and also improvements to the time zone API to deal
with ambiguous time specifications during DST changes.



