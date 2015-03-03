
===============================
mercurial-can-i-do-it-better ?
===============================


http://stackoverflow.com/questions/5393661/mercurial-can-i-do-it-better

We've been using Mercurial for a couple of months now and it's improved our
deployment process A LOT already. This is the good part.

The system we have in place is working but it's still error prone if you're not
careful or rushing. This leave me wondering if there's ways we could improve it
or... maybe we're completely off the track :)

Our environment consist of:

Local development workstation (each developer)
Development server (hosting the DB & the central repository)
An acceptance server (Where QA is done)
A staging server (Where we stage the release branch, we then robocopy to the live systems)
A little background on the reason why we switched:

We are in a work environment that often have us switching from task to task,
leaving many pending tasks. Many would become stale and clutter up the main
branch when we were back on CVS. Deployment was a nightmare as you had to
work around lines that needed to go live and others that didn't using Beyond Compare.

Mercurial with named branches and easy merging solves this for us. So not
knowing what to expect we set it up.

First we cleaned cleaned up our production source, pruning dead files, etc.

We FTP'd that on staging and made this our new repository as "default", this
was to be our stable branch ready to be deployed at all time.

Afterward, we did an hg clone to the development server and had each developer
hg clone from the development default branch.

On acceptance where we do QA we did an hg clone of the development server's
default branch.

At this point we have a stable copy of the code everywhere, everyone is eager
to start!

local machine are pushing to dev, acceptance pulls from dev and staging is
completely isolated and can pull from wherever if the path is provided.

Now the idea behind this was that the default branch on our system would
always be a copy of the code on the live server, provided that we remembered
to pull before starting a new branch. When starting a new feature we would:

hg pull -b default #synch up
hg update default
hg branch {newFeature} #newFeature completely isolated from other changes.

work on {newFeature}


Oh no! A bug! this is unrelated to what I am currently working on lets call
it {bugFix111}.
This appear to call for a new branch independant of my feature; go back to
updated default. This will isolate newFeature and bugFix111 from each other
and each can go live independently as they are based on default.

hg update default
hg pull -u
hg branch {bugFix111}
Once work is completed on say {bugFix111}

hg push -F {bugFix111} #send our fix to the main central repo on dev.
Go to acceptance:

hg pull -b {bugFix111} #pull the fix from the central repo (dev).
hg merge {bugFix111} #merge the code in the default QA branch.
hg commit -m "Merging {bugFix111} into default"

QA sign off on the fix

We have to branch off acceptance - default were QA take place and release
where we merge the stuff as it get signed off.

hg update release
hg merge {bugFix111} #fix is now ready to go live
hg commit -m "Merging {bugFix111} into release"
On staging:

hg pull -b release {PATH TO ACCEPTANCE REPO}
hg merge release
hg commit -m "Merging {bugFix111} into staging default"
hg tag release{date}

* robocopy to live
* run task that pull from staging to dev so that they synch up again.

This has been working for us and save up some deployment time as it's a breeze
to just robocopy the stable release branch.

Issues
------

What we have noticed is:

It's easy to goof up a merge when merging the second time on release, this seem
against the flow. We can break it after the QA sign off.

Could get QA to test our release branch as well but it seems like duplicating
resource, the goal is just to have features isolated and being able to send
them one at a time.

We can completely blow it up by merging release over something wrong, e.g.
hg merge release when you are on the default on acceptance completely overwrites it.

If we forget to pull before starting a new branch we are working off the wrong base.

Few other oddities but those are the biggest hurdles.

I realize this is a long post, but hopefully the answers will help other
Mercurial newbies like me trying to set up a decent workflow at their company.


Response
========

Why not pull on staging from the QA branch? Then the merge job has already been
done and validated, i.e if the commit has some manual merge you will import it
on staging also.

Otherwise you have to replicate the merge on staging as you are doing it now.


Because the QA branch at any given time can have feature1, feature2, ...,
featureN merged on it for QA. What if I want to send only feature3? I can't pull
the entire branch to staging. This is what I meant by stale changes, we don't
necessarily follow a specific release cycle. If we let the QA test each
independently by allowing him to switch branch then the merge is never tested.


@jfrobishow: But, if you want to ship feature 3 only, shouldn't then QA also has
tested this feature isolated from the other features? In that case there should
be a merge for feature 3 only in the QA clone, this could be pulled by staging.


@Oben Sonne: good point... currently we don't do that. Everything that is ready
for QA is in the default branch on acceptance.
The QA test each feature one by one yes, but never isolated from other potential
defect introduced by new features also on the QA branch. Once they sign off we
pull it to staging but that's never tested as a whole or very little.
So far, this has worked as it allowed us to catch future conflicts before
they happened live. Maybe it's our QA system that needs an overhaul :) –








