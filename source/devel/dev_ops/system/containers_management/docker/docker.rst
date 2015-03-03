
.. index::
   ! Docker


.. _docker:

===============================================================
Docker (Système de conteneur Linux, MacOSX et Windows)
===============================================================

.. seealso::

   - http://www.docker.com/
   - http://docs.docker.com/
   - https://twitter.com/docker
   - http://www.docker.com/community/participate/
   - http://docs-stage.docker.com/
   
   

.. figure:: Docker_logo.png
   :align: center
   

.. contents::
   :depth: 3



Description
===========

.. seealso::

   - https://fr.wikipedia.org/wiki/Docker_%28Syst%C3%A8me_de_conteneur_Linux%29
   
   
``Docker`` est un projet open source qui automatise le déploiement d'applications 
dans des conteneurs logiciels. 

Selon la firme de recherche sur l'industrie 451 Research, « Docker est un outil 
qui peut empaqueter une application et ses dépendances dans un conteneur virtuel, 
qui pourra être exécuté sur n'importe quel serveur Linux ». 

Ceci permet d'étendre la flexibilité et la portabilité d’exécution d'une application, 
que ce soit sur la machine locale, un cloud privé ou public, une machine nue, etc..


.. figure:: docker-use-cases.png
   :align: center
   
   

What is Docker ?
=================


.. seealso::

   - http://docs.docker.com/


``Docker`` is an open platform for developers and sysadmins to build, ship, and run 
distributed applications. 

Consisting of Docker Engine, a portable, lightweight runtime and packaging tool, 
and Docker Hub, a cloud service for sharing applications and automating workflows, 
Docker enables apps to be quickly assembled from components and eliminates the 
friction between development, QA, and production environments. 

As a result, IT can ship faster and run the same app, unchanged, on laptops, 
data center VMs, and any cloud. 


.. seealso::

   - https://stackoverflow.com/questions/16647069/should-i-use-vagrant-or-docker-io-for-creating-an-isolated-environment
   - https://stackoverflow.com/users/2678466/solomon-hykes


It's a common misconception that you can only use Docker on Linux. 

That's incorrect, you can also install Docker on Mac, and Windows support is 
underway (April 2014). 

When installed on Mac, Docker bundles a tiny linux VM (25MB on disk!) which acts 
as a wrapper for your container. 
Once installed this is completely transparent, you can use the docker command-line 
in exactly the same way. This gives you the best of both worlds: you can test 
and develop your application using containers, which are very lightweight, 
easy to test and easy to move around (see for example https://index.docker.io 
for sharing reusable containers with the docker community), and you don't need 
to worry about the nitty-gritty details of managing virtual machines, which are 
just a means to an end anyway.



Source code
===========

.. seealso::

   - https://github.com/dotcloud/docker


Docker, the open-source application container engine.



Why do developers like it ?
============================

With Docker, developers can build any app in any language using any toolchain.

**Dockerized** apps are completely portable and can run anywhere - colleagues’
OS X and Windows laptops, QA servers running Ubuntu in the cloud, and
production  data center VMs running Red Hat.

Developers can get going quickly by starting with one of the 13,000+ apps
available  on Docker Hub.

Docker manages and tracks changes and dependencies, making it easier for
sysadmins  to understand how the apps that developers build work.

And with Docker Hub, developers can automate their build pipeline and share
artifacts with collaborators through public or private repositories.

Docker helps developers build and ship higher-quality applications, faster.


Articles
=============

.. toctree::
   :maxdepth: 3
   
   articles/index
   


Installation
=============

.. toctree::
   :maxdepth: 3
   
   installation/index
 
 

Tools
=============

.. toctree::
   :maxdepth: 3
   
   tools/index
   
   
Tutoriaux
=============

.. toctree::
   :maxdepth: 3
   
   tutoriaux/index         
   
Versions
=============

.. toctree::
   :maxdepth: 3
   
   versions/versions
   
   
   

