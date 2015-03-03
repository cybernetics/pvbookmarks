
.. index::
   hg revert
   hg backout

=========
hg revert
=========


- http://hgbook.red-bean.com/read/finding-and-fixing-mistakes.html



[Python-Dev] Useful page in the Hg book by Nick Coghlan <ncoghlan@gmail.com>
============================================================================

::


    Nick Coghlan <ncoghlan@gmail.com>
    à   python-dev@python.org
    date    17 mars 2011 00:09
    objet   [Python-Dev] Useful page in the Hg book


As I'm sure there will be plenty of erring as we get used to Hg:
http://hgbook.red-bean.com/read/finding-and-fixing-mistakes.html

For simple cases of attempting to push a single commit that gets
rejected by the server, hg rollback/hg pull/hg commit/hg push/ may
provide a cleaner history than doing a dummy merge.

hg backout also further emphasises the benefits of working in feature
branches - I was able to revert the default branch in my sandbox to
match upstream by backing out a single changeset.

Cheers,
Nick.


