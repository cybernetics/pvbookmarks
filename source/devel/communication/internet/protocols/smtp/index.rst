
.. index::
   pair: Internet; SMTP
   ! SMTP


.. _smtp:

=====================================
SMTP (Simple Mail Transfer Protocol)
=====================================


.. seealso::

   - https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol


.. contents::
   :depth: 3


Introduction
============

Simple Mail Transfer Protocol (SMTP) is an Internet standard for electronic mail
(e-mail) transmission across Internet Protocol (IP) networks.

SMTP was defined by:

- RFC 821 (1982, eventually declared STD 10),
- and last updated by RFC 5321 (2008) which includes the Extended SMTP (ESMTP) additions,
  and is the protocol in widespread use today.

SMTP uses TCP port 25. The protocol for new submissions (MSA) is effectively the
same as SMTP, but it uses port 587 instead. SMTP connections secured by SSL are
known by the shorthand SMTPS, though SMTPS is not a protocol in its own right.



SMTP servers
==============

.. toctree::
   :maxdepth: 3

   servers/index








