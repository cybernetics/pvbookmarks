
.. index::
   pair: Fabfile; Tips

.. _fabric_tips:

===============
Fabric tips
===============

.. seealso::

   - http://docs.fabfile.org/en/1.6/tutorial.html

.. contents::
   :depth: 3
   
Starters
========


For starters, perhaps we want to run our tests and commit to our VCS so we’re 
ready for a deploy::

    from fabric.api import local

    def prepare_deploy():
        local("./manage.py test my_app")
        local("git add -p && git commit")
        local("git push")


The code itself is straightforward: import a Fabric API function, local, and 
use it to run and interact with local shell commands. 
The rest of Fabric’s API is similar – it’s all just Python.


Organize it your way
====================

Because Fabric is “just Python” you’re free to organize your fabfile any way 
you want. 
For example, it’s often useful to start splitting things up into subtasks::

    from fabric.api import local

    def test():
        local("./manage.py test my_app")

    def commit():
        local("git add -p && git commit")

    def push():
        local("git push")

    def prepare_deploy():
        test()
        commit()
        push()




