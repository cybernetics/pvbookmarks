

.. index::
   pair: github; example


.. _github_example:

================
github example
================


.. seealso:: https://github.com/pvergain/devtools


Global setup
============

Set up git
----------


::

    git config --global user.name "Patrick Vergain"
    git config --global user.email pvergain@gmail.com


Next steps
----------

::


    mkdir devtools
    cd devtools
    git init
    touch README
    git add README
    git commit -m 'first commit'
    git remote add origin git@github.com:pvergain/devtools.git
    git push -u origin master


Existing Git Repo ?
-------------------

::

    cd existing_git_repo
    git remote add origin git@github.com:pvergain/devtools.git
    git push -u origin master




