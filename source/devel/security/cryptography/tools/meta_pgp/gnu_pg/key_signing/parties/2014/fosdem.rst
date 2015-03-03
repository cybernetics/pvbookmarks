
.. index::
   pair: 2014; Key signing

.. _fosdem_2014_key_signing:

===============================
Fosdem 2014 key signing
===============================

.. seealso::

   - https://fosdem.org/2014/keysigning/
   - https://ksp.fosdem.org/
   - https://ksp.fosdem.org/graphs/
   - https://ksp.fosdem.org/files/



Keysigning
===========

The annual keysigning event at FOSDEM is one of the largest of its kind. 
With more than one hundred participants every year, it is an excellent opportunity 
to strengthen the web of trust. 

We use a slightly modified version of the Zimmermann-Sassaman key-signing protocol 
relying on a key submission server rather than email to collect keys.

Before the event
================

Submit your keys
----------------

If you intend to participate in the PGP keysigning event at FOSDEM 2014, you 
must submit the keys you would like to have signed to the keyserver listening 
on ksp.fosdem.org. 

If you are using GnuPG, this can easily be accomplished with::

    gpg --keyserver ksp.fosdem.org --send-key [keyid]

You may want to verify that your submission made it to the keyserver by checking 
the list of submitted keys at https://ksp.fosdem.org/.

During the submission period, graphs will be generated of the density of the 
web of trust and the rate at which keys are being submitted. 

You can find these graphs at: https://ksp.fosdem.org/graphs/

The deadline for submissions is Monday, 27 January 2014. After this date, the 
keyserver will no longer accept submissions and the official keylist will be 
published.

Download the list of participants
----------------------------------

The list of participants has not yet been published !

If you are participating in the keysigning event (i.e.: you have submitted your 
key to the keyserver), you should download the final list of participants and 
follow its instructions closely.

The final list of participants will be available from https://ksp.fosdem.org/files/.

If there is a trust-path between you and the author, you should verify the list's 
detached signature using:::

    gpg --verify ksp-fosdem2014.txt.asc ksp-fosdem2014.txt

The keysigning event takes place on Sunday, at 14:00, in the corridor on the 
second level of the U building. 
Please bring the printed list, a pen and appropriate form of identification 
with you to FOSDEM. Be on time!

After the event
===============

The hashes of the keylist have not been published yet.

If you participated in the keysigning event, but missed (parts of) the participant 
list hashes as they flashed by during the starting presentation, you should 
verify the hashes before signing any keys.

You will be able to download the hashes from https://ksp.fosdem.org/files/. 

If there is a trust-path between you and the author, you should verify the 
file's detached signature using:

    gpg --verify ksp-fosdem2014-hashes.txt.asc ksp-fosdem2014-hashes.txt

Please complete your signing homework before Sunday, 8 June 2014, and upload 
new signatures on your keys to a well-connected keyserver. 

New statistics of the density of the web of trust at FOSDEM will be published 
soon after that date. 


