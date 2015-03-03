
.. index::
   pair: password; generator
   pair: password; checker


.. _password_generator:

==========================
Python password generator
==========================

.. seealso::

   - http://code.activestate.com/recipes/578169-extremely-strong-password-generator/
   - :ref:`password_libraries`


This is an pretty improved version of the generator written by Isendrak Skatasmid
- simple-password-generator. I have introduced few changes in the algorithm.

Also, the entire set of special characters is not being used. Sometimes passwords
that start with special-characters or numbers are generated. I am not sure whether
that is a bad thing.

A few links that I had used to test the password strength are:

- `How Secure Is My Password`_
- `Password Meter`_
- `Password Strength Checker`_

You are welcome to comment/criticize/suggest improvements for the implementation.


.. _`How Secure Is My Password`: http://howsecureismypassword.net/
.. _`Password Meter`:  http://www.passwordmeter.com/
.. _`Password Strength Checker`:  http://www.caeus.com/utilities/password-strength-checker.php


:download:`Télécharger le fichier password_generator.py <password_generator.py>`

.. literalinclude:: password_generator.py
   :language: python
   :linenos:


