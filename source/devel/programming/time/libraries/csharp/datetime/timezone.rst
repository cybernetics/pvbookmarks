

.. index::
   pair: C♯ ; Local Time
   pair: C♯ ; Universal Time

.. _csharp_universal_time:

================================================================
C♯ UTC, ToUniversalTime(),  ToLocalTime()
================================================================

.. seealso::

   - http://msdn.microsoft.com/fr-fr/library/system.datetime.tolocaltime.aspx



Exemple 1
==========

::


    using System;

    public class Example
    {
       public static void Main()
       {
          DateTime date1 = new DateTime(2010, 3, 14, 2, 30, 0, DateTimeKind.Local);
          Console.WriteLine("Invalid time: {0}",
                            TimeZoneInfo.Local.IsInvalidTime(date1));
          DateTime utcDate1 = date1.ToUniversalTime();
          DateTime date2 = utcDate1.ToLocalTime();
          Console.WriteLine("{0} --> {1}", date1, date2);
       }
    }

The example displays the following output::


    Invalid time: True
    3/14/2010 2:30:00 AM --> 3/14/2010 3:30:00 AM



Exemple 1
==========


This code example demonstrates:

- the DateTime Kind,
- Now,
- UtcNow
- the SpecifyKind(),
- ToLocalTime(),
- ToUniversalTime() .



::



    using System;

    class Sample
    {
        public static void Main()
        {
    // Get the date and time for the current moment, adjusted
    // to the local time zone.

        DateTime saveNow = DateTime.Now;

    // Get the date and time for the current moment expressed
    // as coordinated universal time (UTC).

        DateTime saveUtcNow = DateTime.UtcNow;
        DateTime myDt;

    // Display the value and Kind property of the current moment
    // expressed as UTC and local time.

        DisplayNow("UtcNow: ..........", saveUtcNow);
        DisplayNow("Now: .............", saveNow);
        Console.WriteLine();

    // Change the Kind property of the current moment to
    // DateTimeKind.Utc and display the result.

        myDt = DateTime.SpecifyKind(saveNow, DateTimeKind.Utc);
        Display("Utc: .............", myDt);

    // Change the Kind property of the current moment to
    // DateTimeKind.Local and display the result.

        myDt = DateTime.SpecifyKind(saveNow, DateTimeKind.Local);
        Display("Local: ...........", myDt);

    // Change the Kind property of the current moment to
    // DateTimeKind.Unspecified and display the result.

        myDt = DateTime.SpecifyKind(saveNow, DateTimeKind.Unspecified);
        Display("Unspecified: .....", myDt);
        }

    // Display the value and Kind property of a DateTime structure, the
    // DateTime structure converted to local time, and the DateTime
    // structure converted to universal time.

        public static string datePatt = @"M/d/yyyy hh:mm:ss tt";
        public static void Display(string title, DateTime inputDt)
        {
        DateTime dispDt = inputDt;
        string dtString;

    // Display the original DateTime.

        dtString = dispDt.ToString(datePatt);
        Console.WriteLine("{0} {1}, Kind = {2}",
                          title, dtString, dispDt.Kind);

    // Convert inputDt to local time and display the result.
    // If inputDt.Kind is DateTimeKind.Utc, the conversion is performed.
    // If inputDt.Kind is DateTimeKind.Local, the conversion is not performed.
    // If inputDt.Kind is DateTimeKind.Unspecified, the conversion is
    // performed as if inputDt was universal time.

        dispDt = inputDt.ToLocalTime();
        dtString = dispDt.ToString(datePatt);
        Console.WriteLine("  ToLocalTime:     {0}, Kind = {1}",
                          dtString, dispDt.Kind);

    // Convert inputDt to universal time and display the result.
    // If inputDt.Kind is DateTimeKind.Utc, the conversion is not performed.
    // If inputDt.Kind is DateTimeKind.Local, the conversion is performed.
    // If inputDt.Kind is DateTimeKind.Unspecified, the conversion is
    // performed as if inputDt was local time.

        dispDt = inputDt.ToUniversalTime();
        dtString = dispDt.ToString(datePatt);
        Console.WriteLine("  ToUniversalTime: {0}, Kind = {1}",
                          dtString, dispDt.Kind);
        Console.WriteLine();
        }

    // Display the value and Kind property for DateTime.Now and DateTime.UtcNow.

        public static void DisplayNow(string title, DateTime inputDt)
        {
        string dtString = inputDt.ToString(datePatt);
        Console.WriteLine("{0} {1}, Kind = {2}",
                          title, dtString, inputDt.Kind);
        }
    }
