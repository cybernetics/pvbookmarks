

.. index::
   pair: Barray Warsaw; i18n


.. _unicode_python_2:

==============
unicode python
==============


.. seealso::

   - http://pylonsbook.com/en/1.1/unicode.html?highlight=unicode
   - http://pylonsbook.com/en/1.1/internationalization-and-localization.html
   - http://www.wefearchange.org/2012/06/the-right-way-to-internationalize-your.html


.. contents::
   :depth: 3

Discussions
===========


::

    de  Victor Stinner victor.stinner@haypocalc.com
    heure de l'expéditeur   Envoyé à 13:18 (GMT+02:00). Heure locale : 14:55. ✆
    à   python-dev@python.org
    date    24 juin 2011 13:18
    objet   Re: [Python-Dev] EuroPython Language Summit report



::

    Le vendredi 24 juin 2011 à 10:52 +0200, Mark Dickinson a écrit :
    >   - [Armin Ronacher] Python 3's Unicode support still has some dark areas.


What ? Unicode support is perfect in Python 3 !


::

    >   One  example: when opening a text file for reading and writing, the default
    >   encoding used depends on the platform and on various environment variables.


... oh, I agree.

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

it breaks compatibility with Python 3.0, 3.1 and 3.2 (ooops!); the encoding
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


Python tools
============

.. seealso:: http://pypi.python.org/pypi/Unidecode


Barray Warsaw
=============

.. seealso::

   - http://www.wefearchange.org/2012/06/the-right-way-to-internationalize-your.html
   - http://docs.python.org/py3k/library/gettext.html
   - http://pyvideo.org/video/948/pragmatic-unicode-or-how-do-i-stop-the-pain
   - https://wiki.ubuntu.com/Python/FoundationsQPythonVersions






