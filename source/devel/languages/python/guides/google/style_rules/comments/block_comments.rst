
.. index::
   pair: python; Inline Comments


.. _python_inline_comments:

=========================
Block and Inline Comments
=========================

The final place to have comments is in tricky parts of the code.

If you're going to have to explain it at the next code review, you should
comment it now.

Complicated operations get a few lines of comments before the operations
commence. Non-obvious ones get comments at the end of the line.

::

    # We use a weighted dictionary search to find out where i is in
    # the array.  We extrapolate position based on the largest num
    # in the array and the array size and then do binary search to
    # get the exact number.

    if i & (i-1) == 0:        # true iff i is a power of 2

To improve legibility, these comments should be at least 2 spaces away from
the code.

On the other hand, never describe the code. Assume the person reading the code
knows Python (though not what you're trying to do) better than you do.

::

    # BAD COMMENT: Now go through the b array and make sure whenever i occurs
    # the next element is i+1
