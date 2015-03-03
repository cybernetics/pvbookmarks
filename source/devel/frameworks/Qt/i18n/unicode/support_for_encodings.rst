

.. index::
   unicode encodings


=============================
Support for unicode encodings
=============================


.. seealso::

   - http://jimmyg.org/work/code/stringconvert/0.3.0/manual.html


The QTextCodec_ class and the facilities in QTextStream_ make it easy to support
many input and output encodings for your users data.

When an application starts, the locale of the machine will determine the 8-bit
encoding used when dealing with 8-bit data: such as for font selection, text
display, 8-bit text I/O, and character input.

The application may occasionally require encodings other than the default local
8-bit encoding.

For example, an application in a Cyrillic KOI8-R locale (the de-facto standard
locale in Russia) might need to output Cyrillic in the ISO 8859-5 encoding.

Code for this would be::

    QString string = ...; // some Unicode text
    QTextCodec *codec = QTextCodec::codecForName("ISO 8859-5");
    QByteArray encodedString = codec->fromUnicode(string);

Unicode to UTF-8 encoding
=========================

For converting Unicode to local 8-bit encodings, a shortcut is available: the
`QString::toLocal8Bit()`_ function returns such 8-bit data.

Another useful shortcut is `QString::toUtf8()`_, which returns text in the 8-bit
UTF-8 encoding: this perfectly preserves Unicode information while looking like
plain ASCII if the text is wholly ASCII.


UTF-8 to unicode
================

For converting the other way, there are the `QString::fromUtf8()`_ and
`QString::fromLocal8Bit()`_ convenience functions, or the general code, demonstrated
by this conversion from ISO 8859-5 Cyrillic to Unicode conversion::

    QByteArray encodedString = ...; // some ISO 8859-5 encoded text
    QTextCodec_ *codec = QTextCodec::codecForName("ISO 8859-5");
    QString string = codec->toUnicode(encodedString);


.. note:: Ideally Unicode I/O should be used as this maximizes the portability of documents
   between users around the world, but in reality it is useful to support all the
   appropriate encodings that your users will need to process existing documents.

In general, Unicode (UTF-16 or UTF-8) is best for information transferred between
arbitrary people, while within a language or national group, a local standard is
often more appropriate.

codec for locale
=================

The most important encoding to support is the one returned by `QTextCodec::codecForLocale()`_,
as this is the one the user is most likely to need for communicating with other
people and applications (this is the codec used by local8Bit()).

Qt supports most of the more frequently used encodings natively.

For a complete list of supported encodings see the QTextCodec_ documentation.

In some cases and for less frequently used encodings it may be necessary to write
your own QTextCodec_ subclass.

Depending on the urgency, it may be useful to contact Qt's technical support team
or ask on the ``qt-interest`` mailing list to see if someone else is already working
on supporting the encoding.


.. _QTextCodec: http://doc.qt.nokia.com/4.6/qtextcodec.html
.. _QTextStream: http://doc.qt.nokia.com/4.6/qtextstream.html
.. _`QString::toLocal8Bit()`: http://doc.qt.nokia.com/4.6/qstring.html#toLocal8Bit
.. _`QString::toUtf8()`: http://doc.qt.nokia.com/4.6/qstring.html#toUtf8
.. _`QString::fromUtf8()`: http://doc.qt.nokia.com/4.6/qstring.html#fromUtf8
.. _`QString::fromLocal8Bit()`: http://doc.qt.nokia.com/4.6/qstring.html#fromLocal8Bit
.. _`QTextCodec::codecForLocale()`: http://doc.qt.nokia.com/4.6/qtextcodec.html#codecForLocale
.. _QTextCodec: http://doc.qt.nokia.com/4.6/qtextcodec.html


