
.. index::
   pair: Django ; Speedbar


.. _django_speedbar:

=======================
Django speedbar
=======================

.. seealso::

   - https://github.com/theospears/django-speedbar


Description
============

django-speedbar instruments key events in the page loading process (database
queries, template rendering, url resolution, etc) and provides summary
information for each page load, as well as integration with Google Chrome
SpeedTracer to show a tree of the events taking place in a page load.

It is designed to be run on live sites, with minimal performance impact.
Although all requests are monitored, results are only visible for users
with the staff flag.
