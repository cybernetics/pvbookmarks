
.. index::
   pair: Free Electrons ; 2012


.. _free_electrons_2012:

=======================
Free electrons 2012
=======================

.. contents::
   :depth: 3


Toute l’équipe de Free Electrons vous souhaite une bonne année 2013,
avec tout le succès que vous attendez dans vos projets personnels et
professionnels, et dans vos contributions à la vie d’autrui. Nous
saisissons cette occasion pour vous donner des nouvelles de Free Electrons.

En 2012, Free Electrons a continué à travailler sur des projets de
développement. La principale différence avec 2011 est que les projets
ont été bien plus longs. En voici les plus importants:

  * Développement de code pour le noyau Linux, pour prendre en charge
    les processeurs Armada 370 et Armada XP de Marvell dans le noyau
    Linux officiel. Cela représente des mois d’ingénierie ! Les
    modifications que nous avons apportées apparaissent sur
    git.kernel.org
    (http://git.kernel.org/?p=linux%2Fkernel%2Fgit%2Ftorvalds%2Flinux-2.6.git&a=search&h=HEAD&st=author&s=free-electrons.com)
  * Développement de code pour le noyau Linux et mise en place d’un
    environnement de développement pour un nouveau système à base
    d’i.MX28 conçu par Crystalfontz (http://www.crystalfontz.com/), en
    ajoutant le support de cette carte à la version officielle de Linux.
    Vous trouverez plus de détails sur la page du projet sur Kickstarter
    (http://www.kickstarter.com/projects/crystalfontz/cfa-10036-open-hackable-linux-arm-embedded-gpio-mo)
  * Mise en place d’un système de compilation, développement de code de
    chargeur de démarrage et de pilotes noyau, amélioration du mécanisme
    de mise à jour, et plus généralement travail de développement de
    système Linux embarqué.
  * Développement de code noyau pour les convertisseurs
    analogique-numérique des processeurs AT91 d’Atmel, et inclusion dans
    les sources officielles du noyau.
  * Réduction du temps de démarrage et audit de gestion de l’énergie
    pour un terminal de paiement à base de processeur MIPS.
  * Réduction du temps de démarrage sur une plateforme de développement
    à base de processeur ARM pour terminal de paiement.
  * Développement, intégration, et support d’un système Linux embarqué

Que ce soit à travers des contrats ou des contributions directes, 2012
nous a donné de nombreuses occasions de contribuer à des projets
open-source, en particulier:

  * 195 patches inclus dans le noyau Linux, sans compter ceux qui ont
    été acceptés par les mainteneurs mais n’apparaissent pas encore dans
    la version de Linus Torvalds. Voir git.kernel.org
    (http://git.kernel.org/?p=linux%2Fkernel%2Fgit%2Ftorvalds%2Flinux-2.6.git&a=search&h=HEAD&st=author&s=free-electrons.com)
    pour plus de détails.
  * 448 patches inclus dans le système compilation Buildroot: détails
    sur git.buildroot.net
    (http://git.buildroot.net/buildroot/log/?qt=author&q=free-electrons.com).
  * 9 patches inclus dans le chargeur de démarrage U-boot.
  * 7 patches pour le chargeur de démarrage Barebox: détails sur
    git.penguntronix.de
    (http://git.pengutronix.de/?p=barebox.git&a=search&h=HEAD&st=author&s=free-electrons.com).

Au passage, voici la commande git que vous pouvez lancer dans les
dépôts correspondants pour obtenir ces mesures par vous-mêmes:

git shortlog --no-merges -sn --author "free-electrons.com" --since="01/01/2012" --until="12/31/2012"

Nous avons également donné de multiples sessions de nos formations Linux
embarqué (http://free-electrons.com/fr/formation/linux-embarque/) et
développement de pilotes de périphériques noyau Linux
(http://free-electrons.com/fr/formation/noyau-linux/). Nous avons
également fini de migrer nos supports de formation du format Open
Document vers LaTeX, et leurs sources sont maintenant disponibles sur
notre dépôt git public (http://git.free-electrons.com/). Cela devient
beaucoup plus simple de suivre les changements et de soumettre des
contributions.

Nous avons également créé une nouvelle formation sur le développement
système avec Android (http://free-electrons.com/fr/formation/android/),
et avons donné de multiples sessions chez nos clients ainsi qu’en
session publique à Toulouse
(http://free-electrons.com/fr/formation/sessions/toulouse-android/). Il
s’agit d’un programme de quatre jours, pour comprendre l’architecture du
système Android, comment compiler et personnaliser le système pour une
plateforme matérielle particulière, et comment l’étendre pour prendre en
charge de nouveaux périphériques.

Tout comme l’an passé, nous avons partagé notre expérience lors de
conférences techniques internationales:

  * IIO, un nouveau sous-système
    http://free-electrons.com/pub/conferences/2012/fosdem/iio-a-new-subsystem/iio-a-new-subsystem.pdf
    FOSDEM, Bruxelles, février 2012
  * Qt pour des applications non graphiques
    http://free-electrons.com/pub/conferences/2012/fosdem/qt-for-non-graphical-apps/
    FOSDEM, Bruxelles, février 2012
  * Buildroot: un système de compilation élégant, simple et efficace
    pour Linux embarqué
    http://free-electrons.com/pub/conferences/2012/elc/buildroot.pdf
    Embedded Linux Conference, San Francisco, février 2012
  * Buildroot: un système de compilation élégant, simple et efficace
    pour Linux embarqué
    http://free-electrons.com/pub/conferences/2012/lsm/buildroot/buildroot.pdf
    Rencontres Mondiales du Logiciel Libre, Genève, juillet 2012
  * Atelier Buildroot
    http://free-electrons.com/pub/conferences/2012/lsm/buildroot-workshop/buildroot-workshop.pdf
    Rencontres Mondiales du Logiciel Libre, Genève, juillet 2012
  * Noyau Linux: consolidation dans le support de l’architecture ARM
    http://free-electrons.com/pub/conferences/2012/lsm/arm-kernel-consolidation/arm-kernel-consolidation.pdf
    Rencontres Mondiales du Logiciel Libre, Genève, juillet 2012
  * Visite guidée de l’architecture d’Android
    http://free-electrons.com/pub/conferences/2012/lsm/a-look-through-the-Android-stack/a-look-through-the-Android-stack.pdf
    Rencontres Mondiales du Logiciel Libre, Genève, juillet 2012
  * Votre checklist pour ajouter un nouveau SoC ARM à Linux
    http://free-electrons.com/pub/conferences/2012/elce/arm-soc-checklist/arm-soc-checklist.pdf
    Embedded Linux Conference Europe, Barcelone, novembre 2012

En participant à ces conférences, nous avons également enregistré et
publié des vidéos des présentations:

  * FOSDEM 2012
    http://free-electrons.com/blog/fosdem2012-videos/
  * Embedded Linux Conference 2012
    http://free-electrons.com/blog/elc-2012-videos/
  * Android Builders Summit 2012
    http://free-electrons.com/blog/abs-2012-videos/
  * Embedded Linux Conference Europe 2012
    http://free-electrons.com/blog/elce-2012-videos/

Grâce à leurs contributions au noyau Linux official sur la plateforme
ARM, Grégory Clément
(http://free-electrons.com/company/staff/gregory-clement/) et Thomas
Petazzoni (http://free-electrons.com/company/staff/thomas-petazzoni/)
ont également été invités au minisummit ARM
(http://lwn.net/Articles/514159/) au Linux Kernel Summit à San Jose en
août. Ils ont été impliqués dans les décisions techniques sur les
prochaines évolutions du noyau Linux sur l’architecture ARM.

Nous avons aussi organisé et à participé à deux événements « Buildroot
developer days », un à Bruxelles après le FOSDEM
(http://lists.busybox.net/pipermail/buildroot/2012-February/050371.html), et
le deuxième à Barcelone après ELC Europe
(http://www.emlinews.net/2012/11/report-from-the-buildroot-developers-day-in-barcelona/).

Nous avons également continué à participer au développement de la
communauté de Linaro (http://linaro.org), une société d’ingénierie à but
non lucratif dont le but est l’amélioration de Linux sur la plateforme
ARM. Cet engagement est arrivé à son terme, et ceci permet à Michael
Opdenacker de reprendre des projets plus techniques.

Il est maintenant temps de partager nos projets pour 2013.

Nous avons prévu de recruter de nouveaux ingénieurs pour satisfaire une
demande toujours croissante pour nos services de développement et de
formation. En particulier, un nouvel ingénieur nous rejoint en mars.

Nous organisons également de nouvelles sessions publiques de formation
en France, dont les dates sont maintenant disponibles:

  * Android: développement système, Toulouse, 2-5 avril
    http://free-electrons.com/fr/formation/sessions/toulouse-android/
  * Noyau Linux pour l’embarqué et développement de pilotes de
    périphériques, Toulouse, 8-12 avril
    http://free-electrons.com/fr/formation/sessions/toulouse-developpement-noyau-linux/
  * Formation Linux embarqué, Toulouse, 10-14 juin
    http://free-electrons.com/fr/formation/sessions/toulouse-linux-embarque/
  * Noyau Linux pour l’embarqué et développement de pilotes de
    périphériques, Avignon, 10-14 juin (anglais)
    http://free-electrons.com/training/sessions/avignon-linux-kernel-drivers/
  * Android: développement système, Toulouse, 18-21 juin (anglais)
    http://free-electrons.com/training/sessions/toulouse-android/
  * Formation Linux embarqué, Avignon, 7-11 octobre (anglais)
    http://free-electrons.com/training/sessions/avignon-embedded-linux/

Nous prévoyons également d’annoncer plusieurs nouvelles formations.
Étant très pris par des projets en 2012, nous n’avons pas eu le temps
d’avancer dans les objectifs que nous avions annoncés il y a un an:

  * Formation Git. Une formation de deux jours pour bien maîtriser
    l’utilisation du système de gestion de sources distribué Git, que ce
    soit pour des projets internes ou pour contribuer à des projets
    open-source.
  * Formation sur le débogage, le traçage et l’analyse de performance
    sur le noyau Linux. Une session d’une ou deux journées pour tracer
    l’exécution des fonctions du noyau, et pouvoir rechercher les causes
    de dysfonctionnements et de problèmes de performance.
  * Formation sur la réduction du temps de démarrage. Une formation
    d’une ou deux journées pour apprendre et maîtriser la méthodologie
    et les techniques pour faire démarrer plus vite vos systèmes Linux
    embarqué.

Comme nous ne sommes qu’aux premières étapes de la préparation de ces
formations, n’hésitez pas à saisir l’occasion de nous contacter et de
nous faire part de vos attentes, pour influer sur leur contenu final, au
cas où vous seriez intéressés par de telles formations.

Nous continuerons également à participer aux conférences techniques les
plus importantes. En particulier, les ingénieurs de Free Electrons
seront présents à l’Android Builders Summit et à l’Embedded Linux
Conference à San Francisco, ainsi qu’à l’Embedded Linux Conference
Europe à Edinbourg en octobre. Cette participation aux conférences
permet à nos ingénieurs de rester au courant des derniers développements
dans le domaine de Linux embarqué et de créer des contacts utiles dans
la communauté. N’hésitez pas à vous rendre ces conférences, pour
développer vos connaissances techniques et pourquoi pas en profiter pour
nous rencontrer !

Enfin, nous ferons aussi plus d’efforts pour publier ce bulletin
vraiment chaque trimestre. En 2012, nous étions si occupés par nos
projets que nous n’avons pas réussi à publier de bulletins pour les
troisième et quatrième trimestres.

Vous pouvez continuer à suivre les actualités de Free Electrons en
lisant notre blog en anglais (http://free-electrons.com/blog/, 31
articles en 2012), nos actualités francophones
(http://free-electrons.com/fr/infos/) et en suivant nos nouvelles brèves
sur Twitter (http://twitter.com/free_electrons).

Une fois de plus, bonne année 2013 !

L’équipe de Free Electrons.

-- Michael Opdenacker, Free Electrons Kernel, drivers, real-time and embedded
Linux development, consulting, training and support.
http://free-electrons.com +33 484 258 098

