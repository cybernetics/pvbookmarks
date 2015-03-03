

.. _python_docker_1_decembre_2013:

===========================================================
Python projects dependencies with Docker 1er december 2013
===========================================================


.. seealso::

   - https://jpetazzo.github.io/2013/12/01/docker-python-pip-requirements/


.. contents::
   :depth: 3

Description
============


There are many ways to handle Python app dependencies with Docker. 

Here is an overview of the most common ones -- with a twist.

In our examples, we will make the following assumptions:

- you want to write a Dockerfile for a Python app;
- the code is directly at the top of the repo (i.e. there's a setup.py file at 
  the root of the repo);
- your app requires Flask (and possibly other dependencies).


