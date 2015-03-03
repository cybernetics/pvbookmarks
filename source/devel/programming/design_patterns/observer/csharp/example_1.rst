

=====================================
Example_1 C♯ Observer Design pattern
=====================================


The subject
===========

::


    using System;
    using System.IO;
    using System.Collections.Generic;

    namespace VideoCell
    {
        public interface IObservateurLog
        {
            void UpdateLog(string text);
        }

        public static class Log
        {
            static  IList<IObservateurLog> observers = new List<IObservateurLog>();

            public static void Add(IObservateurLog observer)
            {
                observers.Add(observer);
            }

            public static void Remove(IObservateurLog observer)
            {
                observers.Remove(observer);
            }

            static void Notifie(string text)
            {
                foreach (IObservateurLog observer in observers)
                    observer.UpdateLog(text);
            }

            static bool isOpen = false;
            static StreamWriter writerLog;

            /// <summary>
            /// Open a log file.
            /// </summary>
            public static void Open()
            {
                if (isOpen)
                {
                    // already open
                    return;
                }

                string filename = "C:\\VideoCell.log";
                try
                {
                    // false => pas de concaténation
                    writerLog = new StreamWriter(filename, false);
                    isOpen = true;
                }
                catch (Exception ex)
                {
                    isOpen = false;
                    throw new Exception("Cant open log file", ex);
                }
            }


            /// <summary>
            /// Close a log file.
            /// </summary>
            public static void Close()
            {
                if (isOpen)
                {
                    Write("close Log()");

                    writerLog.Flush();
                    writerLog.Close();
                }
                isOpen = false;
            }

            public static void Flush()
            {
                if (isOpen)
                {
                    writerLog.Flush();

                }

            }


            /// <summary>
            /// Get the time with milliseconds.
            /// </summary>
            public static string GetTimeMilliseconds()
            {
                string datenow_milli = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss.fff");

                return datenow_milli;
            }

            /// <summary>
            /// Get the time with microseconds.
            /// </summary>
            public static string GetTimeMicroseconds()
            {
                string datenow_micro = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss.ffffff");

                return datenow_micro;
            }

            /// <summary>
            /// Write a string in a log file.
            /// </summary>
            public static void Write(string text)
            {
                if (!isOpen)
                    return;

                string datenow = GetTimeMicroseconds();

                string str_message = String.Format("{0} {1}\n", datenow, text);

                writerLog.Write(str_message);

                // on avertit les observateurs du log
                Notifie(str_message);

                writerLog.Flush();
            }

        } // public class Log


The observer
============

::

    namespace VideoCell
    {
        public partial class VideoCellForm : Form , IObservateurLog
        {
            ...

            public void UpdateLog(string str_message)
            {
                textBox_logs.AppendText(str_message);
            }

            ...

            void OpenApplication()
            {
                Log.Open();
                Log.Add(this);
                Log.Write("Open VideoCellApplication");
            }

            ...

    } // namespace VideoCell
