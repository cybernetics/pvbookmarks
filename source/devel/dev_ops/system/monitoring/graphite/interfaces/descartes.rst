
.. index::
   pair: Graphite; Descartes


.. _descartes:

===========
Descartes
===========

.. seealso::

   - http://github.com/obfuscurity/descartes
  
  
.. contents::
   :depth: 3   
   
Purpose
========

Provide an additional level of insight and collaboration that is neither 
available nor appropriate for a real-time utility such as Tasseo.

Objectives
===========

Design, build and deploy a dashboard that allows users to correlate 
multiple metrics in a single chart, review long-term trends across one 
or more charts, and to collaborate with other users through a combination 
of annotations and related comment threads. 

This product should be capable of the following sample tasks:

* Display complex charts (2+ disparate metrics including transformations)
* Group related charts into a single view
* Timeshift charts within the same view
* Import existing graphs from external sources (e.g. Graphite API)
* Modify graphs using native interface tooling (i.e. users should not 
  have to use Graphite Composer to make changes)
* Create new graphs using native interface tooling
* Add notes (annotations) to charts
* Add comments associated with specific annotations

Deployment

``Descartes`` stores configuration data in PostgreSQL and Google OpenID state 
in Redis. 

It is assumed you have local PostgreSQL and Redis servers running for 
local development.
