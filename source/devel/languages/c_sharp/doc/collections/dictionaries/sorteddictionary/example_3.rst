

.. index::
   pair: C# ; Dictionary
   pair: Init ; Dictionary
   pair: static  ; Dictionary

.. _example3_csharp_sortedidctionary:

==========================================
Initialisation d'un dictionnaire statique
==========================================

.. contents::
   :depth: 3

Init du tableau statique
========================

::

    using System;
    using System.Collections.Generic;  // SortedDictionary
    using System.Globalization;
    using System.Threading;
    using System.Windows.Forms;
    using System.Resources;
    using System.Reflection; // Assembly

    public partial class VideoCellForm : Form, IObservateurLog
    {
        public VideoCellCulture video_culture;
        public static string en_US_CULTURE = "en-US";
        public static string fr_FR_CULTURE = "fr-FR";
        public static string de_DE_CULTURE = "de-DE";
        public static string current_culture = null;

        public static SortedDictionary<string, VideoCellCulture> cultures = new SortedDictionary<string, VideoCellCulture>()
            {
                    { en_US_CULTURE, new VideoCellCulture(en_US_CULTURE, null)}
                  , { fr_FR_CULTURE, new VideoCellCulture(fr_FR_CULTURE, null)}
                  , { de_DE_CULTURE, new VideoCellCulture(de_DE_CULTURE, null)}
            };


La classe VideoCellCulture
===========================

::

    public class VideoCellCulture
    {
        string _culture_name;
        public string CultureName
        {
            get { return _culture_name; }
            set { _culture_name = value; }
        }


        CultureInfo _cultureInfo;
        public CultureInfo Culture
        {
            get { return _cultureInfo; }
            set { _cultureInfo = value; }
        }

        ToolStripMenuItem _menu_item;
        public ToolStripMenuItem MenuItem
        {
            get { return _menu_item; }
            set { _menu_item = value; }
        }

        public VideoCellCulture(string culture_name, ToolStripMenuItem menu_item)
        {
            _culture_name = culture_name;
            _cultureInfo = new CultureInfo(culture_name);
            _menu_item = menu_item;

        }
    }
