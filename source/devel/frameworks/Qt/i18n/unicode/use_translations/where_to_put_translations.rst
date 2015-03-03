

.. index::
   Qt where to pu translations
   Qt transations resources


============================
Qt where to put translations
============================


.. seealso:: http://stackoverflow.com/questions/4034158/loading-qm-file


In a given directory
====================


Where are the .qm files located ? Your code is attempting to load the file from
the current working directory, which can be anything during runtime.

Specify a directory path in the call to QTranslator::load::

    QTranslator* translator = new QTranslator();
    if (translator->load("hellotr_la", "/path/to/folder/with/qm/files")) {
        app.installTranslator(translator);
    }

In Qt resource
==============

.. image:: qt_resources.png

Translations can be loaded from Qt resources, so it is a good idea to bundle
them inside your executables. Then you would load them somewhat like this::

    QTranslator* translator = new QTranslator();
    if (translator->load("hellotr_la", ":/translations")) {
        app.installTranslator(translator);
    }



