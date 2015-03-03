

.. index::
   pair: C time; strptime


.. _strptime:

==========================
strptime c time function
==========================

.. seealso::

   - :ref:`strftime`
   - http://manpagesfr.free.fr/man/man3/strptime.3.html
   - http://stackoverflow.com/questions/321849/strptime-equivalent-on-windows
   - http://social.msdn.microsoft.com/forums/en-US/vcgeneral/thread/25a654f9-b6b6-490a-8f36-c87483bb36b7


.. contents::
   :depth: 3

Signature
==========

.. c:function:: char *strptime(const char *s, const char *format, struct tm *tm);


Description
============



La fonction strptime() est complémentaire de la fonction strftime(3).
Elle convertit la chaîne de caractères pointée par buf en une valeur qui est
stockée dans la structure tm pointée par l'argument tm, la conversion étant
réalisée en suivant les indications contenues dans la chaîne format.

Cette dernière contient des descripteurs de champs et du texte, rappelant scanf(3).
Chaque descripteur consiste en un caractère % suivi d'un second caractère
indiquant le champ à interpréter.

Tous les autres sont considérés comme du texte, qui doit être présent dans la
chaîne fournie en entrée. Toutefois une espace blanche se trouvant dans la
chaîne de format peut être mise en correspondance avec zéro ou plusieurs
espaces. Il devrait toujours y avoir une espace ou un autre caractère
alphanumérique entre deux descripteurs de champs.

La fonction strptime() traite la chaîne d'entrée de gauche à droite.
Les trois types d'éléments d'entrée possibles (espace, caractère littéral,
conversion) sont manipulés l'un après l'autre.

Si l'entrée ne peut pas être mise en correspondance avec la chaîne de format,
la fonction s'arrête.

Le reste du format et de la chaîne d'entrée ne sont pas traités.


Exemple
=======

L'exemple suivant montre l'utilisation de strptime() et strftime(3).

::


    #define _XOPEN_SOURCE
    #include <stdio.h>
    #include <stdlib.h>
    #include <time.h>

    int
    main(void)
    {
        struct tm tm;
        char buf[255];

        strptime("2001-11-12 18:31:01", "%Y-%m-%d %H:%M:%S", &tm);
        strftime(buf, sizeof(buf), "%d %b %Y %H:%M", &tm);
        puts(buf);
        exit(EXIT_SUCCESS);
    }



Resultat
--------

::

    '29/01/2009 02:34:00'
    Process returned 0 (0x0)   execution time : 0.054 s
    Press any key to continue.











