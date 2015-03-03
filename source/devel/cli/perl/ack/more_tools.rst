


.. _ack_more_tools:

===============
ack more tools
===============

.. seealso::

   - http://beyondgrep.com/more-tools/


.. contents::
   :depth: 3

Tools that work with ack
=========================

vim integration
----------------

.. seealso::

   -  http://www.vim.org/scripts/script.php?script_id=2572

ack.vim provides an interface between ack and the vim text editor. 

For example, you can call :Ack foo, which will run ack and load ack's results 
into a vim buffer for manipulation and navigation.

ack.vim is available at the official vim website at http://www.vim.org/scripts/script.php?script_id=2572 


Other grep-like tools
======================

There are many ways to search source code that are more flexible and tuned to 
programmers than straight grep. 

I suggest you take a look at some of these alternatives, for they may suit your 
needs better than ack. 

If you have any suggestions to add to this list, please let me know at andy@petdance.com.

Ag, the Silver Searcher
------------------------

Geoff Greer says "Ag is like ack, but better. It’s fast. It’s damn fast. 

The only thing faster is stuff that builds indices beforehand, like Exuberant Ctags." 

Geoff has also created a fork of AckMate that uses Ag instead of ack.

https://github.com/ggreer/the_silver_searcher


grin
-----

.. seealso::

   - :ref:`grin` 


"A grep program configured the way I like it", written in Python by Robert Kern.


nak
----

.. seealso::

   - https://github.com/gjtorikian/nak

An implementation of ack, written in :ref:`Node.js <nodejs>`. 

It has inspiration from Ag, and is optimized for speed, not features. 

It's completely asynchronous. Written by Garen J. Torikian.


pss
----

.. seealso::

   - :ref:`pss` 
   

pss is an ack clone written in Python by Eli Bendersky. 

It's written in pure Python with no additional modules necessary.



Indexing tools
===============

Sometimes when you're looking at a large codebase, it makes sense to see 
everything as a whole. 

An indexing tool may help you out.

ctags
-----

ctags is a program almost as old as time itself. 

When run against a codebase, ctags indexes various elements of the code, such 
as variables and functions. 
This lets your editor or other tools use the tags index to jump quickly to that 
element.

The most common ctags implementation is Exuberant ctags: http://ctags.sourceforge.net/


cscope
------


.. seealso::

   - http://cscope.sourceforge.net/

Cscope is a developer's tool for browsing source code. 

Cscope was part of the official AT&T Unix distribution for many years, and has 
been used to manage projects involving 20 million lines of code. 

It also can integrate with vim and Emacs.

CodeQuery
----------

.. seealso::

   - https://github.com/ruben2020/codequery 


CodeQuery indexes and queries C, C++, Java and Python source code. 

It builds upon the databases of cscope and ctags, mentioned above, and provides 
a nice GUI tool.


