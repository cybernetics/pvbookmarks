.. module:: GUI
    :synopsis: GUI
 
 
.. index::
   PAC
   
===
PAC
===

- http://forum.qtfr.org/viewtopic.php?id=7987


Cela fait presque sept ans que je fais du PAC sans le savoir !!!! 
J'avais commencé avec RealBasic sur un Mac 68K sous MacOS 7.1 ! Bon, il 
faut dire que je ne suis pas informaticien professionnel alors, je peux 
me passer de concept fumeux des commerciaux et autres thèseux. Comme je 
suis un pur hacker (j'ai appris sur le tas et je perds un tas de temps à
expérimenter) je vais te donner mes règles d'or en matière de 
programmation orienté objet:

1) Un Objet graphique se gère lui-même. (ex : Une fenêtre ne gère que 
   les événements qui lui sont dédiés)
2) Dès qu'un objet graphique devient complexe (plusieurs 
   événements à gérer) il faut en faire un objet à part.
3) Les données doivent être le plus proche possible de la couche logiciel 
   de base afin de gagner en rapidité et en portabilité. 
   ex : Utilisation des STL en C++ ou de la lib standard en Python, etc. 
   Quel est l'intérêt d'implementer QHttp en python alors qu'il y a la lib 
   urllib2 et httplib, meilleurs et plus rapide ? 
4) Documentez, Documentez, il en restera toujours quelque chose
5) Une chose, un objet, un fichier (bon d'accord, des fois on a un objet de 
   six lignes #include compris)
6) Tout ce que je viens de dire est idiot. En gros, fait ce 
   qu'il te plaît.

Alors, pas mal non ?

PS : Tu veux un coup de main (pas trop fort sur la joue) pour ton prog, 
j'aimerais t'aider, je tourne un peu en rond en ce moment.




   




