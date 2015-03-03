
.. index::
   pair: Internet; Websocket
   ! Websocket


.. _websocket:

==================
Websocket 
==================

.. seealso::

   - http://www.websocket.org
   - http://tools.ietf.org/html/rfc6455
   

.. contents::
   :depth: 3
   

Introduction
============

Le protocole websocket n'est pas encore stabilisé, mais est très 
prometteur.


Abstract
=========

The WebSocket Protocol enables two-way communication between a client
running untrusted code in a controlled environment to a remote host
that has opted-in to communications from that code.  The security
model used for this is the origin-based security model commonly used
by web browsers.  The protocol consists of an opening handshake
followed by basic message framing, layered over TCP.  The goal of
this technology is to provide a mechanism for browser-based
applications that need two-way communication with servers that does
not rely on opening multiple HTTP connections (e.g., using
XMLHttpRequest or <iframe>s and long polling)


WAMP (Web Application Messaging Protocol) subprotocol
======================================================

.. toctree::
   :maxdepth: 3
   
   wamp/index  
   
   
Frameworks
==========

.. toctree::
   :maxdepth: 3
   
   frameworks/index   







