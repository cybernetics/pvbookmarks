

.. _beautiful_native_libraries:

===============================
Beautiful Native Libraries
===============================


.. seealso::

   - http://lucumr.pocoo.org/2013/8/18/beautiful-native-libraries/


Introduction
============

I'm obsessed with nice APIs. 

Not just APIs however, also in making the overall experience of using a library 
as good as possible. 

For Python there are quite a few best practices around by now but it feels like 
there is not really a lot of information available about how to properly structure 
a native library. 

What do I mean by native library? Essentially a dylib/DLL/so.

Since I'm currently spending more time on C and C++ than Python at work I figured 
I might take the opportunity and collect my thoughts on how to write proper 
shared libraries that do not annoy your users.

