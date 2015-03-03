

.. index::
   pair: Formatage; C#
   pair: String ; Formatage


.. _csharp_formatage:

==================================
C# Formatage
==================================


.. seealso:: http://msdn.microsoft.com/fr-fr/library/fht0f5be%28v=vs.80%29.aspx


.. contents::
   :depth: 3

Formatage d'un entier en hexa : {0:X}
=====================================

::


    public static void WriteCommand(byte[] array_command_total, bool notifie = true)
    {
        string message = string.Format("Len command={0}: Command=[", array_command_total.Length);
        foreach (byte elem in array_command_total)
        {
            message = message + string.Format("0x{0:X} ", elem);
        }
        message = message + "]";
        Write(message, notifie);
    }



Résultat
--------

::

    Len command=12: Command=[0x3A 0x0 0x0 0x0 0x4 0x0 0x0 0x0 0x7 0x0 0x0 0x0 ]



Formatage d'un entier sur 4 chiffres : {0:0000}
=================================================

::

    /// <summary>
    /// Retourne le nom d'image pour l'image du puits
    /// </summary>
    public string GetNameForImage(DateTime date, int num_serie)
    {
        string datenow_milli = date.ToString("yyyy_MM_dd__HH_mm_ss");

        string ImageName = string.Format("{0}_{1:0000}_{2}_{3}"
                                        , Microplate.DeviceName
                                        , num_serie
                                        , Text
                                        , datenow_milli
                                        );

        return ImageName;
    }


Formatage d'un double f.ToString("00.00")
=========================================

::


    void AfficherLabelGainAnalogique(double gain_analogique)
    {
        string value_gain = gain_analogique.ToString("00.00");
        label_gain_analogique.Text = value_gain;
    }


