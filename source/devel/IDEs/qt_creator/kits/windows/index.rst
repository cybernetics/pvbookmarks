
.. index::
   pair: Windows; Debugging


.. _qtcreator_windows_kits:

========================
Qt Creator Windows Kits
========================

.. seealso::

   - http://qt-project.org/wiki/Qt_Creator_Windows_Debugging


Installation prerequisites
===========================

Qt Creator uses the cdb.exe command line debugger provided with the 
Debugging Tools for Windows package as part of the Windows SDK.

As of Microsoft Visual Studio 2012, the Windows Kit 8 is installed along 
with Visual Studio. 

.. warning:: Make sure you check the Debugging Tools for Windows component 
   in the installer. 
   

The debuggers are typically located in ``c:\Program Files (x86)\Windows Kits\8.0\Debugger`` .

You need to set up the debugger only if the automatic setup fails, because 
the native debugger is missing (**as is usually the case for the CDB debugger 
on Windows, which you always must install yourself**) or because the 
installed version is not supported (e.g. when your system contains no, 
or an outdated version of GDB and you want to use a locally installed 
replacement instead).

.. note:: If you need to change parameters of an automatically detected 
   toolchain, you can Clone the tool chain and change the parameters in 
   the clone. Make sure to select the cloned tool chain in the build 
   settings of your project.


Debugging tools for Windows	Using this engine requires you to install the 
Debugging tools for Windows:

- http://www.microsoft.com/whdc/devtools/debugging/installx86.Mspx 
- http://www.microsoft.com/whdc/devtools/debugging/install64bit.Mspx package 
  (Version 6.12 for the 32-bit or the 64-bit version of Qt Creator, respectively), 
  which are freely available for download from the Microsoft Developer Network.

The Qt Creator help browser does not allow you to download files, and 
therefore, you must copy the above links to a browser.

.. note:: Visual Studio does not include the Debugging tools needed, and 
   therefore, you must install them separately.



MSVC64
======


.. toctree::
   :maxdepth: 3
   
   msvc64/index
   
   
