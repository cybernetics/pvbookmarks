
.. index::
   pair: 2.0; HTTP
   pair: RFC; 2616

.. _http_2.0:

==================================
HTTP 2.0 (2013-2014 ??)
==================================


.. seealso::

   - http://en.wikipedia.org/wiki/HTTP_2.0
   - http://linuxfr.org/news/en-route-pour-http-2-0



Comments
========

::

	On 11.01.2013 03:45, Terry Reedy wrote:
	> So my conclusion is that this is (mostly) premature for Python at this time. This is a slight
	> performance enhancement of limited use that will make code at least slightly more complex in a core
	> module that must be keep at least as rock solid as it is now. Let Google get it working on both
	> their servers and Chrome browser. And wait for Mozilla, say, to add it to Firefox. Things might
	> change before the first 3.4 beta, but I think 3.5 is more likely. Of course, testing will require
	> all 4 combinations of client and server.

Agreed.

I also wonder how this relates to HTTP pipelining, a feature
to improve the same multiple-requests-to-one-server situation.

Pipelining has been implemented for years both on clients and servers,
yet it is still turned off per default in e.g. Firefox:

http://en.wikipedia.org/wiki/HTTP_pipelining

There's also HTTP 2.0 on the horizon, so it may be better to
what which of those technologies actually gets enough use
in practice, before adding support to the Python library.

That said, it may be useful to have a PyPI package which implements
the FastOpen protocol in a separate socket implementation (which can
then monkey itself into the stdlib, if the application developer
wants this).






