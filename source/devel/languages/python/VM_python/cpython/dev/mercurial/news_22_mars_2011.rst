
====================================================
CPython mercurial learning, march 22 march 2011
====================================================


::

    de   rndblnch <rndblnch@gmail.com>
    à   python-dev@python.org
    date    22 mars 2011 13:06
    objet   Re: [Python-Dev] Let's get PEP 380 into Python 3.3
    liste de diffusion  python-dev.python.org Filtrer les messages de cette liste de diffusion


> On Tue, Mar 22, 2011 at 9:21 AM, Guido van Rossum <guido <at> python.org> wrote:
> > In the light of the recent discussion about Hg clones, perhaps you
> > could make this a server-side clone so it's easier for others to play
> > along?

I don't have push rights so I can not push anything to <http://hg.python.org/>.
However, I tried to click the "server side clone", and to my surprise, it
worked. I was expecting that some verification would be made, but there is now
a new feature branch at: <http://hg.python.org/features/pep-380/>.
Sorry to have done that, once again, I was not expecting to actually have the
rights to cause any side-effect on <http://hg.python.org/>. I guess that it may
not be desirable to allow anyone do such server-side clone.

Anyway, I can not push to this feature branch, so for now it's just a clone of
the curent tip.

> Anyone without push rights for hg.python.org may want to fork the
> mirror the bitbucket folks set up during the PyCon sprints to avoid
> having to push the whole repository up to a separate hosting site:
> https://bitbucket.org/mirror/cpython

Done here:
<https://bitbucket.org/rndblnch/cpython-pep380/>

The pep-380 changeset is pushed on top of current tip and is visible here:
<https://bitbucket.org/rndblnch/cpython-pep380/changeset/40b19d1933ea>

renaud
