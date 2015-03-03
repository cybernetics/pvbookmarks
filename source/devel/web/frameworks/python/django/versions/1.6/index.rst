
.. index::
   pair: Django; 1.6 (6 novembre 2013)



.. _django_1.6:

=============================
Django 1.6 (6 novembre 2013)
=============================

.. seealso::

   - https://docs.djangoproject.com/en/1.6/
   - https://docs.djangoproject.com/en/dev/releases/1.6/
   - https://docs.djangoproject.com/en/dev/releases/1.6.1/

Note
=====

Dedicated to Malcolm Tredinnick

On March 17, 2013, the Django project and the free software community lost a 
very dear friend and developer.

Malcolm was a long-time contributor to Django, a model community member, a 
brilliant mind, and a friend. His contributions to Django — and to many other 
open source projects — are nearly impossible to enumerate. 

Many on the core Django team had their first patches reviewed by him; his 
mentorship enriched us. 

His consideration, patience, and dedication will always be an inspiration to us.

This release of Django is for Malcolm.

The Django Developers


What’s new in Django 1.6
========================

Simplified default project and app templates

The default templates used by startproject and startapp have been simplified 
and modernized. 

The admin is now enabled by default in new projects; the sites framework no 
longer is. 

clickjacking prevention is now on and the database defaults to SQLite.

If the default templates don’t suit your tastes, you can use custom project 
and app templates.


Support for savepoints in SQLite
---------------------------------

Django 1.6 adds support for savepoints in SQLite, with some limitations.


BinaryField model field
------------------------

.. seealso::

   - https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.BinaryField

A new django.db.models.BinaryField model field allows storage of raw binary 
data in the database.


check management command added for verifying compatibility
-----------------------------------------------------------

A check management command was added, enabling you to verify if your current 
configuration (currently oriented at settings) is compatible with the current 
version of Django.


Minor features
---------------

In addition to year, month and day, the ORM now supports hour, minute and 
second lookups.


Time zone-aware day, month, and week_day lookups
------------------------------------------------

Django 1.6 introduces time zone support for day, month, and week_day lookups 
when USE_TZ is True. 

These lookups were previously performed in UTC regardless of the current time zone.

This requires time zone definitions in the database. If you’re using SQLite, 
you **must install pytz**. 

If you’re using MySQL, you must install pytz and load the time zone tables with 
mysql_tzinfo_to_sql.


New lookups may clash with model fields
----------------------------------------

Django 1.6 introduces hour, minute, and second lookups on DateTimeField. 

If you had model fields called hour, minute, or second, the new lookups will 
clash with you field names. 

Append an explicit exact lookup if this is an issue.


BooleanField no longer defaults to False
-----------------------------------------

When a BooleanField doesn’t have an explicit default, the implicit default 
value is None. 

In previous version of Django, it was False, but that didn’t represent accurately 
the lack of a value.

Code that relies on the default value being False may raise an exception when 
saving new model instances to the database, because None isn’t an acceptable 
value for a BooleanField. 

You should either specify default=False in the field definition, or ensure the 
field is set to True or False before saving the object.


Object Relational Mapper changes
--------------------------------

Django 1.6 contains many changes to the ORM. These changes fall mostly in three categories:

- Bug fixes (e.g. proper join clauses for generic relations, query combining, 
  join promotion, and join trimming fixes)
- Preparation for new features. For example the ORM is now internally ready 
  **for multicolumn foreign keys**
- General cleanup.










