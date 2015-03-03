

.. _example2_csharp_sortedidctionary:

==================================
Initialisation d'un dictionnaire
==================================


.. contents::
   :depth: 3


Définition d'une classe TupleCourantAntenne_Distance
====================================================


::


    public class TupleCourantAntenne_Distance
    {
        public double m_CourantAntenne;   // en ampère-mètre crête
        public double m_DistanceElevation; // en cm

        /// <summary>
        /// constructor TupleCourantAntenne_Distance.
        /// </summary>
        public TupleCourantAntenne_Distance(double courantAntenne, double distanceElevation)
        {
            m_CourantAntenne    = courantAntenne;
            m_DistanceElevation = distanceElevation;
        }
    }


Déclaration d'un dictionnaire dans une classe
===============================================

::


    public partial class EstimateZ_Form : Form
    {
        // Storing the list of data collected
        // A data is a tuple of 2 measures:
        // - antenna electric current
        // - elevation distance

        public SortedDictionary<int, TupleCourantAntenne_Distance> m_DataCollected;
        public TupleCourantAntenne_Distance this[int index]
        {
            get { return m_DataCollected[index]; }
        }

        // Nombre de mesures collectées
        // Doit être égal au nombre d'élévations
        public int NbMesures
        {
            get { return m_DataCollected.Count; }
        }


                /// <summary>
        /// Initialisation du formulaire.
        /// </summary>
        void InitForm(ref FedmIscReader i_reader)
        {
            InitializeComponent();

            // ...

            m_DataCollected = new SortedDictionary<int, TupleCourantAntenne_Distance>();

            // ..

        }

        void CloseWindowZForm()
        {
            m_DataCollected.Clear();
            this.Close();
        }

Utilisation d'un indexeur
-------------------------

::

    public TupleCourantAntenne_Distance this[int index]
    {
        get { return m_DataCollected[index]; }
    }


Insertion d'éléments dans le dictionnaire
==========================================

::


    public void test_algo_1()
    {

        TupleCourantAntenne_Distance tuple_1 = new TupleCourantAntenne_Distance(1.05, 60);
        TupleCourantAntenne_Distance tuple_2 = new TupleCourantAntenne_Distance(1.45, 72.2);
        TupleCourantAntenne_Distance tuple_3 = new TupleCourantAntenne_Distance(1.85, 82.3);
        TupleCourantAntenne_Distance tuple_4 = new TupleCourantAntenne_Distance(2.02, 86.2);
        TupleCourantAntenne_Distance tuple_5 = new TupleCourantAntenne_Distance(2.13, 88.6);
        TupleCourantAntenne_Distance tuple_6 = new TupleCourantAntenne_Distance(2.52, 96);
        TupleCourantAntenne_Distance tuple_7 = new TupleCourantAntenne_Distance(2.64, 98.2);
        TupleCourantAntenne_Distance tuple_8 = new TupleCourantAntenne_Distance(3.00, 104.2);


        // à la première non détection, les valeurs de courant d'antenne et de
        // distance d'élévation sont acquises
        m_DataCollected[0] = tuple_1;
        m_DataCollected[1] = tuple_2;
        m_DataCollected[2] = tuple_3;
        m_DataCollected[3] = tuple_4;
        m_DataCollected[4] = tuple_5;
        m_DataCollected[5] = tuple_6;
        m_DataCollected[6] = tuple_7;
        m_DataCollected[7] = tuple_8;

        int ncz = 0;
        m_algo_estimate_Z.calculer_profondeur(ref m_profestimee, ref m_nivhestimee, ref ncz);
    }


