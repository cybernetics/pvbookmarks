
.. index::
   pair: gpg; gen-key

   
      
.. _gnupg_cli1_gen_key:

=================================================================
``gpg`` gen-key commands
=================================================================


   
.. contents::
   :depth: 3   



Key Generation (``gpg`` [--options] ``--gen-key``)
===================================================

Before you can receive encrypted messages and files from others or digitally 
sign files and messages to send to others, you must generate a keypair for yourself. 

A keypair consists of:

- a public key which others use to encrypt messages to  you and to verify 
  signatures that you make 
- and a secret key (often called a private key) which you use to decrypt messages 
  sent to you by others and to sign files and messages that you send to others. 
  (For more information on encryption, ciphers, and keys, see the GNU Privacy Handbook.)

The key generation process in GPG involves several steps and requires you to 
make a several important decisions along the way. 

We start the key generation process with the ``--gen-key`` command.


::

    gpg --gen-key


::


    gpg (GnuPG) 2.0.17; Copyright (C) 2011 Free Software Foundation, Inc.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Sélectionnez le type de clé désiré:
       (1) RSA and RSA (default)
       (2) DSA and Elgamal
       (3) DSA (signature seule)
       (4) RSA (signature seule)
    Votre choix ? 1
    les clés RSA peuvent faire entre 1024 et 4096 bits de longueur.
    Quelle taille de clé désirez-vous ? (2048)
    La taille demandée est 2048 bits
    Spécifiez combien de temps cette clé devrait Ûtre valide.
             0 = la clé n'expire pas
          <n>  = la clé expire dans n jours
          <n>w = la clé expire dans n semaines
          <n>m = la clé expire dans n mois
          <n>y = la clé expire dans n années
    La clé est valide pour ? (0) 0
    La clé n'expire pas du tout
    Est-ce correct ? (o/N) o

    You need a user ID to identify your key; the software constructs the user ID
    from the Real Name, Comment and Email Address in this form:
        "Heinrich Heine (Der Dichter) <heinrichh@duesseldorf.de>"

    Nom réel: Patrick Vergain
    Adresse e-mail: patrick.vergain@id3.eu
    Commentaire: id3 Technologies
    Vous avez sélectionné ce nom d'utilisateur:
        "Patrick Vergain (id3 Technologies) <patrick.vergain@id3.eu>"

    Changer le (N)om, le (C)ommentaire, l'(E)-mail ou (O)K/(Q)uitter ? O
    Vous avez besoin d'une phrase de passe pour protéger votre clé
    secrète.


    Un grand nombre d'octets aléatoires doit Ûtre généré. Vous devriez faire
    autre-chose (taper au clavier, déplacer la souris, utiliser les disques)
    pendant la génération de nombres premiers; cela donne au générateur de
    nombres aléatoires une meilleure chance d'avoir assez d'entropie.
    Un grand nombre d'octets aléatoires doit Ûtre généré. Vous devriez faire
    autre-chose (taper au clavier, déplacer la souris, utiliser les disques)
    pendant la génération de nombres premiers; cela donne au générateur de
    nombres aléatoires une meilleure chance d'avoir assez d'entropie.
    gpg: clé B45AD1F6 marquée comme ayant une confiance ultime.
    les clés publique et secrète ont été créées et signées.

    gpg: vérifier la base de confiance
    gpg: 3 marginale(s) nécessaires, 1 complète(s) nécessaires, modèle
    de confiance PGP
    gpg: profondeur: 0  valide:   2  signé:   5
    confiance: 0-. 0g. 0n. 0m. 0f. 2u
    gpg: profondeur: 1  valide:   5  signé:   1
    confiance: 4-. 0g. 0n. 0m. 1f. 0u
    gpg: profondeur: 2  valide:   1  signé:   0
    confiance: 1-. 0g. 0n. 0m. 0f. 0u
    gpg: la prochaine vérification de la base de confiance aura lieu le 2014-03-28
    pub   2048R/B45AD1F6 2014-01-09
        Empreinte de la clé = 7DF3 26DE 3F6B 0F1C 301A  35A3 0901 81D4 B45A D1F6
    uid                  Patrick Vergain (id3 Technologies) <patrick.vergain@id3.eu>
    sub   2048R/93AB32A8 2014-01-09
