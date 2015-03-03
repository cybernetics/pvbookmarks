

.. index::
   pair: Libusb ; Installation


.. _libusb_installation:

===================
libusb installation
===================

.. seealso::

   - http://git.libusb.org/?p=libusb.git;a=summary;js=1
   - :ref:`libusb_ludovic_rousseau`
   - :ref:`libpcsclite_installation_on_gnu_linux`
   - :ref:`libusb_maintenance_problem`


.. warning:: libusb must be installed before libpcsclite.


.. _libusb_gnu_linux_installation:

Installation on GNU/Linux
=========================

We must be **root** to install the libusb libray.


Options for ./configure
-----------------------

Optional Features::

  --disable-option-checking  ignore unrecognized --enable/--with options
  --disable-FEATURE       do not include FEATURE (same as --enable-FEATURE=no)
  --enable-FEATURE[=ARG]  include FEATURE [ARG=yes]
  --enable-silent-rules          less verbose build output (undo: `make V=1')
  --disable-silent-rules         verbose build output (undo: `make V=0')
  --disable-dependency-tracking  speeds up one-time build
  --enable-dependency-tracking   do not reject slow dependency extractors
  --enable-shared[=PKGS]  build shared libraries [default=yes]
  --enable-static[=PKGS]  build static libraries [default=yes]
  --enable-fast-install[=PKGS]
                          optimize for fast installation [default=yes]
  --disable-libtool-lock  avoid locking (might break parallel builds)
  --enable-timerfd        use timerfd for timing (default auto)
  --disable-log           disable all logging
  --enable-debug-log      enable debug logging (default n)
  --enable-examples-build build example applications (default n)

Optional Packages::

  --with-PACKAGE[=ARG]    use PACKAGE [ARG=yes]
  --without-PACKAGE       do not use PACKAGE (same as --with-PACKAGE=no)
  --with-pic              try to use only PIC/non-PIC objects [default=use
                          both]
  --with-gnu-ld           assume the C compiler uses GNU ld [default=no]


Some influential environment variables::

  CC          C compiler command
  CFLAGS      C compiler flags
  LDFLAGS     linker flags, e.g. -L<lib dir> if you have libraries in a
              nonstandard directory <lib dir>
  LIBS        libraries to pass to the linker, e.g. -l<library>
  CPPFLAGS    (Objective) C/C++ preprocessor flags, e.g. -I<include dir> if
              you have headers in a nonstandard directory <include dir>
  CPP         C preprocessor

Use these variables to override the choices made by :command:`configure` or to help
it to find libraries and programs with nonstandard names/locations.

Report bugs to the package provider.


Install the development version (git version)
---------------------------------------------

::

    wget http://git.libusb.org/?p=libusb.git;a=tree;hb=HEAD
    cd libusb-HEAD-be523f1
    ./autogen.sh
    ./configure
    make
    make install


make install
------------


::

    [root@agave latest]# make install
    Making install in libusb
    make[1]: entrant dans le répertoire « /tmp/latest/libusb »
    make[2]: entrant dans le répertoire « /tmp/latest/libusb »
    test -z "/usr/local/lib" || /bin/mkdir -p "/usr/local/lib"
     /bin/sh ../libtool   --mode=install /usr/bin/install -c   libusb-1.0.la '/usr/local/lib'
    libtool: install: /usr/bin/install -c .libs/libusb-1.0.so.0.0.0 /usr/local/lib/libusb-1.0.so.0.0.0
    libtool: install: (cd /usr/local/lib && { ln -s -f libusb-1.0.so.0.0.0 libusb-1.0.so.0 || { rm -f libusb-1.0.so.0 && ln -s libusb-1.0.so.0.0.0 libusb-1.0.so.0; }; })
    libtool: install: (cd /usr/local/lib && { ln -s -f libusb-1.0.so.0.0.0 libusb-1.0.so || { rm -f libusb-1.0.so && ln -s libusb-1.0.so.0.0.0 libusb-1.0.so; }; })
    libtool: install: /usr/bin/install -c .libs/libusb-1.0.lai /usr/local/lib/libusb-1.0.la
    libtool: install: /usr/bin/install -c .libs/libusb-1.0.a /usr/local/lib/libusb-1.0.a
    libtool: install: chmod 644 /usr/local/lib/libusb-1.0.a
    libtool: install: ranlib /usr/local/lib/libusb-1.0.a
    libtool: finish: PATH="/usr/lib/qt-3.3/bin:/usr/kerberos/sbin:/usr/kerberos/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin:/sbin" ldconfig -n /usr/local/lib
    Libraries have been installed in:
       /usr/local/lib

    If you ever happen to want to link against installed libraries
    in a given directory, LIBDIR, you must either use libtool, and
    specify the full pathname of the library, or use the `-LLIBDIR'
    flag during linking and do at least one of the following:
       - add LIBDIR to the `LD_LIBRARY_PATH' environment variable
         during execution
       - add LIBDIR to the `LD_RUN_PATH' environment variable
         during linking
       - use the `-Wl,-rpath -Wl,LIBDIR' linker flag
       - have your system administrator add LIBDIR to `/etc/ld.so.conf'

    See any operating system documentation about shared libraries for
    more information, such as the ld(1) and ld.so(8) manual pages.
    ----------------------------------------------------------------------
    test -z "/usr/local/include/libusb-1.0" || /bin/mkdir -p "/usr/local/include/libusb-1.0"
     /usr/bin/install -c -m 644 libusb.h '/usr/local/include/libusb-1.0'
    make[2]: quittant le répertoire « /tmp/latest/libusb »
    make[1]: quittant le répertoire « /tmp/latest/libusb »
    Making install in doc
    make[1]: entrant dans le répertoire « /tmp/latest/doc »
    make[2]: entrant dans le répertoire « /tmp/latest/doc »
    make[2]: Rien à faire pour « install-exec-am ».
    make[2]: Rien à faire pour « install-data-am ».
    make[2]: quittant le répertoire « /tmp/latest/doc »
    make[1]: quittant le répertoire « /tmp/latest/doc »
    make[1]: entrant dans le répertoire « /tmp/latest »
    make[2]: entrant dans le répertoire « /tmp/latest »
    make[2]: Rien à faire pour « install-exec-am ».
    test -z "/usr/local/lib/pkgconfig" || /bin/mkdir -p "/usr/local/lib/pkgconfig"
     /usr/bin/install -c -m 644 libusb-1.0.pc '/usr/local/lib/pkgconfig'
    make[2]: quittant le répertoire « /tmp/latest »
    make[1]: quittant le répertoire « /tmp/latest »
    [root@agave latest]#



.. index::
   make install example

Install in /opt/libusb/version
==============================


The last version is the libusb1.0.9 rc3.

.. seealso::

   - http://git.libusb.org/?p=libusb.git;a=commit;h=f07a4a78533b44d124dfe06cbf42afa7fb267359;js=1


download under /tmp
===================

After dowload, uncompress the files under /tmp.

./autogen.sh (as root user)
----------------------------

::

    cd /tmp/libusb-xxxx
    ./autogen.sh

.configure (as root user)
--------------------------


::

    cd /tmp/libusb-xxxx
    ./configure --prefix=/opt/libusb/xxxx --enable-debug-log --enable-examples-build
    make




sudo make install
-----------------

::

    sudo make install


::

    Libraries have been installed in:
       /opt/libusb/1.0.9/lib

    If you ever happen to want to link against installed libraries
    in a given directory, LIBDIR, you must either use libtool, and
    specify the full pathname of the library, or use the `-LLIBDIR'
    flag during linking and do at least one of the following:

       - add LIBDIR to the `LD_LIBRARY_PATH' environment variable
         during execution
       - add LIBDIR to the `LD_RUN_PATH' environment variable during linking
       - use the `-Wl,-rpath -Wl,LIBDIR' linker flag
       - have your system administrator add LIBDIR to `/etc/ld.so.conf'


.. index::
   ln -s example

Link to the the 'current' libusb version
========================================

::

    cd /opt/libusb
    ln -s 1.0.9 current
    ls -als


::

    total 12
    drwxr-xr-x 3 root root 4096 2011-01-11 09:12 ./
    drwxr-xr-x 4 root root 4096 2011-03-04 09:59 ../
    drwxr-xr-x 4 root root 4096 2011-01-11 09:11 1.0.9rc3/
    lrwxrwxrwx 1 root root    5 2011-01-11 09:12 current -> 1.0.9rc3/
    pvergain@houx:/opt/libusb$




