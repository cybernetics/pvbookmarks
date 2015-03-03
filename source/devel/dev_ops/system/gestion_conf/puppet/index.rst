

.. index::
   ! Puppet


.. _puppet:

==========================
Puppet
==========================

.. seealso:: 

   - https://en.wikipedia.org/wiki/Puppet_%28software%29
  

.. contents::
   :depth: 3   

Description
===========

In computing, Puppet is an open source configuration management utility. 

It runs on many Unix-like systems as well as on Microsoft Windows, and includes 
its own declarative language to describe system configuration.


Origin
=======

Puppet is produced by Puppet Labs, founded by Luke Kanies in 2005. 

It is written in Ruby and released as free software under the GPL until version 
2.7.0 and the Apache 2.0 license after that.


Purpose
========

Puppet is a tool designed to manage the configuration of Unix-like and 
Microsoft Windows systems declaratively. 

The user describes system resources and their state, either using Puppet's 
declarative language or a Ruby DSL (domain-specific language). 

This information is stored in files called "Puppet manifests". 

Puppet discovers the system information via a utility called Facter, and 
compiles the Puppet manifests into a system-specific catalog containing resources 
and resource dependency, which are applied against the target systems. 

Any actions taken by Puppet are then reported.

