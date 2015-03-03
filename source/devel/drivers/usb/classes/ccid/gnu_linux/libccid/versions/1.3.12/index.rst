
.. index::
   pair: libccid; 1.3.12



==========================
Changes for libccid 1.3.12
==========================


.. contents::
   :depth: 3


Changes
=======

- add support of Todos AGM2 CCID, Cherry SmartTerminal XX7X, Smart
  SBV280, Ask CPL108, German Privacy Foundation Crypto Stick v1.2
- better support of Dell keyboard
- better support of multislot readers (like the GemCore SIM Pro)
- better support of SCM SCR3310
- The Covadis Véga-Alpha reader is a GemPC pinpad inside. So we use
  the same code to:

    * load the strings for the display
    * avoid limitation of the reader

- IFDHControl() the (proprietary) get firmware version escape
  command is allowed with a Gemalto reader:

      * the (proprietary) switch interface escape command is allowed on
        the Gemalto GemProx DU
      * return IFD_ERROR_NOT_SUPPORTED instead of IFD_COMMUNICATION_ERROR
        if the dwControlCode value is not supported
      * return IFD_ERROR_INSUFFICIENT_BUFFER when appropriate

- IFDHGetCapabilities(): add support of SCARD_ATTR_ICC_PRESENCE and
  SCARD_ATTR_ICC_INTERFACE_STATUS

- **support extended APDU of up to 64kB with APDU readers**

- get the language selected during Mac OS X installation as language
  to use for Covadis Véga-Alpha and Gemalto GemPC PinPad pinpad
  readers

- some minor bugs removed


2010-05-08
==========

Ludovic Rousseau

- [r4932] configure.in: Minimum version of pcsc-lite is 1.6.0
  instead of the unreleased 1.5.6
- [r4931] README, configure.in: release 1.3.12

2010-05-07
==========

Ludovic Rousseau

- [r4930] MacOSX/configure: - use libusb-1.0 and libusb-compat-0.1
  build for Snow Leopard
- [r4928] src/ifdhandler.c: IFDHControl(): set
  PCSCv2_PART10_PROPERTY_bEntryValidationCondition specific value
  only for the Gemalto PC Pinpad V1 & Covadis Véga-Alpha readers.
- [r4927] examples/scardcontrol.c: Reformat output
- [r4926] src/ifdhandler.c: IFDHControl(): The Covadis Véga-Alpha
  share the same firmware with the Gemalto PC Pinpad V1
- [r4925] src/ifdhandler.c: IFDHControl(): add comments
- [r4924] src/ifdhandler.c: IFDHControl(): add support of
  IOCTL_FEATURE_GET_TLV_PROPERTIES bMinPINSize & bMaxPINSize for
  Gemalto Pinpad V1

2010-05-03
==========

Ludovic Rousseau

- [r4914] readers/SCR3500.txt: add SCM SCR3500 (same idProduct as
  SCR355 but different firmware)

2010-05-02
==========

Ludovic Rousseau

