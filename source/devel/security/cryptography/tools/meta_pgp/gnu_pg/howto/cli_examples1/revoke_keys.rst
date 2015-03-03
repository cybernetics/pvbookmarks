
.. index::
   pair: GnuPG; gen-revoke

   
      
.. _gnupg_cli1_revoke:

=================================================================
``gpg`` revoke commands
=================================================================


   
.. contents::
   :depth: 3   


Revoking Keys (``gpg`` [--options] ``--gen-revoke`` name)
==========================================================

At some point in the future you may wish to revoke your key so that no one can 
use it to encrypt email to you. 

Perhaps your secret key has been compromised; or perhaps you've generated 
another keypair and prefer to use that key instead. 

Whatever the case, you'll need a revocation certificate (which is a special 
kind of signature) for the key. 

You can then import that revocation certificate onto your keyring to revoke 
the key. You can also distribute the revocation certificate to others in order 
to revoke copies of your public key that you previously distributed.

You ought to consider generating a revocation certificate immediately after 
creating your keypair. 

You need not import that revocation certificate; you can simply store it for 
future use. Revocation certificates are especially useful if you've forgotten 
the passphrase to your secret key and you need some way to "disable" or revoke 
that key. Since you've forgotten the passphrase, the only way to revoke the key 
will be with a revocation certificate that you generated earlier (when you still 
remembered the passphrase). 

In a way, a revocation certificate is a kind of insurance plan that lets you 
keep ultimate control over your key, even if you lose or forget the passphrase.

You can generate a revocation certificate by using the ``--gen-revoke`` command and 
specifying the key for which you want a revocation certificate generated. 

Use the ``--output`` option to specify an output file for the revocation certificate::

    gpg --output pvergain_revoke.asc --gen-revoke pvergain@gmail.com




::


    gpg --output pvergain_revoke.asc --gen-revoke pvergain@gmail.com


::


    sec  2048R/A27DB4A0 2013-07-02 pvergain (gpg) <pvergain@gmail.com>

    Générer un certificat de révocation pour cette clé ? (o/N) o
    choisissez la cause de la révocation:
      0 = Aucune raison spécifiée
      1 = La clé a été compromise
      2 = La clé a été remplacée
      3 = La clé n'est plus utilisée
      Q = Annuler
    (Vous devriez sûrement sélectionner 1 ici)
    Votre décision ? 0
    Entrez une description optionnelle ; terminez-là par une ligne vide:
    > Pour documenter la commande gen-revoke
    >
    Cause de révocation: Aucune raison spécifiée
    Pour documenter la commande gen-revoke
    Est-ce d'accord ? (o/N) o

    Vous avez besoin d'une phrase de passe pour déverrouiller la
    clé secrète pour l'utilisateur: pvergain (gpg) <pvergain@gmail.com>
    clé de 2048 bits RSA, ID A27DB4A0, créée le 2013-07-02

    sortie avec armure ASCII forcée.
    Certificat de révocation créé.

    Déplacez-le dans un support que vous pouvez cacher ; si Mallory a
    accès à ce certificat il peut l'utiliser pour rendre votre clé
    inutilisable.
    Une bonne idée consiste à imprimer ce certificat puis à le stocker
    ailleurs, au cas où le support devient illisible. Mais attention :
    le système d'impression de votre machine pourrait stocker ces
    données et les rendre accessibles à d'autres personnes !
    
    
    
