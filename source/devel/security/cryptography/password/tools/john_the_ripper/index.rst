

.. index::
   pair: Password; John The Ripper
   pair: Crack; Password
   pair: John; The Ripper
   ! John The Ripper

.. _john_the_ripper:

======================
John The Ripper
======================

.. seealso::

   - http://www.openwall.com/john/
   - http://www.cyberciti.biz/faq/unix-linux-password-cracking-john-the-ripper/

.. contents::
   :depth: 3   
   
Introduction
============

John the Ripper is a fast password cracker, currently available for many 
flavors of Unix, Windows, DOS, BeOS, and OpenVMS. 

Its primary purpose is to detect weak Unix passwords, although Windows 
LM hashes and a number of other password hash types are supported as well. 

John the Ripper is free and Open Source software, distributed primarily 
in source code form.  

Its primary purpose is to detect weak Unix passwords.  

Besides several crypt(3) password hash types most commonly found on 
various Unix flavors, supported out of the box are Kerberos/AFS and
Windows LM hashes, as well as DES-based tripcodes, plus many more 
hashes and ciphers in "community enhanced" -jumbo versions and/or with 
other contributed patches. 

How to install
==============

See INSTALL for information on installing John on your system.


How to use
==========

To run John, you need to supply it with some password files and
optionally specify a cracking mode, like this, using the default order
of modes and assuming that "passwd" is a copy of your password file::

    john passwd

or, to restrict it to the wordlist mode only, but permitting the use
of word mangling rules::

    john --wordlist=password.lst --rules passwd

Cracked passwords will be printed to the terminal and saved in the
file called $JOHN/john.pot (in the documentation and in the
configuration file for John, "$JOHN" refers to John's "home
directory"; which directory it really is depends on how you installed
John).  The $JOHN/john.pot file is also used to not load password
hashes that you already cracked when you run John the next time.

To retrieve the cracked passwords, run::

    john --show passwd

While cracking, you can press any key for status, or Ctrl-C to abort
the session saving its state to a file ($JOHN/john.rec by default).
If you press Ctrl-C for a second time before John had a chance to
handle your first Ctrl-C, John will abort immediately without saving.
By default, the state is also saved every 10 minutes to permit for
recovery in case of a crash.

To continue an interrupted session, run::

    john --restore

These are just the most essential things you can do with John.  For
a complete list of command line options and for more complicated usage
examples you should refer to OPTIONS and EXAMPLES, respectively.

Please note that "binary" (pre-compiled) distributions of John may
include alternate executables instead of just "john".  You may need to
choose the executable which fits your system best, e.g. "john-mmx" to
take advantage of MMX acceleration.

Features and performance
=========================

John the Ripper is designed to be both feature-rich and fast.  

It combines several cracking modes in one program and is fully
configurable for your particular needs (you can even define a custom
cracking mode using the built-in compiler supporting a subset of C).
Also, John is available for several different platforms which enables
you to use the same cracker everywhere (you can even continue a
cracking session which you started on another platform).

Tutorials
==========

.. toctree::
   :maxdepth: 3
   
   art_du_web
   cibercity
   
   

