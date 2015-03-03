

.. index::
   qt i18n translating non-qt classes

.. _qt_translating_non_qt_classes:

==========================
Translating Non-Qt Classes
==========================

.. seealso:: http://doc.qt.nokia.com/4.6/internationalization.html


It is sometimes necessary to provide internationalization support for strings
used in classes that do not inherit QObject_ or use the Q_OBJECT macro to enable
translation features.

Since Qt translates strings at run-time based on the class they are associated
with and ``lupdate`` looks for translatable strings in the source code, **non-Qt classes
must use mechanisms that also provide this information**.

One way to do this is to add translation support to a non-Qt class using the
`Q_DECLARE_TR_FUNCTIONS()`_ macro; for example::

    class MyClass
    {
         Q_DECLARE_TR_FUNCTIONS(MyClass)

        public:
         MyClass();
     ...
    };

This provides the class with tr()_ functions that can be used to translate strings
associated with the class, and makes it possible for ``lupdate`` to find translatable
strings in the source code.

Alternatively, the `QCoreApplication::translate()`_ function can be called with a
specific context, and this will be recognized by ``lupdate`` and ``Qt Linguist``.

.. _QObject:  http://doc.qt.nokia.com/4.6/qobject.html
.. _tr():  http://doc.qt.nokia.com/4.6/qobject.html#tr
.. _`QCoreApplication::translate()`:  http://doc.qt.nokia.com/4.6/qcoreapplication.html#translate
.. _`Q_DECLARE_TR_FUNCTIONS()`: http://doc.qt.nokia.com/4.6/qcoreapplication.html#Q_DECLARE_TR_FUNCTIONS
