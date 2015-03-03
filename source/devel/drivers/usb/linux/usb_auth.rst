.. module:: USB_authorized
    :synopsis: Authorization control for USB devices

.. index::
   USB authorization
   2.6.24 linux
   vendorID
   productID
   SUBSYSTEM
   checkUSBAuth.sh
   udev authorization
   udevcontrol

 
.. _usb_authorizations:

==================
USB authorizations
==================

Source: GNU/Linux magazine N°101, janvier 2008, Mathieu Barthélémy

Linux 2.6.24 marque le début du support de contrôle d'autorisation d'accès 
au système pour les périphériques USB.
Ce framework vise à permettre de contrôler si un tel périphérique a le droit
de se connecter et de fournir une interaction avec l'espace utilisateur  
(notification de nouveau matériel essayant de se connecter) pour permettre
la prise de décision.

Le moyen le plus basique d'interagir avec ce nouveau système est:

- l'entrée sysfs: :file:`/sys/bus/usb/devices/<periphérique>/authorized`
  (0=interdit, 1=permis), qui définit le droit pour un périphérique de se connecter
- l'entrée :file:`/sys/bus/usb/devices/usbX/authorized_default` 
  (0=interdit, 1=permis), qui attribue une politique globale à chaque contrôleur.
  
**Concrètement, une fois le matériel autorisé à se connecter, nous pouvons très 
bien  souhaiter définir des critères personnalisés pour déterminer s'il pourra 
être utilisé**: par quels utilisateurs, suivant le type de matériel...
Ainsi, une organisation peut par exemple appliquer des politiques de 
restriction des clefs USB (pour éviter le vol de données confidentielles à
l'organisation/entreprise), mais accepter les claviers ou souris. Dans ce cas,
authorized_default sera positionnée à 0, et ce sera un mécanisme entièrement
en espace utilisateur qui positionnera éventuellement à 1 cette entrée.

Illustrons par un exemple: créons un script à valeur pédagogique, appelé
grâce à une règle udev à chaque découverte d'un nouveau périphérique USB.
Il n'autorisera que les périphériques dont l'identifiant est présent
dans un fichier de configuration. Nous formerons cet identifiant à partir
du :ref:`vendorID <id3_vendor_id>` et du :ref:`productID <id3_products_id>`

:file:`checkUSBAuth.sh`


:: 

    #!/bin/sh
    if [ ! -z "`grep $2 /etc/authorized_dev_ids`" ]; then
        # si le grep renvoie quelque chose, le périph est autorisé
        echo 1 > /sys$1/device/authorized
    else
        # sinon ... interdit
        echo 0 > /sys$1/device/authorized
    fi

    
Et, enfin la règle udev, à placer avant toute autre règle sur l'USB:

::

    #USB authorzation
    SUBSYSTEM=="usb_device", ACTION="add", RUN+="/root/checkUSBAuth.sh %p %s{idVendor}%s{idProduct}"

    
Cette règle s'applique à tout le sous-système USB (SUBSYSTEM), seulement dans 
le cas d'un ajout (ACTION), et lance donc systématiquement notre script (RUN)
avec en paramètre le chemin du périphérique (%p).

Le branchement d'un périphérique sur un bus ayant l'accès par défaut interdit
doit provoquer l'apparition du message::

    usb X-Y: Device is not authorized for usage

dans le log système.

Lors de son activation/autorisation, la mention::

    usb X-Y: authorized to connect

Un :command:`chmod u+x` sur le script et un :command:`udevcontrol reload_rules`
plus tard et le système est prêt.










 
    