
.. index::
   pair: cli ; Google


.. _google_cli:

==========
Google cli
==========

.. seealso::

   - http://code.google.com/p/googlecl/
   - http://code.google.com/p/googlecl/wiki/ExampleScripts#Picasa
   - :ref:`google_python_data_modules`


.. contents::
   :depth: 3

GoogleCL brings Google services to the command line.

We currently support the following Google services:

Blogger
=======

::

    $ google blogger post --title "foo" "command line posting"

Calendar
========

::

    $ google calendar add "Lunch with Jim at noon tomorrow"

Contacts
========

::

    $ google contacts list Bob name,email > the_bobs.csv

Docs
====

::

    $ google docs edit "Shopping list"

Finance
=======

::

    $ google finance create-txn "Savings Portfolio" NASDAQ:GOOG Buy

Picasa
======

::

    $ google picasa create "Cat Photos" ~/photos/cats/*.jpg

Youtube
=======

::

    $ google youtube post --category Education killer_robots.avi


Dependencies
============

GoogleCL requires Python 2.5 or 2.6 and the gdata python client library.

You can get the library from the project homepage:

http://code.google.com/p/gdata-python-client/

Gcalcli
=======

.. seealso::  http://code.google.com/p/gcalcli/

``gcalcli`` is a Python application that allows you to access your Google Calendar
from a command line. It's easy to get your agenda, search for events, and
quickly add new events. Additionally gcalcli can be used as a reminder service
to execute any application you want.


