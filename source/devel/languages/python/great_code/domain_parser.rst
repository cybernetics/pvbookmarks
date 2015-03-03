

.. index::
   ! Domain parser


.. _domain_parser:

=================================
``domain_parser`` 
=================================

.. seealso::

   - https://github.com/jeffknupp/domain-parser/tree/master/docs
   - http://www.jeffknupp.com/blog/2014/04/03/dont-write-python-scripts-write-python-libraries/


.. contents::
   :depth: 3   


Introduction
=============


When someone asks why the if __name__ == '__main__' idiom should be used, 
I say it's because it makes turning your "script" into a "library" a seamless 
thing. Novices often write a series of one-off Python scripts that exist only 
as long as it takes to finish and run them. More seasoned developers have 
accumulated a set of libraries they've written over the years.

