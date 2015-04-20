
.. index::
   pair: License; GPL v2
   pair: License ; EXPORT_SYMBOL_GPL
   pair: Linux ; 2.6.25
   pair: License; "GPL-only" symbols in the kernel
   pair: Tainted; Kernel

.. _GPL_licences:

============
GPL licenses
============


.. contents::
   :depth: 3


Introduction
============


The following license idents are currently accepted as indicating
free software modules.

============================= ====================================================
License ident                 License
============================= ====================================================
"GPL"                         [GNU Public License v2 or later]
"GPL v2"                      [GNU Public License v2]
"GPL and additional rights"   [GNU Public License v2 rights and more]
"Dual BSD/GPL"                [GNU Public License v2 or BSD license choice]
"Dual MIT/GPL"                [GNU Public License v2 or MIT license choice]
"Dual MPL/GPL"                [GNU Public License v2 or Mozilla license choice]
============================= ====================================================


The different GPL licenses for USB drivers
==========================================

Since the linux 2.6.25 (february 2008), if we build the certisV2.ko kernel module with this line::


    MODULE_LICENSE("Proprietary");


we obtain the following errors::

    Building modules, stage 2.
    MODPOST 1 modules
    FATAL: modpost: GPL-incompatible module certisV2.ko uses GPL-only symbol 'usb_buffer_alloc'

In order to link with the USB kernel functions we have to put this line at
the end of the certis_driver.c file::


    MODULE_LICENSE("GPL");


.. warning:: This means that we must deliver the source code which is not the case.

.. seealso::

    - http://linuxgazette.net/issue32/rubini.html
    - http://linuxmafia.com/faq/Kernel/proprietary-kernel-modules.html
    - http://lkml.org/lkml/2003/12/5/13
    - http://www.gnu.org/licenses/gpl-faq.html



.. _usb_driver_API_moves_to_EXPORT_SYMBOL_GPL:

USB driver API moves to EXPORT_SYMBOL_GPL (February 2008)
=========================================================

.. seealso:: http://archive.netbsd.se/?ml=&a=2009-01&t=6220842

::

    Subject: [PATCH] USB: mark USB drivers as being GPL only
    From: Greg KH
    Date: 2008-01-25 19:02:32

    FYI, this is a patch that will be sent out in the next round to Linus
    for inclusion in 2.6.25.
    If anyone has any objections about it, please let me know.
    thanks,
    greg k-h
    --------
    From: Greg Kroah-Hartman
    Subject: USB: mark USB drivers as being GPL only


.. _no_way_to_create_a_USB_kernel_driver_not_GPL:

No way to create a USB kernel driver that was not under the GPL
---------------------------------------------------------------

.. warning:: Over two years ago, the Linux USB developers stated that
   they believed there was no way to create a USB kernel driver that was not
   under the GPL. This patch moves the USB apis to enforce that decision.


::

    There are no known closed source USB drivers in the wild, so this patch
    should cause no problems.

    Signed-off-by: Greg Kroah-Hartman

    -What:  USB driver API moves to EXPORT_SYMBOL_GPL
    -When:  February 2008
    -Files: include/linux/usb.h, drivers/usb/core/driver.c


.. warning:: The USB subsystem has changed a lot over time, and it has been
    possible to create userspace USB drivers using usbfs/libusb/gadgetfs
    that operate as fast as the USB bus allows.  Because of this, the USB
    subsystem will not be allowing closed source kernel drivers to
    register with it, after this grace period is over.  If anyone needs
    any help in converting their closed source drivers over to use the
    userspace filesystems, please contact the
    linux-usb-<email removed> mailing list, and the developers
    there will be glad to help you out.
    Greg Kroah-Hartman


.. seealso::

   - :ref:`libusb`
   - http://git.libusb.org/?p=libusb.git;a=tree
   - :ref:`libfprint`



