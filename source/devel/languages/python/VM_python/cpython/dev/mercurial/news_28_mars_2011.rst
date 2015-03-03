

.. index::
   mercurial rebase

====================================================
CPython mercurial learning, march 28 march 2011
====================================================


::

    de  Neil Schemenauer <nas@python.ca>
    à   python-dev@python.org
    date    27 mars 2011 21:15
    objet   Re: [Python-Dev] Hg: inter-branch workflow
    liste de diffusion  python-dev.python.org Filtrer les messages de cette liste de diffusion


::

    Guido van Rossum <guido@python.org> wrote:
    > What is "rebase"? Why does everyone want it and hate it at the same time?


It's the same thing that happens when you do a "svn up" with local
changes in your checkout.  Logically, your patch gets modified so
that it applies on a different (newer) version of the code.

If you don't rebase then those modifications end up getting stored
in the history as merge nodes.  That's quite messy in my opinion and
generally not a good idea.  Rebase is an important tool (which can
at times be abused).

Regarding collapsing multiple comments (and rewriting history in
general), I feel there are two main schools of thought.  One school
considers the development history of a change important and that it
should be preserved: every step and misstep of development should
end up in the public repository.

The other school, which I am a member of, considers a logical
development sequence more important than actual development history.
I like to see a feature or fix developed in smallish, logical steps
and I'm willing to spend a lot of time to rewrite patches to make it
happen.  IMO, future maintainers will thank you for the effort.

Note though, when you are worked with a distributed system, you
should not rebase commits that are in other people's repositories.
In practice this is generally not a problem.  If you have a long
lived branch that you are sharing with other people, you can have a
agreement that everyone will destory their old copy when it is
rebased.  Alternatively, you just take care to only publicly push
logical changes.

Regards,

 Neil



::

    de Neil Schemenauer <nas@arctrix.com>
    heure de l'expéditeur   Envoyé à 21:39 (GMT-06:00). Heure locale : 01:03. ✆
    à   python-dev@python.org
    date    27 mars 2011 21:39
    objet   Re: [Python-Dev] Hg: inter-branch workflow


::

    Barry Warsaw <barry@python.org> wrote:
    > I'm asking because I don't know hg and git well enough to answer the
    > question.  In my own use of Bazaar over the last 4+ years, I've almost never
    > rebased or even been asked to.


Maybe it depends on what kind of changes you commit.  I consider
future maintainers the most important "customer" of the repository
history.  As such, I try to make each commit a logical change that
takes a working system and produces another working system.  In that
way, each change to be potentially reversed if later on if it found
to cause problems.  Also, ideally, each revision can be tested to
narrow down the version where a bug was introduced.

I see a VCS system as having two related but different purposes.
The first is to help keep track of changes when they are developed.
This is messy.  I don't know about you but I make lots of mistakes:
changes that don't do what I want, crazy ideas that turn into dead
ends, etc.  I use a VCS to keep track of this experimentation and my
incremental progress.

The second is to keep a record of the change history of a long lived
piece of software.  In that case, I like it that each change has a
logical purpose.  In the first case the "customer" is the developer.
In the second it is the maintainer.


::

    > In this graph:
    >
    >>          A --- B ------------.
    >>         /                     \
    >>... --- X --- C --- D --- E --- M
    >
    > A and B do exist, but I shouldn't care or notice them unless I explicitly
    > drill down.


In my case, I usually have something like::

            A --- B --- C
            /
        --- X --- F --- G --- H

A, B, and C are messy and not logical.  Maybe I write them so I have
two logical patches (assuming they are only in my private repo)::

            A' --- B'
            /
        --- X --- F --- G --- H

Next, putting the merge in public repository generally serves no
purpose so I rebase on H::


    --- X --- F --- G --- H --- A'' --- B''

This very much matches the result I would get if using CVS or
Subversion.  IMHO, the changes A, B, and C represent partially
complete development and there is no purpose to put them in the
public repo.

If you are able to directly commit A' and B' and your tool does a
good job of hiding the logically unimportant merge then I guess you
wouldn't miss the ability to modify history.


::

    de  Ben Finney <ben+python@benfinney.id.au>
    heure de l'expéditeur   Envoyé à 08:14 (GMT+11:00). Heure locale : 18:04. ✆
    à   python-dev@python.org
    date    28 mars 2011 08:14
    objet   Re: [Python-Dev] Hg: inter-branch workflow


::

    Neil Schemenauer <nas@python.ca> writes:
    > Regarding collapsing multiple comments (and rewriting history in
    > general), I feel there are two main schools of thought. One school
    > considers the development history of a change important and that it
    > should be preserved: every step and misstep of development should end
    > up in the public repository.

