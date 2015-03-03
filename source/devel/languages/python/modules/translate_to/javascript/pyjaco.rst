
.. index::
   pair: Javascript; Pyjaco
   pair: Python; Pyjaco
   
.. _pyjaco:

====================================
Pyjaco
====================================

.. seealso::

   - http://pyjaco.org/about
   - http://pyjaco.org/download
   - :ref:`pre_compilers_javascript`

.. contents::
   :depth: 3

About the project
==================

Pyjaco is a Python-to-Javascript compiler. It enables compilation of standard
Python code into a javascript equivalent.

This javascript code can then be run in a browser, or anywhere else that
javascript is used.

Why not just write javascript ?
================================

Using Python through Pyjaco, rather than writing javascript directly, has
several advantages:

You don't have to learn a new language
    The semantic differences between Python and Javascript are huge.
    To name a few differences, javascript has no real classes, support prototypical
    rather than classical inheritance, does not support any hooks like __getattr__
    and the like, and considers an empty list to be True, rather than False.

    Using pyjaco, you only need to know the Python semantics, which you
    already do! Pyjaco translates your python code into javascript code that
    performs the same operations. And the classes are mapped too, even for numbers,
    strings and lists.


Spend less time debugging

    Javascript, JScript or ECMAScript? Version 1.5 or 1.8? Or something else
    entirely ?
    
    Using javascript can be quite complicated in itself, and it is not helped
    by the fact that each browser supports different features.

    Because pyjaco relies only on a minimal subset of javascript, it can be
    guaranteed to run on each major web platform. The extensive test suite has
    nearly-full code coverage, and has achieved a success rate of 100% on Chrome,
    Firefox and Opera. We are still working on Internet Explorer, since it is
    broken in so many ways. When Internet Explorer support is finished, we
    have done the hard work so you do not have to.


Be more productive

    Let's face it, there is a reason people love Python. It is immensily powerful,
    and has an excellent standard library. Javascript lacks almost all the
    features people love in Python, and has a much less comprehensive standard
    library. With pyjaco, you don't have to worry about that.

    Just write your code using Python and the Python standard library, and
    let pyjaco do the hard work for you.


