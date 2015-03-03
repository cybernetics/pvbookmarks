
.. index::
   git flow (nuitka)

.. _nuitka_git_flow:

===============
Nuitka git flow
===============

.. image:: Nuitka-git-flow.png

.. seealso:: http://www.nuitka.net/blog/2011/10/nuitka-git-flow/

Benefits of the new model
=========================

Hotfixes, typically bug fixes, can be made simultaneously on stable and 
develop branch. The git-flow package takes care of the merging to both.

Because that’s so easy now, a stable version can be provided and supported for 
a longer time.
Features can be published while under development. My idea is that feature 
branches should basically work, but the bar will be lower. People can have a 
look at them, or start their own and make me integrate them.

Uses of Feature Branch
======================

For example, in the new feature branch, a couple of boring things are happening. 
Support for frame stack will reduce the diff, as will some work to match 
CPython’s choices for exception line numbers. Completing will take a while, 
but should not block a release. So this is best done in the feature branch, 
esp. as nothing is going to really depend on it.

General Picture
===============

As you can see from this diagram, I am working mostly on documentation things. 
The new and improved README on develop, which is closer to a User Manual 
in PDF form, and other organization things, may get a release before the 
PyCon DE next week. The README also describes this process.

Hope is that with this approach, I will improve transparency (you can see 
earlier what i am working on, because there is now a place where things 
may break (develop) or may not yet be integrated or completed fully 
(feature branches) and yet be public.

The overhead appears to minimal thanks to git-flow. Developing hotfixes is 
actually easier, when done on the stable branch, because problems cannot 
originate from the current development work that may or may not be all that 
perfect yet.

Yours,
Kay Hayen
