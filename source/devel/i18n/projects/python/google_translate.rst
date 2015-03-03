

.. index::
   python google translate (xgoogle)
   Google translate

=================================
Python google translate (xgoogle)
=================================


.. seealso::

   - https://github.com/pkrumins/xgoogle
   - http://www.catonmat.net/blog/python-library-for-google-translate/


The new module is called "xgoogle.translate" and it implements two classes

- "Translator"
- "LanguageDetector".

The "Translator" class can be used to translate text. It provides a function
called "translate" that takes three arguments - "message", "lang_from" and "lang_to".


It returns the translated text as a Unicode string. Don't forget to encode it
to the right encoding before outputting, otherwise you'll get errors such as
"UnicodeEncodeError: 'latin-1' codec can't encode characters in position 0-3:
ordinal not in range(256)"



Readme
======

This is a Google library called 'xgoogle'. Current version is 1.3.

It's written by Peteris Krumins (peter@catonmat.net).

His blog is at http://www.catonmat.net  --  good coders code, great reuse.

License
-------

The code is licensed under MIT license.


Contains
--------

At the moment it contains:

- Google Search module xgoogle/search.py.
  http://www.catonmat.net/blog/python-library-for-google-search/

- Google Sponsored Links Search module xgoogle/sponsoredlinks.py
  http://www.catonmat.net/blog/python-library-for-google-sponsored-links-search/

- Google Sets module xgoogle/googlesets.py
  http://www.catonmat.net/blog/python-library-for-google-sets/

- Google Translate module xgoogle/translate.py
  http://www.catonmat.net/blog/python-library-for-google-translate/



Download
========

- https://github.com/pkrumins/xgoogle


Example
=======

Here is an example usage of Google Translate module::

    >>> from xgoogle.translate import Translator
    >>>
    >>> translate = Translator().translate
    >>> print translate("Mani sauc Pēteris", lang_to="ru").encode('utf-8')
    Меня зовут Петр
    >>> print translate("Mani sauc Pēteris", lang_to="en")
    My name is Peter
    >>> print translate("Меня зовут Петр")
    My name is Peter

The "translate" function takes three arguments - "message", "lang_from" and "lang_to".
If "lang_from" is not given, Google's translation service auto-detects it.
If "lang_to" is not given, it defaults to "en" (English).

In case of an error the "translate" function throws "TranslationError" exception.
Make sure to wrap your code in try/except block to catch it::

    >>> from xgoogle.translate import Translator, TranslationError
    >>>
    >>> try:
    >>>   translate = Translator().translate
    >>>   print translate("")
    >>> except TranslationError, e:
    >>>   print e

    Failed translating: invalid text


The Google Translate module also provides "LanguageDetector" class that can be used
to detect the language of the text.

Here is an example usage of LanguageDetector::

    >>> from xgoogle.translate import LanguageDetector, DetectionError
    >>>
    >>> detect = LanguageDetector().detect
    >>> english = detect("This is a wonderful library.")
    >>> english.lang_code
    'en'
    >>> english.lang
    'English'
    >>> english.confidence
    0.28078437000000001
    >>> english.is_reliable
    True

The "DetectionError" may get raised if the detection failed.


Version history
===============

**v1.0**
    initial release, xgoogle library contains just the Google Search.

**v1.1**
    added Google Sponsored Links Search.
    fixed a bug in browser.py that might have thrown an unexpected exception.


**v1.2**
    added Google Sets module

**v1.3**
    added Google Translate module
    fixed a bug in browser.py when KeyboardInterrupt did not get propagated.


