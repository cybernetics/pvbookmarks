
.. index::
   pair: Compiler ; ocl


.. _python_ocl:

=======================================
Ocl (Python to C99/OpenCL/JS compiler )
=======================================

.. seealso::

   - https://github.com/mdipierro/ocl


ocl is a minimalist library that dynamically (at run time) converts decorated 
Python functions into C99, OpenCL, or JavaScript. 

In the C99 case, it also uses distutils to compile the functions to machine 
language and allow you to run the compiled ones instead of the interpreted ones. 

In the OpenCL case you can run the compiled ones using pyOpenCL.

It consists of a single pure-Python file containing about 600 lines of code. 

Some of the ocl functionalities overlap with Cython, CLyter, and Pyjamas.

It is based on the Python ast module, and the these fantastic libraries:

- http://pypi.python.org/pypi/meta (always required)
- http://pypi.python.org/pypi/pyopencl (required only to run opencl code)







