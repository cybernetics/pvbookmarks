
===============
libfrprint news 
===============


.. index::
   libfprint new maintainer Bastien Nocera
   Bastien Nocera (hadess <at> hadess.net)

2010-08-19 15:28:12 GMT, New releases, new repos, new substitute maintainer
===========================================================================

- http://www.hadess.net/2010/08/fingerprint-readers-new-substitute.html


::

	From: Bastien Nocera <hadess <at> hadess.net>
	Subject: New releases, new repos, new substitute maintainer
	Newsgroups: gmane.linux.fprint
	Date: 2010-08-19 15:28:12 GMT (5 hours and 32 minutes ago)

	
Heya,

Daniel is very busy, and as such, hasn't been able to handle patches and
requests coming in from users and developers. With his approval, I now
moved the canonical git repositories to freedesktop.org, and made
releases so people can stop shipping pre-release tarballs, and git
snapshots.

The most significant changes from the pre-releases are the new UPEK
EikonII driver, from Jorge Suarez de Lis, and Guido Grazioli's work on
updating the AES1610 driver.

If you have patches that are still lingering somewhere, let me know, and
we can start looking at them.

You'll also notice that **fprint_demo and pam_fprint haven't moved**. I
consider them both obsoleted by front-ends to fprintd, though somebody
is more than welcome doing work on those.

Finally, we have a bugzilla coming up, see this bug for the progress:
https://bugs.freedesktop.org/show_bug.cgi?id=29610
and I'll be updating the reactivated.net Wiki as soon as Daniel gives me
access to it.

Releases:

- http://freedesktop.org/~hadess/libfprint-0.2.0.tar.bz2
- http://freedesktop.org/~hadess/fprintd-0.2.0.tar.bz2

git web interface:

- http://cgit.freedesktop.org/libfprint/libfprint/
- http://cgit.freedesktop.org/libfprint/fprintd/

   
   

