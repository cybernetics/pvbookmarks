

.. index::
   pair: Wiki ; Django

.. _django_wiki:

=======================
Django wiki
=======================

.. seealso::

   - https://github.com/benjaoming/django-wiki
   - http://wiki.overtag.dk/


.. contents::
   :depth: 3

Demo
=====

A demo is available here, sign up for an account to see the notification system.

[wiki.overtag.dk](http://wiki.overtag.dk)

Community
==========

Please use our mailing list (google group) for getting in touch on development and support:

[django-wiki@googlegroups.com](https://groups.google.com/d/forum/django-wiki)

[twitter:djangowiki](https://twitter.com/djangowiki)



*THIS IS A WORK IN PROGRE...*
---------------------------------

Currently, the API is subject to smaller changes. South is used so no database changes will cause data loss. You are not encouraged to make your own fiddling with the internal parts of the wiki - the best idea is to customize it through overriding templates and making custom template tags. The second best strategy is to extend the wiki's class-based views.

Please refer to the [TODO](https://github.com/benjaoming/django-wiki/blob/master/TODO.md) for a detailed status or the Issue list.

Manifesto
---------

Django needs a mature wiki system appealing to all kinds of needs, both big and small:

 * **Be pluggable and light-weight.** Don't integrate optional features in the core.
 * **Be open.** Make an extension API that allows the ecology of the wiki to grow. After all, Wikipedia consists of some [680 extensions](http://svn.wikimedia.org/viewvc/mediawiki/trunk/extensions/) written for MediaWiki.
 * **Be smart.** [This is](https://upload.wikimedia.org/wikipedia/commons/8/88/MediaWiki_database_schema_1-19_%28r102798%29.png) the map of tables in MediaWiki - we'll understand the choices of other wiki projects and make our own. After-all, this is a Django project.
 * **Be simple.** The source code should *almost* explain itself.
 * **Be structured.** Markdown is a simple syntax for readability. Features should be implemented either through easy coding patterns in the content field, but rather stored in a structured way (in the database) and managed through a friendly interface. This gives control back to the website developer, and makes knowledge more usable. Just ask: Why has Wikipedia never changed? Answer: Because it's knowledge is stored in a complicated way, thus it becomes very static.

Ideas?
------

Please go ahead and post issues for discussion of ideas.


Installation
------------

### Install

To install the latest stable release:

`pip install wiki`

Install directly from Github, since there is no release yet:

`pip install git+git://github.com/benjaoming/django-wiki.git`

### Configure `settings.INSTALLED_APPS`

The following applications should be listed - NB! it's important to maintain the order due to database relational constraints:

        'django.contrib.humanize',
        'south',
        'django_notify',
        'mptt',
        'sekizai',
        'sorl.thumbnail',
        'wiki',
        'wiki.plugins.attachments',
        'wiki.plugins.notifications',
        'wiki.plugins.images',

### Database

To sync and create tables, do:

    python manage.py syncdb
    python manage.py migrate

### Configure TEMPLATE_CONTEXT_PROCESSORS

Add `'sekizai.context_processors.sekizai'` to `settings.TEMPLATE_CONTEXT_PROCESSORS`. Please refer to the [Django docs](https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors) to see the current default setting for this variable.

### Include urlpatterns

To integrate the wiki to your existing application, you shoud add the following lines at the end of your project's `urls.py`::

    from wiki.urls import get_pattern as get_wiki_pattern
    from django_notify.urls import get_pattern as get_notify_pattern
    urlpatterns += patterns('',
        (r'^notify/', get_notify_pattern()),
        (r'', get_wiki_pattern())
    )

Please use these function calls rather than writing your own include() call - the url namespaces aren't supposed to be customized.

The above line puts the wiki in */* so it's important to put it at the end of your urlconf. You can also put it in */wiki* by putting `'^wiki/'` as the pattern.

### Settings

For now, look in [wiki/conf/settings.py](https://github.com/benjaoming/django-wiki/blob/master/wiki/conf/settings.py) to see a list of available settings.

### Other tips

 1. **Account handling:** There are simple views that handle login, logout and signup. They are on by default. Make sure to set settings.LOGIN_URL to point to your login page as many wiki views may redirect to a login page.

Plugins
------------

Add/remove the following to your `settings.INSTALLED_APPS` to enable/disable the core plugins:

 * `'wiki.plugins.attachments'`
 * `'wiki.plugins.images'`
 * `'wiki.plugins.notifications'`

The notifications plugin is mandatory for an out-of-the-box installation. You can safely remove it from INSTALLED_APPS if you also override the **wiki/base.html** template.

Background
----------

Django-wiki is a rewrite of [django-simplewiki](http://code.google.com/p/django-simple-wiki/), a project from 2009 that aimed to be a base system for a wiki. It proposed that the user should customize the wiki by overwriting templates, but soon learned that the only customization that really took place was that people forked the entire project. We don't want that for django-wiki, we want it to be modular and extendable.

As of now, Django has existed for too long without a proper wiki application. The dream of django-wiki is to become a contestant alongside Mediawiki, so that Django developers can stick to the Django platform even when facing tough challenges such as implementing a wiki.

Contributing
------------

This project will be very open for enrolling anyone with a good idea. As of now, however, it's a bit closed while we get the foundation laid out.

Q&A
------------

 * **Why is the module named just "wiki"?** Because "pip install wiki" returns "No distributions at all found for wiki"! :)
 * **What markup language will you use?** [Markdown](http://pypi.python.org/pypi/Markdown). The markup renderer is not a pluggable part but has been internalized into core parts. Discussion should go here: https://github.com/benjaoming/django-wiki/issues/76
 * **Why not use django-reversion?** It's a great project, but if the wiki has to grow ambitious, someone will have to optimize its behavior, and using a third-party application for something as crucial as the revision system is a no-go in this regard.
 * **Any support for multiple wikis?** Yes, in an sense you can just imagine that you always have multiple wikis, because you always have hierarchies and full control of their permissions. See this discussion: https://github.com/benjaoming/django-wiki/issues/63

Dependencies
------------

So far the dependencies are:

 * [django>=1.4](http://www.djangoproject.com)
 * [django-south](http://south.aeracode.org/)
 * [Markdown>=2.2.0](https://github.com/waylan/Python-Markdown)
 * [django-mptt>=0.5.3](https://github.com/django-mptt/django-mptt)
 * [django-sekizai](https://github.com/ojii/django-sekizai/)
 * [sorl-thumbnail](https://github.com/sorl/sorl-thumbnail)
 * PIL (Python Imaging Library)
 * Python>=2.5<3 (Python 3 not yet supported)

Development
------------

In a your Git fork, run `pip install -r requirements.txt` to install the requirements.

The folder **testproject/** contains a pre-configured django project and an sqlite database. Login for django admin is *admin:admin*. This project should always be maintained, although the sqlite database will be deleted very soon to avoid unnecessary conflicts.

[![Build Status](https://travis-ci.org/benjaoming/django-wiki.png?branch=master)](https://travis-ci.org/benjaoming/django-wiki)

Python 2.5
----------

Due to Markdown using elementree, you should check that you have python-celementtree: `apt-get install python-celementtree`

Acknowledgements
----------------

 * The people at [edX](http://www.edxonline.org/) & MIT for finding and supporting the project both financially and with ideas.
 * [django-cms](https://github.com/divio/django-cms) for venturing where no django app has gone before in terms of well-planned features and high standards. It's a very big inspiration.
 * [django-mptt](https://github.com/django-mptt/django-mptt), a wonderful utility for inexpensively using tree structures in Django with a relational database backend.





