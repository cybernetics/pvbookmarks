
.. index::
   DVCS repositories

==========================
Remarks about repositories
==========================


::

    de  Sebastien Douche <sdouche@gmail.com>
    heure de l'expéditeur   Envoyé à 14:07 (GMT+02:00). Heure locale : 15:13. ✆
    répondre à  gitfr@googlegroups.com
    à   gitfr@googlegroups.com
    cc  Pierre8r <pierre8r-gg@yahoo.fr>
    date    30 mars 2011 14:07
    objet   Re: Est-il conseiller de créer un repository par projet, ou un repository pour l'ensemble des projets ?


::

    > Est-il conseiller de créer un repository par projet ou un repository
    > pour l'ensemble des projets ?

Faire un repos pour tout est pour moi une hérésie et doit être banni.

Même avec SVN, la convention est de faire les répertoires trunk, tags
et branches à la racine, mais par fainéantise (et parce que SVN permet
le checkout partiel), tout est dans un seul dépôt.

Avoir plusieurs projets dans un seul dépôt possède plusieurs inconvénients
majeurs :

- le dépôt risque de devenir obèse
  On ne peut pas cloner un bout de repos, c'est tout ou rien. Les
  commandes vont ralentir vu la taille du working dir.

- un historique incohérent
  Des commits sans relation entre eux, des multiples tags (comment vous
  allez tagger le projet X en 0.2 et le projet Y en 1.3 ?)[1].

- une profusion de branches
  Qui va géner la compréhension

- des développeurs qui commitent tous au même endroit
  Vive le bordel.

Et vu les lacunes de Hg dans la gestion des branches par rapport à
Git, c'est encore plus important de le faire comme cela.

Le seul défaut des dépôts multiples est la gestion qui doit suivre :
administration (création, acl, backup) et obligation d'utiliser un
outil "projet".

Comment résoudre ce dernier point :

- git submodule peut être suffisant
- utiliser un outil comme repo, développer par des Javaistes pour le
  projet Android.
- utiliser Maven, Grails...

En Python, j'utilise Buildout (outil projet comme Maven) et Buildbot
(outil ci comme Jenkins) et quelques scripts maison pour manipuler les
répos.

Mais ca dépend aussi de ce que vous appelez "projet" :).


[1] obligé d'utiliser les namespaces









