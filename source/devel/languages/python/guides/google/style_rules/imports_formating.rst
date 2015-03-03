
.. index::
   pair: python; Imports formatting


.. _python_imports_formatting:

==================
Imports formatting
==================

Imports should be on separate lines.

E.g.:

Yes::

    import os
    import sys

No::

    import os, sys

Imports are always put at the top of the file, just after any module comments
and doc strings and before module globals and constants.

Imports should be grouped with the order being most generic to least generic:

- standard library imports
- third-party imports
- application-specific imports

Within each grouping, imports should be sorted lexicographically, ignoring case,
according to each module's full package path.

::

    import foo
    from foo import bar
    from foo.bar import baz
    from foo.bar import Quux
    from Foob import ar
