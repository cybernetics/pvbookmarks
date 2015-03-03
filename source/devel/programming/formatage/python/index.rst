

.. index::
   pair: Formatage; Python


.. _python_formatage:

==================================
Python Formatage
==================================


.. seealso:: http://msdn.microsoft.com/fr-fr/library/fht0f5be%28v=vs.80%29.aspx


Formatage de byte
=================


::


    from smartcard.util import toHexString
    from smartcard.util import HEX


    print "Command = ", toHexString(Command, HEX)



Résultat
--------

::

    Len command=12: Command=[0x3A 0x0 0x0 0x0 0x4 0x0 0x0 0x0 0x7 0x0 0x0 0x0 ]



BinStringToHexList
====================


::


    from smartcard.util import toHexString
    from smartcard.util import HEX
    from smartcard.util import BinStringToHexList


    print "Command =",
    for elem in command:
        print ord(elem),
    print
    c0 = BinStringToHexList(command)
    print "Command c0= ", c0
    c1 = toHexString(c0, HEX)
    print "Command c1= ", c1


Résultat
--------

::

    Command = 58 0 0 0 4 0 0 0 7 0 0 0
    Command c0=  [58, 0, 0, 0, 4, 0, 0, 0, 7, 0, 0, 0]
    Command c1=  0x3A 0x00 0x00 0x00 0x04 0x00 0x00 0x00 0x07 0x00 0x00 0x00


Smartcard.util.py
==================


.. seealso:: http://pyscard.svn.sourceforge.net/viewvc/pyscard/trunk/pyscard/src/smartcard/util/__init__.py?revision=596&view=markup


.. literalinclude::  smartcard_util.py
   :encoding: latin-1
