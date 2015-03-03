
.. index::
   pair: python; TODO Comments


.. _python_todo comments:

=============
TODO Comments
=============

Use TODO comments for code that is temporary, a short-term solution, or
good-enough but not perfect.

TODOs should include the string TODO in all caps, followed by the name,
e-mail address, or other identifier of the person who can best provide context
about the problem referenced by the TODO, in parentheses.

A colon is optional. A comment explaining what there is to do is required.

The main purpose is to have a consistent TODO format that can be searched to
find the person who can provide more details upon request.

A TODO is not a commitment that the person referenced will fix the problem.
Thus when you create a TODO, it is almost always your name that is given.

::

    # TODO(kl@gmail.com): Use a "*" here for string repetition.
    # TODO(Zeke) Change this to use relations.

If your TODO is of the form "At a future date do something" make sure that
you either include a very specific date ("Fix by November 2009") or a very
specific event ("Remove this code when all clients can handle XML responses.").
