

.. index::
   pair: Windows ; Debugging
   pair: Windows 8; Debugging


.. _windows_debugging:

=================================================================
Windows Debugging
=================================================================

.. seealso:: 

   - http://msdn.microsoft.com/en-us/library/windows/hardware/ff551063%28v=VS.85%29.aspx



.. contents::
   :depth: 3


Introduction
=============


**Debugging Tools for Windows is a collection of debuggers and related 
tools**. 

.. note:: Starting with Windows 8, the driver development environment and the 
   Windows debuggers are integrated into Microsoft Visual Studio. 

To set up the integrated environment, install Visual Studio and then 
install Windows Driver Kit (WDK) 8. 

Debugging Tools for Windows is included in WDK 8. 
You can find more information about how to get the 
integrated environment `here 1 <http://go.microsoft.com/fwlink/p?LinkID=239721>`_.

If you do not need the Windows Driver Kit (WDK), you can get Debugging 
Tools for Windows as part of the Microsoft Windows Software Development 
Kit (SDK) for Windows 8. 

You can find more information about how to get the Windows SDK `here 2 <http://msdn.microsoft.com/en-US/windows/hardware/hh852363>`_.

If you want to download only Debugging Tools for Windows, install the 
Windows SDK; during the installation, check the Debugging Tools box, and 
uncheck all the other boxes.


Download
=========


Windows SDK Download
---------------------

.. seealso:: http://msdn.microsoft.com/en-US/windows/hardware/hh852363


Installation Directory
=======================

These are the default installation directories for Debugging Tools for 
Windows::

    c:\Program Files (x86)\Windows Kits\8.0\Debuggers\x64
    c:\Program Files (x86)\Windows Kits\8.0\Debuggers\x86


Debugging environments
=======================

After you install Visual Studio and the WDK, you have six available 
debugging environments:

- Visual Studio with integrated Windows debuggers
- Microsoft Windows Debugger (WinDbg)
- Microsoft Kernel Debugger (KD)
- NTKD
- :ref:`Microsoft Console Debugger (CDB) <cdb>`
- Microsoft NT Symbolic Debugger (NTSD)

All of these debugging environments provide user interfaces for the same 
underlying debugging engine, which is implemented in dbgeng.dll. 
This debugging engine is called the Windows debugger, and the six 
debugging environments are collectively called the Windows debuggers. 

For detailed descriptions of the different environments, see 
`Debugging Environments <http://msdn.microsoft.com/en-us/library/windows/hardware/hh406268(v=vs.85).aspx>`_ 

Note  
-----

Visual Studio includes its own debugging environment and debugging engine, 
which together are called the Visual Studio debugger. 

**The Visual Studio debugger is completely different from Windows debugger**. 

In Visual Studio, you can debug user-mode code by using either the 
Windows debugger or the Visual Studio debugger. You cannot use the Visual 
Studio debugger to debug kernel-mode code. 

To debug kernel-mode code, you must use the Windows debugger integrated 
with Visual Studio, WinDbg, KD, or NTKD.

The Windows debuggers can run on x86-based or x64-based processors, and 
they can debug code that is running on x86-based or x64-based processors. 

Sometimes the debugger and the code being debugged run on the same computer, 
but other times the debugger and the code being debugged run on separate 
computers. In either case, the computer that is running the debugger is 
called the host computer, and the computer that is being debugged is 
called the target computer. 

New for Windows 8
==================

.. seealso::

   - http://msdn.microsoft.com/en-us/library/windows/hardware/ff551063%28v=VS.85%29.aspx
   
   
For Windows 8, we have integrated the Windows debuggers into Visual Studio. 

We have also integrated the driver development and build environment into 
Visual Studio. 

**So now you can develop, build, and debug both kernel-mode 
and user-mode components all from Visual Studio**. 

We have added support for debugging over a network connection or a 
USB 3.0 connection, and we have improved support for debugging optimized 
code and inline functions.  


Windows Debugging environments
===============================

.. toctree::
   :maxdepth: 3
   
   environments/index
   
   





