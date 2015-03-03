.. module:: PythonInstallation
    :synopsis: Python installation


=======================
Python XX installation
=======================


.. seealso:: http://regebro.wordpress.com/2011/02/02/newbie-hint-on-installing-python-and-its-modules-and-packages/


Newbie hint on installing Python and it’s modules and packages
==============================================================

by Lennart Regebro on February 2, 2011

There is a issue that pops up from time to time, primarily with Python newbies
on Stackoverflow.com and the like, but also with more experienced programmers.

And that is how to use package X that you installed for Python Y with Python Z.
Sometimes it is a library like PIL or NumPy, but quite often it’s pip or
virtualenv and it’s associated scripts.

.. warning:: And the answer is: You don’t!

You install each library/module/package separately, once for each
version of Python. The best way to do it is like this:

1. You install each version of Python in a separate directory,
   like /opt/pythonXX, where XX is the version of Python, and
   /opt/pypy14 for PyPy, and so on.
2. You download the script to install Distribute and run it,
   once for each version of Python you have installed.
3. You will then get one easy_install script in each /opt/pythonXX/bin,
   so you run /opt/pythonXX/bin/easy_install virtualenv and optionally
   /opt/pythonXX/bin/easy_install pip for each version of Python.
4. And that’s it.


How do you then use this? Well:

1. Now when you have a project that needs NumPy you make a project
   directory with the virtualenv of the Python you want to use for that project.
   Like so: /opt/python26/bin/virtualenv /my/projects/coolmaths
2. Then you go to that directory: cd /my/projects/coolmaths
3. Now you can, if you like, activate that virtualenv, but I never do that.
   Instead I just call the correct scripts explicitly like so
   ./bin/easy_install numpy
4. Again, that’s it.

It really is that simple
========================

You install every Python separately, you install every module and package
separately in those Python install, and you use everything explicitly.

That solves all your problems.

You can install all pythons in the same directory, like /usr/local,
or /opt/pythons.

This works well with python, and you then will have to chose which python
by adding the version number to the executable: /usr/local/bin/python-2.4,
for example.

Distribute will work well with this too, you get /usr/local/bin/easy_install-2.7 etc.

However, afaik can tell, pip does not always do this (maybe its’ a question
of which pip version, or maybe it’s intelligent enough to know when it does
have to? Not sure), so there you may have to make a copy of the pip script
each time.

But in any case,  it’s much harder to delete and re-install a Python if you
install them  together like this.

With separate directories you can, if your Python is fudged up, just remove
the directory and do it again.

Also: Avoid the system Python on OS X or Linux distros for your projects.

You get stuck on a specific version, and you get conflicts with versions
of packages, etc.

The OS needs to have it’s versions, and you often needs others, and using
the same Python install makes everything very complicated.

So there. Now you know.


PEP 0394 The "python" command on Unix-Like Systems (march 2011)
===============================================================


.. seealso::  http://www.python.org/dev/peps/pep-0394/





