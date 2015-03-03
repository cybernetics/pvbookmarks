.. module:: LinuxKernelUSB_commands_fr
    :synopsis: Linux kernel documentation USB commands
    :platform: Linux kernel
  

=============================
Doc sur les sources Linux USB
=============================

.. index::
   usbutils
   http://git.kernel.org/?p=linux/kernel/git/gregkh/usbutils.git;a=tree;h=refs/heads/master;hb=refs/heads/master
   http://www.kernel.org/pub/linux/utils/usb/usbutils/
   

Commandes USB linux usbutils
============================

.. seealso::

   - http://git.kernel.org/?p=linux/kernel/git/gregkh/usbutils.git;a=tree;h=refs/heads/master;hb=refs/heads/master
   - http://www.kernel.org/pub/linux/utils/usb/usbutils/

::

    \---usbutils-0.86
            aclocal.m4
            AUTHORS
            ChangeLog
            config.h.in
            configure
            configure.ac
            COPYING
            depcomp
            devtree.c
            devtree.h
            INSTALL
            install-sh
            list.h
            lsusb-t.c
            lsusb.8.in
            lsusb.c
            Makefile.am
            Makefile.in
            missing
            names.c
            names.h
            NEWS
            README
            update-usbids.sh.in
            usb-devices
            usb-devices.1.in
            usb.ids
            usbmisc.c
            usbmisc.h
            usbutils.pc.in


            
.. index::
   usb.ids
   lsusb
   lspci
   
   
lsusb 
-----

::

    lsusb
    

Comment votre système reconnait-il la marque et le modèle du matériel ?
Eh bien la commande :command:`lsusb` utilise un fichier :file:`usb.ids` 
(/var/lib/usbutils/usb.ids sous Debian, /var/lib/misc/usb.ids sous 
ubuntu).
Notez la présence des lignes terminées par "root usb". En fait, la
commande vous propose plusieurs ports USB, mais la plupart du temps,
ces ports appartiennent à un ou plusieurs hubs USB internes, qui 
s'accompagnent de contrôleurs (faisant office d'interface entre les
périphériques et le système).

.. seealso:: 

   - :ref:`linux_2_6_31_drivers_usb_sources`
   - :ref:`usbids`

lspci
-----

:: 

    lspci -v | grep USB
    
La commande :command:`lspci` permet d'identifier les contrôleurs USB mis
en jeu.



