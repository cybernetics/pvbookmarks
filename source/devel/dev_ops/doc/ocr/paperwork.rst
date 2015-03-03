

.. index::
   pair: OCR; Paperwork
   pair: Python; Paperwork
   ! Paperwork


.. _paperwork:

======================================
Paperwork
======================================

.. seealso::

   - http://github.com/jflesch/paperwork.git
   - https://raw.github.com/jflesch/paperwork/master/README.markdown
   - http://www.tiramiseb.fr/


.. contents::
   :depth: 3

Description
===========

Paperwork is a tool to make papers searchable.

The basic idea behind Paperwork is "scan & forget" : You should be able 
to just scan a new document and forget about it until the day you need 
it again. Let the machine do most of the work.


Details
========

Papers are organized into documents. Each document contains pages.

It uses mainly 3 other pieces of software:

* Sane: To scan the pages
* Cuneiform or Tesseract: To extract the words from the pages (OCR)
* GTK/Glade: For the user interface

Page orientation is automatically guessed using OCR.

Paperwork uses a custom indexation system to search documents and to 
provide keyword suggestions. 

Since OCR is not perfect, and since some documents don't contain useful 
keywords, Paperwork allows also to put labels on each document.


Licence
========

GPLv3. See COPYING.


Dependencies
============

* python v2.7<br/>
  Paperwork is written for Python **2.7**.
  So depending of your Linux distribution, you may have to invoke "python2"
  instead of "python" (for instance with Arch Linux)
* pygi (required):
    * Debian/Ubuntu package: python-gi
* gtk v3 (required)
    * Debian/Ubuntu package: gir1.2-gtk-3.0
* gladeui (required)
    * Debian/Ubuntu package: gir1.2-gladeui-2.0
* pycountry (required)
    * Debian/Ubuntu package: python-pycountry
* python-imaging (aka PIL) (required)
    * Debian/Ubuntu package: python-imaging
* poppler (required)
    * Debian/Ubuntu package: gir1.2-poppler-0.18
* Python Cairo bindings for the GObject library (required):
    * Debian/Ubuntu package: python-gi-cairo
* python-enchant (required)
    * Debian/Ubuntu package: python-enchant
* python-levenshtein (required)
    * Debian/Ubuntu package: python-levenshtein
* python-whoosh (required)
    * Debian/Ubuntu package: python-whoosh
* pyinsane (required)
    * Debian/Ubuntu package: none at the moment
    * Manual installation:
        * git clone git://github.com/jflesch/pyinsane.git
        * cd pyinsane
        * sudo python ./setup.py install
* OCR (optional for document searching ; required for scanning)
    * Tesseract (>= v3.01) (recommended)
        * Debian/Ubuntu package: tesseract-ocr tesseract-ocr-<your language>
    * **Or** Cuneiform (>= v1.1)
        * Debian/Ubuntu package: cuneiform
* pyocr (required)
    * Debian/Ubuntu package: none at the moment
    * Manual installation:
        * git clone git://github.com/jflesch/pyocr.git
        * cd pyocr
        * sudo python ./setup.py install


Installation
=============


::

    sudo aptitude install python-gi python-pycountry python-imaging gir1.2-poppler-0.18 python-enchant python-levenshtein tesseract-ocr tesseract-ocr-fra


::

    sudo pip install Whoosh

pyinsane
---------

::

    $ git clone git://github.com/jflesch/pyinsane.git
    $ cd pyinsane
    $ sudo python ./setup.py install
    $ cd ..
    
pyocr
-----
    
    $ git clone git://github.com/jflesch/pyocr.git
    $ cd pyocr
    $ sudo python ./setup.py install

paperwork
---------

::

    $ git clone git://github.com/jflesch/paperwork.git
    $ cd paperwork
    $ sudo python ./setup.py install
    $ paperwork

Enjoy :-)

