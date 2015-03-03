
.. index::
   pair: gpg ; symmetric
   pair: gpg; decrypt
   
      
.. _gnupg_sign_sym:

=================================================================
``gpg`` symmetric command 
=================================================================


.. contents::
   :depth: 3


Symmetric Encryption (gpg [--options] --symmetric file)
========================================================

You can encrypt files using symmtric encryption (as opposed to public key encryption) 
with the --symmetric command. 

You will be prompted for a passphrase to protect the key used to encrypt the file::


    gpg --armor --symmetric f.txt
    

::

    dir f*


::

    09/01/2014  16:44                30 f.txt
    09/01/2014  17:13               203 f.txt.asc


With symmetric encryption, you encrypt and decrypt files with the same key 
(which GPG generates and protects with the passphrase you supply). 

By contrast, the --encrypt command uses asymmetric encryption: you encrypt files 
with other people's public keys, and they decrypt with their secret (or private) 
keys. 

(For more information on symmetric vs. asymmetric encryption, see the GNU Privacy Handbook.) 

Symmetric encryption is useful if you don't plan to deliver or distribute the 
files to other people. 

**For example, you may simply want to protect sensitive files on your own hard 
drive** (not distribute them to other people).


You can combine the --symmetric command with the --output or --armor options, 
just like the --encrypt command.

(For more information on using symmetric encryption, see the GNU Privacy Handbook.)


Decryption (``gpg`` [--options] ``--decrypt`` file)
====================================================

To decrypt an encrypted file, use the ``--decrypt`` command. 

The ``--decrypt`` command should be used no matter whether you have received 
that file from someone else (who encrypted with the ``--encrypt`` command it using 
your public key), or whether you encrypted the file yourself with symmetric 
encryption by using the --symmetric command. 

If the file was encrypted to your public key with the ``--encrypt`` command, 
``gpg`` asks you for the passphrase for your secret key (often called a private key).

::

    gpg --output f2.txt  --decrypt f.txt.gpg
    

::

    gpg: données chiffrées avec CAST5
    gpg: chiffré avec 1a phrase de passe
    gpg: Attention: l'intégrité du message n'était pas protégée




If you encrypted the file yourself with symmetric encryption (``--symmetric``), 
``gpg`` asks for the passphrase that you assigned to the file. 



