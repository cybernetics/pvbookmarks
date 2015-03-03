

.. index::
   pair: Office Suite; Joeffice


.. _joeffice:

=========================
Joeffice
=========================

.. figure:: joeffice.png
   :align: center

.. seealso::

   - https://bitbucket.org/agoubard/joeffice/
   - http://www.joeffice.org/
   - http://www.framablog.org/index.php/post/2013/06/20/joffice-anthony-goubard


.. contents::
   :depth: 3

Joeffice - The community
=========================

Project page on bitbucket: https://bitbucket.org/agoubard/joeffice/.
Product page (download, screenshots): http://www.joeffice.com.


Introdcution
============

Joeffice is an open source office suite written in Java
How can you contribute to Joeffice:

- Tell your friends about this project/software for example using the share 
  button or posting a message about it.
- Like Joeffice on facebook
- Provide feedback of what could be improved in the software or website.
- Creating templates and documents using Joeffice and post your achievements 
  online.
- Contributing to the code
- Writing documentation
- Translate the software

Code contribution
==================

Are you a developer and would like to improve this project, here are the clues:

- Install Netbeans 7.3 or higher.
- Checkout the project from Bitbucket (Menu -> Team -> Mercurial -> Clone Other -> https://agoubard@bitbucket.org/agoubard/joeffice)

Contribute to one of the library that Joeffice is using: 

- `Apache-POI <http://poi.apache.org/>`_ 
- The Netbeans Platform, 
- H2, 
- Batik, 
- SwingX

.. _joeffice_coding_conventions:

Code convention for Joeffice are the following
===============================================

.. seealso::

   - http://www.oracle.com/technetwork/java/javase/documentation/codeconvtoc-136057.html


- :ref:`Oracle Java code convention <oracle_java_coding_standard>`
- No limitation to 80 columns (readability is more important)
- All classes should have Javadoc at the top, telling what the class is about.
- Unneeded code should be removed. (e.g. unneeded constructors, unneeded final 
  keywords, unneeded this., ...)
- The code is based on Java 7 so use Java 7 features
- Indentation is 4 spaces
- No logic in if statements (e.g. if (file.save()) ...)
- Avoid long methods and long classes. Look at principles such as SRP, DRY, KISS.
- No need to provide unit tests but check that opening a file doesn't fail
- No need to create `one issue`_ per change. 
  Just create one issue for all changes and attach a patch file. In the issue 
  describe what you have/will improve and fix. 
  All code will be reviewed and the remarks will go in the issue.


.. _`one issue`:  https://bitbucket.org/agoubard/joeffice/issues?status=new&status=open

Here are a few suggestions to what could be improved
-----------------------------------------------------

- Support for getting charts, pictures positions and cell spanning in Apache-POI sheets
- Graphics: icons for files, for the application and for the different actions (especially for the toolbars)
- Translation in different language (Bundle.properties in the different packages)
- Look also at the bug/RFE database

For translation in other languages, please wait for the Beta stage of Joeffice 
to do it.

Contact me (info@japplis.com) if you want to propose yourself for a specific language.

