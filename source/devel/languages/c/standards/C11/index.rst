

.. index::
   pair: C ; C11 standard
   ! C11

.. _c11_standard:

===================
C11 standard (2011)
===================

.. seealso::

   - http://en.wikipedia.org/wiki/C11_%28C_standard_revision%29

.. contents::
   :depth: 3

Introduction
============

C11 (formerly C1X) is an informal name for ISO/IEC 9899:2011, the
current standard for the C programming language.

It replaces the previous C standard, informally known as C99.

This new version mainly standardizes features that have already been supported
by common contemporary compilers, and includes a detailed memory model to
better support multiple threads of execution.

Due to delayed availability of conforming C99 implementations, C11 makes more
features optional, to make it easier to comply with the core language standard.


CLang , LLVL
============

.. seealso::

   - http://en.wikipedia.org/wiki/Clang
   - :ref:`clang_compiler`



GCC et C11
============

.. seealso::

   - https://linuxfr.org/news/sortie-de-la-version-4-7-du-compilateur-gcc#toc_13
   - :ref:`gcc`


Du côté du bon vieux langage C il y a là aussi des nouveautés puisque les
développeurs de GCC travaillent sur la norme C11 (voir cette dépêche LinuxFr
de GeneralZod_ pour un récapitulatif des nouveautés).

Quand on active l'option -std=c11 on retrouve donc la gestion des chaînes
unicode et des macros __STDC_UTF_16__ et __STDC_UTF_32__.

GCC 4.7 intégre les fonctions d'alignement _Alignas et _Alignof, la gestion
du mot-clé _Noreturn, la fonction __builtin_complex pour profiter des macros
CMPLX, etc.

Maintenant que la norme C11 a été officiellement ratifié par l'ISO le 8
décembre 2011, il est probable que le travail d'intégration dans GCC va
s'accélerer.

C11 n'est pas encore mort
-------------------------

.. seealso::

   - https://linuxfr.org/news/c11-nest-pas-encore-mort

La dernière norme du langage C a été publiée le 8 décembre 2011, la pré-version
finale étant accepté le 10 octobre, peu avant le décès du regretté Denis Ritchie
à l'origine du langage.

C11 intègre principalement la gestion du multithreading et rend optionnelles
certaines fonctionnalités afin de faciliter la conformité des compilateurs
vis-à-vis de la norme.

La précédente norme C99 a eu beaucoup de mal à s'imposer auprès de certains
éditeurs, certains refusant même de l'implémenter (notamment un vendeur
d'environnement Basic, situé à Redmond).


.. _GeneralZod:  https://linuxfr.org/news/c11-nest-pas-encore-mort
