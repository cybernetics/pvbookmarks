

.. index::
   qt i18n LanguageChange event

.. _qt_dynamic_translation:

=======================
Qt dynamic translation
=======================


Some applications, such as Qt Linguist, must be able to support changes to the
user's language settings while they are still running.

To make widgets aware of changes to the installed QTranslators, reimplement the
widget's `changeEvent()`_ function to check whether the event is a LanguageChange_
event, and update the text displayed by widgets using the tr() function in the
usual way. For example::

    void MyWidget::changeEvent(QEvent *event)
    {
         if (e->type() == QEvent::LanguageChange) {
             titleLabel->setText(tr("Document Title"));
             ...
             okPushButton->setText(tr("&OK"));
         } else
             QWidget::changeEvent(event);
    }


All other change events should be passed on by calling the default implementation
of the function.

The list of installed translators might change in reaction to a LocaleChange_
event, or the **application might provide a user interface that allows the user
to change the current application language**.

The default event handler for QWidget subclasses responds to the QEvent::LanguageChange
event, and will call this function when necessary.

LanguageChange_ events are posted when a new translation is installed using the
`QCoreApplication::installTranslator()`_ function.

Additionally, other application components can also force widgets to update
themselves by posting LanguageChange_ events to them.


.. _`changeEvent()`:  http://doc.qt.nokia.com/4.6/qwidget.html#changeEvent
.. _LanguageChange: http://doc.qt.nokia.com/4.6/qevent.html#Type-enum
.. _LocaleChange: http://doc.qt.nokia.com/4.6/qevent.html#Type-enum
.. _`QCoreApplication::installTranslator()`: http://doc.qt.nokia.com/4.6/qcoreapplication.html#installTranslator


