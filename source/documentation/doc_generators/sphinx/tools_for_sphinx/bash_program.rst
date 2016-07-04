
.. index::
   pair: Sphinx building; Bash


.. _bash_program:

=========================================
Automatically-build-sphinx-documentation
=========================================

.. seealso::

   - http://www.hackzine.org/posts/2011/09/11/automatically-build-sphinx-documentation


.. code-block:: bash

	#!/bin/bash
	## Automatically build Sphinx documentation upon file change
	## Copyright (c) 2011 Samuele ~redShadow~ Santi - Under GPL
	 
	WORKDIR="$( dirname "$0" )"
	while :; do
		## Wait for changes
		inotifywait -e modify,create,delete -r "$WORKDIR"
		## Make html documentation
		make -C "$WORKDIR" html
	done
