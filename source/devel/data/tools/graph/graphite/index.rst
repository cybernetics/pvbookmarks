

.. index::
   pair: Data ; Graph
   pair: Tool ; Graph

.. _python_graphite:

========================
Python graphite
========================


.. seealso::

   - http://graphite.wikidot.com/start
   - https://graphite.readthedocs.org/en/latest/index.html

.. contents::
   :depth: 3

What Graphite is and is not
===========================

Graphite does two things:

1. Store numeric time-series data
2. Render graphs of this data on demand

What Graphite does not do is collect data for you, however there are some tools_ out
there that know how to send data to graphite.

Even though it often requires a little code, `sending data`_ to Graphite is very simple.


.. _tools: https://graphite.readthedocs.org/en/latest/tools.html
.. _`sending data`: https://graphite.readthedocs.org/en/latest/feeding-carbon.html

About the project
=================

Graphite is an enterprise-scale monitoring tool that runs well on cheap hardware. It was
originally designed and written by `Chris Davis`_ at `Orbitz`_ in 2006 as side project that
ultimately grew to be a foundational monitoring tool. In 2008, Orbitz allowed Graphite to be
released under the open source Apache 2.0 license. Since then Chris has continued to work on
Graphite and has deployed it at other companies including `Sears`_, where it serves as a pillar
of the e-commerce monitoring system.

Today many large companies_ use it.


.. _companies:  https://graphite.readthedocs.org/en/latest/who-is-using.html


The architecture in a nutshell
==============================

Graphite consists of 3 software components:

1. **carbon** - a `Twisted`_ daemon that listens for time-series data
2. **whisper** - a simple database library for storing time-series data (similar in design to `RRD`_)
3. **graphite webapp** - A `Django`_ webapp that renders graphs on-demand using `Cairo`_


`Feeding in your data`_ is pretty easy, typically most
of the effort is in collecting the data to begin with. As you send datapoints
to Carbon, they become immediately available for graphing in the webapp. The
webapp offers several ways to create and display graphs including a simple
`URL API`_ for rendering that makes it easy to embed graphs in other
webpages.


.. _Django: http://www.djangoproject.com/
.. _Twisted: http://www.twistedmatrix.com/
.. _Cairo: http://www.cairographics.org/
.. _RRD: http://oss.oetiker.ch/rrdtool/
.. _Chris Davis: mailto:chrismd@gmail.com
.. _Orbitz: http://www.orbitz.com/
.. _Sears: http://www.sears.com/
.. _`Feeding in your data`:  https://graphite.readthedocs.org/en/latest/feeding-carbon.html
.. _`URL API`: https://graphite.readthedocs.org/en/latest/render_api.html

Examples
========

.. seealso::

   - http://coreygoldberg.blogspot.fr/2012/04/python-getting-data-into-graphite-code.html

Articles
========

GNU/Linux Magazine, Janvier 2013
--------------------------------

:titre: Vos graphiques avec Graphite

p. 18 à 29.




