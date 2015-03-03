

.. index::
   pair: Base; Directory
   pair: XDG; Freedesktop
   pair: Path; Freedesktop
   pair: User ; Data 
   pair: Base; Directory
   pair: Path; Freedesktop
   pair: Python; Appdirs


.. _basedir:

======== 
Basedir
========

.. seealso::

   - http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html
   
 
 
Appdirs
========  

.. seealso::

   - http://pypi.python.org/pypi/appdirs
   
   
A small Python module for determining appropriate platform-specific 
dirs, e.g. a "user data dir".   
   
Appdirs from pypy is retarded
-----------------------------

.. seealso:: http://ramblingfoo.blogspot.fr/2013/02/appdirs-from-pypy-is-retarded.html

The XDG standard says user-specific data files should be written [in] 
$XDG_DATA_HOME which defaults to $HOME/.local/share.

Appdirs_ explicitly breaks XDG_DATA_HOME specification and returns a path 
based on $XDG_CONFIG_HOME, ~/.config/<appname> instead of 
~/.local/share/<appname> for user_data_dir. 

Although the spec is as clear as day, the authors of appdirs say this 
is 'subject to some interpretation'.

No, it's not, read the damn spec!

http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html


The irony is that initially they got it right, but decided to break the 
standard some two years ago.

Thank you appdirs authors for ignoring a perfectly clear standard just 
because you *think* 'in practice, Linux apps tend to store their data 
in ~/.config/<appname>'.

.. _Appdirs: http://pypi.python.org/pypi/appdirs      
   
