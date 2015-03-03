

.. index::
   pair: USB ; tips



.. _usb_tips:

=========
USB TIPS
=========



Tip 1 : mount -t usbfs usbfs /proc/bus/usb
==========================================

.. seealso:: http://lists.alioth.debian.org/pipermail/pcsclite-cvs-commit/2011-July/005403.html

PCSCD got segmentation fault on ARM v5 with uClibc
--------------------------------------------------


::

    de  Ludovic Rousseau ludovic.rousseau@gmail.com
    heure de l'expéditeur   Envoyé à 14:07 (GMT+02:00). Heure locale : 14:36. ✆
    répondre à  MUSCLE <muscle@lists.musclecard.com>
    à   MUSCLE <muscle@lists.musclecard.com>
    date    8 juillet 2011 14:07
    objet   Re: [Muscle] PCSCD got segmentation fault on ARM v5 with uClibc


::

    > I want to say sorry for wasting your time in this issue, but then I
    > found out the root cause is that the usbfs is not mounted. Too bad,
    > this information is not available when executing pcscd. The issue is
    > solved by simply:
    >
    > mount -t usbfs usbfs /proc/bus/usb
    >
    > I would to propose a patch to check the return value of libusb_init()
    > call inside src/libusb/hotplug_libusb.c so the user will be notified
    > early if there is something wrong with libusb.


Not checking the libusb_init() returned value was a real bug. It is
now fixed thanks to you.

> Thanks for your time and response. Keep the good work!

You are welcome.

Bye
