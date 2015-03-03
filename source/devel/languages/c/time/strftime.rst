

.. index::
   pair: C time; strftime


.. _strftime:

==========================
strftime c time function
==========================


.. seealso::

   - :ref:`strptime`
   - http://manpagesfr.free.fr/man/man3/strftime.3.html

.. contents::
   :depth: 3

Signature
=========




.. c:function:: size_t strftime(char *s, size_t max, const char *format, const struct tm *tm);




Tutorials
=========


.. seealso:: http://www.bien-programmer.fr/time.htm



Afficher l'heure courante
============================


L'affichage de la date ou de l'heure de fait grace à la fonction strftime() qui
a été conçue pour ça.

Elle attend l'adresse d'une structure tm, qu'il va donc falloir mettre à jour au
préalable. On utilise pour ça la valeur retournée par time(), qui donne la
datation courante sous la forme d'un entier et une des fonction localtime() ou
gmtime() selon que l'on veut convertir en heure locale ou en heure GMT (Greenwich).

En France, il y a une heure de différence.

L'usage précis de strftime() et de ses nombreux paramètres de formatage doit
être étudié dans un document de référence.


::


    #include <stdio.h>
    #include <time.h>

    int main (void)
    {
       /* lire l'heure courante */
       time_t now = time (NULL);

       /* la convertir en heure locale */
       struct tm tm_now = *localtime (&now);

       /* Creer une chaine JJ/MM/AAAA HH:MM:SS */
       char s_now[sizeof "JJ/MM/AAAA HH:MM:SS"];

       strftime (s_now, sizeof s_now, "%d/%m/%Y %H:%M:%S", &tm_now);

       /* afficher le resultat : */
       printf ("'%s'\n", s_now);

       return 0;
    }


Resultat
--------

::

    '29/01/2009 02:34:00'
    Process returned 0 (0x0)   execution time : 0.054 s
    Press any key to continue.












