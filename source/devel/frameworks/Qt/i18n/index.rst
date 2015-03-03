
.. index::
   pair: Qt ; i18n


.. _qt_i18n:

=========
Qt i18n
=========


.. seealso::

   - :ref:`i18n`
   - http://doc.qt.nokia.com/4.6/internationalization.html
   - http://doc.qt.nokia.com/4.6/i18n-source-translation.html
   - https://secure.wikimedia.org/wikipedia/en/wiki/IETF_language_tag


Internationalization with Qt
============================


The internationalization of an application is the process of making the
application usable by people in countries other than one's own.



Relevant Qt Classes and APIs
============================

These classes support internationalizing of Qt applications.

======================================  =======================================================================================
QInputContext_                          Abstracts the input method dependent data and composing state
QLocale_                                Converts between numbers and their string representations in various languages
QSystemLocale_                          Can be used to finetune the system locale of the user
QTextCodec_                             Conversions between text encodings
QTextDecoder_                           State-based decoder
QTextEncoder_                           State-based encoder
QTranslator_                            Internationalization support for text output
`Translation Rules for Plurals`_        A summary of the translation rules for plurals produced by Qt's i18n tools.
`Writing Source Code for Translation`_  How to write source code in a way that makes it possible for user-visible text to be translated.
======================================  =======================================================================================


.. _QInputContext: http://doc.qt.nokia.com/4.6/qinputcontext.html
.. _QLocale:  http://doc.qt.nokia.com/4.6/qlocale.html
.. _QSystemLocale: http://doc.qt.nokia.com/4.6/qsystemlocale.html
.. _QTextCodec: http://doc.qt.nokia.com/4.6/qtextcodec.html
.. _QTextDecoder: http://doc.qt.nokia.com/4.6/qtextdecoder.html
.. _QTextEncoder: http://doc.qt.nokia.com/4.6/qtextencoder.html
.. _QTranslator: http://doc.qt.nokia.com/4.6/qtranslator.html
.. _`Translation Rules for Plurals`: http://doc.qt.nokia.com/4.6/i18n-plural-rules.html
.. _`Writing Source Code for Translation`: http://doc.qt.nokia.com/4.6/i18n-source-translation.html


Languages and Writing Systems
=============================

In some cases internationalization is simple, for example, making a US application
accessible to Australian or British users may require little more than a few
spelling corrections.

But to make a US application usable by Japanese users, or a Korean application
usable by German users, will require that the software operate not only in
different languages, but use different input techniques, character encodings and
presentation conventions.

Qt tries to make internationalization as painless as possible for developers.
All input widgets and text drawing methods in Qt offer built-in support for all
supported languages. The built-in font engine is capable of correctly and
attractively rendering text that contains characters from a variety of different
writing systems at the same time.

Qt supports most languages in use today, in particular:

- All East Asian languages (Chinese, Japanese and Korean)
- All Western languages (using Latin script)
- Arabic
- Cyrillic languages (Russian, Ukrainian, etc.)
- Greek
- Hebrew
- Thai and Lao
- All scripts in Unicode 5.1 that do not require special processing


Many of these writing systems exhibit special features:

- Special line breaking behavior. Some of the Asian languages are written
  without spaces between words. Line breaking can occur either after every
  character (with exceptions) as in Chinese, Japanese and Korean, or after
  logical word boundaries as in Thai.
- Bidirectional writing. Arabic and Hebrew are written from right to left,
  except for numbers and embedded English text which is written left to right.
  The exact behavior is defined in the Unicode Technical Annex #9.
- Non-spacing or diacritical marks (accents or umlauts in European languages).
  Some languages such as Vietnamese make extensive use of these marks and some
  characters can have more than one mark at the same time to clarify pronunciation.
- Ligatures. In special contexts, some pairs of characters get replaced by a
  combined glyph forming a ligature. Common examples are the fl and fi ligatures
  used in typesetting US and European books.


https://secure.wikimedia.org/wikipedia/fr/wiki/Qt#Internationalisation
======================================================================

Qt intègre son propre système de traduction, qui n'est pas foncièrement différent
dans le principe de la bibliothèque gettext_.

Selon le manuel de Qt Linguist, l'internationalisation est assurée par la
collaboration de trois types de personnes : les développeurs, le chef de projet
et les traducteurs.

Dans leur code source, les développeurs entrent des chaînes de caractères dans
leur propre langue. Ils doivent permettre la traduction de ces chaînes grâce à
la méthode `tr()`_.

En cas d'ambiguïté sur le sens d'une expression, ils peuvent également indiquer
des commentaires destinés à aider les traducteurs.

Le chef de projet déclare les fichiers de traduction (un pour chaque langue)
dans le fichier de projet.
L'utilitaire ``lupdate`` parcourt les sources à la recherche de chaînes à traduire
et synchronise les fichiers de traduction avec les sources.

Fichier de traduction XML (.ts et .qm)
--------------------------------------

Les fichiers de traductions sont des fichiers XML portant l'extension .ts.

Les traducteurs utilisent Qt Linguist pour renseigner les fichiers de traduction.

Quand les traductions sont finies, le chef de projet peut compiler les
fichiers .ts à l'aide de l'utilitaire ``lrelease`` qui génère des fichiers
binaires portant l'extension .qm, exploitables par le programme.

Ces fichiers sont lus à l'exécution et les chaînes de caractères qui y sont
trouvées remplacent celles qui ont été écrites par les développeurs.



.. _gettext: https://secure.wikimedia.org/wikipedia/fr/wiki/Gettext
.. _`tr()`:  http://doc.qt.nokia.com/4.6/qobject.html#tr

.. toctree::
   :maxdepth: 4

   unicode/index



