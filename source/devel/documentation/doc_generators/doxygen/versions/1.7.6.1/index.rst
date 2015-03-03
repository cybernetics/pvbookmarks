
.. index::
   pair:  doxygen; 1.7.6.1



=======================
Doxygen 1.7.6.1
=======================


.. seealso:: http://www.stack.nl/~dimitri/doxygen/changelog.html


Changes
=======

Doxygen now reports its cache usage (for the symbol and the lookup cache) at the
end of a run (if QUIET=NO), and recommends settings for SYMBOL_CACHE_SIZE and
LOOKUP_CACHE_SIZE for your project if either cache is too small.

New features
============

Added new option LOOKUP_CACHE_SIZE to control the internal cache doxygen uses to
find symbols given their name and a context.

- Python: added support for @staticmethod
