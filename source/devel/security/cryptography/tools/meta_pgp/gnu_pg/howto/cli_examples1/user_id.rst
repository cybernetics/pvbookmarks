
.. index::
   pair: gpg; edit-key
   pair: gpg; adduid
   pair: gpg; primary
   pair: gpg; deluid
   pair: gpg; fingerprint

   
      
.. _gnupg_cli1_user_id:

=================================================================
``gpg`` user-id commands
=================================================================


   
.. contents::
   :depth: 3   


Setting a Primary User ID (``gpg`` [--options] ``--edit-key`` name | ``primary``)
==================================================================================

If you have multiple User IDs on your key, you may wish to change the User ID 
that is designated as the primary User ID. 

The primary User ID is the User ID that GPG displays by default. 

To change the primary User ID, edit the key (--edit-key) and select the User ID 
that you want to be the primary User ID.


    gpg --edit-key pvergain@gmail.com


GPG uses an asterisk ( * ) to indicate your selection. 

Now issue the primary command to set theUser ID you've selected as the primary 
User ID. 

You'll need to enter your passphrase because you're making changes to your key.


Removing User IDs (``gpg`` [--options] ``--edit-key`` name | ``deluid``)
==========================================================================

Removing User IDs is similar to changing the primary User ID. 

Edit the key (--edit-key), select the User ID you wish to remove...

    gpg --edit-key pvergain@gmail.com


::

    gpg (GnuPG) 2.0.17; Copyright (C) 2011 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    La clé secrète est disponible.

    pub  2048R/A27DB4A0  créé: 2013-07-02  expire: jamais      utilisation: SCE
                          confiance: ultime        validité: ultime
    [  ultime ] (1). pvergain (gpg) <pvergain@gmail.com>
    [  ultime ] (2)  Patrick (Adresse professionnelle) <patrick.vergain@id3.eu>

    gpg> 2

    pub  2048R/A27DB4A0  créé: 2013-07-02  expire: jamais      utilisation: SCE
                          confiance: ultime        validité: ultime
    [  ultime ] (1). pvergain (gpg) <pvergain@gmail.com>
    [  ultime ] (2)* Patrick (Adresse professionnelle) <patrick.vergain@id3.eu>

    gpg> deluid
    Enlever réellement ce nom d'utilisateur ? (o/N) o

    pub  2048R/A27DB4A0  créé: 2013-07-02  expire: jamais      utilisation: SCE
                          confiance: ultime        validité: ultime
    [  ultime ] (1). pvergain (gpg) <pvergain@gmail.com>
    

::

    
    Command> save
    
    
    
Adding User IDs (``gpg`` [--options] ``--edit-key`` name | ``adduid``)
=======================================================================

When you generated your keypair, GPG asked you for a name and email address to 
identify you in the User ID for your public key. 

At some later time, though, you may wish to add another User ID to your key 
(for example, to include a new email address that you use). 

You can add User IDs to your key by editing the key (--edit-key) and using the 
adduid command.

    gpg --edit-key pvergain@gmail.com


::

    gpg (GnuPG) 2.0.20; Copyright (C) 2013 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    La clef secrète est disponible.

    pub  2048R/A27DB4A0  créé: 2013-07-02  expire: jamais      utilisation: SCE
                         confiance: ultime        validité: ultime
    [  ultime ] (1). pvergain (gpg) <pvergain@gmail.com>

    gpg> adduid
    Nom réelá: pour doc
    Adresse électronique: pour.doc@net.eu
    Commentaire:
    Vous avez sélectionné cette identité:
        pour doc <pour.doc@net.eu>

    Faut-il modifier le (N)om, le (C)ommentaire, l'(A)dresse électronique
    ou (O)ui/(Q)uitter? O

    Une phrase de passe est nécessaire pour déverrouiller la clef secrète de
    l'utilisateurá: pvergain (gpg) <pvergain@gmail.com>
    clef RSA de 2048 bits, identifiant A27DB4A0, créée le 2013-07-02


    pub  2048R/A27DB4A0  créé: 2013-07-02  expire: jamais      utilisationá: SCE
                         confiance: ultime        validité: ultime
    [  ultime ] (1). pvergain (gpg) <pvergain@gmail.com>
    [ inconnue] (2)  pour doc <pour.doc@net.eu>

     
Fingerprint Keys (``gpg`` ``--fingerprint`` name)
======================================================

.. seealso::

   - http://www.francoz.net/doc/gpg/x228.html
   - http://doc.ubuntu-fr.org/gnupg


Nous allons maintenant afficher le fingerprint d'une clé.

Le fingerprint est le résultat d'un calcul effectué sur la clé. C'est une sorte 
d'empreinte digitale de la clé. 

**Si deux clés ont le même fingerprint, c'est que les deux clés sont identiques**.

Le fingerprint permet de rapidement vérifier qu'une clé provient bien de la 
personne à qui on pense qu'elle appartient.

Si je fais un échange de clé avec Toto, lorsque Toto me prouvera son identité 
il me donnera son fingerprint. 

Je téléchargerai ensuite une clé correspondant à Toto, et j'en calculerai le 
fingerprint. Si le fingerprint calculé à partir de cette clé est identique à 
celui que m'a donné Toto lors de l'échange, alors je peux faire confiance à 
cette clé. Sinon, c'est que ce n'est pas la vraie clé de Toto.

Pour afficher le fingerprint, il faut importer la clé dans le trousseau.


::

    gpg --fingerprint pvergain@gmail.com
    
::
    
    pub   2048R/A27DB4A0 2013-07-02
    Empreinte de la clef = 44B8 721C E05B D10D 29A8  79EF 8A91 10FE A27D B4A0
    uid                  pvergain (gpg) <pvergain@gmail.com>


        
.. note:: Les 8 derniers caractères du fingerprint correspondent à l'identifiant 
   pub de la clé. 



Pour_ trouver l'empreinte d'une clé, vous pouvez utiliser::

    gpg --fingerprint

qui listera toutes les clés connues avec leur empreinte.

Une fois que vous avez vérifié une clé, vous pouvez l'authentifier pour dire 
**je fais confiance à cette clé...** 

La commande est simplement::

    gpg --sign-key uid
    

où "uid" est l'identité de la clé à authentifier. 


.. _Pour:  http://www.lama.univ-savoie.fr/~hyvernat/Enseignement/0910/info204/tp2.html



