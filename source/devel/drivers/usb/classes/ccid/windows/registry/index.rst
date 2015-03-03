.. Windows_registry
    :platform: windows XP, Vista, windows 7


.. index::
   pair: registry ; HKLM
   pair: registry ;  "Device Parameters" key
   pair: registry ;  HKLM\\SYSTEM\\CurentControlSet\\Enum\\USB

=========================================
HKLM\\SYSTEM\\CurentControlSet\\Enum\\USB
=========================================

.. seealso:: :ref:`windows_devcon_tool`


"Device Parameters" key
=======================

EscapeCommandEnable value
-------------------------

.. seealso:: http://www.microsoft.com/whdc/device/input/smartcard/USB_CCID.mspx

In order to send or receive an Escape command to a reader, the DWORD
registry value EscapeCommandEnable must be added and set to a non-zero
value under the HKLM\SYSTEM\\CurentControlSet\\Enum\\USB\\Vid*Pid*\\*\\Device Parameters key.

Then the vendor IOCTL for the Escape command is defined as follows::

    #define IOCTL_CCID_ESCAPE SCARD_CTL_CODE(3500).

With the enabled Escape Command, security against malicious escape
commands becomes the reader's responsibility.
