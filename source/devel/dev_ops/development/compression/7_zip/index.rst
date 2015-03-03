
.. index::
   pair: Compression ; 7-zip


.. _7_zip:

=======================
7-zip
=======================


.. seealso:: http://www.7-zip.org/

.. figure:: 7ziplogo.png
   :align: center
   
   
.. contents::
   :depth: 3
   
      
Licence
=============

7-Zip is open source software. Most of the source code is under the 
GNU LGPL license. 

The unRAR code is under a mixed license: GNU LGPL + unRAR restrictions. 

Check license information here: 7-Zip license.

You can use 7-Zip on any computer, including a computer in a commercial
organization. You don't need to register or pay for 7-Zip.      

The main features of 7-Zip
===========================

High compression ratio in 7z format with LZMA and LZMA2 compression

Supported formats:

- Packing / unpacking: 7z, XZ, BZIP2, GZIP, TAR, ZIP and WIM
  Unpacking only: ARJ, CAB, CHM, CPIO, CramFS, DEB, DMG, FAT, HFS, ISO, 
  LZH, LZMA, MBR, MSI, NSIS, NTFS, RAR, RPM, SquashFS, UDF, VHD, WIM, 
  XAR and Z.

For ZIP and GZIP formats, 7-Zip provides a compression ratio that is 2-10 % 
better than the ratio provided by PKZip and WinZip

- Strong AES-256 encryption in 7z and ZIP formats
- Self-extracting capability for 7z format
- Integration with Windows Shell
- Powerful File Manager
- Powerful command line version
- Plugin for FAR Manager
- Localizations for 79 languages


FAQ
===

.. seealso:: http://www.7-zip.org/faq.html


Why doesn't -r switch work as expected ?
-----------------------------------------

In most cases you don't need -r switch. 7-Zip can compress subfolders 
even without -r switch.

Example 1::

    7z.exe a c:\a.7z "C:\Program Files"
    7z.exe a c:\a.7z "C:\Tmp"

compresses "C:\Program Files" completely, including all subfolders.


Example 2::

    7z.exe a -r c:\a.7z "C:\Program Files"

searches and compresses "Program Files" in all subfolders of C:\ 
(for example, in "C:\WINDOWS").

If you need to compress only files with some extension, you can use -r 
switch::

    7z a -r c:\a.zip c:\dir\*.txt 

compresses all .txt files from folder c:\dir\ and all it's subfolders.


Usage examples
==============

Dotnetperls
------------

.. seealso::

   - http://www.dotnetperls.com/7-zip-examples
  
  
Framasoft
----------


.. seealso::

   - http://www.framasoft.net/article1902.html
   
flocked.net
-----------
    
.. seealso::

   - http://www.flocked.net/topic/computing/item/475-useful-7-zip-batch-examples-in-windows      
   
   
   
   


