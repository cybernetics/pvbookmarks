

.. index::
   pair: Python ; Requests
   ! Requests


.. _requests:

=================================
``Requests`` : Python great code
=================================

.. seealso::

   - http://docs.python-requests.org/en/latest/
   - https://github.com/kennethreitz/requests
   - https://raw.githubusercontent.com/kennethreitz/requests/master/README.rst


.. contents::
   :depth: 3

Description
============


Requests is an Apache2 Licensed HTTP library, written in Python, for human
beings.

Most existing Python modules for sending HTTP requests are extremely
verbose and cumbersome. Python's builtin urllib2 module provides most of
the HTTP capabilities you should need, but the api is thoroughly broken.
It requires an enormous amount of work (even method overrides) to
perform the simplest of tasks.

Things shouldn't be this way. Not in Python.

.. code-block:: pycon

    >>> r = requests.get('https://api.github.com', auth=('user', 'pass'))
    >>> r.status_code
    204
    >>> r.headers['content-type']
    'application/json'
    >>> r.text
    ...

See `the same code, without Requests <https://gist.github.com/973705>`_.

Requests allow you to send HTTP/1.1 requests. You can add headers, form data,
multipart files, and parameters with simple Python dictionaries, and access the
response data in the same way. It's powered by httplib and `urllib3
<https://github.com/shazow/urllib3>`_, but it does all the hard work and crazy
hacks for you.
