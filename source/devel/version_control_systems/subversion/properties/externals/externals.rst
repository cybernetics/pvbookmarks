

.. index::
   pair: Subversion; externals
   pair: Subversion; propset
   pair: Subversion; propget   

.. _svn_externals:

========================
svn externals
========================

.. seealso::

   - http://svnbook.red-bean.com/nightly/en/svn.advanced.externals.html


.. contents::
   :depth: 3

svn propget svn:externals
==========================

::

	$ svn propget svn:externals .


::
    
	^/../P3N161/Concept/Common common
	^/../P3N161/Concept/LIB_2P147_id3Image/2.0.0/Livraison native/id3Image
	^/../P3N161/Concept/LIB_9X164_FFT/Livraison native/fftw
	^/../P3N161/Concept/LIB_3U142_id3.Controls/1.0/Livraison dotNET/id3.Controls
	../../LIB_9Z119_id3FingerBase/2.4     native/id3FingerBase
	../../LIB_9Y440_id3FingerEnroll/2.2   native/id3FingerEnroll
	../../LIB_9X168_id3FingerFIR/1.4      native/id3FingerImageRecord
	../../LIB_9X167_id3FingerMatch/2.4    native/id3FingerMatch
	../../LIB_9X171_id3FingerImage/1.3    native/id3FingerImage
	../../LIB_9X170_id3FingerTemplate/1.5 native/id3FingerTemplate
	../../LIB_9Z231_id3FingerScan/1.4     native/id3FingerCapture
	../../LIB_9X165_id3FingerExtract/3.0  native/id3FingerExtract
	../../LIB_9X166_id3FingerFMR/1.4      native/id3FingerTemplateRecord
	../../LIB_1N106_id3FingerNFIQ/1.2     native/id3FingerNFIQ
	../../LIB_1S056_id3FingerLicense/2.6  native/id3FingerLicense
	../../LIB_1W036_id3FingerSlapSeg/2.1  native/id3FingerSlapSeg
	../../LIB_2W008_id3FingerWSQ/1.2      native/id3FingerWSQ
	../../LIB_3R110_id3FingerBSP/1.0      native/id3FingerBSP



svn propset svn:externals
==========================


::

    svn propset svn:externals  . -F externals.txt
    svn up
    
    








