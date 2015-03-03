
.. index::
   pair: PEX ; Format
   ! PEX


.. _pex:
.. _pex_format:

===========================
PEX
===========================


.. seealso::

   - https://github.com/twitter/commons/tree/master/src/python/twitter/common/python


.. contents::
   :depth: 3

Introduction
============

::

    Sujet:  [Distutils] PEX at Twitter (re: PEX - Twitter's multi-platform executable archive format for Python)
    Date :  Fri, 31 Jan 2014 11:31:02 -0800
    De :    Brian Wickman <wickman@gmail.com>
    Pour :  DistUtils mailing list <distutils-sig@python.org>



This is in response to Vinay's thread but since I wasn't subscribed to
distutils-sig, I couldn't easily respond directly to it.

Vinay's right, the technology here isn't revolutionary but what's
notable is that we've been using it in production for almost 3 years at
Twitter.  

It's also been open-sourced for a couple years at 
https://github.com/twitter/commons/tree/master/src/python/twitter/common/python
but not widely announced (it is, after all, just a small subdirectory in
a fairly large mono-repo, and was only recently published independently
to PyPI as twitter.common.python.)

PEX files are just executable zip files with hashbangs containing a
carefully constructed __main__.py and a PEX-INFO, which is json-encoded
dictionary describing how to scrub and bootstrap sys.path and the like.

They work equally well unpacked into a standalone directory.

In practice PEX files are simultaneously our replacement for virtualenv
and also our way of distributing Python applications to production.  

Now we could use virtualenv to do this but it's hard to argue with a
deployment process that is literally "cp".  
Furthermore, most of our machines don't have compiler toolchains or external 
network access, so hermetically sealing all dependencies once at build time 
(possibly for multiple platforms since all developers use Macs) has huge appeal.  

This is even more important at Twitter where it's common to run a dozen
different Python applications on the same box at the same time, some
using 2.6, some 2.7, some PyPy, but all with varying versions of
underlying dependencies.

Speaking to recent distutils-sig threads, we used to go way out of our
way to never hit disk (going so far as building our own .egg packager
and pure python recursive zipimport implementation so that we could
import from eggs within zips, write ephemeral .so's to dlopen and
unlink) but we've since moved away from that position for simplicity's
sake.  

For practical reasons we've always needed "not zip-safe" PEX files where all 
code is written to disk prior to execution (ex: legacy Django applications that 
have __file__-relative business logic) so we decided to just throw away the 
magical zipimport stuff and embrace using disk as a pure cache.  

This seems more compatible philosophically with the direction wheels are going 
for example.

Since there's been more movement in the PEP space recently, we've been evolving 
PEX in order to be as standards-compliant as possible, which is why I've been 
more visible recently re: talks, .whl support and the like.  

I'd also love to chat about more about PEX and how it relates to things like 
PEP 441 and/or other attempts like pyzzer.

cheers,

brian
twitter.com/wickman <http://twitter.com/wickman>


PEX news
========

.. toctree::
   :maxdepth: 3
   
   news/index
   
 
PEX based appli
===============

.. toctree::
   :maxdepth: 3
   
   pex_based_appli/index 
   
PEX tools
==========

.. toctree::
   :maxdepth: 3
   
   tools/index
   
      
   
