

.. index::
   pair: Unicode ; Python
   pair: Encoding; cp1252
   pair: Encoding; "C" locale


.. _unicode_python:

==============
Unicode python
==============


.. seealso::

   - http://pylonsbook.com/en/1.1/unicode.html?highlight=unicode
   - http://pylonsbook.com/en/1.1/internationalization-and-localization.html
   - http://www.haypocalc.com/wiki/Python_Unicode
   - http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html
   - http://nedbatchelder.com/text/unipain.html



.. contents::
   :depth: 3


Introduction
============

This choice is a big portability issue. Mac OS X, most Linux distro, BSD systems
use UTF-8 local encoding, whereas Windows use legacy code pages like cp1252
(something like ISO-8859-1) or cp952 (shift jis).

But sometimes, the locale is "C" (e.g. on our buildbots) and programs start to
fail with Unicode errors...

I see two options to improve the situation

(1) hard way
============

change open() API to make encoding a mandatory argument.

Problem
-------

It breaks compatibility with Python 3.0, 3.1 and 3.2 (ooops!); the encoding
argument is the 4th argument, you have to use a keyword or choose a value for
the buffering argument.

I proposed to change open() API in Python 3.1 to make all arguments -except the
filename and the mode- keyword-only arguments, but Guido rejected my idea::

    "Remember, for 3.0 we're trying to get a release out of the door, not
    cram in new features, no matter how small."


http://bugs.python.org/issue4121


(2) soft way
============

add a warning if the encoding is implicit (locale encoding).


I don't know what is the best warning type, and if it should be always displayed,
only once, or not by default.

Even if it is hidden by default, a careful developer will be able to use
``-Werror`` to fix bugs...

I suspect that most tests fail if open() raises an exception if the encoding is
not specified (e.g. see distutils/packaging issues about the file encoding).


Victor


Remarque
---------

::

    From: Laurent Pointal <laurent.pointal@limsi.fr>
    To: python@aful.org
    Cc: yannick <philaos31@yahoo.fr>
    Date: Fri, 17 May 2013 09:28:54 +0200
    Subject: Re: [Python-Fr] encodage


Deux règles simples pour les caractères accentués:

* travailler en unicode en interne
* spécifier l'encodage lors des entrées/sorties de toutes sortes

Entre autres, ouvrir les fichiers textes en indiquant encoding="xxx" 

- paramètre standard du builtin open() en Python3, 
- il faut passer le open() du module codecs en Python2.

Python tools
============

.. seealso:: 

   - http://pypi.python.org/pypi/Unidecode


Python3
--------

.. seealso::

   - http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html
   - http://nedbatchelder.com/text/unipain.html
   
   
   


