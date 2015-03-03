
====================================================
CPython mercurial learning, march 23 march 2011
====================================================

::

    de  Dirkjan Ochtman <dirkjan@ochtman.nl>
    heure de l'expéditeur   Envoyé à 08:51 (GMT+01:00). Heure locale : 09:54. ✆
    à   "Stephen J. Turnbull" <stephen@xemacs.org>
    cc  skip@pobox.com,
    python-dev@python.org
    date    23 mars 2011 08:51
    objet   Re: [Python-Dev] I am now lost - committed, pulled, merged, what is "collapse"?


::

    On Wed, Mar 23, 2011 at 03:12, Stephen J. Turnbull <stephen@xemacs.org> wrote:
    > No, software engineering scales up to a point, then it breaks and you
    > need a serialization scheme.  The problem is not the DVCS, it's the
    > demand for a *centralized*, authoritative, safe, stable version.  DVCS
    > can scale at least to Linux kernel pace if you only ask for
    > centralized authoritative.<wink>  DVCS is "No Silver Bullet", it only
    > helps with some accidental costs of development.  It doesn't help with
    > the costs of review and testing.


Yeah, Linux employs the other solution here (which Mercurial also
uses, in fact, for development of Mercurial itself): only one person
pushes to the central repository, that person pulls from other
"staging" repositories as he is aware of changes being made.

::

    > There are in fact problems with the current generation of DVCSes.
    > Lack of plists on commits, for example.  You'd like to have a "tested"
    > property, in fact two of them (one for the committer, one for the
    > buildbots).  You'd like to have a "checkpoint" property, which commits
    > would by default be ignored by "log" and "bisect".  You'd like to have
    > an "issues" property, a list of issues applicable to this commit.  But
    > again, these would only reduce accidental costs.

Mercurial does in fact have a mechanism to attach arbitrary metadata
to changesets (the extra dictionary), but there's no easy access from
the command-line. One could also argue that this is basically just a
special case of smart commit message formatting, which python-dev
already does, and could extend. (For example, Mozilla sometimes closes
their tree to general commits, but then has a CLOSED tag that can be
put in a commit message to override that.)

Cheers,

Dirkjan



::

    de  Éric Araujo <merwok@netwok.org>
    heure de l'expéditeur   Envoyé à 04:28 (GMT+01:00). Heure locale : 10:27. ✆
    à   "Stephen J. Turnbull" <stephen@xemacs.org>
    cc  Antoine Pitrou <solipsis@pitrou.net>,
    python-dev@python.org
    date    23 mars 2011 04:28
    objet   Re: [Python-Dev] Workflow proposal



> So what you're saying is that Mercurial by itself can't support the
> recommended workflow, because any "collapsing" of commits requires
> stripping, whether done by hg strip or implicitly by some other
> "non-average" hg command.

Pretty average: http://mercurial.selenic.com/wiki/PruningDeadBranches

> I don't see the connection; mq supplies "qfinish" for the purpose of
> turning a patch into a commit.  All I'm suggesting is that "qrefresh"
> is a nicer way to handle both the collapsing process and the strip/
> re-merge/recommit process, although there is the problem of reverting
> the commit back to an mq patch, which AFAIK requires a "strip --keep"
> followed by "qnew".

I like mq as a power tool, but only for short-term work.  Most of the
time I don’t need it.  Refreshing is painful to me whereas merging is
straightforward.  Mercurial devs themselves advocate real branches
(named, pbranch or what-have-you) for long-term work.

Regards


::

    de  Éric Araujo <merwok@netwok.org>
    heure de l'expéditeur   Envoyé à 02:01 (GMT+01:00). Heure locale : 11:11. ✆
    à   Glenn Linderman <v+python@g.nevcal.com>
    cc  python-dev@python.org
    date    23 mars 2011 02:01
    objet   Re: [Python-Dev] Hg: inter-branch workflow



::

    >>> I'm curious: what are the benefits of the Mercurial model?
    >> Simplicity.
    >
    > That's an amusing response, after reading hundreds of emails on this
    > list

I think the great number of messages is caused by incomplete learning,
confusion caused by familiarity with other tools, FUD and anxiety.

Just in case my position is not clear: I have a lot of sympathy for
people who struggle with the new tool and workflow and do try to help.

::

    > about 5-12 step sequences of commands required to perform one operation.

Committing, merging and sharing are not one operation.

::

    > So I must ask: where is the simplicity manifested?


I used simplicity in its strict (or scientific, if this speaks to you)
meaning: not complex, not many-sided.  Having one thing (a notion of an
unnamed branch) instead of two things (a notion of trunk and a notion of
side branch) is by definition simpler.

I often describe Mercurial’s simplicity (or chosen stupidity) as the
reason for its robustness and consistency.  (For example, the frowning
upon history rewriting, or the absence of octopus merging.)

That said, I cannot learn Mercurial for you, not force you to read the
devguide.  I would advise you to learn Mercurial with one of the many
available resources (http://hginit.com/,
http://mercurial.aragost.com/kick-start/), proceed to the devguide,
clone https://bitbucket.org/mirror/cpython and start fixing things in
http.server (and thanks in advance for that work!).

Regards


Re: [Python-Dev] Workflow proposal
==================================

::


    de  Antoine Pitrou <solipsis@pitrou.net>
    heure de l'expéditeur   Envoyé à 14:30 (GMT+01:00). Heure locale : 17:24. ✆
    à   python-dev@python.org
    date    23 mars 2011 14:30
    objet   Re: [Python-Dev] Workflow proposal
    liste de diffusion  python-dev.python.org Filtrer les messages de cette liste de diffusion


::

    On Wed, 23 Mar 2011 12:30:17 +0900
    "Stephen J. Turnbull" <stephen@xemacs.org> wrote:
    > Antoine Pitrou writes:
    >
    >  > Now, "hg strip" should definitely be absent of any recommended or even
    >  > suggested workflow. It's a power user tool for the experimented
    >  > developer/admin. Not the average hg command.
    >
    > So what you're saying is that Mercurial by itself can't support the
    > recommended workflow, because any "collapsing" of commits requires
    > stripping,


Not really. It requires that you either:

- work on your long-term features in a separate repo (and produce a
  diff at the end that you will apply to the main repo)
- use mq
- use a non-committing equivalent of mq (iterate on a patch which you
  periodically save with "hg di", for example; that's what I do for
  most patches)

Apparently some of you think "collapsing" should involve some specific
hg command. It doesn't. Perhaps the devguide should be rephrased there.

Regards

Antoine.
