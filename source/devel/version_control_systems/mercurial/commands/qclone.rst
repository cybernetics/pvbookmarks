
.. index::
   hg qclone


.. _hg_qclone:

=========
hg qclone
=========


.. seealso::

   - http://mercurial.selenic.com/wiki/MqMerge

::

    de  rndblnch <rndblnch@gmail.com>
    à   python-dev@python.org
    date    24 mars 2011 15:31
    objet   Re: [Python-Dev] Let's get PEP 380 into Python 3.3



::

    > > Anyone without push rights for hg.python.org may want to fork the
    > > mirror the bitbucket folks set up during the PyCon sprints to avoid
    > > having to push the whole repository up to a separate hosting site:
    > > https://bitbucket.org/mirror/cpython
    >
    > Done here:
    > <https://bitbucket.org/rndblnch/cpython-pep380/>


Now that I have figured out how to use patch queues with bitbucket, I will
maintain greg's pep380 implementation as a patch on top of cpython here:
<https://bitbucket.org/rndblnch/cpython-pep380/>

Testing it should be as simple as::

    % hg qclone https://bitbucket.org/rndblnch/cpython-pep380
    % cd cpython-pep380
    % hg qpush pep380

and then the usual ./configure etc.


To test on an already existing clone of <http://hg.python.org/cpython>::

    % hg clone http://hg.python.org/cpython
    % cd cpython
    % hg update -C default

you should enable mq extension...::

    % hg init --mq

get the pep380 patch and apply it...::

    % pushd .hg/patches/
    % hg pull https://bitbucket.org/rndblnch/cpython-pep380/.hg/patches
    % hg update
    % popd
    % hg qpush pep380

and then the usual ./configure etc.


The patch is now visible here:
<https://bitbucket.org/rndblnch/cpython-pep380/qseries?apply=t&qs_apply=pep380>

Hope this helps,
