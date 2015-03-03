

.. index::
   pair: Boost ; thread C++ library


.. _boost_thread_cplusplus_library:

============================
Boost thread C++ library
============================

.. seealso::

   - http://www.boost.org/doc/libs/1_47_0/doc/html/thread.html


Boost.Thread enables the use of multiple threads of execution with shared data
in portable C++ code. It provides classes and functions for managing the threads
themselves, along with others for synchronizing data between the threads or
providing separate copies of data specific to individual threads.

The Boost.Thread library was originally written and designed by William E. Kempf.

This version is a major rewrite designed to closely follow the proposals
presented to the C++ Standards Committee, in particular N2497, N2320, N2184,
N2139, and N2094

In order to use the classes and functions described here, you can either
include the specific headers specified by the descriptions of each class or
function, or include the master thread library header::

    #include <boost/thread.hpp>

which includes all the other headers in turn.
