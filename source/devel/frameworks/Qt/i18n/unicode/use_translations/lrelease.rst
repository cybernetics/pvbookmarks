

.. index::
   lrelease


========
lrelease
========


Usage
=====

::

    lrelease -h


::


    Usage:
        lrelease [options] project-file
        lrelease [options] ts-files [-qm qm-file]

    lrelease is part of Qt's Linguist tool chain. It can be used as a
    stand-alone tool to convert XML-based translations files in the TS
    format into the 'compiled' QM format used by QTranslator objects.

    Options:
        -help  Display this information and exit
        -idbased
               Use IDs instead of source strings for message keying
        -compress
               Compress the QM files
        -nounfinished
               Do not include unfinished translations
        -removeidentical
               If the translated text is the same as
               the source text, do not include the message
        -markuntranslated <prefix>
               If a message has no real translation, use the source text
               prefixed with the given string instead
        -silent
               Do not explain what is being done
        -version
               Display the version of lrelease and exit


