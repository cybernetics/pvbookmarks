



.. _linux_kernel_3_9_0:

==============================================================
linux  kernel 3.9.0  (2013-04-29 00:36:01, Unicycling Gorilla)
==============================================================

.. seealso::

   - http://kernelnewbies.org/Linux_3.9
   - http://linuxfr.org/news/sortie-du-noyau-linux-3-9


.. contents::
   :depth: 3


Commit
=======

.. seealso::

   - https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=c1be5a5b1b355d40e6cf79cc979eb66dafa24ad1
   
   
:author:	Linus Torvalds <torvalds@linux-foundation.org>	2013-04-29 00:36:01 (GMT)
:committer:	Linus Torvalds <torvalds@linux-foundation.org>	2013-04-29 00:36:01 (GMT)

::

    diff --git a/Makefile b/Makefile
    
::
    
    index 46263d8..8fe6991 100644
    --- a/Makefile
    +++ b/Makefile
    @@ -1,7 +1,7 @@
    VERSION = 3
    PATCHLEVEL = 9
    SUBLEVEL = 0
    -EXTRAVERSION = -rc8
    +EXTRAVERSION =
    NAME = Unicycling Gorilla
    
Summary
========

**Linux 3.9 has been released**.

This Linux release includes support for experimental RAID5/6 modes and 
better defragmentation in files shared by snapshots in Btrfs; support for 
the "goldfish" emulator used by the Android SDK, ability to SSD storage 
as cache device; two new architecture ports: Synopsys ARC 700 and Meta 
Imagination processors; KVM virtualization support in the ARM architecture, 
a Intel driver that "injects" idle states to improve performance-per-watt, 
support for Chrome OS laptops, a new suspend power state, and the removal 
of the obsolete CONFIG_EXPERIMENTAL configuration option. 

Many small features and new drivers and fixes are also available. 

Android "goldfish" emulator
----------------------------

The Android development environment provides a QEMU-based ARM virtualized 
platform called "goldfish". 

This platform provides a virtual CPU and drivers for battery, MMC, audio, 
graphics, etc. This release includes support for the Goldfish platform, 
which makes possible to develop for Android with out-of-the-box kernels. 


Linux fr
========

.. seealso:: http://linuxfr.org/news/sortie-du-noyau-linux-3-9

La sortie de la version stable 3.9 du noyau Linux vient d’être annoncée 
par Linus Torvalds.

Le nouveau noyau est, comme d’habitude, téléchargeable sur les serveurs 
du site kernel.org.

Pour cette version, on voit surtout la poursuite de travaux de longue 
haleine (nettoyage/regroupement des architectures ARM, refonte de la 
gestion des modes d’affichage des puces graphiques Intel…), des traditionnelles 
corrections de bogues et optimisations (LZO, gestion de l’énergie…) même 
si quelques nouveautés se démarquent (gestion des ventilateurs de 
certaines puces graphiques NVIDIA, prise en charge des RAID 5 et 6 sous 
Btrfs, prise en charge de certaines architectures ARM par KVM, possibilité 
d’utiliser un SSD comme cache d’une autre unité de stockage…).

À noter, une nouveauté déconnectée des notes de cette version mais apparue 
pendant son développement : Xen est dorénavant un projet de la Fondation 
Linux (lire la dépêche dédiée).

Le détail des évolutions, nouveautés et prévisions est dans la seconde 
partie de la dépêche.

Merci aux participants à la rédaction de cette dépêche : Davy Defaud, 
Batchyx (notamment la partie réseau), jcr83, Jiehong, Sidonie Tardieu, 
yogitetradim, baud123, Étienne Bersac (notamment la partie virtualisation), 
detail_pratique, Martin Peres, Mali, Maxime, Xavier Claude, Jarvis, alpentux, 
Nils Ratusznik, Tata Jeanette, kripteks, Strash, Akiel 
et patrick_g (notamment la partie statistiques).

