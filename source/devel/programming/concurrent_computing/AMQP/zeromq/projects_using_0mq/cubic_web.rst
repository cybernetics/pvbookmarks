
.. index::
   pair: cubic; web


.. _cubic_web:

===================
Cubic web
===================


.. seealso::

   - http://www.cubicweb.org/blogentry/2219569


There has been a growing interest in ZMQ in the past months, due to its ability
to efficiently deal with message passing, while being light and robust.

We have worked on introducing ZMQ in the CubicWeb framework for various uses :

- As a replacement/alternative to the Pyro source, that is used to connect to
  distant instances. ZMQ may be used as a lighter and more efficient alternative
  to Pyro. The main idea here is to use the send_pyobj/recv_pyobj API of PyZMQ
  (python wrapper of ZMQ) to execute methods on the distant Repository in a
  totally transparent way for CubicWeb.

- As a JSONServer. Indeed, ZMQ could be used to share data between a server and
  any requests done through ZMQ. The request is just a string of RQL, and the
  response is the result set formatted in Json.
- As the building block for a simple notification (publish/subscribe) system
  between CubicWeb instances. A component can register its interest in a
  particular topic, and receive a callback whenever a corresponding message is
  received. At this point, this mechanism is used in CubicWeb to notify other
  instances that they should invalidate their caches when an entity is deleted.

