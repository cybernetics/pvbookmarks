

.. index::
   pair: github; pvdevtools


.. _pvdevtools_on_github:

=====================
pvdevtools on github
=====================

.. seealso:: https://github.com/pvergain/pvdevtools


.. contents::
   :depth: 3
   

Setup on GNU/linux ubuntu
=========================

.. seealso:: http://help.github.com/linux-set-up-git/

::

	2016  sudo aptitude install git-core
	2017  sudo aptitude install git-gui
	2018  sudo aptitude install git-doc
	2019  cd ~/.ssh
	2020  ls
	2021  mkdir key_backup
	2022  cp id_rsa* key_backup
	2023  rm id_rsa*
	2024  ssh-keygen -t rsa -C "pvergain@gmail.com"
	2025  ssh -T git@github.com
	2026  cd ..
	2027  ssh-add ~/.ssh/id_rsa
	2028  ssh -T git@github.com
	2029  git config --global github.user pvergain
	2030  git config --global github.token 1da1d809f5834bb85ff1efe497ffbf99


Create A Repo
=============

.. seealso:: 

   - http://help.github.com/create-a-repo/
   - https://github.com/repositories/new
   
   
Global setup
-------------

Set up git
+++++++++++

::

	git config --global user.name "Patrick Vergain"
	git config --global user.email pvergain@gmail.com
      
Next steps
++++++++++


::

	cd pvdevtools
	git init
	git add .
	git commit -m 'first commit'
	git remote add origin git@github.com:pvergain/pvdevtools.git
	git push -u origin master   

::

	patrick@vercors:~/projects/devtools_doc$ git push -u origin master
	Counting objects: 9016, done.
	Compressing objects: 100% (7429/7429), done.
	Writing objects: 100% (9016/9016), 23.42 MiB | 27 KiB/s, done.
	Total 9016 (delta 1756), reused 0 (delta 0)
	To git@github.com:pvergain/pvdevtools.git
	 * [new branch]      master -> master
	Branch master set up to track remote branch master from origin.



