

.. index::
   pair: C♯; before tuple


====================
example before tuple
====================


If we have a version of C♯ < 4.0 we have to use classes.


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




