
.. index::
   pair: Firefox ; CertWatch

.. _cert_watch:

===========================
CertWatch
===========================

.. seealso::

   - https://addons.mozilla.org/en-US/firefox/addon/certificate-watch/
   - http://certwatch.simos.info/
   - :ref:`openssl_firefox`


.. contents::
   :depth: 3


Introduction
============

CertWatch is a Firefox add-on that helps you control how digital certificates 
are used when you visit secure websites. 

While there exist tools that help control how, for example, scripts like Javascript 
are executed (NoScript addon), there has not been a tool for digital certificates.

The closest Firefox addon to the functionality of CertWatch is :ref:`Certificate Patrol <certificate_patrol>`, 
which keeps track of website certificates and notifies when a revisited website 
has a different website certificate. 

CertWatch collects more information than Certificate Patrol and keeps track of 
root, intermediate and website certificates, plus visit details.

Once you install CertWatch and restart Firefox, CertWatch will take up to 30 
seconds to parse all root certificates that your Firefox comes with. 

Every secure website that you visit is vouched for by some root certificate 
that pre-exists in Firefox. 

Your Firefox has about 150 of those root certificates, and you can traditionally 
view them in Edit»Preferences»Advanced»Encryption»View Certificates»Authorities.


