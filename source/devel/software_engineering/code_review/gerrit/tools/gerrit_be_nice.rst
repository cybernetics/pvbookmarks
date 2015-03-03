
.. index::
   pair: Gerrit; Wikitech

.. _gerrit_be_nice:

=====================
Git be nice
=====================


.. seealso::

   - https://github.com/jdlrobson/gerrit-be-nice-to-me
   - https://raw.github.com/jdlrobson/gerrit-be-nice-to-me/master/README.txt
   - :ref:`git`

Context
=======

::

    Jon Robson <jdlrobson@gmail.com>
    répondre à:  Wikimedia developers <wikitech-l@lists.wikimedia.org>
    à:   Wikimedia developers <wikitech-l@lists.wikimedia.org>
    date:    3 avril 2013 07:14
    objet:   Re: [Wikitech-l] Gerrit actively discourages discussion
    liste de diffusion:  wikitech-l.lists.wikimedia.org


I feel very dirty having done this but I made a chrome extension that
autoexpands all comments and adds a comment count next to unexpanded older
patchsets.

The code's horrible but it works - feel free to try it out:

https://github.com/jdlrobson/gerrit-be-nice-to-me

I suspect the best long term solution might be to rewrite the interface.
The fact it is so ajaxay makes enhancements hard unless someone actually
wants to get to know and work on the gerrit codebase themselves...


::

    On Tue, Apr 2, 2013 at 7:54 PM, MZMcBride <z@mzmcbride.com> wrote:

    > Christian Aistleitner wrote:
    > >while I do not want to discourage discussion of those items on
    > >wikitech-l, I nevertheless filed them in bugzilla, so we can keep
    > >track of the issues / solutions.
    >
    > This is wonderful. Thank you for filing these bugs, Christian. I'll take a
    > look at them now.
    >
    > MZMcBride


Setup
=====

* Go to chrome://extensions/
* Click Developer mode checkbox in top right
* Click load unpacked extension
* Navigate to this directory and enable
* Visit Gerrit for a few UI tweaks
