
.. index::
   pair: C♯ datetime  ; interval


=====================
C♯ datetime interval
=====================


::

    DateTime nextDate = firstDate;
    nextDate = videoCellTimers.AddIntervalTimeToDateTime(firstDate);


    /// <summary>
    /// Add interval time to the dateTime parameter.
    /// </summary>
    /// <remarks>
    /// </remarks>
    /// <returns>
    /// DateTime.
    /// </returns>
    public DateTime AddIntervalTimeToDateTime(DateTime dateTime)
    {
        DateTime newDate = dateTime.AddHours(interval.hours).AddMinutes(interval.minutes).AddSeconds(interval.seconds);

        return newDate;
    }




