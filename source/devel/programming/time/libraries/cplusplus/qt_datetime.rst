

.. index::
   pair: Datetime; Qt Datetime


.. _qt_datetime:

============================
Qt datetime
============================


.. seealso::

   -  http://doc.qt.nokia.com/4.7-snapshot/qdatetime.html



.. contents::
   :depth: 3


#include QDateTime
==================


::

    #include <QDateTime>


Detailed Description
=====================

The QDateTime class provides date and time functions.

A QDateTime object contains a calendar date and a clock time (a "datetime").
It is a combination of the QDate and QTime classes.

It can read the current datetime from the system clock. It provides functions for
comparing datetimes and for manipulating a datetime by adding a number of seconds,
days, months, or years.

A QDateTime object is typically created either by giving a date and time
explicitly in the constructor, or by using the static function currentDateTime()
that returns a QDateTime object set to the system clock's time.

The date and time can be changed with setDate() and setTime().

A datetime can also be set using the setTime_t() function that takes a
POSIX-standard "number of seconds since 00:00:00 on January 1, 1970" value.

The fromString() function returns a QDateTime, given a string and a date format
used to interpret the date within the string.

The date() and time() functions provide access to the date and time parts of the
datetime. The same information is provided in textual format by the toString()
function.

QDateTime provides a full set of operators to compare two QDateTime objects where
smaller means earlier and larger means later.

You can increment (or decrement) a datetime by a given number of milliseconds
using addMSecs(), seconds using addSecs(), or days using addDays().

Similarly you can use addMonths() and addYears().

The daysTo() function returns the number of days between two datetimes, secsTo()
returns the number of seconds between two datetimes, and msecsTo() returns the
number of milliseconds between two datetimes.

QDateTime can store datetimes as local time or as UTC. QDateTime::currentDateTime()
returns a QDateTime expressed as local time; use toUTC() to convert it to UTC.

You can also use timeSpec() to find out if a QDateTime object stores a UTC time
or a local time.

Operations such as addSecs() and secsTo() are aware of daylight saving time (DST).

.. note:: QDateTime does not account for leap seconds.


Example 1
=========

::


    #include <QDateTime>

    void test_datetime()
    {
        char buf[200];
        struct tm tm;

        char acComment[200];
        QDateTime qDateExamen = QDateTime::fromString("2012-06-26 09:12:30", "yyyy-MM-dd hh:mm:ss");

        sprintf(acComment, "DateExamen=%s\n", qDateExamen.toString().toStdString().c_str());
        CR_Log_Write(acComment, true);
        int seconds = 520;

        int i = 0;
        while (i < 40)
        {
            qDateExamen = qDateExamen.addSecs(seconds);
            sprintf(acComment, "DateExamen +%d seconds =%s\n"
                    , seconds
                    , qDateExamen.toString("yyyy-MM-dd hh:mm:ss").toStdString().c_str());

            CR_Log_Write(acComment, true);

            char acDateReponse[300];
            sprintf(acDateReponse, "%s", qDateExamen.toString("yyyy-MM-dd hh:mm:ss").toStdString().c_str());
            char *pdate =  id3_strptime(acDateReponse, "%Y-%m-%d %H:%M:%S", &tm);
            strftime(buf, sizeof(buf), "%Y-%m-%d %H:%M:%S", &tm);
            sprintf(acComment, "\t=>DateExamen avec struct tm: %s\n\n"
                    , buf);
            CR_Log_Write(acComment, true);

            i +=1;
        }

    }



