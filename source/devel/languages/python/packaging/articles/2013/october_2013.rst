

.. index::
   pair: Articles ; Packaging (2013 october)


.. _python_packaging_articles_october_2013:

=======================================
Python packaging articles october 2013
=======================================



.. seealso::

   - https://lwn.net/Articles/570471/
   
   


The Python language comes with a long list of nice features, in keeping with the 
language's "batteries included" mantra. 

One battery that is noticeably absent, though, is a comprehensive mechanism for 
the building, distribution, and installation of Python packages. 

That leaves packagers and users having to choose between a variety of third-party 
tools or just giving up and solving the whole problem themselves. 

The good news is that Python 3.4 is likely to solve this problem, but Python 2 
users may still have to go battery shopping on their own.

Python packaging has long been recognized as a problem for users of the language. 

There is an extensive collection of add-on modules in the Python Package Index 
(PyPI), but there is no standard way for a user to obtain one of those modules 
(and, crucially, any other modules it depends on) and install it on their system. 

The distutils package — the engine behind the nearly omnipresent setup.py files 
found in modules — can handle some of the mechanics of installation, but it is 
showing its age and lacks features. 

Distutils2 is a fork of distutils intended to solve many of the problems there, 
but this project appears to have run out of steam. 

Setuptools is a newer approach found on many systems, but it has a long list of 
problems of its own. 

Distribute is "a deprecated fork" of Setuptools. And so on; one does not need 
to look for long to see that the situation is messy — and that's without looking 
at the variety of package formats ("egg," "wheel," etc.) out there.

For a while, the plan was to complete work on distutils2 and merge the result 
into the Python 3.3 release. 
But, in June 2012, that effort collapsed when it became clear that the work 
would not be anywhere near complete in time. The results were a 3.3 release 
without an improved packaging story, an epic email thread on the nature of the 
problem and what should be done about it, and a virtual halt to distutils2 work. 



