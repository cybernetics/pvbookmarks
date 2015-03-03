
.. index::
   pair: Signature Electronique ; Linux


.. _signature_electronique_linux:

================================================
Signature électronique du noyau linux
================================================

.. seealso::

   - https://www.kernel.org/category/signatures.html
   - :ref:`gnupg_sign`



.. contents::
   :depth: 3
   
   
Linux kernel releases PGP signatures
=====================================


All kernel releases are cryptographically signed using OpenPGP-compliant 
signatures. 

Everyone is strongly encouraged to verify the integrity of downloaded kernel 
releases by verifying the corresponding signatures.

Linux kernel releases and all other files distributed via kernel.org mirrors 
are no longer signed by one centrally issued key. You will need to rely on the 
PGP Web of Trust in order to verify the authenticity of downloaded archives.

Basic concepts
===============

Every kernel release comes with a cryptographic signature from the person making the release. This cryptographic signature allows anyone to verify whether the files have been modified or otherwise tampered with since the developer created and signed them. The signing and verification process uses public-key cryptography and it is next to impossible to forge a PGP signature without first gaining access to the developer's private key. If this does happen, the developers will revoke the compromised key and will re-sign all their previously signed releases with the new key.

To learn more about the way PGP works, please consult Wikipedia.