::

    From: Greg KH
    Date: 2008-02-02 20:19:30

    On Sat, Feb 02, 2008 at 12:37:10PM +0100, Christer Weinigel wrote:
    > On Fri, 25 Jan 2008 10:02:32 -0800
    > Greg KH  wrote:
    >
    > > FYI, this is a patch that will be sent out in the next round to Linus
    > > for inclusion in 2.6.25.
    > >
    > > If anyone has any objections about it, please let me know.
    >
    > Yes, I have objections and I've told you before.

    You sent one message on this topic to me, back in Feb of 2007,
    disagreeing that you could write a userspace USB driver running at full
    speed in a non-racey manner.

    Unfortunately, many other userspace USB drivers seem to disprove your
    statement, including a number of vision systems running in military
    applications (tanks running Linux!).  Perhaps this is just a matter of
    using the api properly :)

    I do know that the current usbfs interface is a major pain, hence the
    work to create usbfs2.  I know those developers could use the help in
    getting that cleaned up and into the kernel tree.

    Also see the rapid development these days in wrappers around usbfs.
    There is competing projects right now with OpenUSB and the
    revitalization of the old libusb project.  I know those developers are
    looking for examples where their new frameworks do not meet the needs of
    developers for stuff exactly like you describe (lots of threads, async
    callbacks, high throughput, cross-platform portability, etc.)

    > For some of these drivers, being in kernel space is very important
    > since they transfer large amounts of data with very tight latency
    > requirements.  It may, in theory, be possible to do the same thing in
    > userspace with multiple cooperative threads and libusb, but it would be
    > much more complex and much more error prone (it's hard to do control
    > loops where you need about 40 us turnaround time).

    See statement above about vision systems in tanks, it can, and is done
    all the time...

    If a company wants to keep a driver closed, then use another operating
    system, it's not like there isn't other options out there.  I hear the
    BSDs and Microsoft are quite comfortable with things like that.  :)

::


    From: Christer Weinigel
    Date: 2008-02-03 12:48:49

    On Sat, 2 Feb 2008 11:19:30 -0800
    Greg KH  wrote:

    > If a company wants to keep a driver closed, then use another operating
    > system, it's not like there isn't other options out there.  I hear the
    > BSDs and Microsoft are quite comfortable with things like that.  :)

    So in other words you want to crack down on GPL violations, and you're
    going to ignore anyone who does have a proprietary driver as "not
    relevant" or "it can be done with usbfs" (maybe). So why even ask on
    the mailing list?  Just do it.

    Saying "use BSD" instead isn't a good answer for me since I don't know
    BSD well enough.  And personally, I want to see Linux everywhere; I
    think it's a lot better to have Linux + a proprietary driver in an
    embedded system than BSD or Windows CE.  It means that the customers
    get used to Linux, and if I can get them to at least contribute back a
    bit (any improvements to the core kernel for example), to me that is a
    lot better than giving a lot more money to BillG.

    Later, when I can show them how much easier everything gets if they use
    open drivers (I'd never have managed to get my latest Samsung platform
    up and running as quickly as I did without the patches I got from
    Sandeep Patil, and by posting my patches to his patches I got some
    feedback that helped me fix a bunch of bugs).  But it usually takes
    some time to convince a company that the things they get back is more
    valuable than keeping things proprietary.  So I think Linux as a whole
    gains a lot more by being a bit lenient about proprietary drivers.
    That is why I'm opposed this change of yours.



.. seealso:: http://kerneltrap.org/node/2991

::

    In 2001 during the 2.4 kernel development cycle, a MODULE_LICENSE macro was
    introduced which allows a module to explicitly declare how it is licensed.

    Currently (2004) there are five supported types of free software modules:

    - "GPL",
    - "GPL v2"
    - "GPL and additional rights"
    - "Dual BSD/GPL",
    - "Dual MPL/GPL"

    otherwise the kernel is considered "tainted". The include/linux/module.h
    header file lists three reasons for this macro: to allow users to review
    their license info to verify that they have a free setup, so the development
    community can ignore bug reports that include proprietary modules which don't
    release their source code, and so that vendors can do as is defined by their
    own policies. Further information is available in the lkml FAQ, as well as
    this earlier thread.



From Linus Torvals: RE: Linux GPL and binary module exception clause ?
======================================================================

.. seealso:: http://lkml.org/lkml/2003/12/5/13


