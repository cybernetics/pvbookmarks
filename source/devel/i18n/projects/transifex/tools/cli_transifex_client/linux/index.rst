
.. index::
   pair: Transifex; Linux


.. _transifex_client_linux:

===================================
Installation on Linux and Mac OS X
===================================

.. seealso::

   - http://support.transifex.com/customer/portal/articles/995605-installation-on-linux-and-mac-os-x-
   - http://code.transifex.com/transifex-client


.. contents::
   :depth: 3

Installation
=============

The Transifex Client is written in Python and most Unix-based systems have Python
pre-installed.

The easiest way to install it is with :ref:`pip`. Like most Python development tools,
you probably want to install it inside a :ref`virtualenv`, but you can surely install
it as root using sudo.

::

    root# pip install transifex-client

If you don't have pip installed, you can install it as follows::

    user% curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    root# python get-pip.py

Upgrading
----------

::

    root# pip install --upgrade transifex-client


Installing from source
----------------------

Just grab the code from GitHub and run the install script::

    user% git clone http://code.transifex.com/transifex-client
    user% cd transifex-client
    root# python setup.py install

