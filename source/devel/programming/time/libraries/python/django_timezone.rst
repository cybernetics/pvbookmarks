

.. index::
   pair: Time; Django Time Zones
   pair: Naive ; Datetime
   pair: Aware ; Datetime

.. _django_timezone:

================
Django Time zone
================

.. seealso::

   -  https://docs.djangoproject.com/en/dev/topics/i18n/timezones/


.. contents::
   :depth: 3



Overview
=========

When support for time zones is enabled, Django stores date and time information
in UTC in the database, uses time-zone-aware datetime objects internally, and
translates them to the end user’s time zone in templates and forms.

This is handy if your users live in more than one time zone and you want to
display date and time information according to each user’s wall clock.

Even if your Web site is available in only one time zone, it’s still good practice
to store data in UTC in your database.
One main reason is Daylight Saving Time (DST). Many countries have a system of
DST, where clocks are moved forward in spring and backward in autumn.
If you’re working in local time, you’re likely to encounter errors twice a year,
when the transitions happen. (The pytz documentation discusses these issues in
greater detail.)
This probably doesn’t matter for your blog, but it’s a problem if you over-bill
or under-bill your customers by one hour, twice a year, every year.

The solution to this problem is to use UTC in the code and use local time only
when interacting with end users.

Time zone support is disabled by default. To enable it, set USE_TZ = True in your
settings file. Installing pytz is highly recommended, but not mandatory.

It’s as simple as::

    $ sudo pip install pytz


Naive and aware datetime objects
================================

Python’s datetime.datetime objects have a tzinfo attribute that can be used to
store time zone information, represented as an instance of a subclass of
datetime.tzinfo.

When this attribute is set and describes an offset, a datetime object is **aware**.
Otherwise, it’s **naive**.

You can use is_aware() and is_naive() to determine whether datetimes are aware
or naive.

When time zone support is disabled, Django uses naive datetime objects in local
time.

This is simple and sufficient for many use cases. In this mode, to obtain the
current time, you would write::

    import datetime
    now = datetime.datetime.now()

When time zone support is enabled, Django uses time-zone-aware datetime objects.
If your code creates datetime objects, they should be aware too.

In this mode, the example above becomes::

    import datetime
    from django.utils.timezone import utc

    now = datetime.datetime.utcnow().replace(tzinfo=utc)



Should I install pytz ?
=======================

**Yes.**

Django has a policy of not requiring external dependencies, and for this reason
pytz is optional. **However, it’s much safer to install it**.

As soon as you activate time zone support, Django needs a definition of the
default time zone.
When pytz is available, Django loads this definition from the tz database.
This is the most accurate solution. Otherwise, it relies on the difference
between local time and UTC, as reported by the operating system, to compute
conversions. This is less reliable, especially around DST transitions.

Furthermore, if you want to support users in more than one time zone, pytz is
the reference for time zone definitions


now.date() is yesterday! (or tomorrow)
======================================

If you’ve always used naive datetimes, you probably believe that you can convert
a datetime to a date by calling its date() method.

You also consider that a date is a lot like a datetime, except that it’s less accurate.

None of this is true in a time zone aware environment::

::

    >>> import datetime
    >>> import pytz
    >>> paris_tz = pytz.timezone("Europe/Paris")
    >>> new_york_tz = pytz.timezone("America/New_York")
    >>> paris = paris_tz.localize(datetime.datetime(2012, 3, 3, 1, 30))
    # This is the correct way to convert between time zones with pytz.
    >>> new_york = new_york_tz.normalize(paris.astimezone(new_york_tz))
    >>> paris == new_york, paris.date() == new_york.date()
    (True, False)
    >>> paris - new_york, paris.date() - new_york.date()
    (datetime.timedelta(0), datetime.timedelta(1))
    >>> paris
    datetime.datetime(2012, 3, 3, 1, 30, tzinfo=<DstTzInfo 'Europe/Paris' CET+1:00:00 STD>)
    >>> new_york
    datetime.datetime(2012, 3, 2, 19, 30, tzinfo=<DstTzInfo 'America/New_York' EST-1 day, 19:00:00 S


As this example shows, the same datetime has a different date, depending on the
time zone in which it is represented. But the real problem is more fundamental.

A datetime represents a point in time. It’s absolute: it doesn’t depend on
anything.
On the contrary, a date is a calendaring concept. It’s a period of time whose
bounds depend on the time zone in which the date is considered.

As you can see, these two concepts are fundamentally different, and converting a
datetime to a date isn’t a deterministic operation.

What does this mean in practice?
--------------------------------

**Generally, you should avoid converting a datetime to date.**

For instance, you can use the date template filter to only show the date part of
a datetime. This filter will convert the datetime into the current time zone
before formatting it, ensuring the results appear correctly.

If you really need to do the conversion yourself, you must ensure the datetime
is converted to the appropriate time zone first.

Usually, this will be the current timezone::

    >>> from django.utils import timezone
    >>> timezone.activate(pytz.timezone("Asia/Singapore"))
    # For this example, we just set the time zone to Singapore, but here's how
    # you would obtain the current time zone in the general case.
    >>> current_tz = timezone.get_current_timezone()
    # Again, this is the correct way to convert between time zones with pytz.
    >>> local = current_tz.normalize(paris.astimezone(current_tz))
    >>> local
    datetime.datetime(2012, 3, 3, 8, 30, tzinfo=<DstTzInfo 'Asia/Singapore' SGT+8:00:00 STD>)
    >>> local.date()
    datetime.date(2012, 3, 3)



