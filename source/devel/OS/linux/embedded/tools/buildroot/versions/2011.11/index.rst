

.. _buildroot_versions_2011:

=======================
buildroot 2011.11
=======================

.. seealso:: http://git.buildroot.net/buildroot/plain/CHANGES?id=2011.11


2011.11, Released November 30th, 2011
======================================

Fixes all over the tree.

Bump kernel headers / default Linux version to 3.1.4.

Updated/fixed packages: ruby

2011.11-rc3, Released November 26th, 2011
=========================================

Fixes all over the tree.

Toolchain: Fix gdb dependencies for external toolchains,
adjust uClibc patches so they don't confuse modern versions of
patch, bump crosstool-ng, kernel headers and linux versions.

Updated/fixed packages: busybox, freetype, mplayer, opencv,
php, rsyslog, ruby, thttpd, xapp_xf86dga

Issues resolved (http://bugs.uclibc.org):

#4357: Prevent patch commands from accessing source control
#4369: Fix permissions on untared lsof archive

2011.11-rc2, Released November 18th, 2011
==========================================

Fixes all over the tree and new features.

Updated asciidoc documentation

Toolchain: Bumped 3.x stable kernel headers, use wget in
crosstool-ng as well, bump crosstool-ng version, gdb fixes,
uClibc sparc fix.

Updated/fixed packages: distcc, file, gst-plugins-bad, libxcb,
mplayer, newt, qt, rpm, rrdtool, tar, tftpd


2011.11-rc1, Released November 11th, 2011
=========================================

Fixes all over the tree and new features.

Moved misc scripts and support stuff to support/. Renamed
patch-kernel.sh to support/scripts/apply-patches.sh.

Documentation: Moved to asciidoc format, make targets to
generate text/html/pdf/epub output added.

Defconfigs: Qemu configs updated to 3.1 kernel and readmes
added.

Bootloaders: Add support for custom git tree / tarballs for
barebox, similar to how it's handled for u-boot. Clean up
menuconfig options.

Toolchain: Update external codesourcery toolchain download
URLs after Codesourcery got bought by Mentor, add x86
toolchain, update toolchain versions and optimize toolchain
sysroot copying. Fix uClibc 0.9.32 builds for e500 PPC,
updated GDB versions / download URLs. Binutils
libbfd/libopcodes static/dynamic linking fix. GCC 4.6.2 added,
use ctng-1.13.0.

Package infrastructure: Support for local packages /
overrides, package dir / name arguments dropped from
{GEN,AUTO,CMAKE}TARGETS.

Linux: Kernel extensions infrastructure support, Xenomai +
RTAI support.

Updated/fixed packages: acpid, bind, busybox, dash, dbus,
dbus-glib, directfb, dnsmasq, drystone, e2fsprogs, ethtool,
fakeroot, fbdump, file, freetype, fuse, gamin, gmp, gmpc,
gnutls, gob2, gst-plugins-{base,bad,good,ugly}, gstreamer,
hostapd, ifplugd, imagemagick, intltool, ipsec-tools, ipset,
iptables, iw, jpeg, kexec, leafpad, less, libargtable2, libao,
libconfuse, libcuefile, libcurl, libdaemon, libevent,
libglib2, libiconv, libmpd, libreplaygain, libroxml,
libsamplerate, libsndfile, libsoup, libsvgtiny, libtool,
libxcb, lighttpd, links, linux-fusion, lite, lrzsz, lsof, lzo,
lzop, makedevs, mcookie, mpg123, mpd, mpfr, mtd, musepack,
mutt, mysql_client, ncftp, ncurses, neon, netcat, netsnmp,
ntfs-3g, ntfsprogs, ntp, openntpd, openssh, openssl, oprofile,
orc, pciutils, psmisc, python, qt, quagga, radvd, rpm, rsync,
samba, sawman, sdl_sound, smartmontools, sqlite, squid,
stunnel, sudo, sylpheed, sysstat, taglib, tar, tcpreplay,
tslib, usbutils, util-linux, valgrind, wget, whetstone, which,
wpa-supplicant, xdata_xcursor-themes, xmlstarlet, xterm

New packages: bluez-utils, cifs-utils, fftw, fluxbox, json-c,
libev, libftdi, libgeotiff, libmodbus, libplayer, live555,
ngrep, noip, opencv, openocd, picocom, poco, portaudio,
pulseaudio, pv, rtai, vala, xenomai.

Removed packages: liboil, sfdisk, swfdec, webif

Issues resolved (http://bugs.uclibc.org):



