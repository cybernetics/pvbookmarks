

.. index::
   pair: Python ; Grin
   pair: Search ; Grin
   ! Grin


.. _grin:

====================
Grin
====================


.. seealso::

   - https://pypi.python.org/pypi/grin


A grep program configured the way I like it.

I wrote grin to help me search directories full of source code. 

The venerable GNU grep and find are great tools, but they fall just a little 
short for my normal use cases.

The main problem I had with GNU grep is that I had no way to exclude certain 
directories that I knew had nothing of interest for me, like .svn/, CVS/ and build/. 

The results from those directories obscured the results I was actually 
interested in. 

There are tools like ack, which skip these directories, but ack also only 
grepped files with extensions that it knew about. 

Furthermore, it had not implemented the context lines feature, which I had grown 
accustomed to. Recent development has added these features, but I had already 
released grin by the time I found out.

One can construct a GNU find command that will exclude .svn/ and the rest, but 
the only reliable way I am aware of runs grep on each file independently. 

The startup cost of invoking many separate grep processes is relatively large.

Also, I was bored. It seems to be catching. Perl has ack, Ruby has rak, and 
now Python has grin.

I wrote grin to get exactly the features I wanted:

- Recurse directories by default.
- Do not go into directories with specified names.
- Do not search files with specified extensions.
- Be able to show context lines before and after matched lines.
- Python regex syntax (one can quibble as to whether this is a feature or my 
  laziness for using the regex library provided with my implementation language, 
  but as a Python programmer, this is the syntax I am most familiar with).
- Unless suppressed via a command line option, display the filename regardless 
  of the number of files.
- Accept a file (or stdin) with a list of newline-separated filenames. 
  This allows one to use find to feed grin a list of filenames which might have 
  embedded spaces quite easily.
- Grep through gzipped text files.
- Be useful as a library to build custom tools quickly.

I have also exposed the directory recursion logic as the command-line tool 
"grind"  in homage to find. 

It will recurse through directories matching a glob pattern to file names and 
printing out the matches. 

It shares the directory and file extension skipping settings that grin uses.

For configuration, you can specify the environment variables GRIN_ARGS and 
GRIND_ARGS. 

These should just contain command-line options of their respective programs. 

These will be prepended to the command-line arguments actually given. 

Options given later will override options given earlier, so all options explicitly 
in the command-line will override those in the environment variable. 

For example, if I want to default to two lines of context and no skipped directories, 
I would have this line in my bashrc::

    export GRIN_ARGS="-C 2 --no-skip-dirs"
    
    

