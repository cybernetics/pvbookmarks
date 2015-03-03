

.. index::
   ivy (C library)

.. _ivy_c_library:

=============
ivy C library
=============

.. seealso:: http://www2.tls.cena.fr/products/ivy/documentation/ivy-c/index.html


The Ivy C library (aka Ivy-C or ivy-c) is a C library that allows you to 
connect applications to an Ivy bus. You can use it to write applications 
in C or any other language that supports C extensions. 

You can also use it **to integrate an application that already has a main loop** 
(such as a GUI application) within an Ivy bus. 
This guide is here to help you do that.
   
  
Basic functions
===============

.. seealso:: http://www2.tls.cena.fr/products/ivy/documentation/ivy-c/x76.html
  
Initialization and main loop (IvyMainLoop)
------------------------------------------

The Ivy C library provides its own main loop: IvyMainLoop. You should use it 
unless you already use a toolkit that provides its own main loop and you want 
to use that one. If it is the case, please refer to section XX. Otherwise, 
just call IvyMainLoop. From within the main loop, you can call IvyStop to exit 
the loop.


Using Ivy with another main loop
================================

.. seealso:: http://www2.tls.cena.fr/products/ivy/documentation/ivy-c/x200.html

The ivyprobe source code holds examples of use of Ivy within other main loops, 
namely Xt and Gtk.

Adding Ivy to another main loop
===============================


You can decide to use the main loop from another toolkit than the X Toolkit 
or the Tk toolkit. If you do that, you'll have to define four functions that 
Ivy will use to get its own channels managed by the other toolkit. you should 
link ivy with your new module insted of the ivy(xxx)loop module. 

These functions are declared in ivychannel.h: 

- IvyChannelInit
- IvyChannelStop
- IvyChannelAdd
- IvyChannelRemove

