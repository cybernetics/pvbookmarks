
.. index::
   pair: Dash ; Doxygen

.. _doxygen_dash_docset:

=======================
Doxygen dash docset
=======================


.. seealso::

   - :ref:`dash`
   - http://kapeli.com/docsets#doxygen



Description
===========

Doxygen can generate docsets from source files of C, C++, C#, PHP, Objective-C, 
Java, Python (and some others).

These are the entries you need to add into your Doxygen config file to make it 
generate a docset (note: the last 3 entries are optional)::

    GENERATE_DOCSET   = YES
    DISABLE_INDEX     = YES 
    SEARCHENGINE      = NO
    GENERATE_TREEVIEW = NO

When Doxygen is done generating the documentation, run make inside the generated 
folder. 

Afterwards, scroll down to the bottom of this page where you'll find some tips 
on how to improve your docset. 
