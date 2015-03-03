

.. index::
   pair: Android; Logcat
   ! Logcat

.. _logcat:

============================
Logcat
============================

.. seealso::

   - https://developer.android.com/tools/help/logcat.html
   - https://developer.android.com/tools/debugging/debugging-log.html


.. contents::
   :depth: 3

Introduction
=============

.. seealso::

   - :ref:`adb`

The Android logging system provides a mechanism for collecting and viewing system
debug output.

Logs from various applications and portions of the system are collected in a
series of circular buffers, which then can be viewed and filtered by the logcat
command.

You can use logcat from an ADB shell to view the log messages.

For complete information about logcat options and filtering specifications,
see `Reading and Writing Logs <https://developer.android.com/tools/debugging/debugging-log.html>`_ .

For more information on accessing logcat from DDMS, instead of the command line,
see Using `DDMS <https://developer.android.com/tools/debugging/ddms.html>`_ .


Logcat et propriétés système
=============================

:Source:  MISC Hors série N°7 2013, p.57


Android permet aux applications d’enregistrer leurs messages de debug dans un
fichier de logs commun à l’ensemble du système ; la consultation des logs est
possible grâce à la commande ``adb logcat``.

Le binaire :ref:`adb` est présent dans le SDK et permet de nombreuses actions
comme :

- le forwarding de port
- l'obtention d'un shell sur le système
- le dépôt la récupération de fichiers

Étant donné le nombre d’applications inscrivant leurs informations dans ce journal
de logs, il peut vite devenir difficile à lire en temps réel. Afin d’être plus
efficace, il est possible d’appliquer des filtres et des couleurs (COLORLOGCAT)_
pour différencier lesentrées selon leur TAG.


.. _(COLORLOGCAT):  http://jsharkey.org/downloads/coloredlogcat.pytxt


Vide le journal de logs
------------------------

::

    $ adb logcat -c



Affiche les informations dont le niveau de criticité
-----------------------------------------------------

On affiche les informations dont le niveau de criticité est supérieur à Info
pour MonApplication et Debug pour Monapplication2, en masquant
(Silent) les autres applications.

::

    $ adb logcat *:S MonApplication:I MonApplication2:D


Redirige stdio des binaires natifs vers logcat
------------------------------------------------

Il est également possible d’ajouter des informations supplémentaires à ``logcat`` en
modifiant les propriétés du système (une sorte de base de registre sous Android),
via l’utilisation de la commande ``setprop`` (``getprop`` permet de consulter la
valeur des propriétés) :


Redirige stdio des binaires natifs vers logcat

::

    $ adb shell ‘stop; setprop log.redirect-stdio true; start’


Certaines applications utilisent les propriétés système pour activer ou non leur
mode de debug et une partie de leurs fonctionnalités, pensez donc à vérifier
l’utilisation de ``System.getProperty`` ou ``Runtime.exec(«getprop ...»)``
(pour la partie Dalvik) et property_get (pour la partie native).

Par exemple, la DalvikVM, vérifie la présence de la propriété système debug.jni.logging.
Lorsque celle-ci est à 1, la DalvikVM enregistrera dans ``logcat`` les appels aux
méthodes JNI durant l’exécution d’une application Android. Ci-dessous l’activation
de la propriété et sa conséquence sur logcat::

    $ adb shell ‘setprop debug.jni.logging 1’
    $ adb logcat |grep dalvikvm
    [...]
    I/dalvikvm( 6152): -> com.sh4ka.native.MainActivity
    isRootedDevice(Ljava/lang/String;)I this=0x41dddad8 (0x41e27838)
    I/dalvikvm( 6152): <- com.sh4ka.native.MainActivity
    isRootedDevice(Ljava/lang/String;)I returned 0
