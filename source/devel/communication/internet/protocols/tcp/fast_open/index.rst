
.. index::
   pair: Fast Open; TCP
   ! TCP Fast Open


.. _tcp_fast_open:

==============================================
TCP Fast Open Protocol
==============================================


.. seealso::

   - http://research.google.com/pubs/pub37517.html


.. contents::
   :depth: 3



Abstract
========

Today’s web services are dominated by TCP flows so short that they terminate a
few round trips after handshaking; this handshake is a significant source of
latency for such flows.

In this paper we describe the design, implementation, and deployment of the TCP
Fast Open protocol, a new mechanism that enables data exchange during TCP’s initial
handshake.

In doing so, TCP Fast Open decreases application network latency by one full
round-trip time, decreasing the delay experienced by such short TCP transfers.

We address the security issues inherent in allowing data exchange during the
three-way handshake, which we mitigate using a security token that verifies IP
address ownership.

We detail other fall-back defense mechanisms and address issues we faced with
middleboxes, backwards compatibility for existing network stacks, and incremental
deployment.

Based on traffic analysis and network emulation, we show that TCP Fast Open would
decrease HTTP transaction network latency by 15%and whole-page load time over 10%
on average, and in some cases up to 40








