
.. index::
   pair: Linux; Password Cracking
   

.. _cibercity_john:

=====================================================================================
Linux Password Cracking: Explain unshadow and john commands ( john the ripper tool ) 
=====================================================================================

.. seealso::

   - http://www.cyberciti.biz/faq/unix-linux-password-cracking-john-the-ripper/

.. contents::
   :depth: 3   
   
   

How do I use John the ripper to check weak passwords / crack passwords ?
========================================================================

First use the unshadow command to combines the /etc/passwd and /etc/shadow 
files so John can use them. 

You might need this since if you only used your shadow file, the GECOS 
information wouldn’t be used by the "single crack" mode, and also you 
wouldn’t be able to use the -shells option. On a normal system you’ll 
need to run unshadow as root to be able to read the shadow file. 

So login as root or use old good sudo su command under Debian/Ubuntu Linux::
        
    sudo /usr/sbin/unshadow /etc/passwd /etc/shadow > /tmp/crack.password.db
