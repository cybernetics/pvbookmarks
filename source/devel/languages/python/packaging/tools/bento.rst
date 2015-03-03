
.. index::
   pair: Python; bento
   pair: David Cournapeau; packaging

.. _python_bento:

=======================
Bento, packaging
=======================

.. seealso::

   - http://cournape.github.com/Bento/html/index.html
   - http://cournape.github.com/Bento/



.. contents::
   :depth: 3


Introduction
============

Bento is a packaging tool solution for python softwares, targeted as an
alternative to distutils, setuptools, distribute, etc....

Bento philosophy is reproducibility, extensibility and simplicity (in that order).

Bento is under constant development. The main implemented features are

- Declarative description of your package. Metadata and package content are
  described in a simple format.
- Flexible installation scheme: you can install any file anywhere.
- Layered internal architecture: core functionalities, command line interface
  are clearly separated: bento is designed as a library from the ground-up.
- Hackable and extensible: bento is designed to be extensible: commands are not
  hardly coupled, and new ones can be inserted between existing ones without the
  need for monkey-patching.
- Scale down: a core principle of bento is to make software easier to package,
  and avoid too many choices for packages with simple needs.
- Scale up: on the other hand, bento is designed for complex packages. Bento is
  already capable to build numpy and scipy with less code than distutils.
- Distutils Compatibility Layer: bento can convert an existing distutils package
  into the bento format. Bento packages can be installed with tools which
  normally expect a setup.py (pip, easy_install, etc...).


Reaction de Tarek (21 juin 2012)
================================

::

    David Cournapeau's Bento project takes the opposite approach, everything is explicit and without any magic.
    http://cournape.github.com/Bento/
    It had its 0.1.0 release a week ago.
    Please, I don't want to reopen any discussions about Bento here -- distutils2 vs.
    Bento discussions have been less than constructive in the past -- I just wanted
    to make sure everybody is aware that distutils2 isn't the only horse in this race.
    I don't know if there are others too?


That's *exactly* the kind of approach that has made me not want to continue.

People are too focused on implementations, and 'how distutils sucks'
'how setuptools sucks' etc 'I'll do better' etc

Instead of having all the folks involved in packaging sit down together and try
to fix the issues together by building PEPs describing what would be a common
set of standards, they want to create their own tools from scratch.

That will not work. And I will say here again what I think we should do imho:

1. take all the packaging PEPs and rework them until everyone is happy
   compilation sucks in distutils ?  write a PEP !!!

2. once we have a consensus, write as many tools as you want, if they rely on
   the same standards => interoperability => win.

But I must be naive because everytime I tried to reach people that were building
their own tools to ask them to work with us on the PEPs, all I was getting was
"distutils sucks!'

It worked with the OS packagers guys though, we have built a great data files
managment system in packaging + the versions (386)


Declare stable, include in 3.3
------------------------------

::

    On Wed, Jun 20, 2012 at 9:31 PM, Tarek Ziadé<tarek@ziade.org>  wrote:
        Yeah maybe this subset could be left in 3.3
        and we'd remove packaging-the-installer part (pysetup, commands, compilers)
        I think it's a good idea !
    OK, to turn this into a concrete suggestion based on the packaging docs.
    Declare stable, include in 3.3
    ------------------------------------------
        packaging.version — Version number classes
        packaging.metadata — Metadata handling
        packaging.markers — Environment markers
        packaging.database — Database of installed distributions

I think that's a good subset.

+1 on all of the things you said after

If you succeed on getting the sci people working on "PEP: Distutils replacement:
Compiling Extension Modules" it will be a big win.



