
.. index::
   pair: Python; PGP

.. _python_pgp:

===============================
python-gnupg (Python PGP)
===============================

.. seealso::

   - https://github.com/isislovecruft/python-gnupg
   - https://python-gnupg.readthedocs.org/en/latest/index.html



Fork of [python-gnupg-0.3.2](https://code.google.com/p/python-gnupg/), patched
to fix a potential vulnerability which could result in remote code execution,
do to unsanitised inputs being passed to ```subprocess.Popen([...], shell=True)```.
