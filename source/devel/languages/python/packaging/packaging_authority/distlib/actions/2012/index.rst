
.. index::
   pair: Dislib ; 2012


.. _distlib_2012:


===============================
Distlib 14 décembre 2012 02:06
===============================

::

    de:  Nick Coghlan <ncoghlan@gmail.com> via python.org
    à:   Antonio Cavallo <a.cavallo@cavallinux.eu>
    cc:  "distutils-sig@python.org" <distutils-sig@python.org>,
     python-dev@python.org
    date:    14 décembre 2012 02:06
    objet:   Re: [Python-Dev] [Distutils] Is is worth disentangling distutils?


    I'll have a look into distutils2, I tough it was (another) dead end.
    I every case my target is py2k (2.7.x) and I've no case for transitioning to py3k (too much risk).


``distutils2`` started as a copy of distutils, so it's hard to tell the difference
between the parts which have been fixed and the parts which are still just
distutils legacy components (this is why the merge back was dropped from 3.3 -
too many pieces simply weren't ready and simply would have perpetuated problems
inherited from distutils).

``distlib`` (https://distlib.readthedocs.org/en/latest/overview.html) is a successor
project that takes a different view of building up the low level pieces without
inheriting the bad parts of the distutils legacy (a problem suffered by both
setuptools/distribute and distutils2).

distlib also runs natively on both 2.x and 3.x, as the idea is that these
interoperability standards should be well supported in *current* Python versions,
not just those where the stdlib has caught up (i.e. now 3.4 at the earliest)

The aim is to get to a situation more like that with wsgiref, where the stdlib d
efines the foundation and key APIs and data formats needed for interoperability,
while allowing a flourishing ecosystem of user-oriented tools (like pip, bento,
zc.buildout, etc) that still solve the key problems addressed by setuptools/distribute
without the opaque and hard to extend distutils core that can make the existing
tools impossible to debug when they go wrong.







