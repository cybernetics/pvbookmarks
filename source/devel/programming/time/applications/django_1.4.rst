

.. index::
   pair: Time Applications; Django 1.4


.. _django_1.4_time:

==================
Django 1.4
==================


.. seealso::

   - https://docs.djangoproject.com/en/dev/topics/i18n/timezones/#time-zones-faq
   - https://github.com/django/django/blob/master/docs/topics/i18n/timezones.txt



Introduction
============

The biggest new feature in Django 1.4 is support for time zones when handling
date/times.

When enabled, this Django will store date/times in UTC, use timezone-aware
objects internally, and translate them to users’ local timezones for display.

If you’re upgrading an existing project to Django 1.4, switching to the
time-zone aware mode may take some care: the new mode disallows some rather
sloppy behavior that used to be accepted.

We encourage anyone who’s upgrading to check out the `timezone migration guide`_
and the `timezone FAQ`_ for useful pointers.

.. _`timezone migration guide`: https://docs.djangoproject.com/en/dev/topics/i18n/timezones/#time-zones-migration-guide
.. _`timezone FAQ`:  https://docs.djangoproject.com/en/dev/topics/i18n/timezones/#time-zones-faq


Support for time zones
======================

.. seealso:: http://fr.wikipedia.org/wiki/UTC


In previous versions, Django used “naive” date/times (that is, date/times
without an associated time zone), leaving it up to each developer to interpret
what a given date/time “really means”.

This can cause all sorts of subtle timezone-related bugs.

In Django 1.4, you can now switch Django into a more correct, time-zone aware
mode.
In this mode, Django stores date and time information in UTC in the database,
uses time-zone-aware datetime objects internally and translates them to the
end user’s time zone in templates and forms.

Reasons for using this feature include:

- Customizing date and time display for users around the world.
- Storing datetimes in UTC for database portability and interoperability.
  (This argument doesn’t apply to PostgreSQL, because it already stores
  timestamps with time zone information in Django 1.3.)
- Avoiding data corruption problems around DST transitions.

Time zone support is enabled by default in new projects created with
startproject.

If you want to use this feature in an existing project, read the migration guide.
If you encounter problems, there’s a helpful FAQ.

