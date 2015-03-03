

.. index::
   pair: Crosstool ; NG
   ! Crosstool-NG


.. _crosstool_ng:

===========================================
Crosstool-NG
===========================================


.. seealso::

   - http://crosstool-ng.org/
   - http://ymorin.is-a-geek.org/projects/crosstool
   - :ref:`yann_morin` 


Introduction
============


**crosstool-NG aims at building toolchains**


Toolchains are an essential component in a software development project.
It will compile, assemble and link the code that is being developed. Some pieces
of the toolchain will eventually end up in the resulting binary/ies: static libraries
are but an example.

So, a toolchain is a very sensitive piece of software, as any bug in one of the
components, or a poorly configured component, can lead to execution problems,
ranging from poor performance, to applications ending unexpectedly, to mis-behaving
software (which more than often is hard to detect), to hardware damage, or even
to human risks (which is more than regrettable).

Toolchains are made of different pieces of software, each being quite complex
and requiring specially crafted options to build and work seamlessly.

This is usually not that easy, even in the not-so-trivial case of native toolchains.

The work reaches a higher degree of complexity when it comes to cross-compilation,
where it can become quite a nightmare...

Some cross-toolchains exist on the internet, and can be used for general development,
but they have a number of limitations:

- they can be general purpose, in that they are configured for the majority: no
  optimisation for your specific target,
- they can be prepared for a specific target and thus are not easy to use, nor
  optimised for, or even supporting your target,
- they often are using aging components (compiler, C library, etc…) not supporting
  special features of your shiny new processor;

On the other side, these toolchains offer some advantages:

- they are ready to use and quite easy to install and setup,
- they are proven if used by a wide community.

But once you want to get all the juice out of your specific hardware, you will
want to build your own toolchain. This is where crosstool-NG comes into play.

There are also a number of tools that build toolchains for specific needs, which
are not really scalable. Examples are:

- :ref:`buildroot` whose main purpose is to build complete root file systems, hence the
  name. But once you have your toolchain with buildroot, part of it is installed
  in the root-to-be, so if you want to build a whole new root, you either have
  to save the existing one as a template and restore it later, or restart again
  from scratch. This is not convenient,
- ptxdist, whose purpose is very similar to buildroot,
- other projects (openembedded for example), which is again used to build complete
  root file systems.

crosstool-NG is really targetted at building toolchains, and only toolchains.
It is then up to you to use it the way you want.

With crosstool-NG, you can learn precisely how each component is configured and
built, so you can finely tweak the build steps should you need it.

crosstool-NG can build from generic, general purpose toolchains, to very specific
and dedicated toolchains.
Simply fill in specific values in the adequate options.


Crosstool-NG source code
========================

.. seealso::

   - http://crosstool-ng.org/hg/crosstool-ng/


If you want to use the latest development stuff::

    hg clone http://crosstool-ng.org/hg/crosstool-ng
    cd crosstool-ng
    ./bootstrap
    ./configure --enable-local
    make
    ./ct-ng help
    ./ct-ng menuconfig
    ./ct-ng build




