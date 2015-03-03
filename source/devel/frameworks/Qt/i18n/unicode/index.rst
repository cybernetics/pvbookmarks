
.. index::
   qt unicode


.. _qt_unicode_support:

==================
Qt unicode support
==================


.. seealso::

   - http://www.siteduzero.com/tutoriel-3-11350-traduire-son-programme-avec-qt-linguist.html
   - http://www.loc.gov/standards/iso639-2/php/English_list.php


.. _qt_application_translation_process:

Translation of a Qt application is a four-step process
=======================================================

Translation of a Qt application is a three-step process:


0. :ref:`Prepare the source code for the translation <prepare_the_source_code_for_translation>`

1. :ref:`Run lupdate to extract translatable text from <qt_i18n_produce_translations>`:

   - the C++ source code of the Qt application,
   - the ``.ui`` file produced by QtCreator

   resulting in a message file for translators (a ``.ts`` file).

   The utility recognizes the `tr()`_ construct and the QT_TR*_NOOP() macros
   described above and produces TS files (usually one per language).

2. Provide translations for the source texts in the TS file, :ref:`using Qt Linguist <qt_translate_with_qt_linguist>`.
   .. note:: Since TS files are in XML format, you can also edit them by hand.

3. Run ``lrelease`` to obtain a light-weight message file (a QM file) from the TS file,
   suitable only for end use.
   Think of the TS files as "source files", and QM files as "object files".
   The translator edits the TS files, but the users of your application only need
   the QM files.
   Both kinds of files are platform and locale independent.

Typically, you will repeat these steps for every release of your application.
The ``lupdate`` utility does its best to reuse the translations from previous releases.


.. _tr():  http://doc.qt.nokia.com/4.6/qobject.html#tr

.. toctree::
   :maxdepth: 4

   prepare_translation/index
   produce_translations/index
   translate/index
   use_translations/index
   support_for_encodings
   translating_non_qt_classes
   dynamic_translation
   system_support
