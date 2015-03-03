
.. index::
   pair: Social concerns; Python


.. _distil_news_1_fevrier_2014_4:

==============================
4) Distil news 1 fevrier 2014
==============================

::

    Sujet: Re: [Distutils] PEX at Twitter (re: PEX - Twitter's multi-platform executable archive format for Python)
    Date : Sat, 1 Feb 2014 12:20:55 +0000 (GMT)
    De : Vinay Sajip <vinay_sajip@yahoo.co.uk>
    Pour : Nick Coghlan <ncoghlan@gmail.com>
    Copie à : DistUtils mailing list <distutils-sig@python.org>


On Sat, 1/2/14, Nick Coghlan <ncoghlan@gmail.com> wrote:

> My point is that doing it the way virtualenv/pip did avoided a bunch
> of design work and associated testing, and reduced the
> opportunities for bugs - when you're trying to get things done with
> limited resources, that's a sensible engineering trade-off to make.

A "bunch of design work" makes it seem a **lot more complicated
than it really is**. 

Your suggestion comes across like an ex post facto rationalisation of a decision 
which was perhaps more truly based on **social concerns** than technical ones.

Note that I've developed distil as part of my volunteer activities - it
doesn't pay any of my bills - and on my own. 
And you're telling me about how to get the best out of **limited resources** ? :-)

::

    > That said (and this is a point that hadn't occurred to me earlier),
    > it's also worth noting that not only does the bootstrapping
    > approach work well enough in most cases, but it also solves the
    > problem of being able to easily have a newer (or older!) pip in
    > virtual environments than is provided by the distro package
    > manager on Linux systems

Eh?  The problem of having a newer or older pip in a venv
only exists because pip needs to be in a venv ... so I don't see
the relevance of this to our earlier discussion. 

Since distil doesn't occupy a space in venvs,. the concern of a system
version being older or newer than that in a venv doesn't arise.

Regards,

Vinay Sajip
