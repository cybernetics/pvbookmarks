
.. index::
   pair: http://wwwkeys.pgp.net; OpenPGP

.. _wwwkeys.pgp.net:

=======================================
http://wwwkeys.pgp.net OpenPGP server
=======================================


.. seealso:: 

   - http://wwwkeys.pgp.net
   - http://wwwkeys.pgp.net/#submit
   
  
  

Exemple 
=======

Envoi de la clé publique de pvergain sur le serveur http://pgp.mit.edu.

On s'assure que la clé publique existe bien avec la commande::

    gpg --fingerprint pvergain@gmail.com
   
   
::


    gpg --send-keys --keyserver wwwkeys.pgp.net A27DB4A0

::

    gpg: envoi de la clef A27DB4A0 au serveur hkp wwwkeys.pgp.net



Ajout par l'interface web
==========================

.. seealso::

   - http://wwwkeys.pgp.net/#submit
   
   
