

.. index::
   qt lupdate


===================
Qt lupdate program
===================


``lupdate`` is part of Qt's Linguist tool chain.

It extracts translatable messages from:

- Qt UI files
- C++
- Java
- JavaScript/QtScript


Extracted messages are stored in textual translation source files (typically
Qt TS XML).

New and modified messages can be merged into existing TS files.


::

   lupdate



::

    Usage:
        lupdate [options] [project-file]...
        lupdate [options] [source-file|path|@lst-file]... -ts ts-files|@lst-file

    lupdate is part of Qt's Linguist tool chain. It extracts translatable
    messages from Qt UI files, C++, Java and JavaScript/QtScript source code.
    Extracted messages are stored in textual translation source files (typically
    Qt TS XML). New and modified messages can be merged into existing TS files.

    Options:
        -help  Display this information and exit.
        -no-obsolete
               Drop all obsolete strings.
        -extensions <ext>[,<ext>]...
               Process files with the given extensions only.
               The extension list must be separated with commas, not with whitespace
               Default: 'java,jui,ui,c,c++,cc,cpp,cxx,ch,h,h++,hh,hpp,hxx,js,qs,qml'
        -pluralonly
               Only include plural form messages.
        -silent
               Do not explain what is being done.
        -no-sort
               Do not sort contexts in TS files.
        -no-recursive
               Do not recursively scan the following directories.
        -recursive
               Recursively scan the following directories (default).
        -I <includepath> or -I<includepath>
               Additional location to look for include files.
               May be specified multiple times.
        -locations {absolute|relative|none}
               Specify/override how source code references are saved in TS files.
               Default is absolute.
        -no-ui-lines
               Do not record line numbers in references to UI files.
        -disable-heuristic {sametext|similartext|number}
               Disable the named merge heuristic. Can be specified multiple times.
        -pro <filename>
               Name of a .pro file. Useful for files with .pro file syntax but
               different file suffix. Projects are recursed into and merged.
        -source-language <language>[_<region>]
               Specify the language of the source strings for new files.
               Defaults to POSIX if not specified.
        -target-language <language>[_<region>]
               Specify the language of the translations for new files.
               Guessed from the file name if not specified.
        -ts <ts-file>...
               Specify the output file(s). This will override the TRANSLATIONS
               and nullify the CODECFORTR from possibly specified project files.
        -codecfortr <codec>
               Specify the codec assumed for tr() calls. Effective only with -ts.
        -version
               Display the version of lupdate and exit.
        @lst-file
               Read additional file names (one per line) from lst-file.


lupdate Usage
=============


::

    lupdate myproject.pro


``lupdate`` is a command line tool that finds the translatable strings in the specified
source, header and Qt Designer interface files, and produces or updates .ts
translation files.

The files to process and the files to update can be set at the command line, or
provided in a .pro file specified as an command line argument.

The produced translation files are given to the translator who uses Qt Linguist
to read the files and insert the translations.

Companies that have their own translators in-house may find it useful to run
lupdate regularly, perhaps monthly, as the application develops.

This will lead to a fairly low volume of translation work spread evenly over the
life of the project and will allow the translators to support a number of
projects simultaneously.

Companies that hire in translators as required may prefer to run lupdate only a
few times in the application's life cycle, the first time might be just before
the first test phase.

This will provide the translator with a substantial single block of work and
any bugs that the translator detects may easily be included with those found
during the initial test phase.

The second and any subsequent lupdate runs would probably take place during the
final beta phase.

The TS file format is a simple human-readable XML format that can be used with
version control systems if required.

``lupdate`` can also process Localization Interchange File Format (XLIFF) format
files; files in this format typically have file names that end with the .xlf suffix.

.. note:: The minimum supported version for XLIFF format files is 1.1. XLIFF 1.0
   version files are not supported.


Produce the ``.ts`` files from a ``.ui`` file
=============================================


In this example we want to have 5 translations:

- english
- deutsch
- français
- italiano
- español

In order to produce :file:`.ts` files from a :file:`.ui` file 2 steps:


1. add the following lines in your .pro file::

    TRANSLATIONS = your_project_en.ts
    TRANSLATIONS = your_project_de.ts
    TRANSLATIONS = your_project_fr.ts
    TRANSLATIONS = your_project_it.ts
    TRANSLATIONS = your_project_es.ts

2. type the following command in your terminal::

    lupdate your_project.pro


::

    Updating 'your_project_en.ts'...
        Found 170 source text(s) (0 new and 170 already existing)
    Updating 'your_project_de.ts'...
        Found 170 source text(s) (170 new and 0 already existing)
    Updating 'your_project_fr.ts'...
        Found 170 source text(s) (170 new and 0 already existing)
    Updating 'your_project_it.ts'...
        Found 170 source text(s) (170 new and 0 already existing)
    Updating 'your_project_es.ts'...
        Found 170 source text(s) (170 new and 0 already existing)




