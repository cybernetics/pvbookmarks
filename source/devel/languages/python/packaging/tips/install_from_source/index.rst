

.. index;;
   pair: Distributions; Installation

.. _python_install_from_source:


======================================================================================
Installation de distributions locales à un environnement virtuel à partir des sources
======================================================================================

.. seealso::

   - :ref:`python_virtualenv`
   
 
.. contents::
   :depth: 3 
 
But
====

Dans les grosses boites, l'accès internet est souvent inexistant ou interdit.
Il faut donc installer les distributions Python à partir du code source.



pip freeze > requirements.txt
==================================================

Dans un premier temps, on récupère la liste des distributions installées
dans l'environnement virtuel Python courant.


::

    (eurocopter) >pip freeze > requirements.txt
 
    
::

    Django==1.5.1
    Jinja2==2.7
    MarkupSafe==0.18
    Pygments==1.6
    South==0.7.6
    Unipath==1.0
    diff-match-patch==20120106
    django-debug-toolbar==0.9.4
    django-import-export==0.1.3
    django-model-utils==1.3.1
    docutils==0.10
    pytz==2013b
    tablib==0.9.11


    
Sauvegarder les distributions dans un répertoire 'distributions'
================================================================

Sur son ordinateur connecté à internet on télécharge le code source compressé
des distributions Python.


::

    mkdir distributions
    pip install --download=distributions -r requirements.txt
    
    
On obtient
==========

::

    (eurocopter) c:\Tmp>dir distributions\
     Le volume dans le lecteur C s'appelle OS
     Le numéro de série du volume est 46AD-0A9C

     Répertoire de c:\Tmp\distributions

    30/10/2013  14:08    <DIR>          .
    30/10/2013  14:08    <DIR>          ..
    30/10/2013  14:07            54 099 diff-match-patch-20120106.tar.gz
    30/10/2013  14:07         8 028 963 Django-1.5.1.tar.gz
    30/10/2013  14:07           150 062 django-debug-toolbar-0.9.4.tar.gz
    30/10/2013  14:08            17 898 django-import-export-0.1.3.tar.gz
    30/10/2013  14:08            29 005 django-model-utils-1.3.1.tar.gz
    30/10/2013  14:08         1 602 552 docutils-0.10.tar.gz
    30/10/2013  14:07           377 603 Jinja2-2.7.tar.gz
    30/10/2013  14:07            11 748 MarkupSafe-0.18.tar.gz
    30/10/2013  14:07         1 423 161 Pygments-1.6.tar.gz
    30/10/2013  14:08           199 509 pytz-2013b.tar.bz2
    30/10/2013  14:07            91 528 South-0.7.6.tar.gz
    30/10/2013  14:08           571 410 tablib-0.9.11.tar.gz
    30/10/2013  14:07            29 306 Unipath-1.0.tar.gz
                  13 fichier(s)       12 586 844 octets
         
         

Pour installer ces distributions sans avoir accès à internet chez le client
============================================================================


On lance le fichier install.bat:


::


    pip install distributions\Django-1.5.1.tar.gz
    pip install distributions\diff-match-patch-20120106.tar.gz
    pip install distributions\django-debug-toolbar-0.9.4.tar.gz
    pip install distributions\tablib-0.9.11.tar.gz
    pip install distributions\django-import-export-0.1.3.tar.gz
    pip install distributions\django-model-utils-1.3.1.tar.gz
    pip install distributions\docutils-0.10.tar.gz
    pip install distributions\Jinja2-2.7.tar.gz
    pip install distributions\MarkupSafe-0.18.tar.gz
    pip install distributions\Pygments-1.6.tar.gz
    pip install distributions\pytz-2013b.zip
    pip install distributions\South-0.7.6.tar.gz
    pip install distributions\Unipath-1.0.tar.gz

                     
                  
    

    


