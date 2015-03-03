
.. index::
   pair: Secure Sockets Layer ; SSL
   pair: SSL; BREACH
   pair: Authentication; Web
   ! SSL
   ! TLS

.. _ssl:
.. _tls:

============================================================
Secure Sockets Layer (SSL) , Transport Layer Security (TLS)
============================================================


.. seealso::

   - http://en.wikipedia.org/wiki/Transport_Layer_Security
   - http://fr.wikipedia.org/wiki/Transport_Layer_Security
   - https://www.ssllabs.com/index.html


.. contents::
   :depth: 3


Introduction
============

Transport Layer Security (TLS), et son prédécesseur Secure Sockets Layer 
(SSL), sont des protocoles de sécurisation des échanges sur Internet, 
développé à l'origine par Netscape (SSL version 2 et SSL version 3). 

Il a été renommé en Transport Layer Security (TLS) par l'IETF suite au 
rachat du brevet de Netscape par l'IETF en 2001. 

Le groupe de travail correspondant à l'IETF a permis la création des 
RFC 2246 pour le TLS et RFC 4347 pour son équivalent en mode datagramme, 
le DTLS. 

Depuis son rapatriement par l'IETF, le protocole TLS a vécu deux révisions 
subséquentes : 

- TLSv1.1 décrite dans la RFC 4346 et publiée en 2006 
- et TLSv1.2, décrite par la RFC 5246 et publiée en 2008.



Attack
======

SSL, GONE IN 30 SECONDS A BREACH beyond CRIME (Browser Reconnaissance & Exfiltration via Adaptive Compression of Hypertext) 
----------------------------------------------------------------------------------------------------------------------------

.. seealso::

   - http://breachattack.com/
   - http://en.wikipedia.org/wiki/CRIME_%28security_exploit%29
   
   

Test
====

.. seealso::

   - https://www.ssllabs.com/ssltest/
   
   
Advices
=======

::

    Pip uses the same base set of certificates as firefox ships with. 
    
    However a problem i've seen is if your server is not set to serve 
    all the intermediate certificates firefox will attempt to traverse 
    the chain downloading each one as it needs to until it finds one in 
    the certificate store. Pip on the other hand does not do this and 
    expects your server to properly be serving all the intermediate 
    certificates.
    If your internal server is publically available you can run it against 
    https://www.ssllabs.com/ssltest/ and look for errors in the 
    Authentication section.   



Tools 
=====

.. toctree::
   :maxdepth: 3
   
   tools/index
   
   
   


