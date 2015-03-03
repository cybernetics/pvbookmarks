
.. index::
   Python c (nb_inline)

.. _python_nb_module_modules:

=========================== 
python nb_inline module
===========================

.. seealso:: http://pages.cs.wisc.edu/~johnl/np_inline/doc-0.3.html

Overview
=========

The np_inline module was written as a simplified replacement for 
scipy.weave.inline for numeric computations on numpy arrays. 
The module is implemented in a single file containing less than 500 lines 
of code, including the C-file template, docstrings, comments and white space.

One advantage np_inline has over weave.inline is that it works properly in a 
multiprocessing environment because it uses a multiprocessing.Lock object to 
protect the module production code. 

  
