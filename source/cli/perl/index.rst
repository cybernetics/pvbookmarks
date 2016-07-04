
.. index::
   pair: CLI ; Perl  


.. _cli_perl:

=============
CLI with Perl 
=============

.. seealso::

   - http://www.activestate.com/activeperl/
   - :ref:`perl_language`


.. contents::
   :depth: 3

perl usage
==========

windows .bat file
-----------------


::

    perl -p -e 's/\/_ext\/_DOTDOT\/_DOTDOT//g' %1
    perl -p -e 's/\/\${CND_PLATFORM}//g' %1


UNIX .sh file
-----------------

::

    #!/usr/bin/sh

    perl -pi -e 's/\/_ext\/_DOTDOT\/_DOTDOT//g' $1
    perl -pi -e 's/\/\${CND_PLATFORM}//g' $1


Perl modules
=============

.. toctree::
   :maxdepth: 4

   ack/index
   
   
