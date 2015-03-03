
.. index::
   ! State Machine
   pair: State ; Machine
   pair: Machine; Etat
   pair: State Machine; Alan Cox

.. _state_machine:

==============
state machine
==============


.. seealso::

   - http://linuxfr.org/news/pourquoi-les-developpeurs-n-utilisent-pas-plus-de-machines-a-etat


Qt state machine
================

.. toctree::
   :maxdepth: 2

   qt_state_machine
   qt_quick_transition
   python_fsm_state_machine



.. contents::
   :depth: 3

Articles
========


Alan Cox
---------

.. seealso::

   - http://lkml.indiana.edu/hypermail/linux/kernel/0001.2/1335.html


::

    > the IBM paper), that if your application depends on huge numbers of
    > threads, you're always going to keep bumping up against the scheduler?
    > a lot of people throw lots of threads at a problem and it can really
    > be bad design.

That is the least of your worry. 1000 threads is 8Mb of kernel stacks, and
enough switching of tasks to be sure you might as well turn most of your
cache off. A computer is a state machine. Threads are for people who cant
program state machines.

There are plenty of cases Linux is most definitely not helping the situation
notably asynchronous block I/O.

Alan


Pourquoi les développeurs n'utilisent pas plus de machines à état ?
-------------------------------------------------------------------

.. seealso::

   - http://linuxfr.org/news/pourquoi-les-developpeurs-n-utilisent-pas-plus-de-machines-a-etat
   - http://www.shopify.com/technology/3383012-why-developers-should-be-force-fed-state-machines


Les langages de programmations, de quelques paradigmes qu'ils soient (bien qu'un
peu moins pour le paradigme logique), sont basés sur le concept de liste
d'instructions exécutées à la suite par la machine.

La machine exécutant ce code est une machine à état, mais le programme n'est pas
formellement pensé comme tel.

Les machines à état semblent pourtant un bon outil pour la programmation des
logiciels que nous avons l'habitude de développer : facile à dessiner sur papier,
permettant un découpage clair du fonctionnement de l'application.

Sans compter qu'une machine à état se patche plus facilement qu'un code classique
où l'effet spaghetti peut vite impliquer des effets indésirables.

Les designers de Qt l'ont bien compris en permettant de définir des machines à
état pour décrire le comportement du contrôleur.

C'est pourquoi certains se sont demandés si la programmation en machine à état
ne devrait pas être plus pratiquée et aimée des programmeurs.

C'est, par exemple, ce que se demande Willem van Bergen, carrément enthousiaste_.
Celui-ci pense que c'est le stockage de l'historique qui est essentiel.


.. _enthousiaste:  http://www.shopify.com/technology/3383012-why-developers-should-be-force-fed-state-machines



