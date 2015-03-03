
.. index::
   Python c (weave)

.. _python_weave_module:

=========================== 
python weave module
===========================

.. seealso:: 

   - http://www.scipy.org/Weave

Overview
========

The weave package allows the inclusion of C/C++ within Python code and is 
useful in accelerating Python code.

Weave is a subpackage of scipy. (I.e. you have it already if you installed SciPy)
Alternatively, you can check-out and install weave separately using 

::

	svn co http://svn.scipy.org/svn/scipy/trunk/scipy/weave weave
	cd weave
	sudo python setup.py install

- Current documentation (which is still being updated to reflect the move to 
  NumPy) can be seen here_ .
- PerformancePython_: A comparison of various ways to improve the performance 
  of Python code using Numeric, weave, Pyrex, Psyco and Fortran (f2py) for 
  solving Laplace's equation. These are compared with code written in C++.

.. _here: http://projects.scipy.org/scipy/scipy/browser/trunk/scipy/weave/doc/tutorial.txt?format=raw
.. _PerformancePython: http://www.scipy.org/PerformancePython
  
