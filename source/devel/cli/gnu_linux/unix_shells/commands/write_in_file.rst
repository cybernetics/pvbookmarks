

.. index::
   cli (write in file with python)

.. _write_in_file_with_python:

==========================
write in file with python
==========================


.. seealso:: http://hg.piranha.org.ua/sphinxedhg/docs/test-hgrc.html

Write in a file with python

::

  $ TEST=`pwd`/test_insert.txt
  $ export TEST

::

    python -c "print '[foo]\nbar = a\n b\n c \n  de\n fg \nbaz = bif cb \n'" >  $TEST



