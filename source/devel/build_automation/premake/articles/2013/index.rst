


.. _premake_2013:

=========================
Articles on premake 2013
=========================

.. contents::
   :depth: 3
   

Beautiful Native Libraries written on Sunday, August 18, 2013 
=============================================================


.. seealso::

   - http://lucumr.pocoo.org/2013/8/18/beautiful-native-libraries/


I used to be a huge fan of cmake but I now switched to premake. 

The reason for this is that cmake has some stuff hardcoded which I need to 
customize (for instance building a Visual Studio solution for Xbox 360 is 
something you cannot do with stock cmake). 

Premake has many of the same problems as cmake but it's written almost entirely 
in lua and can be easily customized. 

Premake is essentially one executable that includes a lua interpreter and a 
bunch of lua scripts. 
It's easy to recompile and if you don't want to, your premake file can override 
everything if you just know how.

