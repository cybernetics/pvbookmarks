
.. index::
   pair: Qt; Localization

========================
Qt localization (l10n)
========================

.. seealso:: http://doc.qt.nokia.com/4.6/internationalization.html


Time localization
=================


Localization is the process of adapting to local conventions, for example
presenting dates and times using the locally preferred formats.

Such localizations can be accomplished using appropriate tr()_ strings..

.. code-block:: c

    void Clock::setTime(const QTime &time)
    {
         if (tr("AMPM") == "AMPM") {
             // 12-hour clock
         } else {
             // 24-hour clock
         }
    }

In the example, for the US we would leave the translation of "AMPM" as it is and
thereby use the 12-hour clock branch; but in Europe we would translate it as
something else and this will make the code use the 24-hour clock branch.

For localized numbers use the QLocale_ class.

.. _tr():  http://doc.qt.nokia.com/4.6/qobject.html#tr
.. _QLocale: http://doc.qt.nokia.com/4.6/qlocale.html


For localized numbers use the QLocale class
===========================================

Localizing images is not recommended. Choose clear icons that are appropriate
for all localities, rather than relying on local puns or stretched metaphors.

The exception is for images of left and right pointing arrows which may need to
be reversed for Arabic and Hebrew locales.
