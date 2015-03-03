
.. index::
   pair: HTTP; Request


.. _request:

==================================
HTTP python request library
==================================

.. seealso::

   - http://docs.python-requests.org/en/latest/
   - https://crate.io/packages/requests/
   - http://pypi.python.org/pypi/requests


.. contents::
   :depth: 3


Introduction
============

Requests is an Apache2 Licensed HTTP library, written in Python, for human beings.

Python’s standard urllib2 module provides most of the HTTP capabilities you need,
but the API is thoroughly broken.

It was built for a different time — and a different web. It requires an enormous
amount of work (even method overrides) to perform the simplest of tasks.


Requests takes all of the work out of Python HTTP/1.1 — making your integration
with web services seamless. There’s no need to manually add query strings to
your URLs, or to form-encode your POST data.

Keep-alive and HTTP connection pooling are 100% automatic, powered by urllib3,
which is embedded within Requests.

Testimonials
============

Amazon, Google, Twilio, Mozilla, Heroku, PayPal, NPR, Obama for America,
Transifex, Native Instruments, The Washington Post, Twitter, SoundCloud, Kippt,
Readability, and Federal US Institutions use Requests internally.

It has been downloaded over 1,500,000 times from PyPI.



Get the Code
=============

Requests is actively developed on GitHub, where the code is always available.

You can either clone the public repository::

    git clone git://github.com/kennethreitz/requests.git

Download the tarball::

    $ curl -OL https://github.com/kennethreitz/requests/tarball/master

Or, download the zipball::

    $ curl -OL https://github.com/kennethreitz/requests/zipball/master

Once you have a copy of the source, you can embed it in your Python package, or
install it into your site-packages easily::

    $ python setup.py install


Projects using requests
=======================

- http://pypi.python.org/pypi/rt
- http://pypi.python.org/pypi?%3Aaction=search&term=requests&submit=search




