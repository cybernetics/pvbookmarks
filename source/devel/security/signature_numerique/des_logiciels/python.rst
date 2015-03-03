
.. index::
   pair: Signature Electronique ; Python


.. _signature_electronique_python:

================================================
Signature électronique de l'interpréteur Python
================================================

.. seealso::

   - http://www.python.org/download/#pubkeys
   - :ref:`gnupg`


.. contents::
   :depth: 3


Python OpenPGP Public Keys
==========================

.. seealso::

   - http://www.python.org/download/#pubkeys


Source and binary executables are signed by the release manager using their 
**OpenPGP key**. 

The release managers and binary builders since Python 2.3 have been:

- Anthony Baxter (key id: 6A45C816)
- Georg Brandl (key id: 36580288)
- Martin v. Löwis (key id: 7D9DC8D2)
- Benjamin Peterson (key id: 18ADD4FF and A4135B38)
- Barry Warsaw (key ids: A74B06BF, EA5BBD71, and ED9D77D5)
- Ronald Oussoren (key id: E6DF025C)
- Ned Deily (key id: 6F5E1540)
- Larry Hastings (key id: F73C700D)

.. note:: Barry's key id A74B06BF is used to sign the Python 2.6.8 and 2.6.9 releases. 
   His key id EA5BBD71 was used to sign all other Python 2.6 and 3.0 releases. 
   His key id ED9D77D5 is a v3 key and was used to sign older releases.


You can import the release manager public keys by either downloading the 
public key file from here and then running::

    % gpg --import pubkeys.txt

or by grabbing the individual keys directly from the keyserver network by 
running this command::

    % gpg --recv-keys 6A45C816 36580288 7D9DC8D2 18ADD4FF A4135B38 A74B06BF EA5BBD71 ED9D77D5 E6DF025C 6F5E1540 F73C700D

On the version-specific download pages, you should see a link to both the 
downloadable file and a detached signature file. 

To verify the authenticity of the download, grab both files and then run 
this command::

    08/01/2014  15:05        14 122 529 Python-3.3.3.tar.bz2
    08/01/2014  15:02               230 Python-3.3.3.tar.bz2.asc

    > gpg --verify Python-3.3.3.tar.bz2.asc
    > gpg: Signature faite le 11/17/13 09:03:57 Paris, Madrid avec la clÚ DSA ID 36580288
    > gpg: Bonne signature de Georg Brandl (Python release signing key) <georg@python.org>

Note that you must use the name of the signature file, and you should use the 
one that's appropriate to the download you're verifying.


Python 2.7 releasers
====================

.. seealso::

   - http://www.python.org/download/releases/2.7.6/

The source tarballs are signed with Benjamin Peterson's key, which has key id 
**18ADD4FF**. 

The Windows installer was signed by Martin von Löwis' public key, which has a 
key id of **7D9DC8D2**. 

The Mac installers were signed with Ned Deily's key, which has a key id of 
**6F5E1540**. 

The public keys are located on the `download page`_.


.. _`download page`:  http://www.python.org/download#pubkeys


Python 3.3 releasers
====================


.. seealso:: 

   - http://www.python.org/download/releases/3.3.3/


The source tarballs are signed with Georg Brandl's key, which has a key id of 
**36580288**; the fingerprint is 26DE A9D4 6133 91EF 3E25 C9FF 0A5B 1018 3658 0288. 

The Windows installer was signed by Martin von Löwis' public key, which has 
a key id of **7D9DC8D2**. 

The Mac installers were signed with Ned Deily's key, which has a key id of **6F5E1540**. 

The public keys are located on the `download page`_.

.. _`download page`:  http://www.python.org/download#pubkeys

