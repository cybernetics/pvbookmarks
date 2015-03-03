


.. index::
   python data (tablefactory)

===========================
Python tablefactory module
===========================


.. seealso::

   - http://kstrauser.github.com/tablefactory/
   - git clone git://github.com/kstrauser/tablefactory



TableFactory is a simple API for creating tables in popular formats.
It acts as a wrapper around other popular Python report generators and handles
all the tedious, boilerplate problems of extracting columns from input data,
creating the layout, applying formatting to cells, etc.

Why ?
=====

I maintain an internal web application with many reports for our customers.

After writing the code to generate a report's data, I'd have to make custom
backends to write that data out in each of several formats that different
customers might want.

If someone asked me to add a new column to a report, I'd have to add it
separately to each of the output types. That got old quickly.

TableFactory is my solution to the problem. It lets me spend my efforts on
making efficient, useful reports instead of on the boring, repetitive process
of formatting them.

Dependencies
=============

HTML tables are made using only standard Python modules.

Spreadsheets are made with xlwt (http://pypi.python.org/pypi/xlwt).

PDFs are made with ReportLab (http://www.reportlab.com/software/opensource/).


License
=======

TableFactory is available under the permissive MIT License.



