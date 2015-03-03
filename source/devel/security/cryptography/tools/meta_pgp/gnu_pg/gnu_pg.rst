
.. index::
   pair: Privacy;  GNU PG
   pair: RFC; 4880
   ! GNU Privacy Guard
   ! GPG

.. _gnu_privacy_guard:
.. _gpg:
.. _gnupg:

===================================
GNU Privacy Guard (GNU-PG or GPG)
===================================

.. seealso::

   - http://www.gnupg.org/
   - http://www.g10code.com/
   - http://fr.wikipedia.org/wiki/GPG
   - http://fr.wikipedia.org/wiki/GNU_Privacy_Guard
   - http://openpgp.vie-privee.org/gnupg-win.htm
   - :ref:`reseaux_de_confiance`
   - :ref:`pgp`
   - :ref:`privacy`

.. figure:: Gnupg_logo.png
   :align: center

   *GPG logo*



Introduction
=============

``GNU Privacy Guard`` (**GnuPG** or ``GPG``) is a GPL Licensed alternative to the 
PGP_ suite of cryptographic software. 

GnuPG is compliant with `RFC 4880`_, which is the current IETF standards track 
specification of OpenPGP.


.. _`RFC 4880`:  http://www.ietf.org/rfc/rfc4880.txt
.. _PGP:  https://en.wikipedia.org/wiki/Pretty_Good_Privacy

Description
============

Three different versions of GnuPG are actively maintained:

- GnuPG "modern" (2.1) is the latest development with a lot of new
  features.  

- GnuPG "stable" (2.0) is the current stable version for general use.
  This is what most users are currently using.

- GnuPG "classic" (1.4) is the old standalone version which is most
  suitable for older or embedded platforms.

You may not install "modern" (2.1) and "stable" (2.0) at the same
time.  However, it is possible to install "classic" (1.4) along with
any of the other versions.


Informations
=============


.. toctree::
   :maxdepth: 4

   howto/index
   key_signing/index
   new_web_site/index
   signer_logiciels/index
   tools/index
   versions/versions



