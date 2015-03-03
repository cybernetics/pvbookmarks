
.. index::
   pair: windows 7 ; smartcards


=========================
What's New in Smart Cards
=========================

- http://technet.microsoft.com/en-us/library/dd367851%28WS.10%29.aspx

Updated: February 9, 2009

Applies To: Windows 7,Windows Server 2008 R2

Windows® 7 includes new features that make smart cards easier to use and
to deploy, and makes it possible to use smart cards to complete a greater
variety of tasks.

The new smart card features are available in all versions of Windows 7.

What's new in smart cards?
==========================

Windows 7 features enhanced support for smart card–related Plug and Play
and the Personal Identity Verification (PIV) standard from the
National Institute of Standards and Technology (NIST).

This means that users of Windows 7 can use smart cards from vendors who
have published their drivers through Windows Update without needing
special middleware.

These drivers are downloaded in the same way as drivers
for other devices in Windows.

When a PIV-compliant smart card is inserted into a smart card reader,
Windows attempts to download the driver from Windows Update.
If an appropriate driver is not available from Windows Update, a PIV-compliant
minidriver that is included with Windows 7 is used for the card.

Who will want to use smart cards ?
==================================

Network administrators who want to enhance the security of the organization's
computers, particularly portable computers used by remote users, will
appreciate the simplified deployment and use scenarios made possible
by smart card Plug and Play PIV support.

Users will appreciate the ability to use smart cards to perform
critical business tasks in a secure manner.

What are the benefits of the new and changed features ?
=======================================================

The new smart card support options in Windows 7 include:

- Encrypting drives with BitLocker Drive Encryption. In the Windows 7
  Enterprise and Windows 7 Ultimate operating systems, users can choose
  to encrypt their removable media by turning on BitLocker and then
  choosing the smart card option to unlock the drive.
  At run time, Windows retrieves the correct minidriver for the smart
  card and allows the operation to complete.

- Smart card domain logon by using the PKINIT protocol.
  In Windows 7, the correct minidriver for a smart card is retrieved
  automatically, enabling a new smart card to authenticate to the
  domain without requiring the user to install or configure additional
  middleware.

- Document and e-mail signing. Windows 7 users can rely on Windows to
  retrieve the correct minidriver for a smart card at run time to
  sign an e-mail or document.
  In addition, XML Paper Specification (XPS) documents can be
  signed without the need for additional software.

- Use with line-of-business applications. In Windows 7, any application
  that uses  Cryptography Next Generation (CNG) or CryptoAPI
  to enable the application to use certificates can rely on
  Windows to retrieve the correct minidriver for a smart card
  at run time so that no additional middleware is needed.

What's the impact of these changes on smart card usage ?
========================================================

Smart card usage is expanding rapidly. To encourage more organizations
and users to adopt smart cards for enhanced security, the process
to provision and use new smart cards is simplified and supports
more end user scenarios.




