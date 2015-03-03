.. module:: lafargue_smart_tools  
    :synopsis: lafargue smart tools  


.. index::
   lafargue smart tools 

   
========================
lafargue smartcard tools 
========================

.. seealso:: 

   - https://www.lafargue.name/smart-tools/index.html
   - https://www.lafargue.name/smart-tools/atr/
   - http://www.sconnect.com/FAQ/index.html


https://www.lafargue.name/smart-tools/index.html
================================================
   
Before anything else, two things:

* This page contains tools which will give you advanced access, 
  in particular to French Navigo cards: you must be aware that 
  absolutely NO restricted documents were used in the process of 
  building these tools: only standard and publicly available 
  information was used.
* Second, though these tools use a technology called SConnect 
  which is developed by Gemalto, Gemalto is not associated at all 
  to these tools and their capabilities.


..  index::
    sconnect
	
	
Sconnect
========
  
http://www.sconnect.com/FAQ/index.html
--------------------------------------
  
SConnect is a smart card agnostic browser extension for major web 
browsers for Windows, Mac OS X and Linux operating systems. 
The primary purpose of SConnect is to provide a connectivity b
ridge between JavaScript that runs in a rendered web page in 
browser and a smart card.
   
  
How does SConnect help solving the aforementioned problems ?
------------------------------------------------------------

Coming up with abstractions in software has always been a challenge. 
Some abstractions work really well and some abstractions leak. 
The cryptographic abstraction used by browsers to access smart 
card functionality unfortunately leak in the context of web applications. 
They were primarily conceived to be used with client applications and find 
themselves very stretched in a different context. SConnect addressees this 
problem of leaky abstractions by moving down the the abstraction stack and 
to use an abstraction that targets smart cards. This abstraction stack 
fortunately is the same across operating systems and is an industry standard. 
It is known as PC/SC. The implementation of this standard is installed by 
default on all operating system images and exposes the same API as mandated.


What SConnect does is that it helps the JavaScript that runs in the browser 
access the PC/SC layer of the operating system. This enables programming 
the logic of accessing applications in a smart card through a cross browser 
consistent and simple interface via JavaScript. Using this approach one can 
write the logic that was earlier implemented as compiled binaries, partially 
in JavaScript and partially in a server side language of your choice 
(ASP.NET, PHP, Java, Python, etc). Not only does the end user experience 
get enhanced multi-fold, this technique also does not have the limitations 
of the classical architecture.  



     
   

   

   