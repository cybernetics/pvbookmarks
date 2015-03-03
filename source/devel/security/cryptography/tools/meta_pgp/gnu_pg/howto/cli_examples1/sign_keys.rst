
.. index::
   pair: GnuPG; Signing
   pair: gpg ; sign-key

   
      
.. _gnupg_sign_keys:

=================================================================
``gpg`` sign keys commands
=================================================================



.. _gpg_signing_keys:

Signing Keys (``gpg`` [--options] ``--sign-key`` name)
======================================================

.. seealso::

   - :ref:`key_signing`


One of the more important things you will do with keys is sign them. 

You'll recall that when you generated your own keypair, ``gpg`` used your 
secret key (or private key) to sign your public key (an act known as **self-signing**). 

**You can use your secret key to sign other people's public keys as well**. 

Signing other people's keys is important because it certifies those keys as 
trusted and integrates them into the Web of Trust used by ``gpg`` and PGP.

When you sign and certify someone else's public key, you are making a statement 
about your confidence that the public key you're signing actually belongs to 
the person specified in the User ID for that key. 

By signing someone's public key, you are building the Web of Trust for the keys 
on your own keyring and contributing to the Web of Trust for the larger 
community ``gpg`` and PGP users. 

Until you sign someone's public key and change the trust level associated with 
that key, ``gpg`` will warn you that the key is untrusted whenever you use that 
key to verify signatures or encrypt files and messages (see the note on 
Understanding Signatures & Trust above for a discussion of this warning). 

(For more information on signing keys and using the Web of Trust, see the GNU Privacy Handbook.)

Before signing someone's key, you should validate it. 

Validating a key means that you have checked with the owner of the key 
(identified in the User ID) and verified that the key that you have is in fact 
that person's key. 

Ideally, you would contact the key owner and check the key fingerprint on the 
key you have against the key fingerprint the owner has. 

(A key's fingerprint is preferable to the Key ID, even the long version of the 
Key ID, as there is the remote chance the multiple keys can have the same Key ID.) 

You can get the key fingerprint either by using the ``--fingerprint`` command::


    gpg --fingerprint pvergain@gmail.com

::


    pub   2048R/A27DB4A0 2013-07-02
        Empreinte de la clé = 44B8 721C E05B D10D 29A8  79EF 8A91 10FE A27D B4A0
    uid                  pvergain (gpg) <pvergain@gmail.com>
    uid                  Patrick (Adresse professionnelle) <patrick.vergain@id3.eu>




.. or by editing the key (``--edit-key``) and using the fpr command::

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

    gpg> fpr
    pub   2048R/A27DB4A0 2013-07-02 pvergain (gpg) <pvergain@gmail.com>
     Empreinte de la clé principale: 44B8 721C E05B D10D 29A8  79EF 8A91 10FE A27D B4A0


Once you have validated the key, you can sign it. 


To sign someone's public key on your keyring, use the ``--sign-key`` command and 
specify the key you want to sign. 

GPG will ask you how carefully you have checked the identity of the person 
specified in the key's User ID::

    gpg --sign-key nad@acm.org

    pub  2048R/6F5E1540  créé: 2011-01-15  expire: jamais      utilisation: SC
                          confiance: inconnu       validité: inconnu
    sub  2048R/25DF8957  créé: 2011-01-15  expire: jamais      utilisation: E
    [ inconnue] (1). Ned Deily <nad@acm.org>


    pub  2048R/6F5E1540  créé: 2011-01-15  expire: jamais      utilisation: SC
                          confiance: inconnu       validité: inconnu
    Empreinte de la clé principale: C9B1 04B3 DD3A A72D 7CCB  1066 FB99 2128 6F5E 1540

         Ned Deily <nad@acm.org>

    Etes-vous vraiment sûr(e) que vous voulez signer cette clé
    avec votre clé  pvergain (gpg) <pvergain@gmail.com> ╗ (A27DB4A0)

    Signer réellement ? (o/N) o

    Vous avez besoin d'une phrase de passe pour déverrouiller la
    clé secrÞte pour l'utilisateur:  pvergain (gpg) <pvergain@gmail.com> 
    clé de 2048 bits RSA, ID A27DB4A0, créée le 2013-07-02


Listing Signatures (``gpg`` [--options] ``--list-sigs`` names)
===============================================================

You can view a list of the signatures on public keys with the ``--list-sigs`` command::


    gpg --list-sigs samtuke@fsfe.org
    
    
::
    
    gpg: vérifier la base de confiance
    gpg: 3 marginale(s) nécessaires, 1 complète(s) nécessaires, modèle de confiance PGP
    gpg: profondeur: 0  valide:   1  signé:   5
    confiance: 0-. 0g. 0n. 0m. 0f. 1u
    gpg: profondeur: 1  valide:   5  signé:   1
    confiance: 4-. 0g. 0n. 0m. 1f. 0u
    gpg: profondeur: 2  valide:   1  signé:   0
    confiance: 1-. 0g. 0n. 0m. 0f. 0u
    gpg: la prochaine vérification de la base de confiance aura lieu le 2014-03-28
    pub   2048D/D8FB6105 2010-07-27 [expire: 2014-03-28]
    uid                  Sam Tuke <samtuke@owncloud.com>
    sig 2        3B90C658 2012-09-03  [Nom utilisateur introuvable]
    sig 3        D8FB6105 2012-03-28  Sam Tuke <samtuke@owncloud.com>
    sig          8450377F 2012-05-16  [Nom utilisateur introuvable]
    sig          FD74DBDF 2012-05-16  [Nom utilisateur introuvable]
    sig          A27DB4A0 2014-01-09  pvergain (gpg) <pvergain@gmail.com>
    uid                  Sam Tuke <mail@samtuke.com>
    sig          797EBFAB 2011-04-01  [Nom utilisateur introuvable]
    sig 2        3B90C658 2012-09-03  [Nom utilisateur introuvable]
    sig 3        D8FB6105 2010-07-27  Sam Tuke <samtuke@owncloud.com>
    sig 3        D8FB6105 2012-03-28  Sam Tuke <samtuke@owncloud.com>
    sig          E7AD5568 2011-04-01  [Nom utilisateur introuvable]
    sig          E2BF04F6 2012-02-06  [Nom utilisateur introuvable]
    sig          FD74DBDF 2011-09-16  [Nom utilisateur introuvable]
    sig          8450377F 2011-10-05  [Nom utilisateur introuvable]
    sig          A27DB4A0 2014-01-09  pvergain (gpg) <pvergain@gmail.com>
    uid                  Sam Tuke <samtuke@fsfe.org>
    sig 2        3B90C658 2012-09-03  [Nom utilisateur introuvable]
    sig 3        D8FB6105 2012-03-28  Sam Tuke <samtuke@owncloud.com>
    sig          8450377F 2012-05-16  [Nom utilisateur introuvable]
    sig          FD74DBDF 2012-05-16  [Nom utilisateur introuvable]
    sig          A27DB4A0 2014-01-09  pvergain (gpg) <pvergain@gmail.com>
    sub   4096g/2444E47D 2010-07-27
    sig          D8FB6105 2010-07-27  Sam Tuke <samtuke@owncloud.com>


Checking Signatures (``gpg`` [--options] ``--check-sigs`` names)
=================================================================

You can view a list of the signatures on public keys and verify those signatures 
with the ``--check-sigs`` command::

    gpg --check-sigs samtuke@owncloud.com





