
.. index::
   pair: Autobahn; WAMP


.. _autobahn:

======================
Autobahn Python (WAMP)
======================

.. seealso::

   - http://autobahn.ws/python/
   - :ref:`autobahn_1`



.. figure:: logo_autobahn.png
   :align: center


.. contents::
   :depth: 3
   

Introduction
=============      

Autobahn|Python is a subproject of Autobahn and provides open-source implementations of

- The WebSocket Protocol
- The Web Application Messaging Protocol (WAMP)

in Python 2 and 3, running on Twisted and asyncio.

WebSocket allows bidirectional real-time messaging on the Web.

WAMP implements two messaging patterns on top of WebSocket:

- Publish & Subscribe: Publishers publish events to a topic, and subscribers to 
  the topic receive these events. A router brokers these events.
- Remote Procedure Calls: A callee registers a remote procedure with a router. 
  A caller makes a call for that procedure to the router. 
  The router deals the call to the callee and returns the result to the caller.

Basic router functionality is provided by Autobahn|Python.







