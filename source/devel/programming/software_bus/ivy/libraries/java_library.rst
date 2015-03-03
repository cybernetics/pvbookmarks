

.. index::
   ivy (Java library)
   Java (Swing)
   Java (Ivy)
   
   
.. _ivy_java_library:

================
ivy Java library
================

.. seealso:: 

   - http://www2.tls.cena.fr/products/ivy/documentation
   - http://www2.tls.cena.fr/products/ivy/documentation/ivy-java/index.html
   - http://www2.tls.cena.fr/products/ivy/download/packages/IvyGUIMonitor.jar


.. index::
   main loop (swing thread)
   
Ivy and swing GUI
=================

.. seealso:: http://www2.tls.cena.fr/products/ivy/download/packages/IvyGUIMonitor.jar


Swing requires the code to run in the main swing thread. In order to avoid 
problems, be sure tu use the SwingUtilities.invokeLater() or 
SwingUtilities.invokeAndWait() methods if you Ivy callbacks impact swing 
components. 

Java sources
============

::

    svn co http://svn.tls.cena.fr/svn/ivy/ivy-java/trunk
    
    

