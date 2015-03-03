
.. index::
   pair: Non-technical battles ; Python

.. _distil_news_1_fevrier_2014_5:

==============================
5) Distil news 1 fevrier 2014
==============================


::

    Sujet: Re: [Distutils] PEX at Twitter (re: PEX - Twitter's multi-platform executable archive format for Python)
    Date : Sat, 1 Feb 2014 14:04:53 +0000 (GMT)
    De : Vinay Sajip <vinay_sajip@yahoo.co.uk>
    Pour : Nick Coghlan <ncoghlan@gmail.com>
    Copie à : DistUtils mailing list <distutils-sig@python.org>

On Sat, 1/2/14, Nick Coghlan <ncoghlan@gmail.com> wrote:

::

    > I have no idea how most of the internal design decisions on
    > pip were made (and I neither need nor particularly want to
    > know - that would be rather missing the point of collaborative
    > development). However, you're trying to make out that the
    > distil approach is so clearly superior that you don't

Not "superior" in terms of "clever". I've made a point of saying
that distil *doesn't do anything clever* in this area. If you're
saying "a bunch of design work", making "a bunch" sound like
"a lot", without any detailed knowledge of the design internals,
then how do you know if it was a hard engineering issue or a
trivial one? If I say "I didn't find it hard, and I'm not claiming to
be especially clever" then at least I'm speaking from a
knowledge of what it takes to achieve something, rather than
perhaps taking someone else's word for it. Decisions should
be properly informed, in my view.

Oh, and collaborative development sometimes involves
challenging prior work and assumptions. That's one way
in which things get better - we build on the past, but
don't remain enslaved to it.

> understand why anyone would ever have implemented it
> differently, and I'm trying to point out that there's an entirely
> plausible answer to that question that doesn't involve
> assuming poor engineering trade-offs on the part of the pip
> development team.

I didn't (at least, not intentionally) say anything about poor
engineering trade-offs made by anyone - what would be the
point of that? I do say that better engineering approaches might
exist, and suggest that the way distil does it one such approach.
If you can suggest technical flaws in the approach distil takes,
that's one thing, and I will be keen to look at any points you make.
If you have no time to examine distil and make pronouncements,
that's fine too - we're all busy people. But defending the status
quo seemingly on nebulous technical grounds like "a bunch", while
avowing no knowledge of the technical details, seems wrong.
How many milli-hodges are there in a bunch? ;-)

> No, things we do in our free time are the *best* opportunities
> to investigate things like that, because they're not necessarily
> goal oriented - they're more about satisfying our curiousity.

I don't disagree - my clumsily made point  was to to say
"volunteer" in the sense of "part-time", and therefore to
strengthen the fact that I well understand "limited resources".

> Consider the following two engineering design options:
[details snipped]
> Now *a priori*, you don't know how complex B is going to be.
> On the other hand, you already *know* A will work, because you
> already have working virtual environments.

That is fine as an *a priori* position, and it's the position I was in
when contemplating the development of distil. But we don't stay 
stuck in *a priori* forever: as I developed distil, it became clear
that alternative approaches can work. Of course there were
uncertainties at the beginning, but by doing the development
work I was able to understand better the nature of those, and
I could convert them into certainties of what would and wouldn't
work.

::

    > And from a design uncertainty point of view, A also has the
    > advantage: there is *no* design uncertainty, because you're
    > just using the already-known-to-work virtual environment
    > mechanism.

So you're saying PEP 405 was a mistake? We should just have
stuck with the tried-and-tested virtualenv, which required changing
every time a new Python version came out, because it used (of
necessity) what might be uncharitable to call "hacks"?
 

::
 
    > Now, you *have* had time to explore option B in distil, and
    > have discovered that it actually wasn't that hard after all.
    > Cool, that's great and would be a nice feature to have in pip
    > as well. However, the fact that *having already done it*, you
    > discovered it wasn't all that difficult, doesn't change the fact
    > that the level of effort involved was still greater than the
    > nonexistent amount of work needed to get the existing solution
    > working

Yes, but it's not as if I'm just presenting this aspect of distil *now*. 

I certainly highlighted the salient features on this list *before* the
:ref:`PEP 453 <python_pep_0453>` ship set sail and distil is pretty well 
documented on readthedocs.org.

::

    > and I noticed that you cut the part of the email pointing out the
    > concrete technical benefits of being able to isolate the installer
    > in addition to the installed components.

I wasn't trying to gloss over anything. If an installer maintains
backward compatibility, then isolating the installer is not
especially valuable. Even if the installer doesn't get it right,
using different versions of the installer is perfectly possible
(and easy with distil, as it's a single-file executable), and in
my experience it's not been unheard of to have had to
"downgrade" virtualenv or pip because a new release broke
something.
 
::
 
    > It's one thing to disagree with a design decision after we
    > have made the absolutely best possible case that we can
    > for why that decision was the right choice, and still failing
    > to convince ourselves. It's something else entirely to
    > dismiss someone else's use case as invalid and *then*
    > argue that an arguably simpler design (that doesn't handle
    > the dismissed use case and was still only hypothetical at
    > the time the decision was made)

Is this some revisionist view of history? I'm confused :-) 
The original announcement I made about distil was on 26 March, 2013::

    http://thread.gmane.org/gmane.comp.python.distutils.devel/17336

The relevant features were fully documented in the version 0.1.0
documentation for distil, which was tagged on 22 March, 2013::

    https://bitbucket.org/vinay.sajip/docs-distil/commits/04ac4badcab941e12ff6ecc0a3b6784fdc977e9b

This was on readthedocs.org and pythonhosted.org at the time
of the announcement.

The date on PEP 453 is 10 August, 2013 - at least four months
later: http://www.python.org/dev/peps/pep-0453/

So, if no one who participated in the PEP 453 decision had time
to look at distil in that four month period, fair enough. 

It doesn't mean that I'm somehow trying to bring something *new* to the
discussion *now*. 

I certainly made my reservations about the pip-bundling route at the time it 
was being discussed here, but if nobody was willing to look at alternatives, 
it's not something I could help.

Of course, once the decision is made, what can you do but defend it ? 

I understand your position, and I'm not trying to change anything. 
If anyone wants to provide specific, technical feedback about any problems 
with distil's approach in any area, I'll welcome that feedback - but I've 
already expressed my view on non-technical battles.

Regards,

Vinay Sajip
