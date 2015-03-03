
.. index::
   November 3, 2009

===============================================
Troubleshooting Smart Card Plug and Play Issues
===============================================

- http://technet.microsoft.com/en-us/library/dd979547%28WS.10%29.aspx

Updated: November 3, 2009
Applies To: Windows 7, Windows Server 2008 R2

Symptom
=======

After installing or upgrading to Windows 7, smart card Plug and Play 
detection may not work as expected, and a user or local administrator 
needs to find and resolve problems that prevent smart card Plug and Play
detection on Windows 7 from functioning correctly.

Cause
=====

This section of the guide provides troubleshooting information that 
helps you find and resolve smart card Plug and Play issues in Windows 7.

Resolution
==========

Before you begin troubleshooting smart card Plug and Play, you should 
ensure that you can provide administrative credentials. 

You should also understand smart card solutions that are not compatible with 
Plug and Play and how smart cards work with **Remote Desktop connections**.

Administrative credentials
==========================

You must be a member of the local Administrators group on the 
Windows 7–based computer on which you are troubleshooting 
smart card issues or know the user name and password of a 
local administrator account. 

If you are not logged on with an administrator account, you must
provide administrator credentials to perform many of the tasks in this guide.

Smart card solutions that are not compatible with Plug and Play
===============================================================

Smart card Plug and Play only supports smart cards that require 
drivers to function. 

Not all smart card solutions require drivers for integrating with Windows. 
These solutions do not use the Windows Smart Card Framework and must be installed 
on the computer before using the smart card for the first time.

The following solutions are not compatible with smart card Plug and Play:

- Custom cryptographic service provider (CSP)-based solutions.
- Custom key storage provider (KSP)-based solutions.
- Public Key Cryptography Standard #11 (PKCS #11)-based solutions.
- Smart card driver packages without complete INF files or with 
  incorrect device identifications.
- Some multislot smart card readers that create only one device for 
  all available slots in the smart card reader.

Each time a smart card is inserted in the computer, Windows attempts to download 
and install the smart card driver if it is not already available on the computer. 

You may see a Plug and Play error when you insert a non-Plug and Play smart card
on the computer. This does not necessarily mean that there is a problem 
with the smart card.

If your deployment uses only non-Plug and Play smart card solutions, 
smart card Plug and Play can be disabled by a local administrator 
on a client computer. 

Disabling smart card Plug and Play prevents smart card drivers, 
also known as smart card mini-drivers, from downloading and prevents 
smart card Plug and Play prompts.

To disable smart card Plug and Play in local Group Policy

- On a client computer, click Start, type gpedit.msc in the Search programs 
  and files box, and then press ENTER.
- In the console tree under Computer Configuration, 
  click Administrative Templates.
- In the details panel, double-click Windows Components, 
  and then double-click Smart Card.
- Right-click Turn on Smart Card Plug and Play service, 
  and then click Edit.
- Click Disabled, and then click OK.

For enterprise deployments, smart card Plug and Play can be disabled by 
deploying a Group Policy. 

For information about administrative templates, 
see Administrative templates overview for GPMC (http://go.microsoft.com/fwlink/?LinkId=152390).

.. warning:: 
    For commercial deployments that target end-users (such as online banking) 
    and environments that include both Plug and Play and non-Plug and Play 
    smart cards, using Group Policy to disable Plug and Play for smart cards 
    is strongly discouraged because it will affect all the smart cards 
    in your environment.

Remote Desktop connections and smart cards
==========================================

Smart card Plug and Play works only for local sessions on a computer. 

The smart card driver must be installed on the local computer before 
attempting to use smart cards with Remote Desktop connections. 

The driver can be installed by inserting a Plug and Play–compatible 
smart card in a smart card reader on the local computer or by manually 
installing the driver. 

For information about manually installing drivers, 
see Manually Install a Smart Card Driver in this guide.

Steps for troubleshooting smart card Plug and Play
==================================================

The steps to identify and resolve issues associated with smart card detection 
and driver installation are demonstrated in the following flowchart.

Smart Card troubleshooting steps
================================

The table follows the troubleshooting steps in the flowchart and provides 
links to the information about the troubleshooting step that may 
help you resolve the issue.
 
Troubleshooting step Description
================================

User inserts smart card in the smart card reader
When the smart card is inserted in the smart card reader, Windows 
searches for a smart card driver.

Does the smart card work as expected ?
======================================	

If the smart card works as expected, the user can use the smart card.
If the smart card does not work as expected, begin the troubleshooting process.

Is the logon screen displayed ?
===============================
	
If the logon screen is displayed, log on to the computer as a 
local administrator, and then see Verify that the Smart Card 
Reader Device and Driver Are Installed Correctly.

If the computer is configured to allow only smart card logon, 
see Log On in Safe Mode to Configure the Computer for Password Logon.

If the logon screen is not displayed, see Verify that the Smart Card 
Reader Device and Driver Are Installed Correctly.

Are the smart card reader device and driver installed correctly ?
=================================================================

To check the smart card reader device and driver, see Verify that the 
Smart Card Reader Device and Driver Are Installed Correctly. 
If you reinstalled the smart card device driver, reinsert the smart card 
into the smart card reader.

If the smart card reader device and driver are installed correctly, 
see Verify that the Smart Card Is Installed Correctly.

Is the Smart cards node listed in Device Manager ?
==================================================
	
If the smart card is listed in the Smart cards node in Device Manager,
the user can use the smart card.

If the Smart cards node is not listed in Device Manager, see Verify Network Connectivity.

Is network connectivity available ?
===================================

If network connectivity is available, see Verify that 
Windows Update Is Enabled.

If network connectivity is not available, enable network connectivity, 
and then reinsert the smart card into the smart card reader.

Is Windows Update enabled ?
===========================
	
If Windows Update is enabled, see Verify that the Certificate Propagation 
and Smart Card Services Are Running.
If Windows Update is not enabled, enable Windows Update, and then 
see Verify that the Smart Card Is Installed Correctly.

Are the Certificate Propagation and Smart Card services running ?
-----------------------------------------------------------------
	
If the services are running, see Manually Install a Smart Card Driver, 
and then reinsert the smart card into the smart card reader.

If the services are not running, start the services, and then see Verify 
that the Smart Card Is Installed Correctly.



