




.. _csharp_indexer:

================
c♯ Indexer
================

.. seealso::

   - http://www.dotnetperls.com/indexer


Tuple
=======

::

    using System;

    class Layout
    {
        string[] _values = new string[100]; // Backing store

        public string this[int number]
        {
            get
            {
                // This is invoked when accessing Layout instances with the [ ].
                if (number >= 0 && number < _values.Length)
                {
                // Bounds were in range, so return the stored value.
                return _values[number];
                }
                // Return an error string.
                return "Error";
            }
            set
            {
                // This is invoked when assigning to Layout instances with the [ ].
                if (number >= 0 && number < _values.Length)
                {
                // Assign to this element slot in the internal array.
                _values[number] = value;
                }
            }
        }
    }




