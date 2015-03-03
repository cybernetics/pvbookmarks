.. module:: pyusb_news
    :synopsis: pyUSB news
    :platform: GNU/Linux, Windows
  
  
.. index::
   pyUSB news
   USB testlibusb-win.exe
   USB inf-wizard.exe
   
==========
pyUSB news
==========

INF file (for WinUSB)
=====================

:: 

    from    Xiaofan Chen <xiaofanc@gmail.com>
    reply-to    pyusb-users@lists.sourceforge.net
    to  pyusb-users@lists.sourceforge.net
    date    Mon, May 31, 2010 at 1:13 AM
    subject Re: [pyusb-users] XP
    

On Sun, May 30, 2010 at 11:31 PM, Karl Palsson <tweak@tweak.net.au> wrote:
> If you're screwing around with inf files, (in my opinion) you're doing it wrong.
>
> I (finally) got windows XPand ubuntu working with (almost) the same code, and no
> inf files.
>
> http://github.com/karlp/karlnet/tree/usbmaster/producers/pyhid/ has the simple
> code, and the README there is....
>

I see you are using libusb-1.0, that is fine. Moreover you are using HID device,
So you do not need to generate your own INF file. But you still need to generate
the INF (for WinUSB) if you are using non-HID device.

The OP can of course try libusb-1.0 and WinUSB as well. For driver installation,
zadig/libwdi is quite nice. The git version actually supports both:

- winusb.sys and
- libusb0.sys.


http://www.libusb.org/wiki/windows_backend


:: 

    from    Xiaofan Chen <xiaofanc@gmail.com>
    date    Wed, Jun 2, 2010 at 12:46 AM
    subject Re: [pyusb-users] XP
        
        
On Wed, Jun 2, 2010 at 5:27 AM, Mark <mhh@absamail.co.za> wrote:
> I created the INF file using inf-wizard.exe. My lsusb output is:
>...
> cannot read device status, Broken pipe (32)

This is not a real problem. If you run as root or sudo, lsusb may be fine.

What is the output of testlibusb-win.exe under Windows?



PyUSB 1.0 alpha 0 release notification
======================================

::


    from    Wander Lairson <wander.lairson@gmail.com>
    reply-to    pyusb-users@lists.sourceforge.net
    to  pyusb-users <pyusb-users@lists.sourceforge.net>
    date    Fri, Apr 16, 2010 at 5:14 PM
    subject [pyusb-users] PyUSB 1.0 alpha 0 release notification
        

Dear all,

This is the first PyUSB 1.0 series public release. This is an alpha
release, which means that most of the features described in the README 
file and on the website are not yet stable or even implemented.

Features not implemented
------------------------

- Full support for legacy 0.4 legacy code (although partial support is
  provided).
- OpenUSB backend.
- libusb 1.0 windows backend stability (although it is reasonable usable).
- Support for several standard control requests (including GET_STRING).
- Python < 2.6 and Python 3 not yet fully tested.

Known issues
------------

- 'reset' method fails under FreeUSB (libusb 1.0 backend).
- 'reset' method hangs under Windows (libusb 1.0 backend).
- Sometimes occurs `read` timeout on Windows (libusb 1.0 backend).
- Test cases fail to run under cygwin.

Best regards,
Wander




