

.. highlight:: console

.. index::
   pair: virtualbox ; windows

============================
Virtualbox et 'vrai' Windows
============================

.. seealso:: 

   - http://www.guilde.asso.fr/lurker/thread/20120125.074153.4498f5de.en.html
   - http://www.sysprobs.com/access-physical-disk-virtualbox-desktop-virtualization-software


::

	-------- Message original --------
	Sujet: 	Re: Virtualbox et 'vrai' Windows
	Date de renvoi : 	Sat, 28 Jan 2012 14:39:40 +0100
	De (renvoi) : 	guilde@guilde.asso.fr
	Date : 	Sat, 28 Jan 2012 14:39:30 +0100
	De : 	Olivier Allard-Jacquin <olivieraj@free.fr>
	Pour : 	guilde@guilde.asso.fr


	Bonjour,

::

	Le 24/01/2012 14:11, Frédéric a écrit :
	> Le mardi 24 janvier 2012, sly (sylvain letuffe) a écrit :
	> 
	>> Les deux sont possibles, il y a cependant quelques trucs sioux à gérer
	>> pour convertir en disque virtuel, mieux vaut refaire l'installation est
	>> activer le windows avec la clef de licence.
	> 
	> La solution d'utiliser directement l'installation d'origine est donc 
	> possible est plus simple ? Parfait :o)
	> 
	> Tu sais où c'est documenté ? Je ne trouve pas, dans la doc officielle...

Ce que tu veux faire, c'est de l'accès physique depuis virtualbox. 
Je l'ai déjà pratiqué par le passé, et l'explication est ici:

- http://www.sysprobs.com/access-physical-disk-virtualbox-desktop-virtualization-software


    VBoxManage internalcommands createrawvmdk -filename mydrive.vmdk -rawdisk /dev/sda

Mais attention, il y a plusieurs raisons pour lesquelles cela peut ne
pas marcher, et quelques précautions à prendre.

- D'abord, sache que la licence de Windonws Seven "starter" n'autorise
  pas une utilisation dans une machine virtuelle. Seul les licences plus
  chères l'autorisent.

- Si le Windows utilise un tatouage placé dans le BIOS, il ne pourra pas
  le retrouver dans le BIOS de la virtualbox. Donc, il refusera de booter

- Si le Windows utilise un tatouage placé dans le MBR (512 premiers
  octets du disque), ton LILO/GRUB risque de l'écraser. Il vaut mieux
  alors laisser le boot loader de Windows se charger du boot, puis de
  "rebondir" sur le Linux http://doc.ubuntu-fr.org/tutoriel/comment_amorcer_ubuntu_avec_bootmgr

- Si le Windows utilise un tatouage placé dans la "piste 0", il est
  préférable de faire un backup de cette piste, avec un bon vieux "dd". 
  En effet, GRUB pourra écraser le tatouage, lorsqu'il s'installera dans la
  "piste 0":
  
  + Boot le portable sur un liveCD/liveUSB
  + Utilise "fdisk -lu /dev/sda" pour repérer la taille de la piste 0
    (généralement des blocs 0 à 62)
  + Et créé ton backup : dd if=/dev/sda of=ma_piste0.bin bs=512 count=63

- Pour essayer de détecter le type de tatouage utilisé, tu peux
  utiliser un "hexedit /dev/sda" ou "hexdump -C /dev/sda|less", afin
  d'étudier le contenu du début du disque. 
  L'idée est alors de trouver des trucs "louches" par rapport à une 
  installation non-tatouée.

- Sache enfin que le mécanisme de restauration du Windows pourra ne plus
  fonctionner, simplement parce que la taille de la partition Windows a
  changé suite à l'installation du Linux (j'ai déjà vu ce type de
  vérification stupide de la part d'un mécanisme de restauration choisit
  par un construteur).
  Un conseil : Utilise donc un bon vieux http://clonezilla.org/ afin de
  créer ton propre mécanisme de restauration.

- Une fois le Linux installé, utilise http://www.sysprobs.com/access-physical-disk-virtualbox-desktop-virtualization-software
  afin de créer ton "disque virtuel". Ce ne sera en fait qu'un petit
  fichier texte de quelques octets.

- Le problème, c'est que ton utilisateur Linux ("frederic") a besoin
  d'un accès direct à /dev/sda . Soit tu modifies udev pour le permettre,
  soit tu t'écris un petit programme qui fait un chown (via sudo).
  L'avantage, c'est que quelques secondes plus tard, Linux remettra les
  droits normaux de /dev/sda , ce qui empêchera d'autres programmes que
  virtualbox d'avoir un accès direct au disque
  

::

	<fichier>
	#!/bin/bash -norc
	sudo chown frederic /dev/sda
	exec vitualbox --startvm "le nom de ton virtualbox"
	</fichier>


et dans ton /etc/sudoers.d/virtualbox (pour une Debian)::

	<fichier>
	User_Alias      PRIVILEDGE_USERS = frederic
	Cmnd_Alias      PRIVILEDGE = \
			chown frederic /dev/sda
	PRIVILEDGE_USERS ALL = NOPASSWD: PRIVILEDGE
	</fichier>

- Enfin, dans cette configuration tu peux être confronté à des lenteurs
  tout bonnement inacceptables, avec un temps de boot de Windows de
  plusieurs minutes (juste pour voir apparaître la fenêtre de login). La
  cause de ce problème vient d'une configuration APIC+Windows+Virtualbox.
  Je ne sais pas si c'est toujours d'actualité, notamment avec un Windows
  Seven (j'ai eu le problème il y a quelques années avec un Windows XP).
  La solution est là:
  
  - http://ubuntuforums.org/showthread.php?t=1330484
  - https://www.google.com/#q=virtualbox+apic+windows

Notes
=====

que dans une telle configuration, ton Windows a accès lui aussi au
/dev/sda, donc potentiellement il peut mettre à mal ton Linux

De plus, tu pourrais re-lancer ton Linux depuis le virtualbox,
lui-même exécuté par le Linux. Et alors là, bonjour les dégâts !!! 

Afin de limiter les risques, je te suggère donc de laisser le Windows en boot
par défaut, ou de ne pas permettre à un OS de booter automatiquement au
bout d'un timeout de grub ou du boot loader de Windows

Je pense que cette réponse devrait couvrir tout les problèmes que tu
devrais rencontrer.

Cordialement,
Olivier

::

	-- 
	~~~~~~~  _____/\_____  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Phoenix /   _ \/ _   \    Olivier Allard-Jacquin
		   /   / \  / \   \   Web:  http://olivieraj.free.fr/
		  /___/  /  \  \___\  Mail: olivieraj@free.fr
	~~~~ /////  ///\\\  \\\\\ ~~~~~~~~~~~~~~~~~~~~~~~ Linux Powered !!





