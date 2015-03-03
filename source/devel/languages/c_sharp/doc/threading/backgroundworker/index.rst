

.. index::
   pair: C♯ threading; backgroundworker



.. _csharp_threading_backgroundworker:

=============================
C♯ threading backgroundworker
=============================


.. seealso::

   - http://msdn.microsoft.com/fr-fr/library/system.componentmodel.backgroundworker.aspx
   - http://webman.developpez.com/articles/dotnet/introbackroundworker/
   - http://www.dotnetperls.com/backgroundworker


.. contents::
   :depth: 3

Notes
=====

La classe :class:`BackgroundWorker` vous permet d'exécuter une opération sur un
thread séparé, dédié.


Les opérations longues comme les téléchargements et les transactions de base de
données peuvent vous donner l'impression que votre interface utilisateur a cessé
de répondre au cours de leur exécution.

Si vous souhaitez une interface utilisateur réactive et êtes confronté à de
longs délais associés à ce type d'opérations, la classe BackgroundWorker fournit
une solution pratique.

Pour exécuter une longue opération en arrière-plan, créez un objet
BackgroundWorker et écoutez les événements qui indiquent la progression de
votre opération et lorsque celle-ci se termine.



.. warning:: Veillez à ne pas manipuler d'objets interface utilisateur dans votre
   gestionnaire d'événements DoWork. À la place, communiquez à l'interface
   utilisateur via les événements ProgressChanged et RunWorkerCompleted.


Utilisation du background worker
================================

Le background worker est un composant que l'on peut utiliser indifféremment de
manière graphique par glisser/déposer sur un formulaire Windows par exemple ou
alors en le déclarant directement dans le code.

Instanciation d'un Background worker
------------------------------------

::

    BackgroundWorker bgw1 = new BackgroundWorker();

    bgw1.DoWork += new DoWorkEventHandler(bgw1_DoWork);
    bgw1.ProgressChanged += new ProgressChangedEventHandler(bgw1_ProgressChanged);
    bgw1.RunWorkerCompleted += new RunWorkerCompletedEventHandler(bgw1_RunWorkerCompleted);

Après avoir instancié le background worker il suffit d'appeler la méthode
:meth:`RunWorkerAsync` pour lancer le traitement asynchrone, cela signifie que le code
associé est exécuté dans un thread dédié et qu'il ne provoque donc pas un
blocage ou un ralentissement de l'affichage et des traitements du thread
principal.


La méthode :meth:`RunWorkerAsync` prend un paramètre qui est de type object, cela
laisse donc le loisir de passer ce que l'on veut au thread qui exécutera le code.

Nous verrons plus tard dans ce tutoriel comment récupérer un résultat.

Le composant background worker possède 3 évènements qui vont nous servir:

- à placer le code que l'on souhaite exécuter,
- à détecter la progression
- ainsi que la fin de cette exécution.

Il faut s'abonner à ces 3 évènements pour pouvoir tirer parti du composant.


Propriétés
==========

CancellationPending
-------------------

Obtient une valeur qui indique si l'application a demandé l'annulation d'une
opération d'arrière-plan


IsBusy
-------

Obtient une valeur qui indique si BackgroundWorker exécute une opération
asynchrone.


WorkerReportsProgress
---------------------

Obtient ou définit une valeur qui indique si BackgroundWorker peut signaler des
mises à jour de progression.


WorkerSupportsCancellation
--------------------------

Obtient ou définit une valeur qui indique si BackgroundWorker prend en charge
l'annulation asynchrone.


Méthodes
========


CancelAsync
-----------

Demande l'annulation d'une opération d'arrière-plan en attente.


RunWorkerAsync()
----------------

Démarre l'exécution d'une opération d'arrière-plan.


RunWorkerAsync(Object)
----------------------


Démarre l'exécution d'une opération d'arrière-plan.


ReportProgress(Int32)
----------------------

Déclenche l'événement ProgressChanged.


ReportProgress(Int32, Object)
------------------------------

Déclenche l'événement ProgressChanged.


Evénements
===========

DoWork
------

Se produit lorsque RunWorkerAsync est appelé.


ProgressChanged
----------------

Se produit lorsque ReportProgress est appelé.


::

    // This event handler updates the progress bar.
    private void backgroundWorker1_ProgressChanged(object sender,
        ProgressChangedEventArgs e)
    {
        this.progressBar1.Value = e.ProgressPercentage;
    }

RunWorkerCompleted
-------------------

Se produit lorsque l'opération d'arrière-plan est terminée, a été annulée ou a
levé une exception.




.. _backgroundworker_examples:

backgroundworker Examples
=========================

.. toctree::
   :maxdepth: 4

   example_1
   example_2

