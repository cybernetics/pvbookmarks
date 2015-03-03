

.. index::
   i18n django projects
   Django i18n projects


====================
Django i18n projects
====================

.. seealso::

   - http://docs.djangoproject.com/en/dev/topics/i18n/


Overview
========

Django has full support for internationalization of text in code and templates,
and format localization of dates and numbers. Here’s how it works.

Essentially, Django does two things:

- It allows developers and template authors to specify which parts of their apps
  should be translatable.
- It uses these hooks to translate Web apps for particular users according to
  their language preferences.

The complete process can be seen as divided in three stages.
It is also possible to identify an identical number of roles with very well
defined responsibilities associated with each of these tasks (although it’s
perfectly normal if you find yourself performing more than one of these roles):

- For application authors wishing to make sure their Django apps can be used in
  different locales: Internationalization_.
- For translators wanting to translate Django apps: Localization_.
- For system administrators/final users setting up internationalized apps or
  developers integrating third party apps: `Deployment of translations`-.

For more general information about the topic, see the `GNU gettext documentation`_
and the Wikipedia_ article.


.. _Internationalization: http://docs.djangoproject.com/en/dev/topics/i18n/internationalization/
.. _Localization: http://docs.djangoproject.com/en/dev/topics/i18n/localization/
.. _`Deployment of translations`: http://docs.djangoproject.com/en/dev/topics/i18n/deployment/
.. _`GNU gettext documentation`:  http://www.gnu.org/software/gettext/manual/gettext.html#Concepts
.. _Wikipedia: http://en.wikipedia.org/wiki/Internationalization_and_localization

.. toctree::
   :maxdepth: 4


   django_transmeta



