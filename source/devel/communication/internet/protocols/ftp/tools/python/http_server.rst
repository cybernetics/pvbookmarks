
.. index::
   pair: Python ; Http


.. _python_http_server:

============================================================
Partager simplement ses fichiers en LAN Python http.server
============================================================


.. seealso::

   - http://sebsauvage.net/links//?3DuywA  

Je vois circuler un article sur woof (http://sandrocazzaniga.fr/?p=128), 
un outil simple de partage de fichiers en réseau local.

Je signale juste qu'il est ultra-simple de partager un dossier en réseau 
SANS LOGICIEL SUPPLÉMENTAIRE. 

Placez-vous dans le répertoire à partager et tapez::

    python -m SimpleHTTPServer 5555

Et c'est tout !   

Et vous pouvez y accéder par::

    http://adresseip:5555/(5555 étant le port ; vous pouvez le changer.)

Ce qui est cool, c'est que ça utilise Python qui est installé par défaut dans 
tous les systèmes d'exploitation (sauf Windows bien sûr: là il vous faudra 
installer Python).

Si par hasard vous préférez Python 3, c'est::

    python -m http.server 5555
    


EDIT: Et sous Windows, avec quelques softs légers: http://sebsauvage.net/links/?jme7RA


