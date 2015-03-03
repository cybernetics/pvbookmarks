


.. index::
   pair: Tutorial ; Mediawiki

.. _mediawiki_api_tutorial:

=======================
Mediawiki API tutorial
=======================

.. seealso::

   - https://www.mediawiki.org/wiki/API/Tutorial

Tutorial for MediaWiki's RESTful web service API
================================================

Why should you use the web API? Bots, AJAX, Gadgets, other things.

Roan says: generally any Ajax feature is going to use the api.php entry 
point. 

But right now the easiest thing to do is to write a bot or to use 
the API clients.


Definitions
============

REST API for MediaWiki exposes things MediaWiki has in the database or 
otherwise understands does not include semantic stuff like "definition 
of a word in Wiktionary" or even "lead paragraph of an article"

Usage 
======
send HTTP requests (GET or POST) to the api.php URL, receive XML or JSON 
or other formats. 

You'll usually want JSON or XML.

w:en:JSON and w:en:XML and w:en:Representational state transfer (RESTful)

There are other things that also get casually called the MediaWiki API, 
like the internal interfaces that extensions and special pages can hook 
into. 

We're not talking about that right now, just the web API.
(possibly talk about how it works from the back end, if people ask)...
