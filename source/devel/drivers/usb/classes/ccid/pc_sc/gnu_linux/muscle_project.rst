.. module:: PCSC_muscle 
    :synopsis: pcsc muscle 

    
.. index::
    MUSCLE
    ScardIntroduceCardType()
    ATR
    http://smartcard-atr.appspot.com/
    
===========
pcsc muscle
===========

Le projet MUSCLE ou la bibliothèque PC/SC Lite.

.. seealso:: GNU/Linux magazine N° 39, p.18 de Ludovic Rousseau et David Corcoran.


.. _ATR_muscle:

ATR
===

Windows identifie une carte en fonction de son ATR (Answer to Reset).

C'est avec l'ATR qu'une carte est entrée dans la base (de registres) avec ScardIntroduceCardType().

Le problème est que de nos jours une carte à puce est une plateforme (JavaCard, .NET ou même MULTOS)
sur laquelle il est possible de charger plusieurs applications.


.. seealso:: http://smartcard-atr.appspot.com/


The parsing code is part of pyscard and is available at `parseATR.py <http://pyscard.svn.sourceforge.net/viewvc/pyscard/trunk/contrib/parseATR/parseATR.py?view=markup>`_ 
The list of known ATR is also available online at `smartcard_list.txt <http://ludovic.rousseau.free.fr/softwares/pcsc-tools/smartcard_list.txt>`_. 


