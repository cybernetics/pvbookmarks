.. module:: pyQt
    :synopsis: Python pyQt
 
 
.. index::
   python pyqt formlayout
   
=========
pyQt libs
=========

http://code.google.com/p/formlayout/
====================================

formlayout is a tiny Python module for creating form dialogs/widgets to edit 
various type of parameters with having to write any GUI code (it requires 
Python 2.x and PyQt4 4.y, with x  >= 5 and y > 3). 


Installation
------------

formlayout requires Python 2.x and PyQt4 4.y, with x >= 5 and y > 3:

* All supported platforms (GNU/Linux, MacOS and Microsoft Windows XP/Vista): 
  install Python and PyQt4
* Microsoft Windows XP/Vista: note that Python(x,y) (scientific-oriented 
  Python distribution: http://www.pythonxy.com) includes formlayout 
  as a standard plugin 

Installation instructions:
--------------------------

* Python(x,y): nothing to do, it's already included
* Without setuptools: download the .tar.gz file, extract files and type python 
  setup.py install
* With setuptools: simply type easy_install formlayout 

Simple example
--------------

The main feature of formlayout is to provide the fedit function which transforms 
a list of parameters into a GUI-based form (you may also create a list of 
parameter lists - see formlayout.py for more advanced examples)::

	from formlayout import fedit

	datalist = [('Name', 'Paul'),
				('Age', 30),
				('Sex', [0, 'Male', 'Female']),
				('Size', 12.1),
				('Eyes', 'green'),
				('Married', True),
				]

	print "result:", fedit(datalist, title="Describe yourself",
						   comment="This is just an <b>example</b>.")
						   
						   
						   

   




