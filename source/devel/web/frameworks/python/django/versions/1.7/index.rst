
.. index::
   pair: Django; 1.7 (in development May 15th: Final release)



.. _django_1.7:

=============================================
Django 1.7 (in dev May 15th: Final release)
=============================================

.. seealso::

   - https://docs.djangoproject.com/en/dev/releases/1.7/
   - https://docs.djangoproject.com/en/dev/releases/1.7/#what-s-new-in-django-1-7



.. contents::
   :depth: 3


1.7 release timeline
=====================

- January 20th: 1.7 alpha
- March 6th: 1.7 beta
- May 1st: 1.7 release candidate
- May 15th: Final release (assuming a second release candidate is not needed)


What’s new in Django 1.7
=========================


Schema migrations
------------------

Django now has built-in support for schema migrations. 

It allows models to be updated, changed, and deleted by creating migration files 
that represent the model changes and which can be run on any development, 
staging or production database.

Migrations are covered in their own documentation, but a few of the key features 
are:

- syncdb has been deprecated and replaced by migrate. Don’t worry - calls to 
  syncdb will still work as before.

- A new makemigrations command provides an easy way to autodetect changes to 
  your models and make migrations for them.

- pre_syncdb and post_syncdb have been replaced by pre_migrate and post_migrate 
  respectively. These new signals have slightly different arguments. 
  Check the documentation for details.

The allow_syncdb method on database routers is now called allow_migrate, but 
still performs the same function. 

Routers with allow_syncdb methods will still work, but that method name is 
deprecated and you should change it as soon as possible (nothing more than 
renaming is required).

App registry consistency
-------------------------

It is no longer possible to have multiple installed applications with the same 
label. 

In previous versions of Django, this didn’t always work correctly, but didn’t 
crash outright either.

If you have two apps with the same label, you should create an AppConfig for 
one of them and override its label there. You should then adjust your code 
wherever it references this application or its models with the old label.

It isn’t possible to import the same model twice through different paths 
any more. 
As of Django 1.6, this may happen only if you’re manually putting a directory 
and a subdirectory on PYTHONPATH. 
Refer to the section on the new project layout in the 1.4 release notes for 
migration instructions.

You should make sure that:

- All models are defined in applications that are listed in INSTALLED_APPS 
  or have an explicit app_label.
- Models aren’t imported as a side-effect of loading their application. 
  Specifically, you shouldn’t import models in the root module of an application 
  nor in the module that define its configuration class.

Django will enforce these requirements as of version 1.9, after a deprecation period.



Applications
------------

.. seealso::

   - https://docs.djangoproject.com/en/dev/ref/applications/

Django contains a registry of installed applications that stores configuration 
and provides introspection. It also maintains a list of available models.

This registry is simply called apps and it’s available in django.apps::

    >>> from django.apps import apps
    >>> apps.get_app_config('admin').verbose_name
    'Admin'




Standalone scripts
-------------------

If you’re using Django in a plain Python script — rather than a management 
command — and you rely on the DJANGO_SETTINGS_MODULE environment variable, 
you must now explicitly initialize Django at the beginning of your script with::

    >>> import django
    >>> django.setup()



pytz may be required
---------------------

If your project handles datetimes before 1970 or after 2037 and Django raises 
a ValueError when encountering them, you will have to install pytz. 

You may be affected by this problem if you use Django’s time zone-related 
date formats or django.contrib.syndication.


Miscellaneous
--------------

AutoField columns in SQLite databases will now be created using the AUTOINCREMENT 
option, which guarantees monotonic increments. 

This will cause primary key numbering behavior to change on SQLite, becoming 
consistent with most other SQL databases. 

This will only apply to newly created tables. 

If you have a database created with an older version of Django, you will need 
to migrate it to take advantage of this feature. 

For example, you could do the following:

- Use dumpdata to save your data.
- Rename the existing database file (keep it as a backup).
- Run migrate to create the updated schema.
- Use loaddata to import the fixtures you exported in (1).


syncdb
-------

The syncdb command has been deprecated in favor of the new migrate command. 

migrate takes the same arguments as syncdb used to plus a few more, so it’s 
safe to just change the name you’re calling and nothing else.


SplitDateTimeWidget with DateTimeField
---------------------------------------

SplitDateTimeWidget support in DateTimeField is deprecated, use SplitDateTimeWidget 
with SplitDateTimeField instead.

validate
---------

validate command is deprecated in favor of check command.


New system check framework

We’ve added a new System check framework for detecting common problems (like 
invalid models) and providing hints for resolving those problems. 

The framework is extensible so you can add your own checks for your own apps 
and libraries.

To perform system checks, you use the check management command. This command 
replaces the older validate management command.







