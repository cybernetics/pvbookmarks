
.. index::
   pair: gpg; Keys
   pair: gpg; list-secret-keys
   pair: gpg; list-keys

   
      
.. _gnupg_cli1_list:

=================================================================
``gpg`` list commands
=================================================================


   
.. contents::
   :depth: 3   


Listing Public Keys (``gpg`` [--options] ``--list-keys``)
===========================================================

You can see the public keys that are on your keyring with the ``--list-keys`` command::


    gpg --list-keys
    

::     


    C:/Users/pvergain/AppData/Roaming/gnupg/pubring.gpg
    ---------------------------------------------------
    pub   2048R/A27DB4A0 2013-07-02
    uid                  pvergain (gpg) <pvergain@gmail.com>
    uid                  Patrick (Adresse professionnelle) <patrick.vergain@id3.eu>
    pub   1024D/6A45C816 2003-09-24
    uid                  Anthony Baxter <anthony@interlink.com.au>
    uid                  Anthony Baxter <anthony@python.org>
    uid                  Anthony Baxter <anthony@ekit-inc.com>
    sub   1024g/C974A028 2003-09-24
    pub   1024R/ED9D77D5 1997-12-08
    uid                  Barry A. Warsaw <barry@warsaw.us>
    uid                  Barry A. Warsaw <barry@wooz.org>
    uid                  Barry A. Warsaw <barry@zope.com>
    uid                  Barry A. Warsaw <barry@python.org>
    uid                  Barry A. Warsaw <barry@digicool.com>
    uid                  Barry A. Warsaw <bwarsaw@beopen.com>
    uid                  Barry A. Warsaw <bwarsaw@python.net>
    uid                  Barry A. Warsaw <bwarsaw@python.org>
    uid                  Barry A. Warsaw <bwarsaw@cnri.reston.va.us>
    sub   1024D/BB3C3203 2000-07-07
    sub   1024g/4CC9779E 2000-07-07
    sub   1024g/8DF91D04 2000-11-29

    pub   2048R/6F5E1540 2011-01-15
    uid                  Ned Deily <nad@acm.org>
    sub   2048R/25DF8957 2011-01-15

    pub   1024D/7D9DC8D2 2002-12-18
    uid                  Martin v. Löwis <martin@v.loewis.de>
    sub   2048g/D1BE5048 2002-12-18

    pub   2048D/36580288 2010-07-31
    uid                  Georg Brandl (Python release signing key) <georg@python.org>
    sub   2048g/E779804A 2010-07-31

    pub   1024D/A4135B38 2008-03-01
    uid                  Benjamin Peterson <benjamin@python.org>
    uid                  Benjamin Peterson <gutworth@users.sourceforge.net>
    uid                  Benjamin Peterson <musiccomposition@gmail.com>
    sub   4096g/B930B46A 2008-03-01

    pub   4096R/18ADD4FF 2013-10-09
    uid                  Benjamin Peterson <benjamin@python.org>
    sub   4096R/4CB4FCA4 2013-10-09

    pub   2048D/D8FB6105 2010-07-27 [expire: 2014-03-28]
    uid                  Sam Tuke <samtuke@owncloud.com>
    uid                  Sam Tuke <mail@samtuke.com>
    uid                  Sam Tuke <samtuke@fsfe.org>
    sub   4096g/2444E47D 2010-07-27


``gpg`` tells us that both keys are public keys (pub). For each key GPG also 
tells us the key length (2048 or 1024), the key type (R for RSA, D for DSA, 
g for ElGamal), the Key IDs, as well as the creation dates and the User IDs. 


Listing Secret Keys (``gpg`` [--options] ``--list-secret-keys``)
==================================================================

You can see the secret keys on your keyring with the ``--list-secret-keys`` command::

    gpg --list-secret-keys

::

    C:/Users/pvergain/AppData/Roaming/gnupg/secring.gpg
    ---------------------------------------------------
    sec   2048R/A27DB4A0 2013-07-02
    uid                  pvergain (gpg) <pvergain@gmail.com>
    uid                  Patrick (Adresse professionnelle) <patrick.vergain@id3.eu>

