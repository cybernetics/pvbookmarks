

.. index::
   pair: Sqlite;  C♯
   
   

.. _bac_melange_csharp:

========================
Exemple bac_melange  C♯
========================

.. contents::
   :depth: 3



Creation
=========

::

    /// <summary>
    /// Données concernant un tag mélange
    /// </summary>
    public class CBacMelange
    {
        [AutoIncrement, PrimaryKey]
        public int id { get; set; }

        // Les dates dans la base sont au format UTC
        public DateTime date_fabrication { get; set; }
        [IgnoreAttribute]
        public DateTime DateFabrication_AnneeMoisJour 
        {
            get 
            {
                //DateTime date_fab_locale = date_fabrication.ToLocalTime();
                //DateTime date_annee_mois_jour = new DateTime(date_fab_locale.Year, date_fab_locale.Month, date_fab_locale.Day, 0, 0, 0);

                return date_fabrication;//date_annee_mois_jour; 
            }
            set 
            {
                DateTime date_fab_universelle = value.ToUniversalTime();
                DateTime date_annee_mois_jour = new DateTime(date_fab_universelle.Year, date_fab_universelle.Month, date_fab_universelle.Day
                                                            , date_fab_universelle.Hour, date_fab_universelle.Minute, 0);

                date_fabrication = value;// date_annee_mois_jour; 
            } 
        }

        public int minutes_date_fabrication { get; set; }
        public int temps_de_murissement { get; set; }
        public int duree_de_vie { get; set; }
        public int code_vacation { get; set; }
        public int numero_melange_vacation { get; set; }
        [MaxLength(5)]
        public string nom_melange { get; set; }
        public int viscosite { get; set; }
        public int temperature { get; set; }
        [MaxLength(10)]
        public string matricule_operateur { get; set; }
        public int lmp { get; set; }
        public int traite { get; set; }

        /// <summary>
        /// Constructeur
        /// </summary>
        public CBacMelange()
        {
            ;
        }

        /// <summary>
        /// Constructeur
        /// </summary>
        public CBacMelange(TagRFIDMelange tagMelange)
        {
            nom_melange = tagMelange.NomMelange;
            DateFabrication_AnneeMoisJour = tagMelange.DateFabrication;
            minutes_date_fabrication = tagMelange.MinutesDateFabrication;
            temps_de_murissement = tagMelange.TempsDeMurissement;
            duree_de_vie = tagMelange.DureeDeVie;
            code_vacation = tagMelange.CodeVacation;
            numero_melange_vacation = tagMelange.NumeroMelangeVacation;
            viscosite = tagMelange.Viscosite;
            temperature = (int)tagMelange.Temperature;
            matricule_operateur = tagMelange.MatriculeOperateur;

            lmp = tagMelange.LMP ? 1 : 0;
        }
    }


Recherche 
==========

::

    // On cherche le mélange dans la base de données
    // Attention: dans le tag -> date à la mn près; dans la DB -> date à la seconde près
    SQLite.TableQuery<CBacMelange> tableMelanges = DB_Eurocopter.Database.Table<CBacMelange>();

    CBacMelange dbMelange = null;
    foreach (CBacMelange melange in tableMelanges)
    {
        if (melange.nom_melange == tagMelange.NomMelange)
        {
            DateTime dateDB = melange.date_fabrication.AddSeconds(-melange.date_fabrication.Second);
            if (tagMelange.DateFabrication.CompareTo(dateDB) == 0)
            {
                dbMelange = melange;
                break;
            }
        }
    }
