


.. index::
   pair: linux ; lsmod
   pair: linux ; module lsmod
   pair: linux ; modprobe
   pair: linux ; module modprobe



.. _linux_modules_bis:

=============
linux modules
=============

.. seealso::

   - http://tjworld.net/books/ldd3/#5
   - http://www.kernel.org/pub/linux/utils/kernel/modutils/


.. contents::
   :depth: 3


Introduction
=============

Many programming books begin with a "hello world" example as a way of showing
the simplest possible program. This book deals in kernel modules rather than
programs; so, for the impatient reader, the following code is a complete
"hello world" module::

    #include <linux/init.h>
    #include <linux/module.h>
    MODULE_LICENSE("Dual BSD/GPL");

    static int hello_init(void)
    {
        printk(KERN_ALERT "Hello, world\n");
        return 0;
    }

    static void hello_exit(void)
    {
        printk(KERN_ALERT "Goodbye, cruel world\n");
    }

    module_init(hello_init);
    module_exit(hello_exit);

This module defines two functions, one to be invoked when the module is loaded
into the kernel (hello_init) and one for when the module is removed
(hello_exit). The module_init and module_exit lines use special kernel macros
to indicate the role of these two functions. Another special macro
(MODULE_LICENSE) is used to tell the kernel that this module bears a free
license; without such a declaration, the kernel complains when the module
is loaded.


Loading and Unloading Modules
=============================


After the module is built, the next step is loading it into the kernel.
As we've already pointed out, insmod does the job for you. The program loads
the module code and data into the kernel, which, in turn, performs a function
similar to that of ld, in that it links any unresolved symbol in the module
to the symbol table of the kernel. Unlike the linker, however, the kernel
doesn't modify the module's disk file, but rather an in-memory copy. insmod
accepts a number of command-line options (for details, see the manpage), and
it can assign values to parameters in your module before linking it to the
current kernel. Thus, if a module is correctly designed, it can be configured
at load time; load-time configuration gives the user more flexibility than
compile-time configuration, which is still used sometimes.
Load-time configuration is explained in the section "Module Parameters,"
later in this chapter.

Interested readers may want to look at how the kernel supports insmod it
relies on a system call defined in kernel/module.c. The function
sys_init_module allocates kernel memory to hold a module (this memory
is allocated with vmalloc; see the section "vmalloc and Friends" in Chapter 8);
it then copies the module text into that memory region, resolves kernel
references in the module via the kernel symbol table, and calls the module's
initialization function to get everything going.

If you actually look in the kernel source, you'll find that the names of the
system calls are prefixed with sys. This is true for all system calls and
no other functions; it's useful to keep this in mind when grepping for the
system calls in the sources.

The modprobe utility is worth a quick mention. modprobe, like insmod, loads
a module into the kernel. It differs in that it will look at the module to
be loaded to see whether it references any symbols that are not currently
defined in the kernel. If any such references are found, modprobe looks
for other modules in the current module search path that define the relevant
symbols. When modprobe finds those modules (which are needed by the module
being loaded), it loads them into the kernel as well. If you use insmod in
this situation instead, the command fails with an "unresolved symbols"
message left in the system logfile.

As mentioned before, modules may be removed from the kernel with the rmmod
utility. Note that module removal fails if the kernel believes that the
module is still in use (e.g., a program still has an open file for a device
exported by the modules), or if the kernel has been configured to disallow
module removal. It is possible to configure the kernel to allow "forced"
removal of modules, even when they appear to be busy. If you reach a point
where you are considering using this option, however, things are likely
to have gone wrong badly enough that a reboot may well be the better
course of action.


lsmod
=====

/proc/modules, /sys/module
--------------------------

The lsmod program produces a list of the modules currently loaded in the
kernel. Some other information, such as any other modules making use of
a specific module, is also provided. lsmod works by reading the /proc/modules
virtual file. Information on currently loaded modules can also be found in
the sysfs virtual filesystem under /sys/module.


depmod
======

man depmod


Linux kernel modules can provide services (called "symbols") for other
modules to use (using EXPORT_SYMBOL in the code).
If a second module uses this symbol, that second module clearly depends
on the first module.  These dependencies can get quite complex.

depmod creates a list of module dependencies, by reading each module under
/lib/modules/version and  determining  what  symbols  it
exports,  and what symbols it needs.  By default this list is written to
modules.dep in the same directory.  If filenames are given
on the command line, only those modules are examined (which is rarely
useful, unless all modules are listed).



::

    root@portuxg20:/mnt/portuxg20# cat /lib/modules/2.6.31/modules.dep

::


    /lib/modules/2.6.31/certisV2.ko:
    /lib/modules/2.6.31/kernel/drivers/usb/gadget/gadgetfs.ko: /lib/modules/2.6.31/kernel/drivers/usb/gadget/at91_udc.ko
    /lib/modules/2.6.31/kernel/drivers/usb/gadget/g_file_storage.ko: /lib/modules/2.6.31/kernel/drivers/usb/gadget/at91_udc.ko
    /lib/modules/2.6.31/kernel/drivers/usb/gadget/at91_udc.ko:
    /lib/modules/2.6.31/kernel/drivers/usb/gadget/g_serial.ko: /lib/modules/2.6.31/kernel/drivers/usb/gadget/at91_udc.ko
    /lib/modules/2.6.31/certis_bio.ko: /lib/modules/2.6.31/certisV2.ko


