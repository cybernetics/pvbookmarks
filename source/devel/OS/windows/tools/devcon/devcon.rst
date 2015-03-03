.. module:: Windows_devcon_tool
   :synopsis: Windows devcon tool
 
 
.. index::
   devcon
   
  
.. _windows_devcon_tool:

===========
devcon (mt)
===========
   
L'utilitaire DevCon est un utilitaire de ligne de commande qui peut être 
utilisé à la place du Gestionnaire de périphériques. Il vous permet d'activer, 
de désactiver, de redémarrer, de mettre à jour, de supprimer et d'interroger 
des périphériques individuels ou des groupes de périphériques. 

Il fournit également des informations utiles aux développeurs de pilotes, 
mais non disponibles dans le Gestionnaire de périphériques.

.. seealso::
 
   - http://support.microsoft.com/kb/311272


Usage
=====

:: 

    Device Console Help:
    devcon [-r] [-m:\\<machine>] <command> [<arg>...]
    -r if specified will reboot machine after command is complete, if needed.
    <machine> is name of target machine.
    <command> is command to perform (see below).
    <arg>... is one or more arguments if required by command.
    For help on a specific command, type: devcon help <command>
    classfilter          Allows modification of class filters.
    classes              List all device setup classes.
    disable              Disable devices that match the specific hardware or instance ID.
    driverfiles          List driver files installed for devices.
    drivernodes          Lists all the driver nodes of devices.
    enable               Enable devices that match the specific hardware or instance ID.
    find                 Find devices that match the specific hardware or instance ID.
    findall              Find devices including those that are not present.
    help                 Display this information.
    hwids                Lists hardware ID's of devices.
    install              Manually install a device.
    listclass            List all devices for a setup class.
    reboot               Reboot local machine.
    remove               Remove devices that match the specific hardware or instance ID.
    rescan               Scan for new hardware.
    resources            Lists hardware resources of devices.
    restart              Restart devices that match the specific hardware or instance ID.
    sethwid              Modify Hardware ID's of listed root-enumerated devices.
    stack                Lists expected driver stack of devices.
    status               List running status of devices.
    update               Manually update a device.
    updateni             Manually update a device (non interactive).
                            

Exemples de commandes DevCon
============================

.. index::
   devcon find usb\vid*

devcon find usb\vid*
--------------------

::

    C:\Tmp>devcon find usb\vid\*
    
::


    USB\VID_0B81&PID_0200\5&344BCE15&0&1   : USB Smart Card reader

Trouve tous les périphériques USB commençant par 'vid'


devcon -m:\\test find pci\\*
----------------------------


:: 

    devcon -m:\\test find pci\\*
    

Dresse la liste de tous les périphériques PCI connus présents sur l'ordinateur 
test (l'argument -m permet de spécifier un ordinateur cible ; vous devez utiliser 
la communication entre processus (IPC) pour pouvoir accéder à cet ordinateur).

devcon -r install %WINDIR%\Inf\Netloop.inf MSLOOP
---------------------------------------------------

::

    devcon -r install %WINDIR%\Inf\Netloop.inf *MSLOOP

Installe une nouvelle instance de la carte de bouclage Microsoft. 
Cette commande crée un nouveau nœud pour les périphériques énumérés 
à la racine, avec lequel vous pouvez installer un « périphérique virtuel », 
tel qu'une carte de bouclage. 
Elle redémarre également l'ordinateur en mode silencieux, si nécessaire.

devcon classes
--------------

::

    devcon classes

Dresse la liste de toutes les classes de configuration connues. 
La sortie contient le nom court non traduit (« USB », par exemple) 
et le nom descriptif (« contrôleurs Universal Serial Bus », par exemple).


devcon classfilter upper !filter1 !filter2
------------------------------------------

::

    devcon classfilter upper !filter1 !filter2
    

Supprime les deux filtres spécifiés.


devcon classfilter lower !badfilter +goodfilter
-----------------------------------------------

::

    devcon classfilter lower !badfilter +goodfilter

Remplacez « badfilter » par « goodfilter ».



devcon driverfiles =ports
-------------------------

::

    devcon driverfiles =ports

Dresse la liste des fichiers associés à chaque périphérique de la classe de 
configuration ports.

devcon disable MSLOOP
----------------------

Désactive tous les périphériques dont l'ID de matériel se termine par 
« MSLOOP » (y compris "\*MSLOOP").

devcon drivernodes @ROOT\PCI_HAL\PNP0A03
----------------------------------------

::

    devcon drivernodes @ROOT\PCI_HAL\PNP0A03


Dresse la liste de tous les pilotes compatibles avec le périphérique 
ROOT\PCI_HAL\PNP0A03. Cette commande peut servir à déterminer la raison 
pour laquelle un fichier .inf (Integral Device Information) a été préféré 
à un fichier .inf tiers.

devcon enable MSLOOP
----------------------

::

    devcon enable \*MSLOOP


Active tous les périphériques dont l'ID de matériel est "\*MSLOOP". 
Le guillemet simple indique qu'il faut considérer l'ID de matériel comme 
une expression littérale (en d'autres termes, l'astérisque [« * »] représente 
bien un astérisque ; il ne s'agit pas d'un caractère générique).

