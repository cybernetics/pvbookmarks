

.. index::
   pair: ORM ; Django


.. _django_orm:

===============================================
Django ORM models
===============================================

.. seealso::

   - https://docs.djangoproject.com/en/dev/topics/db/models/
   - https://docs.djangoproject.com/en/dev/howto/legacy-databases/


.. contents::
   :depth: 3

Integrating Django with a legacy database
=========================================

.. seealso::

   - https://docs.djangoproject.com/en/dev/howto/legacy-databases/


While Django is best suited for developing new applications, it’s quite possible
to integrate it into legacy databases.

Django includes a couple of utilities to automate as much of this process as possible.

This document assumes you know the Django basics, as covered in the tutorial.

Once you’ve got Django set up, you’ll follow this general process to integrate
with an existing database.


Auto-generate the models
========================

Django comes with a utility called inspectdb that can create models by
introspecting an existing database.

You can view the output by running this command::

    python manage.py inspectdb

Save this as a file by using standard Unix output redirection::

    python manage.py inspectdb > models.py

