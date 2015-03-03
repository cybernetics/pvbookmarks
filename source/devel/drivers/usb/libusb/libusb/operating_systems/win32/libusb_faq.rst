.. module:: libUSB-winusb 
    :synopsis: libUSB-winusb annexes 


.. index::
   signtool
   libusb on windows 7 64bits
   64bits libusb on windows 7
   
libusb FAQ
==========

Libusb on windows 7 64bits
--------------------------

:: 

    from    Xiaofan Chen <xiaofanc@gmail.com>
    reply-to    libusb-win32-devel@lists.sourceforge.net
    to    libusb-win32-devel@lists.sourceforge.net
    date    Fri, Jan 22, 2010 at 3:07 AM
    subject    Re: [Libusb-win32-devel] Building Libusb for 64-bit Windows Vista and Seven
    mailing list    <libusb-win32-devel.lists.sourceforge.net> Filter messages from this mailing list
    mailed-by    lists.sourceforge.net
    unsubscribe    Unsubscribe from this mailing-list
    

> I have read on a forum that the digital signing process requires the major
> version number of the DLL to be greater or equal to 1. The current major
> version number of Libusb is 0.

Yes that is said to be the major thing to be changed to get WHQL
for libusb-win32 based driver.

> Could you please tell me how to build these 64-bit files?
You need DDK/WDK.

One company has already got their libusb-win32 based device driver
WHQL certified. Please refer to the following archived thread.
http://old.nabble.com/Win-Vista-32-64-Build.-td17313102.html

The modified sources can be downloaded here.
http://www.pruftechnik.com/condition-monitoring/support-and-downloads/software.html
http://www.pruftechnik.com/fileadmin/user_upload/COM/Condition_Monitoring/Common/gplusb/PTLibUSB_SRC.tar

The file change_mfh.txt list the changes.


::

    from    Bachelier, Georges <georges.bachelier@atmel.com>
    reply-to    libusb-win32-devel@lists.sourceforge.net
    to    libusb-win32-devel@lists.sourceforge.net
    date    Mon, Jan 25, 2010 at 4:03 PM
    subject    Re: [Libusb-win32-devel] Building Libusb for 64-bit WindowsVistaand Seven
    mailing list    <libusb-win32-devel.lists.sourceforge.net> Filter messages from this mailing list
    mailed-by    lists.sourceforge.net
    unsubscribe    Unsubscribe from this mailing-list


Yes, we are using our own certificate to sign the driver package.
The INF file seems to be OK according to the Pruftechnik one and examples
I have found.

I use inf2cat to build the catalog files, then signtool to sign them.

::


    signtool sign /f E:\labo\tools\atmel.pfx  /p **** atmel_usb_dfu.cat
    signtool sign /f E:\labo\tools\atmel.pfx  /p **** atmel_usb_dfu_x64.cat
    

I am currently reading this paper:
http://www.microsoft.com/whdc/winlogo/drvsign/kmcs_walkthrough.mspx

It contains detailed information about the signing process. I will let you know about the results.

:: 

    from    Bachelier, Georges <georges.bachelier@atmel.com>
    reply-to    libusb-win32-devel@lists.sourceforge.net
    to    libusb-win32-devel@lists.sourceforge.net
    date    Tue, Jan 26, 2010 at 5:39 PM
    subject    Re: [Libusb-win32-devel] Building Libusb for 64-bit WindowsVistaand Seven
    mailing list    <libusb-win32-devel.lists.sourceforge.net> Filter messages from this mailing list
    mailed-by    lists.sourceforge.net
    unsubscribe    Unsubscribe from this mailing-list
    

Hi Xiaofan!

After some tweaking in our driver building and signing processes, we finally 
got a successful Vista and Seven 64-bit LibUsb driver installation! We also 
have had to modify our INF file accordingly to the Pruftechnik's one.

Thanks a lot for your support on this topic, and thanks to all contributors 
who sent me solutions.

Kind regards,




  


   
   

     
   

   

   