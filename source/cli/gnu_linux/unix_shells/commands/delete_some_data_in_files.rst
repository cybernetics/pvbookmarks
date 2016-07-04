
.. index::
   pair: cli; delete some data in files

==========================
Delete some data in a file
==========================


:source: guilde@guilde.asso.fr


::
    Je cherche un moyen de supprimer un bloc de manière automatique d'un fichier de
    conf de proftpd.

    Exemple de conf :
    Plein de lignes à garder
    <IfUser BLa>
    <Limit LOGIN>
    Allow 1.2.3.4 5.6.7.8...
    DenyAll
    </Limit>
    </IfUser>
    Plein de lignes à garder :

    Je pense le faire avec sed mais je ne m'en sors pas. Je connais le début du
    bloc (<IfUser BLa>) et la fin du bloc (le premier </IfUser> après le début du
    bloc). [...]



Réponse d'Edgar
===============

::

    sed '/<IfUser BLa>/,/<\/IfUser>/d'


