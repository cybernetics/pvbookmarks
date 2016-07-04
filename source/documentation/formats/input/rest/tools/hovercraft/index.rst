

.. index::
   pair: Rest ; Hovercraft
   pair: Rest ; Presentation
   pair: Impress.js ; Hovercraft
   pair: Lennart ; Regebro
   ! Hovercraft

.. _hovercraft:

=======================
Hovercraft
=======================

.. seealso::

   - https://github.com/regebro/hovercraft
   - http://bartaz.github.com/impress.js/#/bored
   - https://github.com/regebro/hovercraft/tree/master/docs


.. contents::
   :depth: 3



Hovercraft Documentation
========================

.. seealso:: https://hovercraft.readthedocs.org/en/1.0/


Hovercraft source code
======================

.. seealso:: https://github.com/regebro/hovercraft

Announce
=========

.. seealso:: http://regebro.wordpress.com/2013/02/07/presenting-hovercraft-the-merge-of-convenience-and-cool/


reStructuredText
----------------

reStructuredText, reST or RST, is a so called “lightweight” markup language.
Although there is nothing lightweight about it, it is in fact massive and have
an incredible amount of features, which is one reason it’s popular.

It’s used a lot within the Python community, and is often used to write everything
from readme files to books.

There are other languages that have their benefits, most notably Markdown and
textile, but I don’t know if any of them have the feature set required for Hovercraft,
and I’m used to reStructuredText.

There are several ways to make slides from reStructuredText.

One is included in the docutils library that implements reStructuredText, and it
can generate **S5 slides**.

Another is Landslide, which i have used as it has a presenter console. But these
generate standard left-to-right slide presentations in HTML.
Nothing wrong with that, but it’s a bit boring.

Enter impress.js.

impress.js
----------

impress.js is a tool to make HTML presentations that zoom and rotate.

It’s cool and I used that to make a zooming/panning version of my talk on
intellectual properties.  And then I made a presentation about Calendaring
for PyCon PL 2012 and PloneConf 2012. And by that time I was seriously tired of it,
because you write your presentations in HTML, and that sucks in itself, and
then you have to position each slide separately.

That worked fine in the first case, where I had this huge image to zoom around it.
But for the Calendaring talk I ended up having to reposition a lot of slides
each time I needed to insert or delete a slide.
Not a practical solution.

I needed to somehow be able to write reStrcuturedText and get impress.js out.
After a false start with a template for Landslide, I hit on the solution:
Use docutils to generate XML from reStructuredText and the use XSLT to transform
it into an impress.js presentation.

That worked, and the solution is Hovercraft!

Hovercraft!
===========

*The merging of convenience and cool!*

Hovercraft! is a tool to make impress.js_ presentations from reStructuredText.

Documentation is currently sparse, but available in the `documentation subdirectory`_.


.. _`documentation subdirectory`: https://github.com/regebro/hovercraft/tree/master/docs


Why?
----

As a programmer, I like making my presentations in some sort of text-markup.

GUI tools feel restricted and limited when it comes to creating the
presentation, simply writing it in text makes it easier to move things around
as you like.

But the tools that exist to make presentations from text-markup will make
slideshows that has a sequence of slides from left to right. That was fine
until Prezi arrived, with zooms and slides and twists and turns.

But Prezi is a GUI toool.
And it's closed source.
But the open source community fixed that problem with impress.js.

But impress.js is an HTML tools.
Sitting and writing HTML is an annoying pain.
**It's not a very smooth tool compared reStructuredText or markdown.**

It's especially annoying since you have to sit and add x/y/zoom/rotation
for each slide, and if you insert a new slide in the middle, you have to
change everything around.

There are GUI tools to layout impress.js presentations but they are all in
alpha-state, and doesn't work very well. They also do not support having
presenter notes via impress-console_, a feature I of course need. After all,
that's why I wrote it.

So, I wanted to make impress.js presentations from reStructuredText.

That turned out to be easy, I make landslide-impress_, a template for Landslide
that create an impress.js presentation.
But I ran into a limitation of Landslide. There was no way to get the position
information out from the reStructuredText to impress.js.

As such, with Landslide all I could do with impress.js was slides that boringly
went from left to right, completely losing the whole point of impress.js.

So, I have to make something myself. Hence: Hovercraft!

Contributors
------------

Hovercraft! was written by Lennart Regebro <regebro@mail.com>, and is licensed
as CC-0, except for the following:

* ``reST.xsl`` is (c) Michael Alyn Miller <malyn@strangeGizmo.com> and
  published under a BSD-style license included in reST.xsl itself.

* ``impress.js`` is (c) Bartek Szopka (@bartaz) released under MIT and GPL
  licenses. See the impress.js_ page for more information.

.. _impress.js: http://github.com/bartaz/impress.js
.. _landslide-impress: https://github.com/regebro/landslide-impress
.. _impress-console: https://github.com/regebro/impress-console


Demo
====

.. seealso::

   - https://github.com/regebro/hovercraft
   - http://bubbly.colliberty.com/slides/PyConUS-2013


Hovercraft news
================

.. toctree::
   :maxdepth: 3
   
   news/index
   
   

