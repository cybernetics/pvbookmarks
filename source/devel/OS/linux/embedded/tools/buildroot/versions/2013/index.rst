

.. _buildroot_2013:

=======================
buildroot 2013
=======================

.. seealso:: http://git.buildroot.net/buildroot/plain/CHANGES?id=2013.02


.. contents::
   :depth: 3

2013.02, Released February 28th, 2013
=====================================

Misc manual updates.

Updated/fixed packages: busybox, collectd, flashbench,
libgtk2, libupnp, mii-diag, quota

2013.02-rc3, Released February 26th, 2013
=========================================

Minor fixes.

Updated/fixed packages: conntrack-tools, dialog,
enlightenment, haserl, keyutils, libfif, libmad,
linux-firmware, linux-fusion, matchbox-desktop, matchbox-wm,
ruby, spawn-fcgi, vtun

Issues resolved (http://bugs.uclibc.org):

#5960: fusion.ko driver does not install to target rootfs

2013.02-rc2, Released February 19th, 2013
=========================================

Fixes all over the tree.

Various manual updates and fixes.

Updated/fixed packages: busybox, collectd, gesftpserver,
glib-networking, gnutls, inotify-tools, libcurl, libffi,
libglib2, libtorrent, libvorbis, neard, network-manager,
ntfs-3g, openssl, qt, rpi-userland, rtorrent, thttpd, vim.

Issues resolved (http://bugs.uclibc.org):

#5906: collectd client headers not exported

2013.02-rc1, Released February 10th, 2013
==========================================

Toolchain: Crosstool-ng 1.17.0, default to GCC 4.6.3, target
libraries install fixed. Add Linaro ARM
2012.11/2012.12/2013.01, AArch64 12.11/12.12/13.01. Sourcery
CodeBench MIPS 2012.03/09. Infrastructure to warn about
missing 32bit support for binary toolchains. Toolchain wrapper
is now relocatable. Add GDB 7.5.1 / Remove 6.8 / 7.0 /
7.1. Deprecate uClibc 0.9.31.

Architecture: Xtensa fixes, add missing powerpc variants, arm
1136jf-s rev1, add A5/A15, neon support toggle, OABI
deprecated. Sparc: drop old unused variants

Bootloaders: At91bootstap: fix upstream URL, Barebox: add
2012.12/2013.01/2013.02, remove 2012.08/09/10, lzop fixes,
environment image support, U-Boot: add 2013.01.01

Linux: fix appended dtb handling for v3.8+ kernels, support
multiple device trees

Defconfigs: calao USB-A9260, snowball, QEMU PPC440 on ML507
board, QEMU ARM Exynos4210, Kernel version in QEMU defconfigs
updated, at91rm9200df: misc fixes. Lock kernel headers to
match kernel.

Infrastructure: Git download fixes. Toolchain make target
renamed from 'cross' to 'toolchain'. Eclipse integration
support. Option to set root password, post image scripts,
config scripts handling.

Updated/fixed packages: alsa-lib, argp-standalone, argus,
arptables, atk, audiofile, axel, beecrypt, bind, bison,
bluez_utils, boost, cairo, can-utils, bmon, boa, busybox,
cairo, ccache, cdrkit, cifs-utils, cjson, cmake, collectd,
connman, coreutils, cpanminus, cups, dbus, dhcp, dialog,
diffutils, directfb, distcc, divine, dnsmasq, docker,
dosfstools, dstat, e2fsprogs, ebtables, ed, empty, ethtool,
expedite, fbset, fbv, ffmpeg, flex, fltk, fluxbox, freetype,
gadget-test, gawk, gdb, genext2fs, gettext, giblib,
glib-networking, gmp, gmpc, gnupg, gnutls, gpsd,
gst-plugins-{bad,base,good}, gstreamer, gzip, haserl, hdparm,
heirloom-mailx, hiawanta, hostapd, icu, imagemagick, imlib2,
inadyn, infozip, iproute2, ipset, iptables, iw, jpeg, jquery,
jquery-sparklines, jqeury-validation, kismet, kmod, lame,
libao, libcap, libcurl, libdvdnav, libdvdread, libecore,
libedbus, libedje, libeet, libefreet, libeina, libeio,
liberation, libelementary, libembryo, libethumb, libev,
libevas, libffi, libfribidi, libfuse, libgcrypt, libglib2,
libgpg-error, libgtk2, libhid, libidn, libmicrohttpd, libmpd,
libnl, libnspr, libnss, libogg, libpcap, libplayer, libpng,
libroxml, librsvg, libseccomp, libsigc, libsndfile, libungif,
libupnp, liburcu, libusb-compat, libvncserver, libvorbis,
libxml2, libxslt, lighttpd, links, linux-firmware,
linux-fusion, ltp-testsuite, ltrace,
lttng-{babel,libust,modules,tools}, lvm2, lua, luajit, lzop,
matchbox-{desktop,lib}, mdadm, metacity, midori, minicom, mpd,
mpfr, mplayer, mtd, mysql_client, ncurses, neon, netatalk,
networkmanager, nspr, ntfs-3g, nuttcp, ofone, olsr, openssl,
openvpn, opkg, oprofile, opus, opus-tools, orc, ortp, pango,
pciutils, pcmanfm, pcre, pcsc-lite, perl, php, pixman,
pkgconf, polarssl, pptp-linux, proxychains, pulseaudio,
python, python3, qemu, qextserialport, qt, quagga, radvd,
readline, rng-tools, rt-tests, rubix, ruby, sam-ba, samba,
sane-backends, sconeserver, scons, screen, sdl, sdl_gfx,
sdl_mixer, sdl_ttf, sdparm, sed, ser2net, smartmontools,
speex, sqlite, squid, sshfs, strace, sudo, sylpheed, tn5250,
taglib, tar, torsmo, transmission, tslib, uboot-tools, ulogd,
usb_modeswitch, util-linux, valgrind, vim, vsftpd, wavpack,
webkit, wipe, wireless_tools, wpa_supplicant, xapp_xinit,
xapp_xinput-calibrator, xapp_xman, xapp_xmh, xlib_libX11,
xlib_libXdmcp, xlib_libXft, xlib_libpthread-stubs,
xlib_xtrans, xproto_xcmiscproto, xproto_xextproto,
xserver_xorg-server, xstroke, xvkbd, xz

New packages: b43-firmware, b43-fwcutter, bustle,
cache-calibrator, cegui06, celt051, classpath, curlftpfs,
dvb-apps, dvbsnoop, elfutils, enlightenment, firmware-imx,
flashbench, gd, gesftpserver, gst-fsl-plugins, httping, iftop,
imx-lib, jamvm, jpeg-turbo, keyutils, libatasmart, libcofi,
libebml, libevas-generic-loaders, libfslcodec, libfslparser,
libfslvpuwrap, libgsasl, libiscsi, libmatroska, libmcrypt,
libmhash, libqwt, libseccomp, libsha1, linenoise, mcrypt,
media-ctl, ncdu, neard, neardal, nettle, perf, polkit,
proxychains, python-bottle, python-pyparsing, rpi-firmware,
rpi-userland, sg3_utils, slirp, snowball-hdmiservice, spice,
spice-protocol, tcllib, tvheadend, udisks, usbredir
ux500-firmware, vde2, xcb-utils-keysyms, yavta,
zd1211-firmware

Removed packages: customize, xdriver_xf86-input-{acecad,aiptek},
xdriver_xf86-video-{apm,chips,i740,rendition,s3,s3virge,sisusb},
xdriver_xf86-video-sun{cg14,cg3,cg6,ffb,leo,tcx},
xdriver_xf86-video-{tsend,xgi,xgixp}

Deprecated packages: xstroke

Issues resolved (http://bugs.uclibc.org):

#4237: building shared openssl w/-Os fails due to gcc bug
#5690: python3 does not obey to BR2_PACKAGE_PYTHON3_PYC_ONLY=y
#5602: python3 should install a "python" symbolic link
#5846: Extra slash added to last slash in URL
