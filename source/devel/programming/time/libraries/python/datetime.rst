

.. index::
   pair: Time; Datetime

.. _python_datetime:

========================
Python datetime module
========================

.. seealso::

   - http://docs.python.org/3.4/library/datetime.html


.. contents::
   :depth: 3



Introduction
============

The :mod:`datetime` module supplies classes for manipulating dates and times in
both simple and complex ways.  While date and time arithmetic is supported, the
focus of the implementation is on efficient attribute extraction for output
formatting and manipulation


A datetime object is a single object containing all the information from a date
object and a time object.

Like a date object, datetime assumes the current Gregorian calendar extended in
both directions;
like a time object, datetime assumes there are exactly 3600*24 seconds in every day.


Naive object and Coordinated Universal Time (UTC)
-------------------------------------------------

.. seealso::

   - :ref:`pytz`

A naive object does not contain enough information to unambiguously locate itself
relative to other date/time objects.

Whether a naive object represents Coordinated Universal Time (UTC), local time,
or time in some other timezone is purely up to the program, just like it’s up to
the program whether a particular number represents metres, miles, or mass.

Naive objects are easy to understand and to work with, at the cost of ignoring
some aspects of reality.

For applications requiring aware objects, datetime and time objects have an
optional time zone information attribute, tzinfo, that can be set to an instance
of a subclass of the abstract tzinfo class.
These tzinfo objects capture information about the offset from UTC time, the time
zone name, and whether Daylight Saving Time is in effect.

Note that no concrete tzinfo classes are supplied by the datetime module.
Supporting timezones at whatever level of detail is required is up to the
application.

The rules for time adjustment across the world are more political than rational,
and there is no standard suitable for every application.


.. code-block:: python

    >>> from datetime import datetime, date, time
    >>> # Using datetime.combine()
    >>> d = date(2005, 7, 14)
    >>> t = time(12, 30)
    >>> datetime.combine(d, t)
    datetime.datetime(2005, 7, 14, 12, 30)
    >>> # Using datetime.now() or datetime.utcnow()
    >>> datetime.now()   # doctest: +SKIP
    datetime.datetime(2007, 12, 6, 16, 29, 43, 79043)   # GMT +1
    >>> datetime.utcnow()   # doctest: +SKIP
    datetime.datetime(2007, 12, 6, 15, 29, 43, 79060)
    >>> # Using datetime.strptime()
    >>> dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
    >>> dt
    datetime.datetime(2006, 11, 21, 16, 30)
    >>> # Using datetime.timetuple() to get tuple of all attributes
    >>> tt = dt.timetuple()
    >>> for it in tt:   # doctest: +SKIP
    ...     print(it)
    ...
    2006    # year
    11      # month
    21      # day
    16      # hour
    30      # minute
    0       # second
    1       # weekday (0 = Monday)
    325     # number of days since 1st January
    -1      # dst - method tzinfo.dst() returned None
    >>> # Date in ISO format
    >>> ic = dt.isocalendar()
    >>> for it in ic:   # doctest: +SKIP
    ...     print(it)
    ...
    2006    # ISO year
    47      # ISO week
    2       # ISO weekday
    >>> # Formatting datetime
    >>> dt.strftime("%A, %d. %B %Y %I:%M%p")
    'Tuesday, 21. November 2006 04:30PM'
