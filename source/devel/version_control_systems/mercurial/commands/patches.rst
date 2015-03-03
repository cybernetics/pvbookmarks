
.. index::
   hg push --mq

========================
hg patches/hg push --mq
========================


::

    Floris Bruynooghe <floris.bruynooghe@gmail.com>
    à   bitbucket-users@googlegroups.com
    date    9 mars 2011 14:04
    objet   [Bitbucket] Re: How do I commit to a patch queue?
    liste de diffusion  <bitbucket-users.googlegroups.com> Filtrer les messages de cette liste de diffusion



Basically the .hg/patches directory is a versioned mercurial repo itself.
Your problem is that you forgot to commit this patches repo itself before
pushing it.

The old way of pusing the changes is::

    cd .hg/patches
    hg st
    hg ci -m "updated this cool patch"
    hg push

Or with a new enough mercurial the --mq option can be used::

    hg st --mq
    hg ci --mq -m "..."
    hg push --mq


Regards
Floris


