





==================================
pcsc-tools 1.4.18 18 December 2011
==================================


Hello,

I just released a new version of `pcsc-tools`_. No new feature but
some enhancements.

If you do not know what pcsc-tools is, it contains 4 tools:

- pcsc_scan(1) regularly scans every PC/SC reader connected to the
  host if a card is inserted or removed a "line" is printed.
- ATR_analysis(1) is a Perl script used to parse the smart card ATR.
  This script is called (by default) by pcsc_scan.
- scriptor(1) is a Perl script to send commands to a smart card using
  a batch file or stdin.
- gscriptor(1) the same idea as scriptor.pl(1) but with a Perl-Gtk2 GUI.

An equivalent of ATR_analysis is available online at
http://smartcard-atr.appspot.com/

Changes
=======

1.4.18 - 18 December 2011, Ludovic ROUSSEAU

- gscriptor: Display hex dumps in lines of 16 bytes instead of 17
- gscriptor: Display bytes of value 0x20 as ' ' instead of '.'
- scriptor: Display lines of 16 bytes instead of 24
- 223 new ATRs
- pcsc_scan: Correctly detect reader Plug and Play support


.. _`pcsc-tools`: http://ludovic.rousseau.free.fr/softwares/pcsc-tools/index.html
