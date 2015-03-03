


.. index::
   pair: Images ; Exiftool
   pair: Images ; Time


.. _exiftool:

====================
Exiftool
====================

.. seealso:: 

   - https://launchpad.net/~faster3ck/+archive/converseen


.. contents::
   :depth: 3
   

Short Tip: Changing the original time of a photo at cli level
=============================================================

.. seealso::

   - http://liquidat.wordpress.com/2013/02/21/short-tip-changing-the-original-time-of-a-photo-at-cli-level/
   
   
Sometimes it happens that you take photos with a camera, and realize 
right in the middle of your session that the time of the camera is 
totally offset. 

In such cases: just keep taking photos and make sure that you take a 
photo of a clock at some point.

Afterwards, download the images, check the actual time offset by 
comparing the photographed clock and the time and date given in that 
image, and use exiftool to correct the time stamps of the photo. 

For example, imagine you have to change teh time by adding two hours 
and fifteen minutes::


    $ exiftool -AllDates-='2:15' *.JPG
    
    
You can check the actual date of the image either by the usual GUI 
programs or on command line::

$ exiftool MyImage.jpg|grep Time

::

    File Modification Date/Time     : 2011:11:03 13:00:39+01:00
    Exposure Time                   : 1/100
    Date/Time Original              : 2009:09:05 07:07:49
   
