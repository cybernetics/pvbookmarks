

.. index::
   pair: Python ; Great code


.. _python_great_code:

====================
Python great code
====================


.. seealso::

   - http://python-future.org/index.html
   - https://python-guide.readthedocs.org/en/latest/writing/reading/
   - https://github.com/kennethreitz/python-guide
   - https://github.com/kennethreitz/python-guide/blob/master/docs/writing/reading.rst


.. contents::
   :depth: 3

Reading Great Code
==================


.. seealso::

   - https://raw.githubusercontent.com/kennethreitz/python-guide/master/docs/writing/reading.rst


One of the core tenants behind the design of Python is creating
readable code. The motivation behind this design is simple: The number
one thing that Python programmers do is read code.

One of the secrets of becoming a great Python programmer is to read,
understand, and comprehend excellent code.

Excellent code typically follows the guidelines outlined in code_style,
and does its best to express a clear and concise intent to the reader.

Included below is a list of recommended Python projects for reading. Each of
these projects are paragons of excellent Python code.

- `Howdoi <https://github.com/gleitz/howdoi>`_
  Howdoi is a code search tool, written in Python.

- `Flask <https://github.com/mitsuhiko/flask>`_
  Flask is a microframework for Python based on Werkzeug and Jinja2.
  It's intended for getting started very quickly and was developed with
  best intentions in mind.

- `Werkzeug <https://github.com/mitsuhiko/werkzeug>`_
  Werkzeug started as simple collection of various utilities for WSGI
  applications and has become one of the most advanced WSGI utility modules.
  It includes a powerful debugger, full-featured request and response objects,
  HTTP utilities to handle entity tags, cache control headers, HTTP dates,
  cookie handling, file uploads, a powerful URL routing system and a bunch
  of community-contributed addon modules.

- `Requests <https://github.com/kennethreitz/requests>`_
  Requests is an Apache2 Licensed HTTP library, written in Python,
  for human beings.

- `Tablib <https://github.com/kennethreitz/tablib>`_
  Tablib is a format-agnostic tabular dataset library, written in Python.

.. todo:: Embed and explain YouTube video showing python code reading: http://www.youtube.com/watch?v=Jc8M9-LoEuo This may require installing a Sphinx plugin. https://bitbucket.org/birkenfeld/sphinx-contrib/src/a09f29fc16970f34350ca36ac7f229e00b1b1674/youtube?at=default

.. todo:: Include code examples of exemplary code from each of the projects listed. Explain why it is excellent code. Use complex examples.

.. todo:: Explain techniques to rapidly identify data structures, algorithms and determine what the code is doing.



The code
=========


.. toctree::
   :maxdepth: 3

   domain_parser
   requests
