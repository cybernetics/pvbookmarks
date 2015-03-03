
.. index::
   pair: test tool ; watchr
   pair: continuous ; testing


.. _test_tool_watchr:

=======================
watchr tool
=======================


.. seealso::

   - http://www.nicosphere.net/autotest-avec-watchr-python-php-2429/
   - https://github.com/mynyml/watchr.git



Summary
=======

Agile development tool that monitors a directory tree, and triggers a user
defined action whenever an observed file is modified. Its most typical use is
continuous testing, and as such it is a more flexible alternative to autotest.
Features

watchr is:

- Simple to use
- Highly flexible
- Evented ( Listens for filesystem events with native c libs )
- Portable ( Linux, * BSD, OSX, Solaris, Windows )
- Fast ( Immediately reacts to file changes )

Most importantly it allows running tests in an environment that is agnostic to:

- Web frameworks ( rails, merb, sinatra, camping, invisible, ... )
- Test frameworks ( test/unit, minitest, rspec, test/spec, expectations, ... )
- Ruby interpreters ( ruby1.8, ruby1.9, MRI, JRuby, Rubinius, ... )
- Package frameworks ( rubygems, rip, ... )
