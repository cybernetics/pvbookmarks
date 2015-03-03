


.. _csharp_fingerprint_verification_framework_1:


===============================================
A Framework in C# for Fingerprint Verification
===============================================


By Octavio Loyola-González, Miguel Angel Medina Pérez, Andres Eduardo Gutierrez Rodriguez, 
Milton García Borroto, 18 Apr 2014 


Introduction
=============

Fingerprint recognition is an active research area nowadays. 

An important component in fingerprint recognition systems is the fingerprint 
matching algorithm. 

According to the problem domain, fingerprint matching algorithms are classified 
in two categories: fingerprint verification algorithms and fingerprint 
identification algorithms. 

The aim of fingerprint verification algorithms is to determine whether two 
fingerprints come from the same finger or not. 

On the other hand, the fingerprint identification algorithms search a query 
fingerprint in a database looking for the fingerprints coming from the same finger.

There are hundreds of papers concerning to fingerprint verification but, as far 
as we know, there is not any framework for fingerprint verification available 
on the web. 

So, you must implement your own tools in order to test the performance of your 
fingerprint verification algorithms. Moreover, you must spend a lot of time 
implementing algorithms of other authors to compare with your algorithms. 

This was our motivation to put our fingerprint verification framework available 
for everyone.

The most closely related work to our framework is the `FVC-onGoing web`_ system. 


.. _`FVC-onGoing web`:   https://biolab.csr.unibo.it/fvcongoing/UI/Form/Home.aspx


Our framework is implemented in C# with .Net Framework for two main reasons. 

First, C# has become one of the most popular programming languages. 

Second, the technologies, tools and class libraries available on .Net Framework 
save us a lot of time of coding.

