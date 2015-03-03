

.. index::
   cli (useradd)
   cli (usermod)
   cli (groups)


.. _gnu_linux_groups:

==================================
Gestion des groupes sous GNU/Linux
==================================


Ajouter un utilisateur à un groupe sous GNU/Linux
=================================================

.. seealso:: http://blog.nicolargo.com/2011/10/ajouter-un-utilisateur-a-un-groupe-sous-gnulinux.html


Petit pense-bête à usage intern(et): gérer les utilisateurs dans ses groupes
sous GNU/Linux et en ligne de commande.

Modification du groupe primaire d'un utilisateur
------------------------------------------------

Pour changer le groupe primaire de l'utilisateur nicolargo à admin, il suffit
d'utiliser la commande usermod::

    usermod -g admin nicolargo

Ajout d'un groupe secondaire à un utilisateur existant
------------------------------------------------------

Pour ajouter un groupe secondaire networkadmin à un utilisateur existant nicolargo,
c'est encore la commande usermod qu'il faut utiliser::

    usermod -a -g networkadmin nicolargo

Ajout d'un nouvel utilisateur à un groupe primaire
--------------------------------------------------

Pour ajouter le nouvel utilisateur ritchy et lui configurer un comme groupe
primaire admin, il suffit d'utiliser la commande useradd:

    useradd -g admin nicolargo

Ajout d'un nouvel utilisateur à un groupe secondaire
----------------------------------------------------

Pour ajouter le nouvel utilisateur ritchy et lui configurer un comme groupe
secondaire networkadmin, il suffit d'utiliser la commande useradd::

    useradd -G networkadmin nicolargo

A noter qu'il est possible d'utiliser l'option -G avec plusieurs groupes.

Exemples pour ajouter ritchy au groupe secondaire networkadmin et systemadmin::

    useradd -G networkadmin,systemadmin nicolargo


Vérifier les groupes associés à un utilisateur
----------------------------------------------

Rien de plus simple avec la commande groups::

    groups ritchy


::

    ritchy: networkadmin systemadmin


















