

.. index::
   pair: Svn; Ignore


.. .svnignore:

========================
.svnignore
========================

.. seealso::

   - https://github.com/github/gitignore
   - http://sethholloway.com/blog/2011/03/10/svnignore-example-for-java/



Introduction
============

.. seealso::

   - https://github.com/github/gitignore
   - http://sethholloway.com/blog/2011/03/10/svnignore-example-for-java/


.svnignore is my attempt to create the equivalent of .gitignore. 

After creating the file I had to set the svn:ignore property before it 
worked::

    svn propset svn:ignore -F .svnignore .

First, a little background: my PhD work uses Sun (Oracle) SPOT devices *
that run the Java Squawk VM (kinda like Java ME). 

For version control, we use Subversion. 

In keeping with good version control practices, I want to avoid putting 
binary and compiled files into version control. 

The easiest way to do this is a solid .svnignore file. I spent a few 
minutes trying to find a .svnignore example for Java and could not find 
anything, so I built one myself based on several examples I saw.


