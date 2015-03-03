
.. index::
   pair: http://pgp.mit.edu; OpenPGP

.. _pgp_mit_edu:

===================================
http://pgp.mit.edu OpenPGP server
===================================


.. seealso:: 

   - http://pgp.mit.edu/
   - http://pgp.mit.edu/pks/lookup?search=0xA27DB4A0&op=index
   
  
  

Exemple 
=======

Envoi de la clé publique de pvergain sur le serveur http://pgp.mit.edu.

On s'assure que la clé publique existe bien avec la commande::


    gpg --fingerprint pvergain@gmail.com
   
   
   
::


    gpg --send-keys --keyserver pgp.mit.edu A27DB4A0
