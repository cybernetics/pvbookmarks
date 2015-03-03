
.. index::
   pair: git ; tips
   pair: git tips ; gitk
   pair: git ; log

.. _git_tips:

========
git tips
========


Greg Kroah-Hartman
==================

Best +Git tip I learned in a long time::


::

    gitk ORIG_HEAD..


after pulling a branch from someone.


You can also do::

    git shortlog ORIG_HEAD..


or::

    git diff --stat --summary ORIG_HEAD..


as well.


And if things went wrong::

    git reset --hard ORIG_HEAD


to revert the pull (although I thought there was some other way to do that, but
can't remember it at the moment.)

Many thanks to +David Miller for that one, it's already proving to be indispensable.



Tree of your branch merges. very useful if you want to follow the features you add
==================================================================================

::

    git log --graph --oneline --all





