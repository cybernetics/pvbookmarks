

.. index::
   pair: C# ; Dictionary
   pair: Init ; Dictionary
   pair: static  ; Dictionary


==========================================
Initialisation d'un dictionnaire statique
==========================================

.. contents::
   :depth: 3



::

    using System;
    using System.IO;
    using System.Collections;
    using System.Collections.Generic;  // Dictionary


    namespace VideoCell
    {
        public class CGainsAnalogiques
        {
            public static Dictionary<int, CGainsAnalogiques> LesGainsAnalogiques
            {
                get { return les_gains_analogiques; }
            }
            private static Dictionary<int, CGainsAnalogiques> les_gains_analogiques = new Dictionary<int, CGainsAnalogiques>()
                {
                        { 0, new CGainsAnalogiques(1.0, 0)}
                      , { 1, new CGainsAnalogiques(1.1, 23)}
                      , { 2, new CGainsAnalogiques(1.2, 43)}
                      , { 3, new CGainsAnalogiques( 1.3, 59)}
                      , { 4, new CGainsAnalogiques(1.4, 73)}
                      , { 5, new CGainsAnalogiques(1.5, 85)}
                      , { 6, new CGainsAnalogiques(1.6, 96)}
                      , { 7, new CGainsAnalogiques(1.7, 105)}
                      , { 8, new CGainsAnalogiques(1.8, 114)}
                      , { 9, new CGainsAnalogiques(1.9, 121)}
                      , { 10, new CGainsAnalogiques(2.0, 128)}
                      , { 11, new CGainsAnalogiques(2.1, 134)}
                      , { 12, new CGainsAnalogiques(2.2, 140)}
                      , { 13, new CGainsAnalogiques(2.3, 145)}
                      , { 14, new CGainsAnalogiques(2.4, 149)}
                      , { 15, new CGainsAnalogiques(2.5, 154)}
                      , { 16, new CGainsAnalogiques(2.6, 158)}
                    ...
                      , { 63, new CGainsAnalogiques(9.1, 228)}
                      , { 64, new CGainsAnalogiques(9.5, 229)}
                      , { 65, new CGainsAnalogiques(9.8, 230)}
                      , { 66, new CGainsAnalogiques(10.2, 231)}
                      , { 67, new CGainsAnalogiques(10.7, 232)}
                      , { 68, new CGainsAnalogiques(11.1, 233)}
                      , { 69, new CGainsAnalogiques(11.6, 234)}
                      , { 70, new CGainsAnalogiques(12.2, 235)}
                      , { 71, new CGainsAnalogiques(12.8, 236)}
                      , { 72, new CGainsAnalogiques(13.5, 237)}
                      , { 73, new CGainsAnalogiques(14.2, 238)}
                      , { 74, new CGainsAnalogiques(15.1, 239)}
                      , { 75, new CGainsAnalogiques(16.0, 240)}

                };

            double gainAnalogiqueIHM;         // Affichage IHM
            double analogGainCode_Global;     // AnalogGainCode_Global qui doit être envoyée au microprocesseur

            public CGainsAnalogiques(double _gainAnalogiqueIHM, double _AnalogGainCode_Global)
            {
                gainAnalogiqueIHM = _gainAnalogiqueIHM;
                analogGainCode_Global = _AnalogGainCode_Global;
            }

        } // public class CGainsAnalogiquesAnalogiques

    } // namespace VideoCell





