
.. index::
   pair: Qt; QTemporaryFile
   ! QTemporaryFile



.. _qTemporaryFile:

===================
QTemporaryFile
===================

.. seealso::

   - http://qt-project.org/doc/qt-5.0/qtcore/qtemporaryfile.html


.. contents::
   :depth: 3

Detailed Description
=====================


The QTemporaryFile class is an I/O device that operates on temporary files.

QTemporaryFile is used to create unique temporary files safely. 

The file itself is created by calling open(). 

The name of the temporary file is guaranteed to be unique (i.e., you are 
guaranteed to not overwrite an existing file), and the file will subsequently 
be removed upon destruction of the QTemporaryFile object. 

**This is an important technique that avoids data corruption for applications that 
store data in temporary files**. 

The file name is either auto-generated, or created based on a template, which 
is passed to QTemporaryFile's constructor.

Example::

    // Within a function/method...

    QTemporaryFile file;
    if (file.open()) {
        // file.fileName() returns the unique file name
    }

    // The QTemporaryFile destructor removes the temporary file
    // as it goes out of scope.

Reopening a QTemporaryFile after calling close() is safe. For as long as the 
QTemporaryFile object itself is not destroyed, the unique temporary file will 
exist and be kept open internally by QTemporaryFile.

The file name of the temporary file can be found by calling fileName(). 
Note that this is only defined after the file is first opened; the function 
returns an empty string before this.

