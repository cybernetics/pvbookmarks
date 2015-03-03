
.. index::
   pair: mercurial; hgrc
   pair: git; gitconfig

===========================
Mercurial hgrc examples
===========================

::

    Sujet:  Re: [Afpy-membres] Présentation + atelier Git sur Paris ?
    Date :  Sun, 2 Oct 2011 01:50:19 +0200
    De :    Victor Stinner <victor.stinner@haypocalc.com>
    Pour :  Liste de diffusion des membres de l'association <afpy-membres@lists.afpy.org>


Pour ceux que ça intéresse, voici mes configurations git & hg :

- https://bitbucket.org/haypo/misc/src/tip/conf/gitconfig
- https://bitbucket.org/haypo/misc/src/tip/conf/hgrc


.. index::
   hgrc (Victor Stinner)

.. _hgrc_victor_stinner:

hgrc de Victor Stinner
======================

.. seealso:: https://bitbucket.org/haypo/misc/src/tip/conf/hgrc

::

    [ui]
    username = Victor Stinner <victor.stinner@haypocalc.com>
    verbose = True

    # on commit, hgeditor opens an editor with the diff for the changelog
    # http://selenic.com/hg/raw-file/tip/hgeditor
    editor = /home/haypo/bin/hgeditor

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
    # enable hg histedit: https://bitbucket.org/durin42/histedit/src
    hg_histedit=

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

Mercurial a besoin d'être débridé en activant plein d'options et extensions
que ça soit utilisable de base. Mais avec la bonne config, il y a des moins en
moins de différences entre git & hg. Les développeurs hg m'ont par exemple dit
qu'ils ont (enfin !) implémenté la syntaxe rev^, rev^n, rev~n, ... Et un autre
développeur m'a dit qu'avec la prochaine version de Mercurial, le rebase aura
des performances correct (grâce à un nouveau format de stockage).

Les commandes que j'utilise couramment ::

    git log [fichier] <=> hg log [fichier]
    git blame [fichier] <=> hg blame [fichier]
    git st <=> hg st
    git diff [fichier] <=> hg diff [fichier]
    git ci <=> hg ci
    git add -i [fichier] <=> hg record [fichier]
    git rebase -i rev <=> hg histedit rev
    git out <=> hg out
    git pull --rebase && git push <=> hg pull --rebase && hg push

**Mort aux commits de merge (de Mercurial) ! Rebase for the win!**

Victor

(pour "git out" j'ai "triché" avec mon ~/.gitconfig)


.. index::
   gitconfig (Victor Stinner)

.. _gitconfig_victor_stinner:

gitconfig de Victor Stinner
===========================

.. seealso:: https://bitbucket.org/haypo/misc/src/tip/conf/gitconfig


::

    [color]
    diff = auto
    ui = auto

    [user]
    name = Victor Stinner
    email = victor.stinner@haypocalc.com

    [alias]
    out = log remotes/origin/master..HEAD --pretty='format:%Cred%h%Creset %s' --color
    ci = commit -v --untracked-files=no
    st = status
    rebasei = rebase -i remotes/origin/master

    # Add "&& true" to not pass command line options to the last command
    # eg. git svnup --help doesn't pass --help option to svn rebase
    svnout = log git-svn..HEAD --pretty='format:%Cred%h%Creset %s' --color
    svnup = !git svn rebase && true
    svnci = !git svn rebase && git svn dcommit && true
    svnrebase = rebase -i git-svn


.. index::
   git config
   vimdiff
   vim


Conseils d'Aurélien Bompard
===========================

::

    Date :  Sun, 2 Oct 2011 08:55:01 +0200
    De :    Aurelien Bompard <aurelien@bompard.org>
    Répondre à :    Liste de diffusion des membres de l'association <afpy-membres@lists.afpy.org>
    Pour :  afpy-membres@lists.afpy.org

> (pour "git out" j'ai "triché" avec mon ~/.gitconfig)

Tu as "git cherry -v" qui ressemble un peu à ce que tu fais (mais sans la
couleur à ma connaissance).

> git pull --rebase && git push <=> hg pull --rebase && hg push
> Mort aux commits de merge (de Mercurial) ! Rebase for the win!

Pour le faire automatiquement tu peux aussi faire un::

    git config branch.master.rebase true
    git config branch.autosetuprebase always

La première ligne ajoutera "--rebase" automatiquement sur tes pull, et la
seconde règlera cette option sur les nouvelles branches que tu pourrais
créer.

Au passage, je vois aussi que tu utilises color.ui = auto. Il se peut que le
pager ait du mal à afficher les couleurs dans le terminal, auquel cas il
faut que tu ajoutes::

    git config --global core.pager "less -FXRS"

(tu l'as fait dans ta conf Mercurial)

Et enfin, il est toujours bon d'ajouter::

    git config --global core.editor vim
    git config --global merge.tool vimdiff


parce que bon, quand même, faut pas déconner. (je reste dans le ton du thread)

Aurélien

