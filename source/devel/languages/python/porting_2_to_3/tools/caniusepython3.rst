
.. index::
   pair: Python ; caniusepython3
   ! caniusepython3



.. _caniusepython3:

==================
caniusepython3
==================


.. seealso::

    - https://github.com/brettcannon/caniusepython3
    - https://caniusepython3.com/


.. contents::
   :depth: 3



How can I get a project ported to Python 3 ?
==============================================

Typically projects which have not switched to Python 3 yet are waiting for:

* A dependency to be ported to Python 3
* Someone to volunteer to put in the time and effort to do the port

Since `caniusepython3` will tell you what dependencies are blocking a project
that you depend on from being ported, you can try to port a project farther
down your dependency graph to help a more direct dependency make the transition.

Which brings up the second point: volunteering to do a port. Most projects
happily accept help, they just have not done the port yet because they have
not had the time. Some projects are simply waiting for people to ask for it, so
even speaking up politely and requesting a port can get the process started.

If you are looking for help to port a project, you can always search online for
various sources of help. If you want a specific starting point there are:

- `HOWTOs <http://docs.python.org/3/howto/index.html>`_ in the Python documentation
-  on `porting pure Python modules <http://docs.python.org/3/howto/pyporting.html>`_
- and `extension modules <http://docs.python.org/3/howto/cporting.html>`_.
