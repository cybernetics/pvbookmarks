

.. index::
   pair: Boost ; asio
   pair: System ; C++
   pair: Boost ; asynchronous model


.. _boost_asio_cplusplus_library:

=======================
Boost asio C++ library
=======================

.. seealso::

   - http://think-async.com/Asio
   - http://blog.think-async.com/2006/11/buffer-debugging.html
   - http://sourceforge.net/projects/asio/files/asio/1.4.8%20%28Stable%29/


Introduction
============

Asio is a cross-platform C++ library for network and low-level I/O programming
that provides developers with a consistent asynchronous model using a modern
C++ approach.

Asio comes in two variants: (non-Boost) Asio and Boost.Asio.

The differences between the two are outlined below.

What are the differences in the source code ?
----------------------------------------------

— Asio is in a namespace called asio::, whereas Boost.Asio puts everything under
  boost::asio::.

— The main Asio header file is called asio.hpp. The corresponding header in
  Boost.Asio is boost/asio.hpp. All other headers are similarly changed.

— Any macros used by or defined in Asio are prefixed with ASIO. In Boost.Asio
  they are prefixed with BOOST_ASIO.

— Asio includes a class for launching threads: asio::thread.
  Boost.Asio does not include this class, to avoid overlap with the Boost.Thread library

— Boost.Asio uses the Boost.System library to provide support for error codes
  (boost::system::error_code and boost::system::system_error). Asio includes
  these under its own namespace ( asio::error_code and asio::system_error).
  The Boost.System version of these classes currently supports better extensibility
  for user-defined error codes.

— Asio is header-file-only and for most uses does not require linking against
  any Boost library.

  Boost.Asio always requires that you link against the Boost.System library,
  and also against Boost.Thread if you want to launch threads using boost::thread.



Should I use Asio or Boost.Asio ?
---------------------------------

It depends. Here are some things to consider:

— If you prefer the convenience of header-file-only libraries then using Asio
  over Boost.Asio is suggested.

— If you must use a version of Boost older than 1.35 then Boost.Asio is not
  included. You can use Boost.Asio by copying it over the top of your Boost
  distribution (see above), but not everyone is comfortable doing this.
  In that case, using Asio over Boost.Asio is suggested.

— New versions of both the Asio and Boost.Asio packages will be created on a
  faster release cycle than that followed by Boost.
  If you want to use the latest features you can still use Boost.Asio as long
  as you are happy to copy it over the top of your Boost distribution.
  If you don't want to do this, use Asio rather than Boost.Asio.

Can Asio and Boost.Asio coexist in the same program ?
------------------------------------------------------

Yes. Since they use different namespaces there should be no conflicts, although
obviously the types themselves are not interchangeable. (In case you're wondering
why you might want to do this, consider a situation where a program is using
third party libraries that are also using Asio internally.)

download
========

.. seealso::

   - http://www.boostpro.com/download/
   - http://sourceforge.net/projects/asio/files/asio/1.4.8%20%28Stable%29/



