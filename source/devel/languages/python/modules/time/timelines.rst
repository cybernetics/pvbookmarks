

.. index::
   pair: python time ; timelines
   pair: Time ; timespan

.. _python_timelines:

====================
Python timelines
====================


timespan and scheduling helpers for Python

.. seealso::

   - http://pypi.python.org/pypi/timelines/0.2



::

    >>> import datetime
    >>> from timelines import timespan, timelayer

A timespan object has a start time and an end time. It can be created either
by specifying a start time and an elapsed time, or by specifying both start and
end times:


::

    >>> span1 = timespan(datetime.datetime(1984, 11, 26), datetime.timedelta(1))
    >>> span2 = timespan(datetime.datetime(1984, 11, 26) + datetime.timedelta(2), datetime.datetime(1984, 11, 26) + datetime.timedelta(2, 50))


::

    >>> span1.start


datetime.datetime(1984, 11, 26, 0, 0)


::

    >>> span1.elapsed


datetime.timedelta(1)



