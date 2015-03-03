
.. index::
   pair: PC/SC; Commands



.. _pcsc_commands:

==============
PC/SC commands
==============


.. index::
   APDU wrapping
   SCardTransmit


APDU Wrapping : proposition de comportement de l'API
=====================================================

::

    -----Message d'origine-----
    De : Philippe BOURGAULT [mailto:philippe.bourgault@id3.eu]
    Envoyé : mardi 13 janvier 2009 11:31
    À : 'Fabien Brun'; Patrick Vergain
    Objet : Command Passing Method and APDU Wrapping : proposition de
    comportement de l'API.

Introduction
------------

Managing specific contactless reader functionnalities requires lots of
commands. Some commands are defined by PC/SC 2.01 specifications but some
other commands are vendor specific = proprietary.

When defined by PC/SC 2.01 specifications, commands are formatted like APDU
and passed through a transmit() method call (PC/SC SCardTransmit method).
Regarding proprietary commands, the CL1356A reader allows them to be passed
either through a control() method call (PC/SC SCardControl method) or
through a transmit() method call (PC/SC SCardTransmit method) using a APDU
wrapping mecanism.


.. index::
   EscapeCommandEnable
   SCardControl


ScardControl
------------

SCardControl passing method advantages are:

- Commands be passed using a direct connection to reader avoiding the need
  for a card to be present on reader. Changing reader parameters, loading
  cryptographic keys in reader, etc.. can be performed without asking user to
  place a card on reader.

- Commands can also be passed if a shared connection has been established.


SCardControl passing method drawbacks are :

- This passing method is considered unsecured and both Windows and Linux
  CCID driver forbid the use of this method by default.
- Under Windows, a special registry value named "EscapeCommandEnable"
  must be added for to allow the driver to forward commands to reader
  but this requires administrative rights to modify registry.
- Under Linux, a bit must be set inside a driver configuration file
  requiring root login.

ScardTransmit
-------------

SCardTransmit passing method advantages are :

- This passing method is considered secured and requires only basic user
  rights on both Windows and Linux.

SCardTransmit passing method drawbacks are :

- Commands will be denied if a direct connection to reader has been
  established. Only shared connection are allowed and thus requires asking
  user to place a card on reader even when commands only involve the reader
  and not the card like changing a communication parameter.

Proposition
-----------

**Command passing may be set to AUTOMATIC, CONTROL or TRANSMIT**

When set to TRANSMIT, a successful connect() or connect(false) method call
should have been performed to establish a shared connection to a card. As a
consequence, a card must be physically present on the reader. Specific
reader commands will be passed to the reader using an APDU wrapping mecanism
through a transmit() method call (PC/SC SCardTransmit method). When defined
by PC/SC 2.01, commands will be passed using PC/SC defined APDU format
through a transmit() method call (PC/SC SCardTransmit method).

When set to CONTROL, a successful connectDirect() or connect(true) method
call should have been performed to get a direct connection to the reader.
Specific reader commands will be passed to reader using proprietary format
through a control() method call (PC/SC SCardControl method). It is not
possible to pass commands in PC/SC 2.01 APDU format when direct connection
is established.

When set to AUTOMATIC, appropriate command passing method will be choosen
depending of the current connection type ; direct or shared. If currently
established connection is direct, proprietary commands will be passed
through a control() method call (PC/SC SCardControl method). Commands only
defined by PC/SC 2.01 will fail. If currently established connection is
shared, proprietary commands will be passed through a transmit() method call
(PC/SC SCardTransmit method) using a APDU wrapping mecanism and commands
defined by PC/SC 2.01 will be passed through a transmit() method call (PC/SC
SCardTransmit method)

Passing method defaults to AUTOMATIC.

Please note that when a card is present on the reader, it is also possible
to use a connect() or a connect(false) method call and to use the CONTROL
command passing method. Specicific reader commands will be passed through a
control() method call (PC/SC SCardControl method) and PC/SC 2.01 commands
will be passed through a transmit() method call (PC/SC SCardTransmit method)

Pour avis,
Philippe.




