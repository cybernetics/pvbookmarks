
.. index::
   pair: Wikimedia;  Tools
   pair: Wikimedia;  Search
   
.. _wikimedia_tools:

===================
Wikimedia tools
===================

.. seealsoo

   - http://hexm.de/mw-search
   - http://www.mediawiki.org/wiki/Project:New_contributors#One_ontology

.. contents::
   :depth: 3


Introduction
============


::

    Sujet:  [Wikitech-l] Announcing the Wikimedia technical search tool
    Date :  Sun, 10 Mar 2013 14:50:16 +0000
    De :    Waldir Pimenta <waldir@email.com>
    Répondre à :    Wikimedia developers <wikitech-l@lists.wikimedia.org>
    Pour :  Wikimedia developers <wikitech-l@lists.wikimedia.org>


Hi all,

I'd like to announce a recently created tool that might help the Wikimedia
technical community find stuff more easily. Sometimes relevant information
is buried in IRC chat logs, messages in any of several mailing lists, pages
in mediawiki.org, commit messages, etc. This tool (essentially a custom
google search engine that filters results to a few relevant URL patterns)
is aimed at relieving this problem. Test it here: http://hexm.de/mw-search

The motivation for the tool came from a post by Niklas [1], specifically
the section "Coping with the proliferation of tools within your community".
In the comments section, Nemo announced his initiative to create a custom
google search to fit at least some of the requirements presented in that
section, and I've offered to help him tweak it further. The URL list is
still incomplete and can be customized by editing the page
http://www.mediawiki.org/wiki/Wikimedia_technical_search (syncing with the
actual engine still will have to happen by hand, but should be quick).

Besides feedback on whether the engine works as you'd expect, I would like
to start some discussion about the ability for Google's bots to crawl some
of the resources that are currently included in the URL filters, but return
no results. For example, the IRC logs at bots.wmflabs.org/~wm-bot/logs/.
Some workarounds are used (e.g. using github for code search since gitweb
isn't crawlable) but that isn't possible for all resources. What can we do
to improve the situation?


Waldir

1. http://laxstrom.name/blag/2013/02/11/fosdem-talk-reflections-23-docs-code-and-community-health-stability/

Python tools
============


.. toctree::
   :maxdepth: 4

   python/index
