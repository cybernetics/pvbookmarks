
.. index::
   Ubuntu (11.10)

.. _clic_lanceur:

==========================
Ubuntu 11.10 clic lanceur
==========================


- http://www.clapico.com/2011/11/05/clic-lanceur/


Je vous présentais il y a quelques jours la possibilité de créer lanceurs et 
raccourcis sur votre bureau à l’aide du terminal; je vous propose aujourd’hui 
un script permettant de réaliser la même opération à l’aide d’un simple clic 
droit sur le bureau.

C’est chez Ubuntu Up que j’ai découvert ce script que j’ai du modifier pour 
qu’il fonctionne sur le « Bureau » français plutôt que sur le « Desktop ».

Dans un premier temps, nous allons ouvrir un terminal afin de télécharger 
ce script et de le placer dans notre dossier « Scripts » à l’aide de la commande::

	wget http://www.clapico.com/telechargement/Create-Launcher
	cp Create-Launcher ~/.gnome2/nautilus-scripts
	chmod +x ~/.gnome2/nautilus-scripts/Create-Launcher
	mv ~/.gnome2/nautilus-scripts/Create-Launcher ~/.gnome2/nautilus-scripts/"Créer lanceur ou raccourci"
	
	
