

.. index::
   pair: mercurial; hgrc

===========================
Mercurial hgrc examples
===========================

::

    [paths]
    default = https://pvergain@bitbucket.org/pvergain/devtools_doc

    [ui]
    username = Patrick Vergain <pvergain@gmail.com>
    verbose = True


    [diff]
    git = on
    showfunc = on

    [extensions]
    color=
    # enable hg glog
    graphlog=
    pager=
    progress=
    rebase=
    record=
    # enable hg strip
    mq=


    [color]
    # vim colors (bg=dark theme)
    diff.diffline = green bold
    diff.file_a = green bold
    diff.file_b = green bold
    diff.hunk = yellow bold
    diff.deleted = red bold
    diff.inserted = cyan bold

    [pager]
    # less -F: quit if one screen
    # less -S: chop long lines
    # less -R: raw (keep colors)
    # less -X: no init (don't see termcap init sequences)
    pager = LESS='FSRX' less

    [merge-patterns]
    ** = internal:merge

    [hostfingerprints]
    bitbucket.org=81:2b:08:90:dc:d3:71:ee:e0:7c:b4:75:ce:9b:6c:48:94:56:a1:fe
