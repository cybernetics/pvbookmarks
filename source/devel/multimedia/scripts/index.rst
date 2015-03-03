

.. index::
   pair: Script; Conversion
   pair: Script; Rename
   ! Scripts


.. scripts:

=================
Scripts 
=================

.. contents::
   :depth: 4


Renommage de fichiers
=====================


Pour convertir les espaces des noms de fichiers en caractère *souligné*
------------------------------------------------------------------------

::

    for f in *.mp3; do mv "$f" `echo $f | tr ' ' '_'; done
    

Pour renommer de façon incrémentale
-----------------------------------

Pour renommer de façon incrémentale une série de photos nommées 
"dscnXXX.jpg".

::

   convert dscn*.jpg  'barcelone2014-%d.jpg` 
   


Conversion de sons
==================

::

    for f in *.mp3; do lame --decode $f `basename $f .mp3`.wav; done
    

::

    for f in *.mp3; do mpg123 -w $f `basename $f .mp3`.wav; done
    
           

       
   
   
   



