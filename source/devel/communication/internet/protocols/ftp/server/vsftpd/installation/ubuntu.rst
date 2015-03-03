
.. index::
   pair: Ubuntu ; VsFTPd


.. _VsFTPd_ubuntu_installation:

============================================================
VsFTPd Ubuntu installation
============================================================

.. seealso::

   - http://www.wikihow.com/Set-up-an-FTP-Server-in-Ubuntu-Linux


.. contents::
   :depth: 3


Installation
============

::

    sudo aptitude install vsftpd
    
    
::

    Les NOUVEAUX paquets suivants vont être installés :
    vsftpd 
    0 paquets mis à jour, 1 nouvellement installés, 0 à enlever et 0 non mis à jour.
    Il est nécessaire de télécharger 115 ko d'archives. Après dépaquetage, 372 ko seront utilisés.
    Prendre : 1 http://fr.archive.ubuntu.com/ubuntu/ saucy/main vsftpd i386 3.0.2-1ubuntu2 [115 kB]
    115 ko téléchargés en 0s (196 ko/s)
    Préconfiguration des paquets...
    Sélection du paquet vsftpd précédemment désélectionné.
    (Lecture de la base de données... 1124403 fichiers et répertoires déjà installés.)
    Dépaquetage de vsftpd (à partir de .../vsftpd_3.0.2-1ubuntu2_i386.deb) ...
    Traitement des actions différées (« triggers ») pour « ureadahead »...
    ureadahead will be reprofiled on next reboot
    Traitement des actions différées (« triggers ») pour « man-db »...
    Paramétrage de vsftpd (3.0.2-1ubuntu2) ...
    vsftpd start/running, process 16822
    Traitement des actions différées (« triggers ») pour « ureadahead »...


Vérifier que le serveur FTP tourne bien
=======================================

::

    @vercors:~/$ ps -ef | grep ftp
    root     16822     1  0 08:39 ?        00:00:00 /usr/sbin/vsftpd
 
 
    
Modifier les paramètres du fichier de configuration /etc/vsftpd.conf
====================================================================

::

    sudo geany /etc/vsftpd.conf

    

Redémarrer le serveur (service) FTP
====================================

::

    sudo service vsftpd restart
    
::
    
    vsftpd stop/waiting
    vsftpd start/running, process 20206   
        

    
