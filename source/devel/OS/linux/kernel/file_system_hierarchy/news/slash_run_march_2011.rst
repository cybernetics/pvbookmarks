

.. index::
   pair: File System; /run
   ! /run


.. _slash_run:


=================================
Introducing /run
=================================

.. seealso::

   - http://linuxfr.org/news/run-or-not-run
   - http://lwn.net/Articles/436012/


::

    From:       Lennart Poettering <mzerqung-AT-0pointer.de>
    To:         Fedora Development ML <devel-AT-lists.fedoraproject.org>
    Subject:        What's this /run directory doing on my system and where does it come from?
    Date:       Wed, 30 Mar 2011 13:54:30 +0200


Heya,

I just uploaded a new version of systemd into F15, which establishes a
directory /run in the root directory. Most likely you'll sooner or later
stumble over it, so here's an explanation what this is and why this is.

It's a fairly minor technical change, though presumably people consider
this a bigger political change, so I guess this deserves an
explanation:

For quite a while programs involved with early boot used to place
runtime data in /dev under numerous hidden dot directories. /dev/.udev
was the first one, but over time this grew to at least /dev/.mdadm,
/dev/.systemd, /dev/.mount, dracut, initscripts and more tools. (Other
distros have even more) The reason they used directories there is that
/dev was known to be a tmpfs and available from the first instant the
machine was booted. /var/run otoh is only available very late at
boot, since /var might reside on a separate file system.

However, /dev always has been an inappropriate and ugly place for
runtime data: runtime data is not a device node, and thus simply does
not belong there. Also, hiding the existance of directories from the
administator is a bad idea. Then, the fact that some runtime data was
placed in /var/run/xxx, and other in /dev/.yyy is often not
understandable to ther user, and especially when tools originally
intended to be used only after boot are needed during early boot a
complicated move between these directories needed to take place.

Over time different distributions experimented with different broken
solutions for the early-runtime-dir problem: on Debian /lib/init/rw was
introduced, a tmpfs fs mounted during early boot. On Ubuntu /var/run was
mounted as tmpfs even before /var itself was mounted, with some really
ugly bind mount magic. Most software however just sidestepped the issue
and used /dev/.xxx.

In the past weeks key people from the Debian, Suse, Ubuntu and Fedora
camps (and others, too) discussed the whole issue forth and back, to
find a solution to stop the misuse of /dev before it becomes even more
widespread. Various solutions have been suggested, but in the end it all
boiled down to the fact that /var/run does not belong beneath /var and
what we really want is a top-level directory /run, and that that is the
only really clean solution. The only reason why nobody dared to actually
implement such a directory was unwillingness to deal with the political
backlash, especially messy discussions on mailing lists like this one.

Understanding this, we came to the conclusion that we should rather
implement what everybody thinks is the right technical solution, instead
of evading the political backlash for it. And so we implemented this.

With this upload Fedora and Suse have already adopted /run now. Debian
folks will suggest this for their coming release. Ubuntu has agreed with
introducing /run as well.

**Dracut, udev and systemd have already been updated upstream to make use
of /run**.

We expect mdadm and mount to follow suit quickly.


A few years back Debian folks already suggested introduction of /run,
and even pinged LSB folks about this, and back then there even was a vaguely
positive response from them.

So, what is implemented in F15 precisely?

/run is now a tmpfs, and /var/run is bind mounted to it. /var/lock is
bind mounted to /run/lock. Applications can use /run the same way as
/var/run. Since the latter is FHS/LSB most apps should just use the
latter, only early boot stuff should use /run, for now. The folks who
have packages where this applies already have been informed. If you
haven't heard from any of us, then this doesn't apply to you.

So, what's the benefit of this again?

- There's only one tmpfs used, backing /run, /var/lock and /var/run,
  reducing a bit the ever increasing amount of tmpfs' used on a default
  system.

- All runtime data at the same place. systemd's, udev's, dracut's data
  are all beneath /run and /var/run now. Easily discoverable to the
  admin. For the first time you can see the data all these important
  tools used on your system store just like any other by doing "ls
  /var/run".

- Nothing is hidden anymore. The admin can see everything beneath
  /var/run and /run, no hidden dot-files anymore.

- We have standardized the early-runtime-dir solution across all major
  distributions

- The people involved feel much better since they don't have to misuse
  /dev anymore

- The lifecycle properties of directories are clear from the top-level
  directory name. Lifecycle properties do no longer change the further
  you go down your tree. i.e. /var is "persistant runtime data" and /run
  is "volatile runtime data", and /etc is "persistant system config
  data", and so on. The ugliness that /var/run abd /var/lock had
  completely different liftime guarantees than /var where they both
  reside in is gone.

So, this is what is implemented for F15 now. For F16 we will make a
minor change on top of this: /var/run and /var/lock will become symlinks
to /run (resp /run/lock), so that we don't have to use bind mounts
anymore which are not the most beautiful thing to use by default, and
confusing to the admin. Due to the implications of symlinks and RPM we
didn't want to make that change in F15.

The actual code changes we needed to implement this scheme were trivial
(basically, just bind mount /var/run and /var/lock instead of mounting two
new tmpfs' to them.), which is why we opted to do this so late in the F15
cycle. However, the political implications are much bigger I guess, so
let's see what a fantastic flamewar we can start with this on
fedora-devel now. Flame away!


Lennart Poettering - Red Hat, Inc.











