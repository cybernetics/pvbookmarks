
===========
PSF license
===========

.. seealso::

    - http://www.python.org/psf/contrib/
    - http://www.python.org/psf/contrib/contrib-form/
    - http://wiki.python.org/moin/PythonSoftwareFoundationLicenseFaq

::

    Michael Foord <fuzzyman@voidspace.org.uk>
    heure de l'expéditeur   Envoyé à 00:27 (UTC). Heure locale : 07:51. ✆
    à   the-fellowship-of-the-packaging@googlegroups.com
    cc  VanL <van@python.org>
    date    16 février 2011 00:27
    objet   Re: [Heads Up] Contributors to Distutils2
    liste de diffusion  <the-fellowship-of-the-packaging.googlegroups.com>



On 15 February 2011 23:11, Michael Foord <fuzzyman@voidspace.org.uk> wrote::


    On 15 February 2011 22:10, Fred Drake <fdrake@acm.org> wrote:

        On Tue, Feb 15, 2011 at 4:58 PM, Tarek Ziadé <ziade.tarek@gmail.com> wrote:
        > So are you implying that the Distutils2 project cannot be licensed
        > under PSF ? We will do standalone releases.

        distutils2 can be publicly offered under the PSF license.

    But shouldn't. :-) (Right, Van?)



I've had a reply from Van Lindberg, and I'm posting it here as it may not get
through if he isn't subscribed to the list. My advice is slightly incorrect: it
turns out that the PSF license (different from the Python license) is perfectly
suitable for use by distutils2 (so my apologies):

There is a difference between the Python License Stack (run away!) and the PSF
license. The PSF license is the one at the top of the stack

The PSF license can be used in the same way that the BSD license is used - just
remove "Python Software Foundation" and put in "Michael Foord" or [whomever].
The PSF license isn't bad to use - in fact, it can be a good one to use if the
intent is for the end product to be integrated with Python.

On choosing a license (and on my decision to use BSD for unittest2) Van says::

    This is also ok, and does the same thing as what I just described. It is probably
    preferable if the intent isn't solely to integrate with Python, but instead
    to be a standalone project.
    Licenses form communities, so pick a license that will put you into (or let
    you into) the community you want to be associated with.
    Thanks,
    Van


Licencing your Python apps for dummies
======================================

::

    Mathieu Leduc-Hamel <marrakis@gmail.com>
    heure de l'expéditeur   Envoyé à 00:42 (GMT-05:00). Heure locale : 02:55. ✆
    répondre à  the-fellowship-of-the-packaging@googlegroups.com
    à   the-fellowship-of-the-packaging@googlegroups.com
    date    16 février 2011 00:42
    objet   Re: [Heads Up] Contributors to Distutils2
    liste de diffusion  <the-fellowship-of-the-packaging.googlegroups.com> Filtrer les messages de cette liste de diffusion


::

    > oh my... I thought I was that super cool Python guy by using the PSF licence.
    > We need a "Licencing your Python apps for dummies" talk at Pycon    :D

I can do it, or maybe a tutorial might be more appropriate...

Then it seems we can stick PSF License but there's another requirement
inside the agreement, saying that we should:

"Contributor shall identify each Contribution by placing the following
notice in its source code adjacent to Contributor's valid copyright
notice"

Is it ok from your understanding, if we just extract from bitbucket
all the contributions of the people of Montreal-Python and asking them
to review, i don't wanna ask every person to identify, personally all
possible lines of code on their side, nobody would do it...


protect the author from getting sued by user
============================================

::

    de  Yannick Gingras <ygingras@ygingras.net>
    heure de l'expéditeur   Envoyé à 15:45 (GMT-05:00). Heure locale : 10:23.
    répondre à  the-fellowship-of-the-packaging@googlegroups.com
    à   the-fellowship-of-the-packaging@googlegroups.com
    date    16 février 2011 15:45
    objet   Re: [Heads Up] Contributors to Distutils2
    liste de diffusion  <the-fellowship-of-the-packaging.googlegroups.com>


    On February 16, 2011, Tarek Ziadé wrote:
    > Also, BSD-Like licenses gives credits to the authors I think. And I
    > want to give that recognition to all d2 contributors, because that's
    > all they get in return besides experience ;)

There is that and there is the fact that the almost all free/open
licences protect the author from getting sued by user is the code does
not work.






