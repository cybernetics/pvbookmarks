

.. index::
   ! Exceptions


.. _exceptions:

=======================
Exceptions
=======================

.. seealso::

   - http://fr.wikipedia.org/wiki/Syst%C3%A8me_de_gestion_d%27exceptions


.. contents::
   :depth: 3

Introduction
============

Dans le contexte des langages de programmation fonctionnels et impératifs, un
système de gestion d'exceptions ou SGE permet de gérer les conditions
exceptionnelles pendant l'exécution du programme.

Lorsqu'une exception se produit, l'exécution normale du programme est
interrompue et l'exception est traitée.

L'utilisation des gestionnaires d'exceptions s'est généralisée sur PC avec
l'utilisation du mode protégé sous DOS puis avec les systèmes d'exploitation
multitâches.

Auparavant, une erreur de programmation pouvait facilement aboutir à un
plantage du programme voire de l'ordinateur.

Les erreurs/exceptions les plus courantes sont probablement l'accès non
autorisé à une zone mémoire (erreur de manipulation de pointeur) et la
division par zéro (on ne prévoit pas le cas où le diviseur est nul)


Meilleures pratiques pour la gestion des exceptions
===================================================

.. seealso::

   - http://msdn.microsoft.com/fr-fr/library/seyhszts%28v=vs.100%29.aspx


Un jeu de blocs de code de gestion d'erreurs correctement conçu peut rendre un
programme plus robuste et moins enclin aux blocages dus à la gestion de ces
erreurs par l'application.

La liste suivante contient des suggestions relatives aux meilleures pratiques
pour la gestion des exceptions :

- Déterminez quand vous devez définir un bloc try/catch. Par exemple, vous
  pouvez vérifier par programmation la présence d'une condition qui risque
  probablement de se produire sans le recours à la gestion des exceptions.
  Dans d'autres situations, l'utilisation de la gestion des exceptions pour
  intercepter un cas d'erreur est appropriée.

L'exemple suivant utilise une instruction if pour déterminer si une connexion
est fermée. Vous pouvez utiliser cette méthode au lieu de lever une exception
si la connexion n'est pas fermée.

::

    if (conn.State != ConnectionState.Closed)
    {
        conn.Close();
    }


::

    try
    {
        conn.Close();
    }
    catch (InvalidOperationException ex)
    {
        Console.WriteLine(ex.GetType().FullName);
        Console.WriteLine(ex.Message);
    }


La méthode que vous choisissez dépend de la fréquence à laquelle l'événement
se produit.

**Si l'événement est véritablement exceptionnel** et constitue une erreur (par
exemple une fin de fichier inattendue), l'utilisation de la gestion des
exceptions est plus indiquée car la quantité de code exécutée en situation
normale est moindre.

**Si l'événement se produit régulièrement, l'utilisation de la méthode par
programmation pour rechercher les erreurs est plus appropriée**.

En ce cas, si une exception se produit, la gestion de l'exception prendra plus
de temps.

- Utilisez des blocs try/finally autour du code pouvant potentiellement
  générer une exception et centralisez vos instructions catch en un point unique.
  De cette façon, l'instruction try génère l'exception, l'instruction finally
  ferme ou libère des ressources et l'instruction catch gère l'exception à
  partir d'un point central.

- Veillez à toujours classer les exceptions dans les blocs catch de la plus
  spécifique à la moins spécifique. Cette technique permet de gérer l'exception
  spécifique avant qu'elle ne passe à un bloc catch plus général.

- Terminez les noms de classes d'exception par le mot « Exception ».
  Par exemple::

    public class MyFileNotFoundException : Exception
    {
        ;
    }



Implémentation des exceptions
==============================


.. toctree::
   :maxdepth: 4

   csharp/index