Yep, that's the school I'm in. Other people don't get to say what I
would find useful, and the cost of having data there is very low
compared to the inability to re-create it at the times when it's needed.

::

    > The other school, which I am a member of, considers a logical
    > development sequence more important than actual development history.

That seems to be an artefact of VCS tools which force you to choose
between those two. The reason I prefer Bazaar is that it gives me both
without compromising either.

::

    > I like to see a feature or fix developed in smallish, logical steps
    > and I'm willing to spend a lot of time to rewrite patches to make it
    > happen. IMO, future maintainers will thank you for the effort.


Right, and those logical steps are done as merges from the feature
branch into the trunk (substitute those names as you like). I consider
the merging from one branch to another as the time to decide how to
present my VCS work for others to view.

I haven't heard a useful case for rebase that I don't get with Bazaar's
merging, default history presentation, and shelve capability. And all of
that without ever having to re-write history – nor even choose what
valuable information to lose.


::

    de  Paul Moore <p.f.moore@gmail.com>
    heure de l'expéditeur   Envoyé à 12:13 (GMT+01:00). Heure locale : 15:09. ✆
    à   Neil Schemenauer <nas@python.ca>
    cc  python-dev@python.org
    date    28 mars 2011 12:13
    objet   Re: [Python-Dev] Hg: inter-branch workflow


::

    On 27 March 2011 20:15, Neil Schemenauer <nas@python.ca> wrote:
    > Guido van Rossum <guido@python.org> wrote:
    >> What is "rebase"? Why does everyone want it and hate it at the same time?
    [...]
    > The other school, which I am a member of, considers a logical
    > development sequence more important than actual development history.
    > I like to see a feature or fix developed in smallish, logical steps
    > and I'm willing to spend a lot of time to rewrite patches to make it
    > happen.  IMO, future maintainers will thank you for the effort.

This philosophy is essentially what the "mq" extension to Mercurial
tries to capture. In mq, you maintain a series of patches "on top of"
your repository, amending, refining and rebasing them as you wish
until they are ready to commit, at which time you take them off the
patch queue and convert them into final commits in the repository.

The one downside of mq is that you do not get the usual benefits of
distributed version control - local commits of your work, branching to
manage experiments, etc. This isn't really surprising, as that sort of
"messy" development doesn't really fit with a nice clean picture of
logical and well-defined patches (at least, it doesn't fit easily
enough that it can be automated :-)). There is a facility in mq to try
to integrate the two, by versioning your patch queue, but that makes
my head hurt, so I can't really comment on how useful that is...

For people in the "clean history" school, I'd recommend looking at mq
for your personal use. But it's definitely an advanced feature of
Mercurial, so it may be better to understand core Mercurial (and at
least temporarily accept that Mercurial is based on the "keep all
history" school of thought, or you'll struggle to match the
assumptions of the documentation to your thinking :-)) before diving
into mq.

Paul.

PS You can do everything that mq provides using core Mercurial
commands - and in theory, do it more safely - but it won't necessarily
fit the way you think quite as well...


::

    de  Michael Foord <fuzzyman@voidspace.org.uk>
    heure de l'expéditeur   Envoyé à 14:48 (GMT+01:00). Heure locale : 15:17. ✆
    à   Nick Coghlan <ncoghlan@gmail.com>
    cc  Neil Schemenauer <nas@python.ca>,
    python-dev@python.org
    date    28 mars 2011 14:48
    objet   Re: [Python-Dev] Hg: inter-branch workflow



::

    On Mon, Mar 28, 2011 at 8:13 PM, Paul Moore<p.f.moore@gmail.com>  wrote:

        For people in the "clean history" school, I'd recommend looking at mq
        for your personal use. But it's definitely an advanced feature of
        Mercurial, so it may be better to understand core Mercurial (and at
        least temporarily accept that Mercurial is based on the "keep all
        history" school of thought, or you'll struggle to match the
        assumptions of the documentation to your thinking :-)) before diving
        into mq.

    I'm seeing if I can get the best of both worlds by having a public
    sandbox repo where I work on things (which has the full messy history
    of development on its feature branches), and then just drop them into
    the main repo as coherent patches. Once I land a patch, I'll close the
    original feature branch in the sandbox, so merge conflicts won't be an
    issue.

    Mercurial makes merging easy enough that I'm happy with the way that
    approach is working so far.


For any non-trivial work I think this is the best approach. You still get all
the advantages of working with mercurial (able to commit frequently) without
polluting the history of the core repository.

It has the major advantage of also being very simple to understand.

All the best,

Michael