::

    Date    Thu, 4 Dec 2003 22:58:09 -0800 (PST)
    From    Linus Torvalds <>
    Subject RE: Linux GPL and binary module exception clause?

    On Thu, 4 Dec 2003, David Schwartz wrote:
    >
    > The GPL gives you the unrestricted right to *use* the original work.
    > This implicitly includes the right to peform any step necessary to use
    > the work.

    No it doesn't.

    Your logic is fundamentally flawed, and/or your reading skills are
    deficient.

    The GPL expressly states that the license does not restrict the act of
    "running the Program" in any way, and yes, in that sense you may "use" the
    program in whatever way you want.

    But that "use" is clearly limited to running the resultant program. It
    very much does NOT say that you can "use the header files in any way you
    want, including building non-GPL'd programs with them".

    In fact, it very much says the reverse. If you use the source code to
    build a new program, the GPL _explicitly_ says that that new program has
    to be GPL'd too.

    > Please tell me how you use a kernel header file, other than by including
    > it in a code file, compiling that code file, and executing the result.

    You are a weasel, and you are trying to make the world look the way you
    want it to, rather than the way it _is_.

    You use the word "use" in a sense that is not compatible with the GPL. You
    claim that the GPL says that you can "use the program any way you want",
    but that is simply not accurate or even _close_ to accurate. Go back and
    read the GPL again. It says:

        "The act of running the Program is not restricted"

    and it very much does NOT say

        "The act of using parts of the source code of the Program is not
         restricted"

    In short: you do _NOT_ have the right to use a kernel header file (or any
    other part of the kernel sources), unless that use results in a GPL'd
    program.

    What you _do_ have the right is to _run_ the kernel any way you please
    (this is the part you would like to redefine as "use the source code",
    but that definition simply isn't allowed by the license, however much you
    protest to the contrary).

    So you can run the kernel and create non-GPL'd programs while running it
    to your hearts content. You can use it to control a nuclear submarine, and
    that's totally outside the scope of the license (but if you do, please
    note that the license does not imply any kind of warranty or similar).

    BUT YOU CAN NOT USE THE KERNEL HEADER FILES TO CREATE NON-GPL'D BINARIES.

    Comprende?

    Linus


.. _module_h:

module.h
========


This is the linux :file:`module.h` header file.

::

    /*
     * The following license idents are currently accepted as indicating free
     * software modules
     *
     *  "GPL"               [GNU Public License v2 or later]
     *  "GPL v2"            [GNU Public License v2]
     *  "GPL and additional rights" [GNU Public License v2 rights and more]
     *  "Dual BSD/GPL"          [GNU Public License v2
     *                   or BSD license choice]
     *  "Dual MIT/GPL"          [GNU Public License v2
     *                   or MIT license choice]
     *  "Dual MPL/GPL"          [GNU Public License v2
     *                   or Mozilla license choice]
     *
     * The following other idents are available
     *
     *  "Proprietary"           [Non free products]
     *
     * There are dual licensed components, but when running with Linux it is the
     * GPL that is relevant so this is a non issue. Similarly LGPL linked with GPL
     * is a GPL combined work.
     *
     * This exists for several reasons
     * 1.   So modinfo can show license info for users wanting to vet their setup
     *  is free
     * 2.   So the community can ignore bug reports including proprietary modules
     * 3.   So vendors can do likewise based on their own policies
     */




Other articles about the GPL license
====================================

Being honest with MODULE_LICENSE: http://lwn.net/Articles/82305/
================================================================


MODULE_LICENSE() is a macro which allows loadable kernel modules to declare
their license to the world. Its purpose is to let the kernel developers
know when a non-free module has been inserted into a given kernel.

If you submit an oops report showing a "tainted" kernel, chances you will be
asked to reproduce the problem without the proprietary module loaded, or to
talk to that module's vendor about the problem.
In general, the kernel hackers want to hear about problems, but their interest
drops remarkably when they cannot get at the source to diagnose or fix the problem.

The declared module license is also used to decide whether a given module
can have access to the small number of "GPL-only" symbols in the kernel.

.. warning:: There is no central authority which checks license declarations;
   it is assumed that module authors will not want to lie about the license they
   are using.


.. _certis_bio_taint_the_kernel:

Certis_bio taint the kernel
===========================

When a certis device is inserted we have the following messsages.

::

    dmesg


::

    Certis Bio code detected
    certis_bio: module license 'Proprietary' taints kernel.
    Disabling lock debugging due to kernel taint
    Begin inter_init_module(void)
    Begin certis_GetExchangeObject()
    End certis_GetExchangeObject().
    Begin certis_bio_init(STCOM * pstCOM) with the shared memory.
    End certis_bio_init()
    End inter_init_module(void)
    The certis_bio.ko module is loaded: 0
    The plugged certis device is now attached to the USB minor:<181>
    End certis_probe().
    root@portuxg20:/mnt/portuxg20# lsmod
    Module                  Size  Used by    Tainted: P
    certis_bio             54880  0
    certisV2               35968  1 certis_bio
    root@portuxg20:/mnt/portuxg20#



