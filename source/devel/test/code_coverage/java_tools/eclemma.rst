
.. index::
   pair: Coverage; EclEmma
   ! EclEmma


.. _eclemma:

=========================
EclEmma
=========================


.. seealso::

   - http://www.eclemma.org/
   - http://emma.sourceforge.net/


Overview
=========

EclEmma is a free Java code coverage tool for Eclipse, available under the 
Eclipse Public License. 

It brings code coverage analysis directly into the Eclipse workbench:

- Fast develop/test cycle: Launches from within the workbench like JUnit test 
  runs can directly be analyzed for code coverage.
- Rich coverage analysis: Coverage results are immediately summarized and 
  highlighted in the Java source code editors.
- Non-invasive: EclEmma does not require modifying your projects or performing 
  any other setup.

Since version 2.0 EclEmma is based on the JaCoCo code coverage library. 

The Eclipse integration has its focus on supporting the individual developer 
in an highly interactive way. 

For automated builds please refer to JaCoCo documentation for integrations 
with other tools.

Originally EclEmma was inspired by and technically based on the great EMMA 
library developed by Vlad Roubtsov.

The update site for EclEmma is http://update.eclemma.org/. 

EclEmma is also available via the Eclipse Marketplace Client, simply search 
for "EclEmma".


Launching
==========

EclEmma adds a so called launch mode to the Eclipse workbench. 

It is called Coverage mode and works exactly like the existing Run and Debug 
modes. The Coverage launch mode can be activated from the Run menu or the 
workbench's toolbar: 


   



