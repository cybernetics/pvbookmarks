
.. index::
   ! Heartbleed


.. _Heartbleed:

===================
Heartbleed
===================



.. seealso::

   - http://heartbleed.com/
   - https://www.schneier.com/blog/archives/2014/04/heartbleed.html
   - http://www.smh.com.au/it-pro/security-it/man-who-introduced-serious-heartbleed-security-flaw-denies-he-inserted-it-deliberately-20140410-zqta1.html




The fix
=======



OpenSSL Security Advisory [07 Apr 2014]
----------------------------------------

.. seealso::

   - https://www.openssl.org/news/secadv_20140407.txt

TLS heartbeat read overrun (CVE-2014-0160)
+++++++++++++++++++++++++++++++++++++++++++

A missing bounds check in the handling of the TLS heartbeat extension can be
used to reveal up to 64k of memory to a connected client or server.

Only 1.0.1 and 1.0.2-beta releases of OpenSSL are affected including
1.0.1f and 1.0.2-beta1.

Thanks for Neel Mehta of Google Security for discovering this bug and to
Adam Langley <agl@chromium.org> and Bodo Moeller <bmoeller@acm.org> for
preparing the fix.

Affected users should upgrade to OpenSSL 1.0.1g. Users unable to immediately
upgrade can alternatively recompile OpenSSL with -DOPENSSL_NO_HEARTBEATS.

1.0.2 will be fixed in 1.0.2-beta2.


Articles 
========

.. toctree::
   :maxdepth: 3
   
   articles/index
   
   
