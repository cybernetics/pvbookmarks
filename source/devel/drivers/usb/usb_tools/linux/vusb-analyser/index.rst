

.. index::
   pair: USB tool ; vusb-analyzer


.. _vusb_analyser:

=============
vusb-analyzer
=============

.. seealso::

    - http://vusb-analyzer.sourceforge.net
    - http://vusb-analyzer.svn.sourceforge.net/viewvc/vusb-analyzer/


.. figure:: vusb-analyzer-logo-96.png
   :align: center


.. contents::
   :depth: 3


vusb-analyzer announce
======================


- http://kerneltrap.org/index.php?q=mailarchive/linux-usb/2009/1/13/4711504

::

    Subject: Open source USB sniffer GUI
    Date: Tuesday, January 13, 2009 - 10:54 am
    Hi,
    I apologize in advance if this isn't the right place for such an
    announcement, but I thought this might be of interest to the Linux USB
    driver community.
    I'd like to announce a new open source GUI tool for visualizing USB
    sniffer logs. It's written in Python with PyGTK, and it has some novel
    features including a graphical timeline view.
    We built this tool at VMware for analyzing sniffer logs produced by
    our USB virtualization stack. There are instructions on the web site
    for capturing sniffer logs using VMware products (including the
    free-as-in-beer VMware Player).
    This is pretty useful, since you capture logs from a device's
    Windows driver, then capture logs from your own Linux driver and
    compare the two side-by-side.
    But if VMware isn't your cup of tea, there's also an architecture in
    place for pluggable log file decoder modules. We already have support
    for decoding the logs produced by Ellisys hardware analyzers, and we'd
    love to see someone add support for usbmon.
    If you're interested, the project web site has source code,
    documentation, and plenty of screenshots:
    http://vusb-analyzer.sourceforge.net/


This is a GUI tool for analyzing logs of traced USB
communications.


dependencies
============

- python 2.6 (not python 2.7)
- :ref:`gtk+ <gtk+>`
- pyGTK


Versions
========

vusb-analyser 1.1
-----------------

Version 1.1 Includes support for Linux usbmon logs. (beta)
This code was contribued by Christoph Zimmermann. The usbmon
support hasn't been tested as extensively as the other formats,
and it doesn't support all vusb-analyzer features, but other
than that it should be quite usable and stable.


.. _python_vusb_analyser:

python vusb-analyser
====================

See :ref:`the documentation about usbmon <usbmon>`.


::

    drwxr-xr-x 3 5724 201 4096 aoû 23 14:31 VUsbTools
    [root@houx vusb-analyzer-1.1]# python vusb-analyzer

    usage: vusb-analyzer [-t] vmx.log [vmx.log]

    PyGTK frontend for the virtual USB analyzer
    Micah Dowty <micah@vmware.com>
    Version 1.1

      -t  Tail mode, start from the end of a growing log file.

    Supported log formats:
       VMware VMX log file (*.log)
       Exported XML from Ellisys Visual USB (*.xml)
       Linux usbmon log, raw ASCII format (*.mon)

    Also supports transparent decompression of gzipped
    (*.gz) files. Logs may be appended to while this
    program is running.

    For best results with Ellisys logs, enable 'Expand
    transactions packets' but not 'Expand consecutive
    elements' while exporting.

    Two log files can be specified, in order to invoke
    diff mode.

usbmon
------

See :ref:`the documentation about usbmon <usbmon>`.

Compilation
===========


.. toctree::
   :maxdepth: 3

   dependencies
   compil_examples


