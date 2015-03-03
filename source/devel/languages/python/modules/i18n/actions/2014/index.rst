
.. index::
   pair: i18n; Python (LC_CTYPE, 2014)

.. _py_i18n_actions_2014:

===========================
python i18n actions 2014
===========================


.. seealso::

   - http://bugs.python.org/issue19977


I modified Python 3.5 to use the "surrogateescape" error handler 
(PEP 383) for stdin and stdout when the LC_CTYPE locale is POSIX 
("C" locale):


New behaviour::

    $ mkdir z
    $ touch z/abcé
    $ LC_CTYPE=C ./python -c 'import os; print(os.listdir("z")[0])'
    abcé


Old behaviour, before the change (test with Python 3.3)::

    $ LC_CTYPE=C python3 -c 'import os; print(os.listdir("z")[0])'
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
    UnicodeEncodeError: 'ascii' codec can't encode characters in position
    3-4: ordinal not in range(128)


The POSIX locale is common because it is used by default when no other
locale is set. It's common that programs started by a crontab on UNIX
and daemons are using this locale.

