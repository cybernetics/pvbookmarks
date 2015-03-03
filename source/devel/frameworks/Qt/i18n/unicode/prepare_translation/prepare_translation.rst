
.. index::
   qt prepare the source code for translation



.. _prepare_the_source_code_for_translation:

===========================================
Prepare the source code for the translation
===========================================


Use QString for All User-Visible Text
=====================================

.. seealso::

   - :ref:`unicode_6_0`
   - :ref:`unicode_5_0`

Since QString_ uses the :ref:`Unicode 5.1 <unicode_5_0>` encoding internally, every language in the
world can be processed transparently using familiar text processing operations.
Also, since all Qt functions that present text to the user take a QString_ as a
parameter, there is no char * to QString_ conversion overhead.

Strings that are in "programmer space" (such as QObject names and file format texts)
need not use QString_; the traditional char * or the QByteArray class will suffice.

You're unlikely to notice that you are using Unicode; QString_, and QChar_ are just
like easier versions of the crude const char * and char from traditional C.


Use tr() for All Literal Text
=============================

Wherever your program uses "quoted text" for text that will be presented to the
user, ensure that it is processed by the `QCoreApplication::translate()`_ function.

Essentially all that is necessary to achieve this is to use `QObject::tr()`_.
For example, assuming the LoginWidget is a subclass of QWidget::

    LoginWidget::LoginWidget()
    {
        QLabel *label = new QLabel(tr("Password:"));
     ...
    }


.. note:: This accounts for 99% of the user-visible strings you're likely to write.

If the quoted text is not in a member function of a QObject subclass, use either
the `tr()`_ function of an appropriate class, or the `QCoreApplication::translate()`_
function directly::

    void some_global_function(LoginWidget *logwid)
    {
        QLabel *label = new QLabel(
                 LoginWidget::tr("Password:"), logwid);
    }

    void same_global_function(LoginWidget *logwid)
    {
        QLabel *label = new QLabel(
                 qApp->translate("LoginWidget", "Password:"), logwid);
    }


If you need to have translatable text completely outside a function, there are
two macros to help:

- `QT_TR_NOOP()`_
- and `QT_TRANSLATE_NOOP()`_.

They merely mark the text for extraction by the lupdate utility described below.
The macros expand to just the text (without the context).


Example of `QT_TR_NOOP()`_::

    QString FriendlyConversation::greeting(int type)
    {
     static const char *greeting_strings[] = {
         QT_TR_NOOP("Hello"),
         QT_TR_NOOP("Goodbye")
     };
     return tr(greeting_strings[type]);
    }


Example of `QT_TRANSLATE_NOOP()`_::

    static const char *greeting_strings[] = {
     QT_TRANSLATE_NOOP("FriendlyConversation", "Hello"),
     QT_TRANSLATE_NOOP("FriendlyConversation", "Goodbye")
    };

    QString FriendlyConversation::greeting(int type)
    {
     return tr(greeting_strings[type]);
    }

    QString global_greeting(int type)
    {
     return qApp->translate("FriendlyConversation",
                            greeting_strings[type]);
    }


If you disable the const char * to QString_ automatic conversion by compiling
your software with the macro QT_NO_CAST_FROM_ASCII defined, you'll be very likely
to catch any strings you are missing. See `QString::fromLatin1()`_ for more
information. Disabling the conversion can make programming a bit cumbersome.

If your source language uses characters outside Latin1, you might find
QObject::trUtf8() more convenient than `QObject::tr()`_, as `tr()`_ depends on the
QTextCodec::codecForTr(), which makes it more fragile than QObject::trUtf8().


Use QString::arg() for Dynamic Text
===================================

The `QString::arg()`_ functions offer a simple means for substituting arguments::

    void FileCopier::showProgress(int done, int total,
                               const QString &currentFile)
    {
     label.setText(tr("%1 of %2 files copied.\nCopying: %3")
                   .arg(done)
                   .arg(total)
                   .arg(currentFile));
    }

In some languages the order of arguments may need to change, and this can easily
be achieved by changing the order of the % arguments.

For example::

    QString s1 = "%1 of %2 files copied. Copying: %3";
    QString s2 = "Kopierer nu %3. Av totalt %2 filer er %1 kopiert.";

    qDebug() << s1.arg(5).arg(10).arg("somefile.txt");
    qDebug() << s2.arg(5).arg(10).arg("somefile.txt");


produces the correct output in English and Norwegian::

    5 of 10 files copied. Copying: somefile.txt
    Kopierer nu somefile.txt. Av totalt 10 filer er 5 kopiert.



.. _QString: http://doc.qt.nokia.com/4.6/qstring.html
.. _QChar: http://doc.qt.nokia.com/4.6/qchar.html
.. _tr():  http://doc.qt.nokia.com/4.6/qobject.html#tr
.. _`QT_TR_NOOP()`: http://doc.qt.nokia.com/4.6/qtglobal.html#QT_TR_NOOP
.. _`QT_TRANSLATE_NOOP()`: http://doc.qt.nokia.com/4.6/qtglobal.html#QT_TRANSLATE_NOOP
.. _`QObject::tr()`:  http://doc.qt.nokia.com/4.6/qobject.html#tr
.. _`QCoreApplication::translate()`: http://doc.qt.nokia.com/4.6/qcoreapplication.html#translate
.. _`QString::fromLatin1()`: http://doc.qt.nokia.com/4.6/qstring.html#fromLatin1
.. _`QString::arg()`:  http://doc.qt.nokia.com/4.6/qstring.html#arg

