

.. index::
   pair: Python ; Brython
   ! Brython


.. _brython:

=======
Brython
=======

.. seealso::

   - http://code.google.com/p/brython/
   - http://www.brython.info/
   - :ref:`python_to_javascript`

.. contents::
   :depth: 3


Introduction
============

HTML5 brings a new potential to web applications on all platforms : PCs,
smartphones, tablets, TV etc

At the moment, only Javascript is supported for local client programming.

The objective of Brython is be able to use Python instead of Javascript

All you need to do is to load the script brython.js in the HTML page

<script src="brython.js"></script>

and call the function brython() when the page is loaded :

<body onload="brython()">

Then you can program in Python inside the HTML page, with a programming interface
adapted to browser environment.


Applications
============

.. toctree::
   :maxdepth: 3

   applications/index







