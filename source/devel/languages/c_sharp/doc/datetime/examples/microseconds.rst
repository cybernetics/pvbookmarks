
.. index::
   pair: C♯ datetime  ; microseconds


========================
C♯ datetime microseconds
========================


::

        using System;



        /// <summary>
        /// Get the time with microseconds.
        /// </summary>
        public static string GetTimeMicroseconds()
        {
            string datenow_micro = DateTime.Now.ToString("yyyy-MM-dd_HH:mm:ss.ffffff");

            return datenow_micro;
        }




