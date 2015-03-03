

.. index::
   pair: Virtualenv; pyvenvex.py
   pair: Virtualenv; History


.. _pyvenvex_py:

========================================
pyvenvex.py 
========================================


.. seealso::

   - https://gist.github.com/vsajip/4673395


A script which demonstrates how to extend Python 3.3's EnvBuilder, by 
installing setuptools and pip in created venvs. 

This functionality is not provided as an integral part of Python 3.3 because, 
while setuptools and pip are very popular, they are third-party packages. 

The script needs Python 3.3 or later; invoke it using "python pyvenvex.py -h" 
for all the command line options. 

It's basically a superset of the pyvenv script which comes as part of Python 3.3.



History
=======

::

    Vinay Sajip <vinay_sajip@yahoo.co.uk> via python.org 
    à:   Distutils-Sig@python.org
    date:    12 juillet 2013 10:35
    objet:   Re: [Distutils] PEP 439 and pip bootstrap updated

::

    Donald Stufft <donald <at> stufft.io> writes:

    > We should remember that in general people have considered PyEnv that ships
    > with Python 3.3 an inferior alternative to virtualenv largely in part
    > because they have to fetch setuptools and pip prior to using it whereas in
    > virtualenv they do not.

Let's remember, that's a consequence of packaging being pulled from 3.3 - the
original plan was to have the ability to install stuff in venvs without third-
party software being necessary.

There is no real barrier to using setuptools/pip with Python 3.3+ venvs: 
For example, I published the pyvenvex.py script which creates venvs and 
installs setuptools and pip in a single step::

    https://gist.github.com/vsajip/4673395

Admittedly it's "only a Gist" and not especially publicised to the wider
community, but that could be addressed.

The current situation, as I see it, is a transitional one. When distlib-like
functionality becomes available in the stdlib, other approaches will be
possible, which improve upon what's possible with setuptools and pip. I've
demonstrated some of this using distil. When targeting Python 3.4, shouldn't
we be looking further than just advancing the status quo a little bit?

It's been said numerous times that "executable setup.py" must go. ISTM that,
notwithstanding "practicality beats purity", a pip bootstrap in Python
would bless executable setup.py and help to extend its lifespan.

Regards,

Vinay Sajip




