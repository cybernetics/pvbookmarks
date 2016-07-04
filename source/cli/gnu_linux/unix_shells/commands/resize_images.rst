
.. index::
   pair: Resize; Images


.. _resizing_image_sizes:

====================
Resizing image files
====================

.. seealso:: http://www.commandlinefu.com/commands/tagged/1066/resize

mogrify command
===============

.. seealso:: :ref:`imagemagick_tools`

Resize all JPEGs in a directory

This command requires the :ref:`imagemagick libraries <imagemagick_image_library>`  and will 
resize all files with the .JPG extension to a width of 800 pixels and will 
keep the same proportions as the original image.

::

    mogrify -resize 800 *.JPG
  
  
    

google picasa use case
======================

::

    cp *.JPG web
    cd web
    mogrify -resize 800 *.JPG
    date; google picasa -d "2011-10-27" -n "Minou et Ali à Annecy le 27 octobre 2011" -t "Annecy, 27 octobre 2011" create "Annecy, 27 octobre 2011" *.JPG; date


        
    
    
    













