
.. index::
   pair: gpg; export-secret-keys
   pair: gpg; export
   pair: Export; Secret keys
   pair: Export; Public keys
   
      
.. _gnupg_export:

=================================================================
``gpg`` export commands
=================================================================


   
.. contents::
   :depth: 3   



Exporting Secret Keys (``gpg`` [--options] ``--export-secret-keys`` names)
===========================================================================

You can export secret keys as well as public keys. 

**You should exercise great caution in exporting your secret keys, though.**

Once exported, secret keys should be guarded as zealously as your keyrings. 

Use the ``--export-secret-keys`` command combined with the ``--armor`` 
and ``--output`` options **to export secret keys to ASCII Armored files**.

::

    gpg --armor --output pvergain-sec.asc --export-secret-keys pvergain@gmail.com

Exporting Public Keys (``gpg`` [--options] ``--export`` names)
=====================================================================

Before other people can encrypt messages to you or verify signatures from you, 
they must have a copy of your public key. 

In order to distribute your public key either to a keyserver or to other 
people directly **you need to export your public key**. 


Use the ``--export`` command to export your public key. 


Although you can export your public key as binary data to a :file:`.gpg` file, 
you'll find it more useful to use the ``--armor`` option and export your public key 
as ASCII Armor::

    gpg --armor --export pvergain@gmail.com
    
 
::

    -----BEGIN PGP PUBLIC KEY BLOCK-----
    Version: GnuPG v2.0.20 (MingW32)

    mQENBFHS0kMBCADPsE6p3Po4pTmiZ18yVfFg8ijXOEu/HTQTzRR2DBKG9xHEk2MI
    LASAdXx+3q4tHFSA2qsl0jCHJmGVOrGun2BDnzMUzOSs4ChYKsg2Hn3QYh/rLHif
    4bFAZuE4uFhIKWhay4Z1TuPbusgvPdxIcXGv472QTS4dlg9H6mxEDd5aRsEGrr+A
    AYZCUurRXrEDdLCI98Hmzj4Hh6hJMQ1XY3gtDXr5AgHRC8vBCJserWwy07gDFLBR
    43JJe01gJhC+H/kS8sM3xt2rcN0007XtBJE5Q90Ox827CrykwpdVsuYhN3Ruz4NE
    Fco7kXfQVFvrxYuG4yzhV48h+gKwclhfgPL1ABEBAAG0I3B2ZXJnYWluIChncGcp
    IDxwdmVyZ2FpbkBnbWFpbC5jb20+iQE8BBMBAgAmAhsPBwsJCAcDAgEGFQgCCQoL
    BBYCAwECHgECF4AFAlHT2AMCGQEACgkQipEQ/qJ9tKDBWQf/fjfaKsDn26SUvagJ
    WZBjoSewOwqPgSHx74iaf2deWPpr5W9VmRtWKQ7xgJ+yMzCZ4MznSV5jj/bZOB6c
    HJz9yAdctRZsI7X8FtyK4PecpcRGPEf7QOnw22BcPRm0v89TlFxx4uWbXC6mZrDu
    mWk9jsYAssJCqHf+e73oANDxI0JcmYdQYam/NyMMPgKlu+6kAiEJwLiVWpKvn0Fq
    1E15GVcOERImGBs5W9EeKVb7MDC5xMQYT87H/A5HL3Us7O1cEIqoeENpt/yiQVRi
    EpNieDqFIvRtvK8vse8uOQ1GL56T9cpSlXPdO6b5Mi0YrJ4P+gOtySF3VBo6UXhq
    lFEq4g==
    =jZbc
    -----END PGP PUBLIC KEY BLOCK-----



You can also use the ``--output`` option to specify an output file so that you 
have an easily transportable file::

    gpg --armor --output pvergain-pub.asc --export pvergain@gmail.com

::

    dir pver*
    
::

    09/01/2014  14:05               985 pvergain-pub.asc



