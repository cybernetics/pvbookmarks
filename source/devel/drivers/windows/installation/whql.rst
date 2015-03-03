
.. index::
   pair: Windows; WHQL (Windows Hardware Quality Lab)


.. _windows_drivers_install_whql:

=============================
Windows Drivers install whql
=============================


Windows libusb0.sys back end considerations
===========================================

::

    from    Orin Eman <orin.eman@gmail.com>
    to  graeme@argyllcms.com
    cc  libusb-devel <libusb-devel@lists.sourceforge.net>
    date    Tue, Apr 27, 2010 at 8:13 AM
    subject Re: [Libusb-devel] Windows libusb0.sys back end considerations.


On Mon, Apr 26, 2010 at 10:44 PM, Graeme Gill <graeme2@argyllcms.com> wrote::

    Xiaofan Chen wrote:
    > When you submit the driver packages for WHQL
    > (with a Verisign certificate), the resultant sys file will also
    > embedded the digital signature. This is what I expect.

    I don't think it works that way. The Microsoft documentation
    assumes that you would only do this for test signing, and assumes
    that you create a catalog file for the "real thing".
    This is the case for the PRUFTECHNIK package.


Well, since I put a couple of drivers through WHQL last year...
Only the cat file gets signed by WHQL.  For the sys files, you sign
the sys files with your own code signing certificate along with a
datestamp and cross-certificate that enables the kernel to validate
the signature on the driver.
The WHQL signature enables the driver to be installed silently
- if you sign/datestamp the cat file with your own certificate,
the OS will bring up the "Do you trust..." dialog when you try
to install the driver.
Keyboard filter drivers at least can be installed without WHQL
signing - the driver still needs to be signed/datestamped and
the cross-certificate included, but installation of the driver is
just a matter of adjusting a registry entry and service.
Whether this would extend to a USB filter driver, I don't know.

Orin.


::

    from    Orin Eman <orin.eman@gmail.com>
    to
    cc  libusb-devel <libusb-devel@lists.sourceforge.net>
    date    Tue, Apr 27, 2010 at 8:20 AM
    subject Re: [Libusb-devel] Windows libusb0.sys back end considerations.

        Xiaofan Chen wrote:
        > When you submit the driver packages for WHQL
        > (with a Verisign certificate), the resultant sys file will also
        > embedded the digital signature. This is what I expect.

        I don't think it works that way. The Microsoft documentation
        assumes that you would only do this for test signing, and assumes
        that you create a catalog file for the "real thing".
        This is the case for the PRUFTECHNIK package.

    Well, since I put a couple of drivers through WHQL last year...

    Only the cat file gets signed by WHQL.  For the sys files, you
    sign the sys files  with your own code signing certificate along
    with a datestamp and cross-certificate that enables the kernel
    to validate the signature on the driver.


BTW, the OS will consider a signature invalid if you don't include a
timestamp and the current date and time falls out the range of valid
dates for the code signing certificate...  I've seen signed software
from reputable sources reported as "Unknown Publisher" because the
signature wasn't timestamped and the certificate had run out.

Orin.

::

    from    Xiaofan Chen <xiaofanc@gmail.com>
    to  graeme@argyllcms.com
    cc  libusb-devel <libusb-devel@lists.sourceforge.net>
    date    Tue, Apr 27, 2010 at 11:49 AM
    subject Re: [Libusb-devel] Windows libusb0.sys back end considerations.

    On Tue, Apr 27, 2010 at 1:44 PM, Graeme Gill <graeme2@argyllcms.com> wrote:
    > Xiaofan Chen wrote:
    >> When you submit the driver packages for WHQL
    >> (with a Verisign certificate), the resultant sys file will also
    >> embedded the digital signature. This is what I expect.
    >
    > I don't think it works that way. The Microsoft documentation
    > assumes that you would only do this for test signing, and assumes
    > that you create a catalog file for the "real thing".
    > This is the case for the PRUFTECHNIK package.
    >

    I see. But somehow I have used the driver with no issue
    under my Win74 64bit box. I need to try again.

    And supposedly Pruftechnik can use the same Verisign
    digital signature for both the WHQL and the KMCS since
    they already paid that. I would expect this to be the norm.
    Of course they can have a separate code signing certificate
    for the .sys driver and the Verisign one for WHQL.

http://www.techtalkz.com/microsoft-device-drivers/268236-who-get-code-signing-certificate.html



"First there are two types of signing. There is digital signing to identify
the vendor required for 64-bit Vista, that is what the link you listed
below is about. Second there is the digital signature for passing WHQL and
for accessing the WinQual database of crashes (when you get that nice
prompt after a reboot from a crash that asks if you want to report this to
Microsoft, it goes to WinQual). For the second VeriSign is the only one
that is accepted. So basically, unless you only care about the digital
signature needed for Vista 64-bit you need to go to Verisign."

"I can confirm this. The certificate you use for submitting the WHQL stuff
can be used to sign binaries for Vista. I've used it to sign a driver for
Vista x64. In this case you just need to remember to use the cross-signing
procedures described in the Vista x64 driver signing walkthrough."

Official page:
https://winqual.microsoft.com/help/default.htm#winqual_requirements.htm

And it seems they have a offer, now it is US$99.