- [r4908] readers/Athena_IDProtect_Key.txt,
  readers/supported_readers.txt: add Athena IDProtect Key
  (unsupported see
  http://www.opensc-project.org/pipermail/opensc-user/2010-May/004023.html)

2010-05-01
==========

Ludovic Rousseau

- [r4907] src/ccid_usb.h: Do not try to be smart and always
  #include <usb.h>
  Should fix FreeBSD issues

2010-04-29
==========

Ludovic Rousseau

- [r4902] src/commands.c: SecurePINVerify() & SecurePINModify():
  with a TPDU reader and a T=1 card the ns & nr sequence numbers
  were not correctly handled if the CCID command was rejected at
  the reader level (not sent to the card). The next APDU sent to
  the card would fail.

2010-04-25
==========

Ludovic Rousseau

- [r4897] src/ifdhandler.c: IFDHControl(): reuse ccid_descriptor
  variable when available
- [r4896] src/ccid.h, src/ifdhandler.c: FEATURE_MCT_READER_DIRECT
  is also supported by the Kobil mIDentity visual

2010-04-24
==========

Ludovic Rousseau

- [r4893] readers/Kobil_Smart_Token.txt,
  readers/Kobil_mIDentity_4smart.txt,
  readers/Kobil_mIDentity_4smart_AES.txt,
  readers/Kobil_mIDentity_fullsize.txt,
  readers/Kobil_mIDentity_fullsize_AES.txt,
  readers/Kobil_mIDentity_visual.txt,
  readers/supported_readers.txt: add KOBIL Smart Token, KOBIL
  mIDentity 4smart, KOBIL mIDentity 4smart AES, KOBIL mIDentity
  visual, KOBIL mIDentity fullsize, KOBIL mIDentity 4smart fullsize
  AES

2010-04-18
==========

Ludovic Rousseau

- [r4886] src/commands.c: CmdXfrBlockCHAR_T0(): debug ICCD type A
  algorithm
  Thanks to Alexander Abarzhi for the patch

2010-04-16
==========

Ludovic Rousseau

- [r4879] src/ifdhandler.c: Fix Studio CC warning "ifdhandler.c",
  line 1275: warning: initializer does not fit or is out of range:
  248
- [r4878] src/ifdhandler.c: Fix Sun Studio CC warnings
  "ifdhandler.c", line 910: warning: initializer does not fit or is
  out of range: 250 "ifdhandler.c", line 910: warning: initializer
  does not fit or is out of range: 255 "ifdhandler.c", line 910:
  warning: initializer does not fit or is out of range: 129
  "ifdhandler.c", line 911: warning: initializer does not fit or is
  out of range: 128 "ifdhandler.c", line 911: warning: initializer
  does not fit or is out of range: 193 "ifdhandler.c", line 911:
  warning: initializer does not fit or is out of range: 192
  "ifdhandler.c", line 912: warning: initializer does not fit or is
  out of range: 144 "ifdhandler.c", line 912: warning: initializer
  does not fit or is out of range: 177
- [r4876] readers/SCL01x.txt: SCM SCL01x Contactless Reader

2010-04-09
==========

Ludovic Rousseau

- [r4869] readers/ATMEL_AT90SCR050.txt,
  readers/ATMEL_AT90SCR100.txt, readers/ATMEL_VaultIC420.txt,
  readers/ATMEL_VaultIC440.txt, readers/ATMEL_VaultIC460.txt,
  readers/supported_readers.txt: Add Atmel AT90SCR100, Atmel
  AT90SCR050, Atmel VaultIC420, Atmel VaultIC440, Atmel VaultIC460

2010-04-06
==========

Ludovic Rousseau

- [r4856] readers/supported_readers.txt: Remove duplicate Vid/Pid
  entry for Alcor Micro SCR001 and Micro AU9520
- [r4854] readers/Vasco_DP855.txt, readers/Vasco_DP865.txt,
  readers/Vasco_DPKey200.txt, readers/Vasco_DPKey860.txt,
  readers/supported_readers.txt: Add Vasco DIGIPASS KEY 860, Vasco
  DIGIPASS KEY 200, Vasco DP855, Vasco DP865

2010-03-31
==========

Ludovic Rousseau

- [r4849] readers/GoldKey_PIV_Token.txt,
  readers/supported_readers.txt: add GoldKey PIV Token

2010-03-30
==========

Ludovic Rousseau

- [r4847] src/ccid_ifdhandler.h, src/ifdhandler.c: add support of
  FEATURE_GET_TLV_PROPERTIES
- [r4846] examples/scardcontrol.c: add support of
  FEATURE_GET_TLV_PROPERTIES

2010-03-27
==========

Ludovic Rousseau

- [r4844] src/Info.plist.src, src/commands.c, src/ifdhandler.c:
  remove spaces and tabs at end of line

2010-03-14
==========

Ludovic Rousseau

- [r4815] readers/supported_readers.txt: Enable the Broadcom 5880
  reader. It should work after a firmware upgrade.

2010-03-12
==========

Ludovic Rousseau

- [r4814] INSTALL, examples/scardcontrol.c,
  readers/supported_readers.txt, src/ccid_serial.c,
  src/reader.conf.in: Rename Gemplus in Gemalto

2010-03-05
==========

Ludovic Rousseau

- [r4796] src/commands.c: CmdXfrBlockCHAR_T0(): limit the received
  length to 0x1000 for ICCD Version A length is 16-bits and
  usb_control_msg() fails with "Invalid argument" if the length
  is > 0x100
  The same patch was already present in CmdXfrBlockAPDU_extended
  for ICCD Version B
  Thanks to Alexander Abarzhi for the patch
- [r4795] src/commands.c: CCID_Receive(): set the received length
  for a ICCD Version A device
  Thanks to El Tuba for the patch

2010-02-26
==========

Ludovic Rousseau

- [r4780] readers/supported_readers.txt: SCM SDI 010 removed on
  manufacturer request since not supported by my driver

2010-02-24
==========

Ludovic Rousseau

- [r4776] readers/supported_readers.txt: Removed Smart SBV280 on
  manufacturer request. They use **libusb directly**.
- [r4775] readers/Broadcom_5880.txt: regenerate

2010-02-23
==========

Ludovic Rousseau

- [r4771] readers/Covadis_Auriga.txt,
  readers/supported_readers.txt: add Covadis Auriga

2010-02-12
==========

Ludovic Rousseau

- [r4761] readers/id3_CL1356D.txt, readers/supported_readers.txt:
  id3_CL1356D.txt is a duplicate of id3_CL1356T5.txt
- [r4759] readers/id3_CL1356T5.txt, readers/supported_readers.txt:
  add id3 CL1356T5
- [r4757] readers/Gemalto_PDT.txt, readers/supported_readers.txt:
  update Gemalto PDT

2010-02-09
==========

Ludovic Rousseau

- [r4750] src/ccid_usb.c: Fix 1 compiler warning
  ccid_usb.c: In function "InterruptRead": ccid_usb.c:987: warning:
  pointer targets in passing argument 3 of "log_xxd" differ in
  signedness /usr/include/PCSC/debuglog.h:83: note: expected "const
  unsigned char pointer" but argument is of type "char pointer"
- [r4749] src/commands.c: Fix 2 compiler warnings
  commands.c: In function "CCID_Transmit": commands.c:1107:
  warning: passing argument 5 of "ControlUSB" discards qualifiers
  from pointer target type ccid_usb.h:43: note: expected "unsigned
  char pointer" but argument is of type "const unsigned char pointer"
  commands.c:1130: warning: passing argument 5 of "ControlUSB"
  discards qualifiers from pointer target type ccid_usb.h:43: note:
  expected "unsigned char pointer" but argument is of type "const
  unsigned char pointer"
- [r4748] src/ccid_usb.c: Fix a compiler warning
  ccid_usb.c: In function "OpenUSB": ccid_usb.c:138: warning:
  unused parameter "Channel"
- [r4747] readers/Makefile.am: Do not include the reader
  descriptions in the archive, only the supported_readers.txt file
- [r4746] Makefile.am, configure.in: use readers/ again (revert
  revision 4745)
- [r4745] Makefile.am, configure.in: Do not include the readers/*
  files in the archive

2010-02-05
==========

Ludovic Rousseau

- [r4712] readers/CL1356T.txt, readers/id3_CL1356T.txt: rename
  CL1356T.txt in id3_CL1356T.txt like the other id3_* readers

2010-02-04
==========

Ludovic Rousseau

- [r4709] src/commands.c: add Copyright (C) 2005 Martin Paljak and
  update my copyright date

2010-01-29
==========

Ludovic Rousseau

- [r4694] readers/GPFCryptoStick.txt,
  readers/supported_readers.txt: add German Privacy Foundation
  Crypto Stick v1.2

2010-01-22
==========

Ludovic Rousseau

- [r4684] configure.in: use LT_INIT(disable-static) instead of the
  deprecated AM_DISABLE_STATIC

2010-01-21
==========

Ludovic Rousseau

- [r4680] configure.in: Static lib is disabled by default. Use
  --enable-static if needed

2010-01-19
==========

Ludovic Rousseau

- [r4676] readers/GemPC_Express.txt: update

2010-01-13
==========

Ludovic Rousseau

- [r4665] readers/Ask_CPL108.txt, readers/supported_readers.txt:
  ass Ask CPL108

2010-01-11
==========

Ludovic Rousseau

- [r4655] readers/supported_readers.txt: update Gemalto Prox-DU and
  Prox-SU names
- [r4654] readers/supported_readers.txt: update "Gemalto Prox DU"
  name

2010-01-04
==========

Ludovic Rousseau

- [r4639] src/debug.c: debug.c: In function "log_msg": debug.c:38:
  warning: unused parameter "priority" debug.c: In function
  "log_xxd": debug.c:51: warning: unused parameter "priority"
- [r4638] src/ifdhandler.c: ifdhandler.c: In function
  "IFDHSetCapabilities": ifdhandler.c:553: warning: unused
  parameter "Length" ifdhandler.c:553: warning: unused parameter
  "Value" ifdhandler.c: In function "IFDHTransmitToICC":
  ifdhandler.c:1171: warning: unused parameter "RecvPci"
- [r4637] contrib/Kobil_mIDentity_switch/Kobil_mIDentity_switch.c:
  Kobil_mIDentity_switch.c: In function "main":
  Kobil_mIDentity_switch.c:136: warning: unused parameter "argc"
  Kobil_mIDentity_switch.c:136: warning: unused parameter "argv"
- [r4636] src/openct/proto-t1.c: t1_release(): fix compilation
  warning openct/proto-t1.c:116: warning: unused parameter "t1"

2010-01-02
==========

Ludovic Rousseau

- [r4631] readers/Broadcom_5880v2.txt,
  readers/supported_readers.txt: another Broadcom 5880 reader
  (iProduct: 5880) which looks like to work correctly

2009-12-16
==========

Ludovic Rousseau

- [r4619] src/ccid_usb.c: Todos Argos Mini II with firmware before
  1.01 has a bogus CCID descriptor: "Automatic IFSD exchange as
  first exchange (T=1)" is missing. You can't use a T=1 card with
  this reader.
- [r4618] src/ccid_usb.c: Precise Biometrics Precise 250 MC with
  firmware before 50.00 is bogus: time extension requests are not
  sent back to the host
- [r4617] readers/Todos_AGM2_CCID.txt: firmware 1.01

2009-12-15
==========

Ludovic Rousseau

- [r4614] examples/scardcontrol.c, src/ccid_ifdhandler.h,
  src/ifdhandler.c: rename FEATURE_MCT_READERDIRECT in
  FEATURE_MCT_READER_DIRECT

2009-12-13
==========

Ludovic Rousseau

- [r4610] src/ccid.c: ccid_open_hack_post(): get the language
  selected during Mac OS X installation as language to use for
  Covadis Véga-Alpha and Gemalto GemPC PinPad pinpad readers

2009-12-09
==========

Ludovic Rousseau

- [r4597] readers/Precise_250_MC.txt: firmware update
- [r4594] src/parse.c: do not generate extra space at end of line

2009-12-05
==========

Ludovic Rousseau

- [r4592] src/ccid_usb.c: Precise Biometrics Precise 200 MC with
  firmware before 50.00 is bogus: time extension requests are not
  sent back to the host
- [r4590] readers/supported_readers.txt: improve docmentation of
  bogus readers
- [r4589] readers/supported_readers.txt: add OCS ID-One Cosmo Card
  (with ProductID 0x6356) in a commented line (unsupported)
- [r4588] readers/Gemalto_HybridSmartcardReader.txt: Gemalto Hybrid
  Smartcard Reader

2009-12-02
==========

Ludovic Rousseau

- [r4584] readers/Precise_200_MC.txt: new firmware

2009-11-18
==========

Ludovic Rousseau

- [r4556] readers/Oberthur-CosmoCard1.txt: other version of the OCS
  ID-One Cosmo Card

2009-11-17
==========

Ludovic Rousseau

- [r4550] src/ccid.c, src/ccid.h, src/commands.c: The Covadis
  Véga-Alpha reader is a GemPC pinpad inside. So we use the same
  code to: - load the strings for the display - avoid limitation of
  the reader
  Thanks to Loïs Lherbier for the patch

2009-11-13
==========

Ludovic Rousseau

- [r4545] src/commands.c: CmdGetSlotStatus(): the SCM SCR3310 also
  reports an error 0xFE (ICC_MUTE) when no card is inserted. So
  extend the special case to all readers and not just the O2MICRO
  OZ776.
  Thanks to Ivan Vilata i Balaguer for the bug report (Debian bug
  #555837)

2009-10-28
==========

Ludovic Rousseau

- [r4521] src/ccid_serial.c: set_ccid_descriptor(): reset
  dwSlotStatus to IFD_ICC_PRESENT for the other slots of a
  multislot reader (like a GemCore SIM Pro).
  This is needed because the state of dwSlotStatus may have already
  been changed to IFD_ICC_NOT_PRESENT (by the polling thread) when
  the second slot is created. The polling thread of the second slot
  would then never check for a card since this check is only done
  once. Slots are SAMs and the card is always present or absent.
  The problem was already dealt with on USB from the beginning but
  not on serial.
  Thanks to Emmanuel Deloget for the patch.


.. index::
   CMD_BUF_SIZE


2009-10-25
==========

Ludovic Rousseau

- [r4510] src/defs.h: change CMD_BUF_SIZE to support extended APDU
  of up to 64kB. We need this size for readers in APDU mode to be
  able to receive the card response in one block (chaining is not
  always possible in this direction)
- [r4509] src/defs.h: remove useless #define
- [r4508] src/ifdhandler.c: FDHPowerICC(): use the exact length for
  the PowerOn output buffer
- [r4507] src/defs.h: remove useless #defines

2009-10-24
==========

Ludovic Rousseau

- [r4505] configure.in: check for IFD_ERROR_INSUFFICIENT_BUFFER in
  ifdhandler.h and simplify the PCSC checking code

2009-10-21
==========

Ludovic Rousseau

- [r4502] readers/Precise_250_MC.txt: new firmware
- [r4501] readers/Precise_200_MC.txt: new firmware

2009-10-18
==========

Ludovic Rousseau

- [r4499] src/ifdhandler.c: FDHGetCapabilities(): add support of
  SCARD_ATTR_ICC_PRESENCE
  Required to support the Windows middleware that's used for French
  Healthcar cards.
  Thanks to David Markowitz for the patch.
- [r4498] src/ifdhandler.c: FDHGetCapabilities(): add support of
  SCARD_ATTR_ICC_INTERFACE_STATUS
  Required to support the Windows middleware that's used for French
  Healthcar cards.
  Thanks to David Markowitz for the patch.

2009-10-14
==========

Ludovic Rousseau

- [r4493] readers/Smart_SBV280.txt, readers/supported_readers.txt:
  add Smart SBV280


.. index::
   usb_strerror()


2009-10-08
==========

Ludovic Rousseau

- [r4450] src/ccid_ifdhandler.h, src/ifdhandler.c: IFDHControl():
  do not check if FEATURE_IFD_PIN_PROPERTIES is defined since we
  now require pcsc-lite >= 1.5.6 (with FEATURE_IFD_PIN_PROPERTIES
  defined)
- [r4449] src/ifdhandler.c: IFDHGetCapabilities() & IFDHControl():
  return IFD_ERROR_INSUFFICIENT_BUFFER when appropriate
- [r4448] configure.in, src/commands.c: Require to have pcsc-lite
  >= 1.5.6 to have IFD_ERROR_INSUFFICIENT_BUFFER defined in
  ifdhandler.h
- [r4446] src/ccid_usb.c: Use usb_strerror() instead of
  strerror(errno) to also get the libusb specifc error messages
- [r4441] README: The supported, should work and unsupported lists
  are now online only.
  The information in the README file was not up to date and hard to
  sync.

2009-10-02
==========

Ludovic Rousseau

- [r4417] src/ifdhandler.c: revert change in revision 4414. It is a
  bug in the reader not the driver
- [r4416] ylwrap: update
- [r4414] src/ifdhandler.c: IFDHSetProtocolParameters(): with a T=1
  card, do not try to negociate IFSD if the reader works in APDU
  mode
- [r4413] readers/Todos_AGM2_CCID.txt: update

2009-10-01
==========

Ludovic Rousseau

- [r4411] src/ifdhandler.c: IFDHControl(): typo in comment

2009-09-30
==========

Ludovic Rousseau

- [r4410] src/ifdhandler.c: IFDHControl(): PIN_PROPERTIES_STRUCTURE
  structure do not have the wLcdMaxCharacters and wLcdMaxLines
  fields anymore. Conform with Revision 2.02.06, April 2009 of
  PCSCv2 part 10.
  Modified in pcsc-lite > 1.5.5 (revision 4378, 2009-09-08)

2009-09-28
==========

Ludovic Rousseau

- [r4401] src/ccid_usb.c: OpenUSBByName(): make the libhal scheme
  parsing more robust. Readers serial "numbers" may contain '_'
  characters

2009-09-25
==========

Ludovic Rousseau

- [r4397] src/ifdhandler.c: IFDHPowerICC(): remove a useless ;

2009-09-22
==========

Ludovic Rousseau

- [r4392] readers/CherrySmartTerminalXX7X.txt,
  readers/supported_readers.txt: add Cherry SmartTerminal XX7X
- [r4390] examples/GPL-2, examples/Makefile.am: sample code is
  GPLv2+
- [r4389] src/commands.c: SecurePINVerify(): circumvent a Dell
  keyboard problem avoid the command rejection because the Enter
  key is still pressed. Wait a bit (250ms) for the (Enter) key to
  be released.

2009-09-10
==========

Ludovic Rousseau

- [r4383] src/ccid.h, src/commands.c: circumvent bugs of the Dell
  413c:2100 keyboard
- [r4382] readers/DellSK-3106.txt: regenerate
- [r4380] src/Info.plist.src: typo in comment

2009-08-30
==========

Ludovic Rousseau

- [r4372] readers/Todos_AGM2_CCID.txt,
  readers/supported_readers.txt: add Todos AGM2 CCID

2009-08-27
==========

Ludovic Rousseau

- [r4368] SCARDCONTOL.txt: List of SCardControl() commands
  supported by the CCID driver
- [r4366] src/ifdhandler.c: IFDHControl(): return
  IFD_ERROR_NOT_SUPPORTED instead of IFD_COMMUNICATION_ERROR if the
  dwControlCode value is not supported

2009-07-31
==========

Ludovic Rousseau

- [r4360] src/ccid.c: ccid_open_hack_pre(): do not call
  InterruptRead() on Mac OS X. The libusb does not timeout and
  blocks forever.
- [r4358] src/ifdhandler.c: IFDHControl(): the (proprietary) switch
  interface escape command is allowed on the Gemalto GemProx DU
- [r4356] src/ifdhandler.c: IFDHControl(): the (proprietary) get
  firmware version escape command is allowed with a Gemalto reader
- [r4355] src/ccid.h: add GET_VENDOR macro


