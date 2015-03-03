

.. index::
   pair: freeimage ; 3.15.2


.. _freeimage_3.15.2:

====================
Freeimage 3.15.2
====================



::

    February 20th, 2012 - 3.15.2
    ! FreeImage now uses LibRaw 0.14.5
    ! FreeImage now uses LibPNG 1.5.8
    ! FreeImage now uses LibJPEG 8d
    ! FreeImage now uses ZLib 1.2.6
    ! FreeImage now uses OpenJPEG 1.5.0 (released version)
    ! FreeImage now uses LibTIFF 4.0.0
    - [Herve Drolon] removed dependency on LibMNG 1.0.10 (MNG and JNG files are
       now handled internally)
    + [Herve Drolon] replaced the MNG plugin with a new MNG internal FreeImage plugin (with read support)
    + [Herve Drolon] added a new JNG internal FreeImage plugin (with read/write support)
    + [Christian Heimes] added write support to the TIFF plugin for EXIF_MAIN tags
    + [Herve Drolon] added new Exif maker note tags
    + [Herve Drolon] added TAG_COMPRESSION conversion to FreeImage_TagToString
    * [Mylek Grey] enabled the use of multi-component transforms (MCT) in J2K and JP2 saving
    * [Herve Drolon] refactored PluginICO in order to correctly support Windows Vista 256x256 icons
    * [Herve Drolon] added minor speed improvements to FreeImage_Rescale
    * [Herve Drolon] fixed dib allocation failing with very large images (i.e. more than 4GB)
    * [Herve Drolon] fixed FreeImage_CloneTag behavior with ASCII data handling
    * [Herve Drolon] improved JPEG plugin behavior with very big images
    * [Herve Drolon] improved JPEG plugin behavior with C++ exceptions
    * [Herve Drolon] fixed loading of palettized PNG with more that 256 palette entries
    * [Herve Drolon] fixed a bug inside IFF plugin occuring when loading a 24-bit
      dib with a palette
    * [Herve Drolon] fixed a bug with loading of PNG images containing a cHRM
      chunk (regression introduced by LibPNG 1.5.4 and fixed by LibPNG 1.5.5)
    * [Herve Drolon] allowed loading of PNG with benign errors (such as images
      with too many IDATs)
    * [Mihail Naydenov] fixed some incorrect MIME types returned by FreeImage_GetFIFMimeType
    * [Herve Drolon] fixed loading of Exif with bad thumbnail data or with a bad
      first offset size


