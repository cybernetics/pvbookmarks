
.. index::
   pair: Internet; TCP
   pair: Protocol; TCP
   pair: Transmission Control ; Protocol
   ! TCP


.. _tcp:

=====================================
TCP (Transmission Control Protocol)
=====================================


.. seealso::

   - http://fr.wikipedia.org/wiki/Tcp
   - http://tools.ietf.org/html/rfc793
   - :ref:`zeromq`


.. contents::
   :depth: 3


Introduction
============

Transmission Control Protocol (littéralement, « protocole de contrôle de
transmissions ») abrégé TCP, est un protocole de transport fiable, en mode connecté,
documenté dans la RFC 793 de l'IETF.

Dans le modèle TCP/IP, TCP est situé au niveau de la couche de transport (entre
la couche de réseau et la couche session).

Les applications transmettent des flux de données sur une connexion réseau, et
TCP découpe le flux d'octets en segments, dont la taille dépend de la MTU du
réseau sous-jacent (couche liaison de données).

TCP a été développé en 1973, puis adopté pour Arpanet en 1976 par le DARPA.


RFC 761, 793
============

.. seealso::

   - http://tools.ietf.org/html/rfc793
   - http://tools.ietf.org/html/rfc761



TCP fast open
==============

.. toctree::
   :maxdepth: 3

   fast_open/index








