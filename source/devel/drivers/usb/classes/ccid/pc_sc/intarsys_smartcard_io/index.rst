
.. index::
   pair: PC/SC; Smartcard.io
   pair: Java; Smartcard.io (Intarsys)
   ! Intarsys


.. _java_intarsys_smartcardio:

=========================================================================
Java Intarsys smartcard.io package (Alternate javax.smartcardio provider)
=========================================================================


.. seealso::

   - https://github.com/intarsys/smartcard-io
   - https://github.com/intarsys/native-c
   - https://github.com/intarsys/runtime
   - http://www.intarsys.de/
   - :ref:`java_smartcardio`

.. contents::
   :depth: 3


Resume
======

Generic, platform independent PC/SC wrapper and event driven card model. 

Alternative :ref:`javax.smartcardio <java_smartcardio>` provider with less 
PC/SC restrictions.

Preambule
==========

::

    Michael Traut <michael.traut@gmail.com>
    répondre à:  MUSCLE <muscle@lists.musclecard.com>
    à:   MUSCLE <muscle@lists.musclecard.com>
    date:    5 juillet 2013 13:32
    objet:   Re: [Muscle] RES: RES: Parallel Process with readers - pcsc-lite

We already have a platform independent native adapter to pcsc and pcsc-lite. 

We developed this before smartcardio popped up and never switched because of 
the limitations of smartcardio - it is used in our (closed-source) EAL 
certified signature application.

We'd like to donate this lib if anybody is interested...

The runtime stack consists of

- JNA runtime
- intarsys native memory model (as we dislike the JNA abstractions...). 
  This is already BSD licensed (via jPod on SourceForge)
- intarsys PCSC wrapper (including all SCARD features WE needed so far)
- intarsys Card abstraction. A small layer on top of PCSC, with some features 
  we found very useful in the years.


Introduction
=============

This project contains a PC/SC wrapper and smartcard abstraction layer.

In addition an alternative javax.smartcardio provider is provided.


License
========

::

    /*
     * Copyright (c) 2013, intarsys consulting GmbH
     *
     * Redistribution and use in source and binary forms, with or without
     * modification, are permitted provided that the following conditions are met:
     *
     * - Redistributions of source code must retain the above copyright notice,
     *   this list of conditions and the following disclaimer.
     *
     * - Redistributions in binary form must reproduce the above copyright notice,
     *   this list of conditions and the following disclaimer in the documentation
     *   and/or other materials provided with the distribution.
     *
     * - Neither the name of intarsys nor the names of its contributors may be used
     *   to endorse or promote products derived from this software without specific
     *   prior written permission.
     *
     * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
     * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
     * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
     * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
     * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
     * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
     * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
     * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
     * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
     * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
     * POSSIBILITY OF SUCH DAMAGE.
     */


Service & Support
===================

If you need further support, feel free to contact us.


::

    intarsys consulting GmbH
    Kriegstrasse 100
    76135 Karlsruhe
    Fon +49 721 38479-0
    Fax +49 721 38479-60
    info@intarsys.de
    www.intarsys.de

For service and support contact support@intarsys.de


Examples
========

.. seealso::

   - http://ludovicrousseau.blogspot.fr/2010/06/pcsc-sample-in-java.html


News
====

.. toctree::
   :maxdepth: 3
   
   news/index
   
   




