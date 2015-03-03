

.. index::
   pair: Interop; Excel

.. _ex_interop_excel:

========================
Example Interop Excel
========================


::



    /** @addtogroup Excel
     *  @{
     */


    using RFID_Eurocopter;

    using SQLite;
    using System;
    using System.Collections;
    using System.Collections.Generic;  // Dictionary
    using System.Data.Sql;
    using System.Globalization;
    using System.IO;
    using System.Runtime.InteropServices;
    using System.Threading;
    using System.Windows.Forms;
    using Excel = Microsoft.Office.Interop.Excel;

    namespace RFID_Eurocopter
    {
        /// <summary>
        /// Description des champs d'un fichier excel   
        /// </summary>
        public class CExcelLivraisonPots
        {
            /// <summary>
            /// Constructeur
            /// </summary>
            public CExcelLivraisonPots()
            {
                ;
            }

            /// <summary>
            /// Constructeur
            /// </summary>
            public CExcelLivraisonPots(CExcelLivraisonPots livraisonPots)
            {
                Fournisseur = livraisonPots.Fournisseur;
                DateLivraison = livraisonPots.DateLivraison;
                UniteQuantite = livraisonPots.UniteQuantite;
            }
            // ==============================
            // Champs communs à une livraison
            // ==============================
            /// <summary>
            /// Le fournisseur (ex: "PABAN S.A.S") 
            /// </summary>       
            public static int FOURNISSEUR_LIGNE = 3;
            public static int FOURNISSEUR_COLONNE = 2;
            public static int FOURNISSEUR_MAX_LENGTH = 15;
            private string _fournisseur;
            public string Fournisseur
            {
                get { return _fournisseur; }
                set { _fournisseur = value; }
            }
            /// <summary>
            /// Nombre de feuilles excel    
            /// </summary> 
            public static int NB_FEUILLES_EXCEL_LIGNE = 5;
            public static int NB_FEUILLES_EXCEL_COLONNE = 5;
            static private int _nb_feuilles_excel;
            static public int NbFeuillesExcel
            {
                get { return _nb_feuilles_excel; }
                set { _nb_feuilles_excel = value; }
            }
            /// <summary>
            /// La date de livraison    
            /// </summary>
            public static int DATE_LIVRAISON_LIGNE = 15;
            public static int DATE_LIVRAISON_COLONNE = 8;
            private DateTime _dateLivraison;
            public DateTime DateLivraison
            {
                get { return _dateLivraison; }
                set { _dateLivraison = value; }
            }
            /// <summary>
            /// L'unité pour la quantité
            /// Analyse de la forme: "Cond. en litres"
            /// </summary>       
            public static int UNITE_QUANTITE_LIGNE = 17;
            public static int UNITE_QUANTITE_COLONNE = 7;
            private string _uniteQuantite;
            public string UniteQuantite
            {
                get { return _uniteQuantite; }
                set { _uniteQuantite = value; }
            }
            // ==============================
            // Champs multilignes
            // ==============================
            /// <summary>
            /// La référence du produit (ex: "2K THINNER") 
            /// </summary>    
            public static int REFERENCE_PRODUIT_LIGNE = 20;
            public static int REFERENCE_PRODUIT_COLONNE = 1;
            public static int REFERENCE_PRODUIT_MAX_LENGTH = 20;
            private string _referenceProduit;
            public string ReferenceProduit
            {
                get { return _referenceProduit; }
                set { _referenceProduit = value; }
            }
            /// <summary>
            /// Le nom du produit (ex: "DILUANT")     
            /// </summary>      
            public static int NOM_PRODUIT_LIGNE = 20;
            public static int NOM_PRODUIT_COLONNE = 2;
            public static int NOM_PRODUIT_MAX_LENGTH = 15;
            private string _nomProduit;
            public  string NomProduit
            {
                get { return _nomProduit; }
                set { _nomProduit = value; }
            }
            /// <summary>
            /// Le numéro ECS    
            /// </summary> 
            public static int NUMERO_ECS_LIGNE = 20;
            public static int NUMERO_ECS_COLONNE = 3;
            public static int NUMERO_ECS_MAX_LENGTH = 6;
            private string _numeroECS;
            public string NumeroECS
            {
                get { return _numeroECS; }
                set { _numeroECS = value; }
            }

            /// <summary>
            /// La teinte (Ex: BLANC) 
            /// </summary>      
            public static int TEINTE_LIGNE = 20;
            public static int TEINTE_COLONNE = 4;
            public static int TEINTE_MAX_LENGTH = 15;
            private string _teinte;
            public string Teinte
            {
                get { return _teinte; }
                set { _teinte = value; }
            }
            /// <summary>
            /// Les températures de stockage (Min et Max)
            /// Analyse de la forme : "5-30" par exemple
            /// </summary>
            public static int TEMPERATURE_STOCKAGE_LIGNE = 20;
            public static int TEMPERATURE_STOCKAGE_COLONNE = 5;

            /// <summary>
            /// Températures de stockage Min   
            /// </summary>
            private decimal _temperatureStockageMin;
            public decimal TemperatureStockageMin
            {
                get { return _temperatureStockageMin; }
                set { _temperatureStockageMin = value; }
            }
            /// <summary>
            /// Températures de stockage Max   
            /// </summary>
            private decimal _temperatureStockageMax;
            public decimal TemperatureStockageMax
            {
                get { return _temperatureStockageMax; }
                set { _temperatureStockageMax = value; }
            }
            /// <summary>
            /// Le conditionnement en litres    
            /// </summary>
            public static int COND_EN_LITRES_LIGNE = 20;
            public static int COND_EN_LITRES_COLONNE = 7;
            private decimal _cond_en_litres;
            public decimal ConditionnementEnLitres
            {
                get { return _cond_en_litres; }
                set { _cond_en_litres = value; }
            }
            /// <summary>
            /// Quantité total de pots pour cette livraison    
            /// </summary> 
            public static int QUANTITE_NB_TOTAL_POTS_LIGNE = 20;
            public static int QUANTITE_NB_TOTAL_POTS_COLONNE = 6;
            private int _nb_total_pots;
            public int NbTotalPots
            {
                get { return _nb_total_pots; }
                set { _nb_total_pots = value; }
            }
            /// <summary>
            /// Le numéro de lot (Ex: 2373845102) 
            /// </summary>  
            public static int NUMERO_LOT_LIGNE = 20;
            public static int NUMERO_LOT_COLONNE = 8;
            public static int NUMERO_LOT_MAX_LENGTH = 30;
            private string _numeroLot;
            public string NumeroLot
            {
                get { return _numeroLot; }
                set { _numeroLot = value; }
            }
            /// <summary>
            /// La date de fabrication    
            /// </summary>
            public static int DATE_FABRICATION_LIGNE = 20;
            public static int DATE_FABRICATION_COLONNE = 9;

            private DateTime _dateFabrication;
            public DateTime DateFabrication
            {
                get { return _dateFabrication; }
                set { _dateFabrication = value; }
            }
            /// <summary>
            /// La date de péremption    
            /// </summary>
            public static int DATE_PEREMPTION_LIGNE = 20;
            public static int DATE_PEREMPTION_COLONNE = 10;
            private DateTime _datePeremption;
            public DateTime DatePeremption
            {
                get { return _datePeremption; }
                set { _datePeremption = value; }
            }

            // ==============================
            // Champs non encore renseignés
            // ==============================
            /// <summary>
            /// LMP  ??  
            /// </summary> 
            public static int LMP_LIGNE = 14;
            public static int LMP_COLONNE = 2;
            private string _lmp;
            public  string LMP
            {
                get { return _lmp; }
                set { _lmp = value; }
            }
            /// <summary>
            /// Après avoir ouvert le pot, le nombre de jours au bout desquels la peinture est péremptée 
            /// Non renseigné !!
            /// </summary>
            public static int DELTA_POT_OUVERT_VALIDE_LIGNE = 9;
            public static int DELTA_POT_OUVERT_VALIDE_COLONNE = 2;
            private int _NbJoursPeremption;
            public int NbJoursPeremption
            {
                get { return _NbJoursPeremption; }
                set { _NbJoursPeremption = value; }
            }

            // Fin description des champs
            // ==============================

            /// <summary>
            /// Ecriture des informations lues à partir du fichier excel   
            /// </summary> 
            public void WriteInfo(bool notifie)
            {
                string info = Environment.NewLine;

                string message = string.Format("Informations extraites du fichier excel");
                info += message + Environment.NewLine;

                message = string.Format("NomProduit:{0}", NomProduit);
                info += message + Environment.NewLine;

                message = string.Format("ReferenceProduit:{0}", ReferenceProduit);
                info += message + Environment.NewLine;

                message = string.Format("Fournisseur:{0}", Fournisseur);
                info += message + Environment.NewLine;

                message = string.Format("NumeroLot:{0}", NumeroLot);
                info += message + Environment.NewLine;

                message = string.Format("Teinte:{0}", Teinte);
                info += message + Environment.NewLine;

                message = string.Format("DateFabrication:{0}", DateFabrication.ToString("dd-MM-yyyy"));
                info += message + Environment.NewLine;

                message = string.Format("DatePeremption:{0}", DatePeremption.ToString("dd-MM-yyyy"));
                info += message + Environment.NewLine;

                message = string.Format("DateLivraison:{0}", DateLivraison.ToString("dd-MM-yyyy"));
                info += message + Environment.NewLine;

                message = string.Format("NbJoursPeremption:{0}", NbJoursPeremption);
                info += message + Environment.NewLine;

                message = string.Format("TemperatureStockageMin:{0}°C", TemperatureStockageMin);
                info += message + Environment.NewLine;

                message = string.Format("TemperatureStockageMax:{0}°C", TemperatureStockageMax);
                info += message + Environment.NewLine;

                message = string.Format("ConditionnementEnLitres:{0} Unite:{1}", ConditionnementEnLitres, UniteQuantite);
                info += message + Environment.NewLine;

                message = string.Format("NumeroECS:{0}", NumeroECS);
                info += message + Environment.NewLine;

                message = string.Format("NbTotalPots:{0}", NbTotalPots);
                info += message + Environment.NewLine;

                message = string.Format("LMP:{0}", LMP);
                info += message + Environment.NewLine;

                message = string.Format("Fin Informations extraites du fichier excel\n");
                info += message + Environment.NewLine;

                Log.Write(info, notifie);

            } // public void WriteInfo(bool notifie)


            /// <summary>
            /// Formatage des champs Texte
            /// </summary>
            static string FormateString(string champ, int max_length)
            {
                string res = "";
                try
                {
                    res = champ.Trim();
                    if (res.Length > max_length)
                    {
                        string previous = res;
                        res = res.Substring(0, max_length);
                        string message = string.Format("Information tronquée : {0} au lieu de {1}"
                                                       , previous
                                                       , res);
                        Log.Write(message, true);
                    }
                    res = res.ToUpper();
                }
                catch (Exception ex)
                {
                    string message = string.Format("Pb FormateString():{0} Exception:{1}"
                                                  , champ
                                                  , ex.Message);
                    MessageBox.Show(message);
                }

                return res;
            }

            /// <summary>
            /// Analyse des champs communs d'une feuille excel
            /// </summary>
            public void AnalyseChampsCommunsFeuilleExcel(Excel.Worksheet xlWorksheet, CultureInfo culture)
            {
                Excel.Range xlRange = xlWorksheet.UsedRange;
                int rowCount = xlRange.Rows.Count;
                int colCount = xlRange.Columns.Count;

                string data = "";
                try
                {
                    data = xlRange.Cells[FOURNISSEUR_LIGNE, FOURNISSEUR_COLONNE].Value.ToString();
                    Fournisseur = FormateString(data, FOURNISSEUR_MAX_LENGTH);
                }
                catch (Exception ex)
                {
                    string message = string.Format("Pb Fournisseur:{0}", ex.Message);
                    MessageBox.Show(message);
                }

                try
                {
                    // Analyse de la date de livraison
                    // La date de livraison est de la forme: "123456 DU 20/11/2012"
                    data = xlRange.Cells[DATE_LIVRAISON_LIGNE, DATE_LIVRAISON_COLONNE].Value.ToString();
                    string[] res = data.Split(new string[] { " DU " }, StringSplitOptions.None);
                    if (res != null)
                    {
                        string date_str = res[1];
                        DateLivraison = DateTime.Parse(date_str, culture, DateTimeStyles.NoCurrentDateDefault);
                    }
                    else
                    {
                        string message = string.Format("Date de livraison inconnue");
                        MessageBox.Show(message);
                    }
                }
                catch (Exception ex)
                {
                    string message = string.Format("Pb DateLivraison:{0}", ex.Message);
                    MessageBox.Show(message);
                }

                try
                {
                    // A extraire à partir de la forme: "Cond. en litres"
                    data = xlRange.Cells[UNITE_QUANTITE_LIGNE, UNITE_QUANTITE_COLONNE].Value.ToString();
                    string[] res = data.Split(new string[] { " en " }, StringSplitOptions.None);
                    if (res != null)
                    {
                        string unite = res[1];
                        UniteQuantite = unite.Substring(0, 1).ToUpper();
                    }
                    else
                    {
                        string message = string.Format("Unité inconnue");
                        MessageBox.Show(message);
                    }
                }
                catch (Exception ex)
                {
                    string message = string.Format("Pb UniteQuantite:{0}", ex.Message);
                    MessageBox.Show(message);
                }


            } // static public void AnalyseChampsCommunsFeuilleExcel


            /// <summary>
            /// Analyse d'une feuille excel
            /// </summary>
            static public void AnalyseFeuilleExcel(List<CExcelLivraisonPots> livraisons_pots, Excel.Worksheet xlWorksheet, CultureInfo culture)
            {
                Excel.Range xlRange = xlWorksheet.UsedRange;
                int rowCount = xlRange.Rows.Count;
                int colCount = xlRange.Columns.Count;

                // Création d'une livraison
                CExcelLivraisonPots livraison_pots = new CExcelLivraisonPots();

                livraison_pots.AnalyseChampsCommunsFeuilleExcel(xlWorksheet, culture);

                int num_ligne = 0;
                while (num_ligne >= 0)
                {
                    // Analyse des champs multilignes
                    // ==============================
                    string data = "";
                    // REFERENCE_PRODUIT
                    // ====================
                    try
                    {
                        data = xlRange.Cells[REFERENCE_PRODUIT_LIGNE + num_ligne, REFERENCE_PRODUIT_COLONNE].Value.ToString();
                        livraison_pots.ReferenceProduit = FormateString(data, REFERENCE_PRODUIT_MAX_LENGTH);
                    }
                    catch (Exception ex)
                    {
                        string message = string.Format("Pb ReferenceProduit:{0}", ex.Message);
                        MessageBox.Show(message);
                    }
                    // NOM_PRODUIT_LIGNE
                    // ====================
                    try
                    {
                        data = xlRange.Cells[NOM_PRODUIT_LIGNE + num_ligne, NOM_PRODUIT_COLONNE].Value.ToString();
                        livraison_pots.NomProduit = FormateString(data, NOM_PRODUIT_MAX_LENGTH);
                    }
                    catch (Exception ex)
                    {
                        string message = string.Format("Pb NomProduit:{0}", ex.Message);
                        MessageBox.Show(message);
                    }
                    // NUMERO_ECS
                    // ====================
                    try
                    {
                        string numero_ECS = xlRange.Cells[NUMERO_ECS_LIGNE + num_ligne, NUMERO_ECS_COLONNE].Value.ToString();
                        string[] res = numero_ECS.Split(new string[] { "." }, StringSplitOptions.None);
                        if (res.Length > 1)
                        {
                            int index = 0;
                            numero_ECS = "";
                            while (index < res.Length)
                            {
                                numero_ECS = numero_ECS + res[index];
                                index += 1;
                            }
                        }
                        Check.MinLength(numero_ECS, "NumeroECS", NUMERO_ECS_MAX_LENGTH, ref numero_ECS);
                        Check.MaxLength(numero_ECS, "NumeroECS", NUMERO_ECS_MAX_LENGTH, ref numero_ECS);
                        livraison_pots.NumeroECS = FormateString(numero_ECS, NUMERO_ECS_MAX_LENGTH);
                    }
                    catch (Exception ex)
                    {
                        string message = string.Format("Pb NumeroECS:{0}", ex.Message);
                        MessageBox.Show(message);
                    }
                    // TEINTE
                    // ====================
                    try
                    {
                        data = xlRange.Cells[TEINTE_LIGNE + num_ligne, TEINTE_COLONNE].Value.ToString();
                        livraison_pots.Teinte = FormateString(data, TEINTE_MAX_LENGTH);
                    }
                    catch (Exception ex)
                    {
                        string message = string.Format("Pb Teinte:{0}", ex.Message);
                        MessageBox.Show(message);
                    }
                    // TEMPERATURE_STOCKAGE (min,max)
                    // ==============================
                    try
                    {
                        // Les valeurs sont à extraire à partir de la forme: "5-30" ou "-2-25"
                        string temperatures_min_max = xlRange.Cells[TEMPERATURE_STOCKAGE_LIGNE + num_ligne, TEMPERATURE_STOCKAGE_COLONNE].Value.ToString();
                        string[] res = temperatures_min_max.Split(new string[] { "-" }, StringSplitOptions.None);
                        if (res != null)
                        {
                            int count = res.GetLength(0);
                            string temperature_min = res[count-2];
                            string temperature_max = res[count-1];
                            livraison_pots.TemperatureStockageMin = Convert.ToDecimal(temperature_min);
                            livraison_pots.TemperatureStockageMax = Convert.ToDecimal(temperature_max);

                            if (count == 3)
                            {
                                // Cas invraisemblable où une température min est négative !
                                livraison_pots.TemperatureStockageMin *= -1;
                            }
                        }
                        else
                        {
                            string message = string.Format("Températures min/max inconnues");
                            MessageBox.Show(message);
                        }
                    }
                    catch (Exception ex)
                    {
                        string message = string.Format("Pb Temperatures min/max de stockage:{0}", ex.Message);
                        MessageBox.Show(message);
                    }
                    // QUANTITE_PRODUIT
                    // ====================
                    try
                    {
                        data = xlRange.Cells[COND_EN_LITRES_LIGNE + num_ligne, COND_EN_LITRES_COLONNE].Value.ToString();
                        livraison_pots.ConditionnementEnLitres = Convert.ToInt32(data);
                    }
                    catch (Exception ex)
                    {
                        string message = string.Format("Pb ConditionnementEnLitres:{0}", ex.Message);
                        MessageBox.Show(message);
                    }
                    // [NB_TOTAL_POTS
                    // ====================
                    try
                    {
                        data = xlRange.Cells[QUANTITE_NB_TOTAL_POTS_LIGNE + num_ligne, QUANTITE_NB_TOTAL_POTS_COLONNE].Value.ToString();
                        livraison_pots.NbTotalPots = Convert.ToInt32(data);
                    }
                    catch (Exception ex)
                    {
                        string message = string.Format("Pb NbTotalPots:{0}", ex.Message);
                        MessageBox.Show(message);
                    }
                    // [NUMERO_LOT
                    // ====================
                    try
                    {
                        data = xlRange.Cells[NUMERO_LOT_LIGNE + num_ligne, NUMERO_LOT_COLONNE].Value.ToString();
                        livraison_pots.NumeroLot = FormateString(data, NUMERO_LOT_MAX_LENGTH);
                    }
                    catch (Exception ex)
                    {
                        string message = string.Format("Pb NumeroLot:{0}", ex.Message);
                        MessageBox.Show(message);
                    }
                    // DATE_FABRICATION
                    // ====================
                    string date_str = "";
                    try
                    {
                        date_str = xlRange.Cells[DATE_FABRICATION_LIGNE + num_ligne, DATE_FABRICATION_COLONNE].Value.ToString();
                        livraison_pots.DateFabrication = DateTime.Parse(date_str, culture, DateTimeStyles.NoCurrentDateDefault);
                    }
                    catch (Exception ex)
                    {
                        string message = string.Format("Pb DateFabrication:{0}", ex.Message);
                        MessageBox.Show(message);
                    }
                    // DATE_PEREMPTION
                    // ====================
                    try
                    {
                        date_str = xlRange.Cells[DATE_PEREMPTION_LIGNE + num_ligne, DATE_PEREMPTION_COLONNE].Value.ToString();
                        livraison_pots.DatePeremption = DateTime.Parse(date_str, culture, DateTimeStyles.NoCurrentDateDefault);
                    }
                    catch (Exception ex)
                    {
                        string message = string.Format("Pb DatePeremption:{0}", ex.Message);
                        MessageBox.Show(message);
                    }


                    // Champs absents de la feuille excel
                    // ==================================

                    // Pour l'instant fixé à 30 jours
                    livraison_pots.NbJoursPeremption = 30;
                    livraison_pots.LMP = "LMP";

                    /*
                    try
                    {                  
                        data = xlRange.Cells[DELTA_POT_OUVERT_VALIDE_LIGNE, DELTA_POT_OUVERT_VALIDE_COLONNE].Value.ToString();
                        livraison_pots.NbJoursPeremption = Convert.ToInt32(data);
                    }
                    catch (Exception ex)
                    {
                        string message = string.Format("Pb NbJoursPeremption:{0}", ex.Message);
                        MessageBox.Show(message);
                    }
                     * */

                    // Ajout de la livraison courante 
                    livraisons_pots.Add(livraison_pots);

                    // On regarde si il y a une ligne de plus (i.e une livraison de plus)
                    num_ligne += 1;
                    try
                    {
                        string next_ligne = xlRange.Cells[REFERENCE_PRODUIT_LIGNE + num_ligne, REFERENCE_PRODUIT_COLONNE].Value.ToString();
                        CExcelLivraisonPots new_livraison_pots = new CExcelLivraisonPots(livraison_pots);
                        livraison_pots = new_livraison_pots;
                    }
                    catch (Exception)
                    {
                        // On arrete
                        num_ligne = -1;
                    }

                } // while (num_ligne > 0)

            } // static public void  AnalyseFeuilleExcel()




            /// <summary>
            /// Lecture du fichier excel
            /// 
            /// - http://dontbreakthebuild.com/2011/01/30/excel-and-c-interop-with-net-4-how-to-read-data-from-excel/
            /// - http://stackoverflow.com/questions/1051464/excel-interop-worksheet-or-worksheet
            /// </summary>
            public static List<CExcelLivraisonPots> Read(string full_path_excel)
            {
                string excel_filename = full_path_excel; 
                if (!File.Exists(excel_filename))
                {
                    return null;
                }

                List<CExcelLivraisonPots> livraisons_pots = new List<CExcelLivraisonPots>();
                CultureInfo culture_fr = new CultureInfo("fr"); 
                CultureInfo culture_en = new CultureInfo("en-Gb");
                CultureInfo culture = culture_fr;


                Excel.Application xlApp = null;
                Excel.Workbook xlWorkbook =null;
                Excel.Worksheet xlWorksheet = null;
                try
                {
                    xlApp = new Excel.Application { Visible = false };

                    xlApp.DisplayAlerts = false;

                    xlWorkbook = xlApp.Workbooks.Open(excel_filename);

                    xlWorksheet = xlWorkbook.Sheets[1];
                    Excel.Range xlRange = xlWorksheet.UsedRange;
                    int rowCount = xlRange.Rows.Count;
                    int colCount = xlRange.Columns.Count;

                    int nb_sheets = xlWorkbook.Sheets.Count;
                    NbFeuillesExcel = 1;

                    string data = "";
                    // Analyse de la donnée nécessaire au traitement des livraisons
                    // Le nombre de feuilles excel 
                    try
                    {
                        // "Nombre de feuilles : 1"
                        data = xlRange.Cells[NB_FEUILLES_EXCEL_LIGNE, NB_FEUILLES_EXCEL_COLONNE].Value.ToString();
                        string[] res = data.Split(new string[] { ":" }, StringSplitOptions.None);
                        if (res != null)
                        {
                            data = res[1];
                            NbFeuillesExcel = Convert.ToInt32(data);
                        }
                        else
                        {
                            string message = string.Format("NbFeuillesExcel inconnue");
                            MessageBox.Show(message);
                        }
                    }
                    catch (Exception ex)
                    {
                        string message = string.Format("Pb NbFeuillesExcel:{0}", ex.Message);
                        // MessageBox.Show(message);
                    }

                    int indice_feuille = 1;
                    
                    while (indice_feuille <= NbFeuillesExcel)
                    {
                        xlWorksheet = xlWorkbook.Sheets[indice_feuille];
                        AnalyseFeuilleExcel(livraisons_pots, xlWorksheet, culture);

                        indice_feuille += 1;
                    }
                }
                catch (Exception ex)
                {
                    string message = string.Format("Pb LMP:{0}", ex.Message);
                    MessageBox.Show(message);
                }
                finally
                {
                    // Fermeture de la feuille Excel 
                    // Il faut laisser le temps à Excel de partir; sans cela ca plante tout simplement.
                    // Emploi de GC.collect() http://www.developpez.net/forums/d11288/dotnet/developpement-windows/windows-forms/csharp-excel-liberer-processus/

                    if (xlWorksheet != null)
                    {
                        // http://social.msdn.microsoft.com/Forums/vstudio/en-us/0a702996-cbe4-4086-b248-74793f297f13/microsoft-excel-object-library
                        Marshal.FinalReleaseComObject(xlWorksheet);
                    }

                    if (xlWorkbook != null)
                    {
                        xlWorkbook.Close();
                        Marshal.ReleaseComObject(xlWorkbook);
                        xlWorkbook = null;
                        Thread.Sleep(1000);
                    }

                    Thread.Sleep(1000);
                    if (xlApp != null)
                    {
                        // Fermeture de l'application excel
                        xlApp.Quit();
                        Marshal.ReleaseComObject(xlApp);
                        Thread.Sleep(1000);
                        xlApp = null;
                    }
                    GC.Collect();
                    GC.WaitForPendingFinalizers();
                    GC.Collect();
                    GC.WaitForPendingFinalizers();
                }


                if (livraisons_pots.Count == 0)
                    livraisons_pots = null;

                return livraisons_pots;
            }

        } // static public class LivraisonPots


    } // namespace Eurocopter

    /**
        fin Excel

    @}

    */


