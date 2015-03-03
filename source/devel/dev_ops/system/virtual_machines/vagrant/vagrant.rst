
.. index::
   ! Vagrant


.. _vagrant:

============================
Vagrant
============================

.. seealso:: 

   - https://en.wikipedia.org/wiki/Vagrant_%28software%29
   - https://www.vagrantup.com/
  
.. figure:: Vagrant.png
   :align: center
   
      
.. contents::
   :depth: 3      
   
Description
============
   
``Vagrant`` is free and open-source software for creating and configuring virtual 
development environments.

It can be considered a wrapper around virtualization software such as VirtualBox 
and configuration management software such as Chef, Salt and Puppet.

Since version 1.1, Vagrant is no longer tied to VirtualBox and also works with 
other virtualization software such as VMware, and supports server environments 
like Amazon EC2.

Although written in Ruby, it is usable in projects written in other programming 
languages such as PHP, Python, Java, C# and JavaScript.

As of version 1.6, Vagrant provides native support for using Docker containers 
at runtime, in place of a fully virtualized operating system. 

This reduces overhead as Docker uses lightweight `Linux Containers`_.


.. _`Linux Containers`:  https://en.wikipedia.org/wiki/LXC


Why Vagrant ?
==============

``Vagrant`` provides easy to configure, reproducible, and portable work environments 
built on top of industry-standard technology and controlled by a single consistent 
workflow to help maximize the productivity and flexibility of you and your team.

To achieve its magic, Vagrant stands on the shoulders of giants. Machines are 
provisioned on top of VirtualBox, VMware, AWS, or any other provider. 

Then, industry-standard provisioning tools such as shell scripts, Chef, or Puppet, 
can be used to automatically install and configure software on the machine.


Versions
=========

.. toctree::
   :maxdepth: 3
   
   versions/versions
   
   


