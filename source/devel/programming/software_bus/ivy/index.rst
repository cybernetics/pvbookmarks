

.. index::
   ivy (software bus)

.. _ivy:

====
ivy
====

.. seealso:: http://www2.tls.cena.fr/products/ivy/

Ivy is a simple protocol and a set of open-source (LGPL) libraries and programs 
that allows applications to broadcast information through text messages, with 
a subscription mechanism based on regular expressions. 

Ivy libraries are available in C, C++, Java, Python and Perl, on Windows and 
Unix boxes and on Macs. 
Several Ivy utilities and hardware drivers are available too.

Ivy is currently used in research projects in the air traffic control and 
human-computer interaction research communities as well as in commercial 
products. It is also taught to CS students. 


A software bus
==============

.. seealso:: http://www2.tls.cena.fr/products/ivy/about.shtml

A software bus is a system that allows software applications to exchange 
information with the illusion of broadcasting that information, selection 
being performed by the receiving applications based on the contents of the 
messages. Other denominations are sometimes **publish-subscribe notification services** 
or **message-oriented middleware**. 

**Software buses federate pieces of software written in different programming 
languages on different platforms**. 

The main features of Ivy
========================

Ivy is not based on a centralised server. Actually, Ivy is mostly a 
communication convention, implemented through a collection of libraries 
for various languages and platforms. 
The current version of the Ivy protocol is version 3, which has been stable 
for the last 3 years.
Language bindings are available in C (Unix and Windows), C++ (Mac, Unix, Windows), 
Java and Perl. There have been successful uses through the C library.

Messages are formatted in text, and subscriptions are based on regular 
expressions. Plans to move to an XML-based subscription language are on their way.

From the programmer's point of view, Ivy is an information broadcasting channel. 
The main functions are:

- connecting to a bus. Example: IvyInit (b, "192.126:2011")
- sending a message. Example: IvySend (b, "HELLO %s", world)
- binding a message pattern to a callback function. Example: IvyBind 
  (b, "HELLO (.*)", cb)
- the main loop. Example : IvyLoop () 

Subscriptions are managed on the emitter's side, which limits the actual 
network traffic. Direct point-to-point messages are also available.

Ivy was designed by a research group in Human-Computer Interaction, with 
the goals of connecting applications written on different 
toolkits/languages/platforms (such as an OpenGL application on a SGI 
connected to a PerlTk application on a Linux box), while keeping it simple: 
no server to be lauched and supervised, a simplistic API, and a communication 
model compatible with classical event-based GUI progamming. 
We think we have somewhat reached our goal. 

Latest news
===========

january 17th, 2011
------------------

- ivy-c (and other libraries based on it) is now compatible with IPv6
- ivy-c++ is now compatible with Qt mainloop
- Inventor node for coin3d 3D rendering library 


.. toctree::
   :maxdepth: 4
   
   applications
   libraries/index
   
