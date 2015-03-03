
.. index::
   pair: python; Strings


.. _python_strings:

==================================================
Strings: Use the % operator for formatting strings
==================================================

Use the % operator for formatting strings, even when the parameters are all
strings.

Use your best judgement to decide between + and % though.

No::

    x = '%s%s' % (a, b)  # use + in this case
    x = imperative + ', ' + expletive + '!'
    x = 'name: ' + name + '; score: ' + str(n)

Yes::

     x = a + b
     x = '%s, %s!' % (imperative, expletive)
     x = 'name: %s; score: %d' % (name, n)

Avoid using the + and += operators to accumulate a string within a loop.
Since strings are immutable, this creates unnecessary temporary objects and
results in quadratic rather than linear running time.

Instead, add each substring to a list and ''.join the list after the loop
terminates (or, write each substring to a cStringIO.StringIO buffer).

No::

    employee_table = '<table>'
    for last_name, first_name in employee_list:
        employee_table += '<tr><td>%s, %s</td></tr>' % (last_name, first_name)
    employee_table += '</table>'

Yes::

     items = ['<table>']
     for last_name, first_name in employee_list:
         items.append('<tr><td>%s, %s</td></tr>' % (last_name, first_name))
     items.append('</table>')
     employee_table = ''.join(items)

Use """ for multi-line strings rather than '''.

.. note:: however, that it is often  cleaner to use implicit line joining
   since multi-line strings do not flow with  the indentation of the rest of
   the program.

No::

		print """This is pretty ugly.
	Don't do this.
	"""

Yes::


    print ("This is much nicer.\n"
         "Do it this way.\n")
