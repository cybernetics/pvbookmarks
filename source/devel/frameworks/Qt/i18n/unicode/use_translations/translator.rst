

.. index::
   QTranslator class


=================
QTranslator class
=================


.. seealso:: :ref:`list_of_iso639_codes`

The QTranslator class provides internationalization support for text output.

An object of this class contains a set of translations from a source language
to a target language.

QTranslator provides functions to look up translations in a translation file.

Translation files are created using ``Qt Linguist``.

The most common use of QTranslator is to:

- load a translation file,
- install it using QApplication::installTranslator(),
- use it via QObject::tr().


::

    // i18n translation
    QTranslator qtTranslator;
    QString locale = QLocale::system().name().section('_', 0, 0);
    qtTranslator.load("control_panel_" + locale);
    control_panel.installTranslator(&qtTranslator);


