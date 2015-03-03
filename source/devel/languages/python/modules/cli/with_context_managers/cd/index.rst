
.. index::
   pair: Ptyhon; cd


.. _python_cd:

=================================
Python cd command
=================================


.. contents::
   :depth: 3

Classic 
=======

::


    import os
    import subprocess # just to call an arbitrary command e.g. 'ls'

    class cd:
        def __init__(self, newPath):
            self.newPath = newPath

        def __enter__(self):
            self.savedPath = os.getcwd()
            os.chdir(self.newPath)

        def __exit__(self, etype, value, traceback):
            os.chdir(self.savedPath)

    # Now you can enter the directory like this:
    with cd("~/Library"):
       # we are in ~/Library
       subprocess.call("ls")


.. _with_fabfile_virtualenv:

``with`` fabfile and virtualenv
================================


.. seealso::

   - http://docs.fabfile.org/en/1.6/api/core/context_managers.html


::

    with cd('/path/to/app'):
        with prefix('workon myvenv'):
            run('./manage.py syncdb')
            run('./manage.py loaddata myfixture')
            
            
