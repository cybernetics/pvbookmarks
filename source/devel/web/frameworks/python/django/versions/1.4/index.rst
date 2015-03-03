
.. index::
   pair: Django; 1.4 (23 mars 2012)



.. _django_1.4:

===========================
Django 1.4 (23 mars 2012)
===========================

.. seealso::

   - https://docs.djangoproject.com/en/1.4/ 
   - https://docs.djangoproject.com/en/dev/releases/1.4/




Overview
=========

The biggest new feature in Django 1.4 is support for time zones when handling 
date/times. 

When enabled, this Django will store date/times in UTC, use timezone-aware objects 
internally, and translate them to users’ local timezones for display.

If you’re upgrading an existing project to Django 1.4, switching to the time-zone 
aware mode may take some care: the new mode disallows some rather sloppy behavior 
that used to be accepted. We encourage anyone who’s upgrading to check out the 
timezone migration guide and the timezone FAQ for useful pointers.





