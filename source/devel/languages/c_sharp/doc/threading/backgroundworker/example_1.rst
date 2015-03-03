




.. _csharp_backgroundworker_example:

=============================
C♯  backgroundworker example
=============================


.. seealso::

   - http://stackoverflow.com/questions/3384394/reportprogress-c-sharp-question


.. contents::
   :depth: 3

Implementation of the the background worker
===========================================


::


    /**
    @file       MainForm_BackGroundWorker.cs
    @author     $Author: pvergain $
    @version    $Revision: 476 $
    @date       $Date: 2012-01-25 13:56:47 +0100 (Wed, 25 Jan 2012) $
    @brief      BackGroundWorker.
    @details
     *

    */

    using System;
    using System.Collections.Generic;
    using System.ComponentModel;
    using System.Data;
    using System.Drawing;
    using System.Linq;
    using System.Text;
    using System.Windows.Forms;
    using System.Resources;
    using System.Reflection; // Assembly
    using System.Threading;

    /** @addtogroup MainForm_BackGroundWorker
     *  @{
     */


    using VideoCell;

    namespace VideoCell
    {
        public partial class VideoCellForm : Form , IObservateurLog
        {

            // see http://msdn.microsoft.com/fr-fr/library/system.componentmodel.backgroundworker.aspx
            private BackgroundWorker background_worker_acquisition;
            public BackgroundWorker BackgroundWorkerAcquisition
            {
                get { return background_worker_acquisition; }
                set { background_worker_acquisition = value; }
            }

            /// <summary>
            /// Building of the acquisition date
            /// This event handler is where the time-consuming work is done.
            /// </summary>
            /// <remarks>
            /// </remarks>
            /// <returns>
            /// - true: the fields hours, minutes et seconds are equal to 0.
            /// - false : the fields champs hours, minutes et seconds are not equal to 0.
            /// </returns>
            private void background_worker_acquisition_DoWork(object sender, DoWorkEventArgs e)
            {
                Dictionary<string, string> dict_messages_i18n = e.Argument as Dictionary<string, string>;

                Dictionary<int, string> dict_messages = new Dictionary<int, string>();

                int nb_dates = AcquisitionScheduler.SecondaryAcquisitionDates.Keys.Count();
                int i_date = 1;
                foreach (DateTime date_acquisition in AcquisitionScheduler.SecondaryAcquisitionDates.Keys)
                {
                    if (BackgroundWorkerAcquisition.CancellationPending == true)
                    {
                        e.Cancel = true;
                        break;
                    }
                    else
                    {
                        // Time consuming part
                        string well_name = AcquisitionScheduler.SecondaryAcquisitionDates[date_acquisition];

                        int percentComplete = (i_date * 100) / nb_dates;

                        while (date_acquisition >= DateTime.Now)
                        {
                            dict_messages[0] = "WAITING";
                            string message_acquisition = dict_messages_i18n["waiting_next_acquisition_date"];

                            dict_messages[1] = String.Format("{0} {1:d/M/yyyy HH:mm:ss} "
                                                           , message_acquisition
                                                           , date_acquisition);

                            // give the message to display to the main thread
                            BackgroundWorkerAcquisition.ReportProgress(percentComplete, dict_messages);

                            // We are waiting until date_acquisition > DateTime.Now
                             Thread.Sleep(200);
                         }

                        string message_start_acquisition = dict_messages_i18n["start_image_acquisition_for_well"];
                        string message_date_prevue = dict_messages_i18n["date_prevue_acquisition_image"];
                        dict_messages[0] = "ACQUISITION";
                        dict_messages[1] = String.Format("{0} {1} {2:d/M/yyyy HH:mm:ss} ({3}/{4}) "
                              , message_start_acquisition
                              , well_name
                              , date_acquisition
                              , i_date
                              , nb_dates);

                        // Report progress as a percentage of the total task.
                        BackgroundWorkerAcquisition.ReportProgress(percentComplete, dict_messages);

                        i_date++;
                        Thread.Sleep(500);
                    }
                }

            } // private void background_worker_acquisition_DoWork(object sender, DoWorkEventArgs e)


            private void background_worker_acquisition_ProgressChanged(object sender, ProgressChangedEventArgs e)
            {
                Dictionary<int, string> dict_messages = (Dictionary<int, string>)e.UserState;

                if (dict_messages[0] == "ACQUISITION")
                {
                    label_message.Text = (e.ProgressPercentage.ToString() + "%");
                    Log.Write(label_message.Text);
                    Log.Write(dict_messages[1]);
                }
                else if (dict_messages[0] == "WAITING")
                {
                    label_message.Text = dict_messages[1];
                }
            }

            /// </summary>
            /// Initialize the backgroung worker.
            /// </summary>
            void InitializeBackgroundWorker()
            {
                // see http://msdn.microsoft.com/fr-fr/library/system.componentmodel.backgroundworker.aspx
                background_worker_acquisition = new BackgroundWorker();

                background_worker_acquisition.DoWork += new DoWorkEventHandler(background_worker_acquisition_DoWork);

                background_worker_acquisition.RunWorkerCompleted += new RunWorkerCompletedEventHandler(background_worker_acquisition_RunWorkerCompleted);
                background_worker_acquisition.ProgressChanged += new ProgressChangedEventHandler(background_worker_acquisition_ProgressChanged);

                background_worker_acquisition.WorkerReportsProgress = true;
                background_worker_acquisition.WorkerSupportsCancellation = true;
            }



            /// </summary>
            /// The background worker has been canceled or is finished.
            /// </summary>
            private void background_worker_acquisition_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e)
            {
                AcquisitionIsOver();

                if (e.Cancelled == true)
                {
                    label_message.Text = GetI18nString("acquisition_canceled");
                }
                else if (e.Error != null)
                {
                    label_message.Text = "Error: " + e.Error.Message;
                }
                else
                {
                    label_message.Text = GetI18nString("fin_acquisition");
                }

                Log.Write(label_message.Text);
            }


        } // public partial class VideoCell : Form


    } // VideoCell


    /**
        fin MainForm_BackGroundWorker

    @}

    */


Calling the background worker
==============================


::

    Dictionary<string, string> dict_messages_i18n = new Dictionary<string, string>();

    string message_acquisition = GetI18nString("waiting_next_acquisition_date");
    dict_messages_i18n["waiting_next_acquisition_date"] = message_acquisition;

    string message_start_acquisition = GetI18nString("start_image_acquisition_for_well");
    dict_messages_i18n["start_image_acquisition_for_well"] = message_start_acquisition;

    string date_prevue_acquisition = GetI18nString("date_prevue_acquisition_image");
    dict_messages_i18n["date_prevue_acquisition_image"] = message_start_acquisition;


    // Start the images acquisition.
    BackgroundWorkerAcquisition.RunWorkerAsync(dict_messages_i18n);





