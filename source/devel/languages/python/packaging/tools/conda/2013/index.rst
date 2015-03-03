
.. index::
   pair: 2013; Conda
   pair: C ; Linker
   pair: Environments; Namespaces

.. _conda_2013:

=======================
Conda 2013
=======================


.. contents::
   :depth: 3


Why I promote conda (Friday, December 6, 2013)
===============================================

.. seealso::

   - http://technicaldiscovery.blogspot.ca/2013/12/why-i-promote-conda.html
   - http://www.iecc.com/linker/
   

There is nothing you want more as a package author than
users.  So, to make Multipack (SciPy), then NumPy available, I had to become a
packaging expert by experiencing a lot of pain with the lack of
suitable tools for my (**admittedly complex**) task.

If conda had existed back then with standard conda binaries released for 
different projects, there would have been almost no problem at all.   
That pressure would have largely disappeared.   
Just install the packages again --- problem solved for everybody (not 
just the Linux users who had apt-get and yum).


On Mac and Linux package managers exist --- on Windows things like EPD, 
Anaconda or :ref: C.Gohlke's collection <gohlke_collection>` of binaries 
have been the only solution.


Through all of this work, I've cut my fingers and toes and sometimes face on
compilers, shared and staic libraries on all kinds of crazy systems (AIX,
Windows NT, etc.).  I still remember the night I learned what it meant to have
ABI incompatibilty between different compilers (try passing structs
such as complex-numbers between a file compiled with mingw and a library compiled with
Visual Studio).   I've been bitten more than once by unicode-width
incompatibilities, strange shared-library incompatibilities, and the vagaries
of how different compilers and run-times define the `FILE *` file pointer.

In fact, if you have not read "Linkers and Loaders", you should actually do
that right now as it will open your mind to that interesting limbo between
"developer-code" and "running process" overlooked by even experienced
developers.  I'm grateful Dave Beazley recommended it to me over 6 years ago.
Here is a link:  http://www.iecc.com/linker/


We who have been working on this for the past year have decades of 
Python packaging experience between us: 

- me (Travis Oliphant)
- Peter Wang, 
- Ilan Schnell, 
- Bryan Van de Ven, 
- Mark Wiebe, 
- Trent Nelson, 
- Aaron Meurer, 
- and now Andy Terrel 

are all helping improve things.

At the heart of conda package installation is the concept of **environments**.

Environments are like namespaces in Python -- but for binary packages.  Their
applicability is extensive.  We are using them within Anaconda and Wakari for
all kinds of purposes (from testing to application isolation to easy
reproducibility to supporting multiple versions of packages in different
scripts that are part of the same installation).  Truly, to borrow the famous
Tim Peters' quip: "Environments are one honking great idea -- let's do more of
those"


If union filesystems were better implemented in different operating 
systems, then each environment would simply be a union of the untarred 
binary packages.  
Instead we accomplish the same thing with hard-linking, soft-linking, 
and (when necessary) copying of files.


The design is simple, which helps it be easy to understand and easy to
mix with other ideas.  We don't see easily how to take these simple,
powerful ideas and adapt them to .whl and virtualenv which are trying
to fit-in to a world created by distutils and setuptools.  

You can use conda to build your own distribution of binaries that
compete with Anaconda if you like.  Please do.  I would be completely
thrilled if every other Python distribution (python.org, EPD,
ActiveState, etc.) just used conda packages that they build and in so
doing helped improve the conda package manager.  I recognize that
conda emerged at the same time as the Anaconda distribution was
stabilizing and so there is natural confusion over the two


So, I will try to clarify: Conda is an open-source, general,
cross-platform package manager.  One could accurately describe it as a
cross-platform homebrew written in Python.  Anyone can use the tool and
related infrastructure to build and distribute whatever packages they
want.

We have been fixing those minor issues and have now released a version 
of conda that can be 'pip installed'.   

As conda has significant overlap with virtualenv in particular we are 
still working out kinks in the interop of these two solutions.   
But, it all can and should work together and we fix issues as quickly 
as we can identify them.

It is very important to keep in mind that we created conda to solve
the problem of distributing an environment to end-users that allow
them do to advanced data analytics, scientific discovery, and general
engineering work.  Python has a chance to play a major role in this
space.  However, it is not the only player.  Other solutions exist in
the space we are targeting (SAS, Matlab, SPSS, and R).  

**We want Python to dominate this space**.  

We could not wait for the packaging solution we needed to evolve from the 
lengthy discussions that are on-going which also have to untangle the 
history of distutils, setuptools, easy_install, and distribute.  

What we could do is solve our problem and then look for interoperability 
and influence opportunities once we had something that worked for our 
needs. **That the approach we took and I'm glad we did**.  

We have a working solution now which benefits hundreds of thousands of 
users (and could benefit millions more if IT administrators recognized 
conda as an acceptable packaging approach from others in the community).

We are going to keep improving conda until it becomes an obvious
solution for everyone: users, developers, and IT administrators alike.






