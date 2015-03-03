.. module:: CompilingDrivers
    :synopsis: compiling linux Drivers
    :platform: GNU/Linux
  
 
.. index::
   compiling a linux driver
   kbuild system
   
========================
Compiling a linux driver
========================


.. _kbuild_system:

The new kbuild system
=====================


.. seealso:: http://tjworld.net/books/ldd3/#5


As the first step, we need to look a bit at how modules must be built. The 
build process for modules differs significantly from that used for user-space 
applications; the kernel is a large, stand alone program with detailed and 
explicit requirements on how its pieces are put together. The build process 
also differs from how things were done with previous versions of the kernel; 
the new build system is simpler to use and produces more correct results, but 
it looks very different from what came before. The kernel build system is a 
complex beast, and we just look at a tiny piece of it. The files found in 
the Documentation/kbuild directory in the kernel source are required reading 
for anybody wanting to understand all that is really going on beneath the surface.

There are some prerequisites that you must get out of the way before you can build 
kernel modules. The first is to ensure that you have sufficiently current versions 
of the compiler, module utilities, and other necessary tools. 

The file Documentation/Changes in the kernel documentation directory always lists 
the required tool versions; you should consult it before going any further. 
Trying to build a kernel (and its modules) with the wrong tool versions can 
lead to no end of subtle, difficult problems. Note that, occasionally, a version 
of the compiler that is too new can be just as problematic as one that is too old; 
the kernel source makes a great many assumptions about the compiler, and new 
releases can sometimes break things for a while.

If you still do not have a kernel tree handy, or have not yet configured and 
built that kernel, now is the time to go do it. You cannot build loadable modules 
for a 2.6 kernel without this tree on your filesystem. It is also helpful 
(though not required) to be actually running the kernel that you are building for.

Once you have everything set up, creating a makefile for your module is 
straightforward. In fact, for the "hello world" example shown earlier in this 
chapter, a single line will suffice::

	obj-m := hello.o

Readers who are familiar with make, but not with the 2.6 kernel build system, 
are likely to be wondering how this makefile works. The above line is not how a 
traditional makefile looks, after all. The answer, of course, is that the 
kernel build system handles the rest. The assignment above (which takes advantage 
of the extended syntax provided by GNU make) states that there is one module to 
be built from the object file hello.o. The resulting module is named hello.ko 
after being built from the object file.

If, instead, you have a module called module.ko that is generated from two source 
files (called, say, file1.c and file2.c), the correct incantation would be::

	obj-m := module.o
	module-objs := file1.o file2.o

For a makefile like those shown above to work, it must be invoked within the 
context of the larger kernel build system. If your kernel source tree is 
located in, say, your ~/kernel-2.6 directory, the make command required to 
build your module (typed in the directory containing the module source and 
makefile) would be:

	make -C ~/kernel-2.6 M=`pwd` modules

This command starts by changing its directory to the one provided with 
the -C option (that is, your kernel source directory). There it finds 
the kernel's top-level makefile. The M= option causes that makefile to 
move back into your module source directory before trying to build the 
modules target. This target, in turn, refers to the list of modules found 
in the obj-m variable, which we've set to module.o in our examples.

Typing the previous make command can get tiresome after a while, so the 
kernel developers have developed a sort of makefile idiom, which makes 
life easier for those building modules outside of the kernel tree. 
The trick is to write your makefile as follows::

	# If KERNELRELEASE is defined, we've been invoked from the
	# kernel build system and can use its language.
	ifneq ($(KERNELRELEASE),)
		obj-m := hello.o

	# Otherwise we were called directly from the command
	# line; invoke the kernel build system.
	else

		KERNELDIR ?= /lib/modules/$(shell uname -r)/build
		PWD  := $(shell pwd)

	default:
		$(MAKE) -C $(KERNELDIR) M=$(PWD) modules

	endif


Once again, we are seeing the extended GNU make syntax in action. 
This makefile is read twice on a typical build. When the makefile is invoked 
from the command line, it notices that the KERNELRELEASE variable has not been 
set. It locates the kernel source directory by taking advantage of the fact 
that the symbolic link build in the installed modules directory points back 
at the kernel build tree. If you are not actually running the kernel that 
you are building for, you can supply a KERNELDIR= option on the command line, 
set the KERNELDIR environment variable, or rewrite the line that sets 
KERNELDIR in the makefile. 
Once the kernel source tree has been found, the makefile invokes the 
default: target, which runs a second make command (parameterized in the 
makefile as $(MAKE)) to invoke the kernel build system as described previously. 
On the second reading, the makefile sets obj-m, and the kernel makefiles take 
care of actually building the module.

This mechanism for building modules may strike you as a bit unwieldy and 
obscure. Once you get used to it, however, you will likely appreciate the 
capabilities that have been programmed into the kernel build system. 
Do note that the above is not a complete makefile; a real makefile includes 
the usual sort of targets for cleaning up



