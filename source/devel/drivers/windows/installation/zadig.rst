

.. index::
   Driver (zadig installation)

.. _windows_drivers_install_zadig:

=============================
Windows Drivers install zadig
=============================


Zadig usb_driver output [was: Automated libusb driver installation in Windows]
==============================================================================


::

    de  Pete Batard pete@akeo.ie via lists.sourceforge.net
    heure de l'expéditeur   Envoyé à 22:17 (GMT+01:00). Heure locale : 09:51. ✆
    à   libusb-devel@lists.sourceforge.net
    date    26 septembre 2011 22:17
    objet   Re: [Libusb-devel] Zadig usb_driver output [was: Automated libusb driver installation in Windows]



::

    On 2011.09.26 21:04, Peter Stuge wrote:
    > No my issue has nothing to do with MODs. I just associated to my
    > problem when I read "pre-install".


Ah OK.

Then I'd suggest you have a look at your C:\Windows\setupapi.log after
you plug your printer and it fails, as it should tell us what Windows
did during the driver installation (not sure if driver eligibility will
be mentioned on XP). I believe that the eligibility rules will still
apply, i.e., if there's a competition between your old WHQL driver and
the new WinUSB one, WHQL will win.

You may have to delete your old driver manually for WinUSB to work as a
pre-installed driver in such a situation.

