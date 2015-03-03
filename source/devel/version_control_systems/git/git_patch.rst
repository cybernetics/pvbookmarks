
.. index::
   git patch

=========
git patch
=========



Using my favourite git version control system, I submitted my first patch to GNOME
for gcompris via bugzilla .
Patch [#185360] Manual description error in /math/numeration/magic_hat_minus Bug
[#607080] : http://bugzilla-attachments.gnome.org/attachment.cgi?id=185360
Bug Report[#646961] Modification of skin does not affect gcompris configuration :
https://bugzilla.gnome.org/show_bug.cgi?id=646961

Steps to create patch :

1) Cloning the Gcompris repository::

    git clone git://git.gnome.org/gcompris

2) To check the current branch::

    git branch
    *master

3) Create a new branch for the patch::

    git checkout -n srishti

4)Again recheck the branch::

    git branch
    *master
    srishti

5)Performing alterations

6)To check the alterations perform::

    git diff

7)To commit all the changes in the branch::

    git commit -a


8)And finally perform format patch command::

    git format-patch master --stdout > new.patch







