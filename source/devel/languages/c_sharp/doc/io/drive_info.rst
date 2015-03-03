

.. index::
   pair: C♯ IO; DriveInfo



.. _csharp_drive_nfo:

================
C♯ DriveInfo
================



Exemple
=======


::


    /**
    @file       DriveInfo.cs
    @author     $Author: pvergain $
    @version    $Revision: 505 $
    @date       $Date: 2012-02-06 16:24:18 +0100 (Mon, 06 Feb 2012) $
    @brief      Drive information management.
    @details
     *

    */

    /** @addtogroup DriveInfo
     *  @{
     */


    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Globalization;


    namespace VideoCell
    {
            public class CDriveInfo
            {
                /// <summary>
                /// Retrurns the C DriveInfo.
                /// </summary>
                /// <remarks> see p.567 C#4.0 </remarks>
                public static DriveInfo GetDriveInfoC()
                {
                    DriveInfo c = new DriveInfo("C");
                    long totalSize = c.TotalSize;
                    long freeBytes = c.TotalFreeSpace;
                    long freeToMe = c.AvailableFreeSpace;

                    return c;
                }


                /// <summary>
                /// Humanize the  the C DriveInfo.
                /// http://en.wikipedia.org/wiki/Binary_prefix
                /// </summary>
                public static string  humanize_size_kibi_IEC(long space_available)
                {
                    string str_space_available = string.Empty;

                    long reste;
                    long quotient;

                    if (space_available >= 1073741824)
                    {
                        reste = (space_available % 1073741824);
                        quotient = (space_available / 1073741824);
                        str_space_available = string.Format("{0} GiB ", quotient);
                        if (reste > 0)
                        {
                            str_space_available = str_space_available + "+ " + humanize_size_kibi_IEC(reste);
                        }
                    }
                    else if (space_available >= 1048576)
                    {
                        reste = (space_available % 1048576);
                        quotient = (space_available / 1048576);
                        str_space_available = string.Format("{0} MiB ", quotient);
                        if (reste > 0)
                        {
                            str_space_available = str_space_available + "+ " + humanize_size_kibi_IEC(reste);
                        }
                    }
                    else if (space_available >= 1024)
                    {
                        reste = (space_available % 1024);
                        quotient = (space_available / 1024) ;
                        str_space_available = string.Format("{0} KiB ", quotient);
                        if (reste > 0)
                        {
                            str_space_available = str_space_available + "+ " + humanize_size_kibi_IEC(reste);
                        }
                    }
                    else
                    {
                        str_space_available = string.Format("{0} bytes", space_available);
                    }

                    return str_space_available;
                }

                /// <summary>
                /// Humanize the  the C DriveInfo.
                /// http://en.wikipedia.org/wiki/Binary_prefix
                /// </summary>
                public static string humanize_size_kb_SI(long space_available)
                {
                    string str_space_available = string.Empty;

                    long reste;
                    long quotient;

                    if (space_available >= 1000000000)
                    {
                        reste = (space_available % 1000000000);
                        quotient = (space_available / 1000000000);
                        str_space_available = string.Format("{0} GB ", quotient);
                        if (reste > 0)
                        {
                            str_space_available = str_space_available + "+ " + humanize_size_kb_SI(reste);
                        }
                    }
                    else if (space_available >= 1000000)
                    {
                        reste = (space_available % 1000000);
                        quotient = (space_available / 1000000);
                        str_space_available = string.Format("{0} MB ", quotient);
                        if (reste > 0)
                        {
                            str_space_available = str_space_available + "+ " + humanize_size_kb_SI(reste);
                        }
                    }
                    else if (space_available >= 1000)
                    {
                        reste = (space_available % 1000);
                        quotient = (space_available / 1000);
                        str_space_available = string.Format("{0} KB ", quotient);
                        if (reste > 0)
                        {
                            str_space_available = str_space_available + "+ " + humanize_size_kb_SI(reste);
                        }
                    }
                    else
                    {
                        str_space_available = string.Format("{0} bytes", space_available);
                    }

                    return str_space_available;
                }


                /// <summary>
                /// Log the  the spaces on all the volumes.
                /// </summary>
                public static void LogFreeSpaces(VideoCellForm videoForm)
                {
                    DriveInfo[] allDrives = DriveInfo.GetDrives();

                    foreach (DriveInfo d in allDrives)
                    {
                        if (d.IsReady)
                        {
                            LogAvailableSpace(videoForm, d.Name, d.AvailableFreeSpace, "available_free_space");
                            Log.Write(" ");
                        }
                    }
                }


                /// <summary>
                /// Log the  available space.
                /// </summary>
                public static void LogAvailableSpace(VideoCellForm videoForm, string drive_name, long available_space, string str_key)
                {
                    NumberFormatInfo nfi = videoForm.video_culture.Culture.NumberFormat;
                    string message = string.Format("{0} {1} =    {2} bytes "
                                                  , videoForm.GetI18nString(str_key)
                                                  , drive_name
                                                  , available_space.ToString("N", nfi)
                                                  );
                    Log.Write(message);
                    message = string.Format("{0} {1} SI  = {2} "
                                                  , videoForm.GetI18nString(str_key)
                                                  , drive_name
                                                  , humanize_size_kb_SI(available_space)
                                                  );
                    Log.Write(message);

                    message = string.Format("{0} {1} IEC = {2} "
                                                  , videoForm.GetI18nString(str_key)
                                                  , drive_name
                                                  , humanize_size_kibi_IEC(available_space)
                                                  );
                    Log.Write(message);
                }

                /// <summary>
                /// Log the  the available free space on the C drive
                /// </summary>
                public static void LogFreeSpace(VideoCellForm videoForm)
                {
                    DriveInfo c = GetDriveInfoC();

                    LogAvailableSpace(videoForm, "C", c.AvailableFreeSpace, "available_free_space");
                }


            } // class CDriveInfo

    } // VideoCell

    /**
        fin DriveInfo

    @}

    */



