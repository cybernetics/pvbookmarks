
.. index::
   pair: libpcsclite ; version 1.8.0


.. _libpcsclite_1_8_0:

====================
libpcsclite 1.8.0
====================

.. seealso:: http://ludovicrousseau.blogspot.com/2011/11/new-version-of-pcsc-lite-180.html

Introduction
============

::

    I just released a new version of pcsc-lite 1.8.0.
    As always, please report any issue on this mailing list or using the
    project bugtracker.

    Bye

Changes, pcsc-lite-1.8.0: Ludovic Rousseau 19 November 2011
===========================================================

- PC/SC spy tool
- Support systemd socket activation (the auto start of pcscd from the
  library has been removed. Use systemd instead)
- SCardGetStatusChange(): check all the readers are already known and
  return SCARD_E_UNKNOWN_READER if a reader name is not present.
  Windows XP has this behavior.
- SCardEstablishContext(): Invalidate all the handles in the son after a
  fork
- Add define of FEATURE_EXECUTE_PACE from PCSC v2 Part 10 Amendment 1 2011-06-03
- Fix some memory leaks repoted by Coverity
- Enable silent build by default
- log_line(): correctly calculate delta time when no color is used
  The update of last_time was only done in case of colorization
  (LogDoColor). So on unsupported consoles the time was wrong.
- log_xxd_always(): Use a variable-length array
  The debug message buffer is no more with a fixed size (around 600
  bytes of buffer to log) but uses a variable-length array.
  It is now possible to log extended APDU of 64kB.
  The variable-length array feature is available in GCC in C90 mode and
  is mandatory in C99 standard.
- Some other minor improvements and bug corrections




::

    > On Sat, Nov 19, 2011 at 5:20 PM, Ludovic Rousseau
    > <ludovic.rousseau@gmail.com> wrote:
    >> - PC/SC spy tool
    >
    > Is there more information available somewhere?
    > The only difference I got when building 1.8.0 was that there is a new
    > libpcscspy. But I'm not sure how it can be used.

You have a README file in src/spy/

More information on `PCSC API spy, third try`_ .
I added the link in my blog_ article about pcsc-lite version 1.8.0.
But forgot to also add it in the email to muscle. Sorry.

Bye

.. _`PCSC API spy, third try`: http://ludovicrousseau.blogspot.com/2011/11/pcsc-api-spy-third-try.html
.. _blog:  http://ludovicrousseau.blogspot.com/2011/11/new-version-of-pcsc-lite-180.html
















