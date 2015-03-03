

.. index::
   python mercurial patch
   patch

.. _python_mercurial_patch:

========================
python mercurial patch
========================


::

    "Martin v. Löwis" <martin@v.loewis.de>
    heure de l'expéditeur   Envoyé à 03:31 (GMT-04:00). Heure locale : 08:03. ✆
    à   Nick Coghlan <ncoghlan@gmail.com>
    cc  Python-Dev <python-dev@python.org>
    date    18 mars 2011 03:31
    objet   Re: [Python-Dev] Generating patch files

    I get "unknown revision" (listing the full expression text) when using
    Mercurial 1.6.3 (default version in Ubuntu 10.10).


Based on Baptiste's approach, I propose the script below to compute a patch.
Please report whether it works for you.

Regards,
Martin


.. code-block:: bash


    #!/bin/sh
    base=`hg log --template {rev} -r'max(ancestors(default)-outgoing())'`
    hg diff -r$base



