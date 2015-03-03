

.. index::
   pair: Remote Admin; x2go


.. _x2go_install: 

=======================
x2go install
=======================

.. seealso:: 

   - https://codeghar.wordpress.com/2011/11/15/remote-desktop-in-ubuntu-oneiric-ocelot/

I have always used VNC to remotely connect to a Linux desktop. 

On Windows it’s been RDP. 

I came across a much better way than VNC to connect to my Kubuntu desktop: x2go. 

The application is absolutely wonderful and dead easy to install on Kubuntu. 
But its documentation is a confusing mess. Fortunately, we don’t really need 
to use the documentation that much.

Server
======

::

	sudo add-apt-repository ppa:x2go/stable
	You are about to add the following PPA to your system:
	x2go stable ppa
	Quick howto to turn your machine into an x2go server:
	sudo apt-add-repository ppa:x2go/stable
	sudo apt-get update
	sudo apt-get install x2goserver
	sudo apt-get install x2gognomebindings # if you use GNOME
	sudo apt-get install x2golxdebindings  # if you use LXDE/lubuntu

x2goclient
==========

::

	sudo apt-add-repository ppa:x2go/stable
	sudo apt-get update
	sudo apt-get install x2goclient













