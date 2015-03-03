

.. _distil_news_1_fevrier_2014_2:

==============================
2) Distil news 1 fevrier 2014
==============================


::

    Sujet: Re: [Distutils] PEX at Twitter (re: PEX - Twitter's multi-platform executable archive format for Python)
    Date : Sat, 1 Feb 2014 21:31:49 +1000
    De : Nick Coghlan <ncoghlan@gmail.com>
    Pour : Vinay Sajip <vinay_sajip@yahoo.co.uk>
    Copie à : DistUtils mailing list <distutils-sig@python.org>


On 1 February 2014 20:49, Vinay Sajip <vinay_sajip@yahoo.co.uk> wrote:
> So, I am at a loss to see your point.

My point is that doing it the way virtualenv/pip did avoided a bunch
of design work and associated testing, and reduced the opportunities
for bugs - when you're trying to get things done with **limited
resources**, that's a sensible engineering trade-off to make.

As Paul noted in his reply, there's nothing that *inherently* limits
pip to working that way, it just hasn't been a priority to change.

That said (and this is a point that hadn't occurred to me earlier),
it's also worth noting that not only does the bootstrapping approach
work well enough in most cases, but it also solves the problem of
being able to easily have a newer (or older!) pip in virtual
environments than is provided by the distro package manager on Linux
systems, *without* needing to do a global install outside the package
manager's control.

On that last point, note these two recommendations that PEP 453 makes
to downstream redistributors:

* ``pip install --upgrade pip`` in a global installation should not
  affect any already created virtual environments (but is permitted to
  affect future virtual environments, even though it will not do so when
  using the standard implementation of ensurepip).

* ``pip install --upgrade pip`` in a virtual environment should not
  affect the global installation.

If pip maintained perfect backwards compatibility across every
release, those recommendations wouldn't be necessary. However, we're
still in the process of actively hardening the security model, and
that *does* mean we're going to break things at times. Having the
version of pip in use be virtual environment dependent rather than
Python installation dependent helps deal with that more gracefully.

Cheers,
Nick.