devcon find *
-------------

::

    devcon find *

Dresse la liste de toutes les instances des périphériques présents sur 
l'ordinateur local.

devcon find pci\*
-----------------

::

    devcon find pci\*
    

Dresse la liste de tous les périphériques PCI (Peripheral Component 
Interconnect) connus présents sur l'ordinateur local (cette commande 
suppose qu'un périphérique est de type PCI si son ID de matériel 
commence par « PCI\ »).

devcon find =ports *pnp*
------------------------

::

    devcon find =ports *pnp*


Dresse la liste des périphériques présents appartenant à la classe de 
configuration ports et dont l'ID de matériel contient « PNP ».

devcon find =ports @root\*
--------------------------

::

    devcon find =ports @root\*

Dresse la liste des périphériques présents appartenant à la classe de 
configuration ports et figurant à la racine de l'arborescence d'énumération 
(l'ID d'instance commence par « root\ »). Ne faites aucune supposition quant 
à la façon dont les ID d'instance sont mises en forme dans le code. 
Pour déterminer les périphériques à la racine, vous pouvez examiner les bits 
d'état des périphériques. Cette fonction est incluse dans DevCon pour faciliter 
le débogage.

devcon findall =ports
---------------------

::

    devcon findall =ports

Dresse la liste de tous les périphériques absents et présents appartenant à 
la classe ports. Sont inclus les périphériques supprimés, les périphériques 
transférés dans un autre emplacement et, dans certains cas, les périphériques 
énumérés de façon différente en raison d'une modification du BIOS.

devcon listclass usb 1394
-------------------------

::

    devcon listclass usb 1394

Dresse la liste de tous les périphériques présents pour chaque classe indiquée 
(dans cet exemple, USB et 1394).

devcon remove @usb\*
--------------------

::

    devcon remove @usb\*

Supprime tous les périphériques USB. 
Les périphériques supprimés sont accompagnés de leur état de suppression.

devcon rescan
-------------

::

    devcon rescan

Effectue une nouvelle recherche sur les périphériques Plug and Play.

devcon resources =ports
-----------------------

::

    devcon resources =ports

Dresse la liste de toutes les ressources utilisées par tous les périphériques 
de la classe de configuration ports.

devcon restart =net @'ROOT\*MSLOOP\0000
---------------------------------------

::

    devcon restart =net @'ROOT\*MSLOOP\0000

Redémarre la carte de bouclage ROOT\*MSLOOP\0000. Le guillemet simple dans la 
commande indique qu'il faut considérer l'ID de matériel comme une expression 
littérale.

devcon hwids=mouse
------------------

::

    devcon hwids=mouse

Dresse la liste de tous les ID du matériel des périphériques de classe souris 
sur le système.

devcon sethwid @ROOT\LEGACY_BEEP\0000 := beep
---------------------------------------------

::

    devcon sethwid @ROOT\LEGACY_BEEP\0000 := beep

Attribue l'ID de matériel, beep, au périphérique hérité beep.

devcon stack =ports
-------------------

::

    devcon stack =ports

Indique la pile de pilotes attendue pour le périphérique. Elle inclut les 
filtres inférieurs/supérieurs de classes et de périphériques, ainsi que 
le service de contrôle.

devcon status @pci\*
--------------------

::

    devcon status @pci\*

Indique l'état de chaque périphérique présent dont l'ID d'instance 
commence par « pci\ ».

devcon status @ACPI\PNP0501\1
-----------------------------


::

    devcon status @ACPI\PNP0501\1


Indique l'état d'une instance de périphérique particulière ; dans cet exemple, 
il s'agit d'un port série énuméré par l'interface ACPI (Advanced Configuration 
and Power Interface).

devcon status @root\rdp_mou\0000
--------------------------------

::

    devcon status @root\rdp_mou\0000

Indique l'état du pilote de souris de Microsoft Terminal Server ou des 
services Terminal Server.

devcon status *PNP05*
---------------------

::

    devcon status *PNP05*

Indique l'état de tous les ports COM.

devcon update mydev.inf pnp0501
-------------------------------

::

    devcon update mydev.inf pnp0501


Met à jour tous les périphériques correspondant exactement à l'ID de matériel 
pnp0501 pour qu'ils utilisent le meilleur pilote possible dans Mydev.inf 
associé à l'ID de matériel pnp0501.

.. note:: Cette mise à jour force tous les périphériques à utiliser le pilote 
   figurant dans Mydev.inf, même s'il existe déjà un meilleur choix sur le système. 
   
   
Cela peut être utile lorsque vous souhaitez installer de nouvelles versions 
de pilotes au cours d'une phase de développement, avant d'avoir obtenu une 
signature. 
La mise à jour ne concerne que les périphériques correspondant à l'ID de 
matériel spécifié, mais pas les périphériques enfants. Si le fichier .inf 
spécifié ne comporte pas de signature, il se peut que Windows affiche une 
boîte de dialogue vous invitant à confirmer s'il faut installer le pilote. 
S'il est nécessaire de redémarrer l'ordinateur, vous en êtes averti et 
DevCon renvoie une erreur de niveau 1. Si vous spécifiez l'argument -r, 
le redémarrage se fait automatiquement, le cas échéant. 


