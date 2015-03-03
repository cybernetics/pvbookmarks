
.. index::
   pair: Certificat ; OpenPGP

.. _certificat_openpgp:

====================
Certificats OpenPGP
====================

.. seealso:

   - http://tools.ietf.org/html/rfc6091


Introduction
============


Alors que les premiers sites web "sécurisés" ne pouvaient utiliser que des 
certificats X.509, l'exploitation de la `RFC 6091`_ permet désormais d'utiliser 
des certificats OpenPGP afin de faire du HTTPS.


.. _`RFC 6091`:   http://tools.ietf.org/html/rfc6091


Abstract
=========

.. seealso:

   - http://tools.ietf.org/html/rfc6091


This memo defines Transport Layer Security (TLS) extensions and
associated semantics that allow clients and servers to negotiate the
use of OpenPGP certificates for a TLS session, and specifies how to
transport OpenPGP certificates via TLS. It also defines the registry
for non-X.509 certificate types
