
.. index::
   pair: C♯ datetime  ; milliseconds


========================
C♯ datetime milliseconds
========================


::

        using System;



        /// <summary>
        /// Get the time with milliseconds.
        /// </summary>
        public static string GetTimeMilliseconds()
        {
            string datenow_milli = DateTime.Now.ToString("yyyy-MM-dd_HH:mm:ss.fff");

            return datenow_milli;
        }




