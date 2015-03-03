

.. index::
   pair: Python ; Bootstrap
   ! Bootstrap


.. _bootstrap:

====================
Bootstrap
====================

.. seealso::

   - https://bitbucket.org/pypa/bootstrap
   - :ref:`python_pep_0439`


.. contents::
   :depth: 3

Introduction
============


The pip / setuptools bootstrap to be included in Python 3.4+ and back-ported 
to Python 2.6+. 

http://python.org/dev/peps/pep-0439/ 


History
========

::

    Richard Jones <r1chardj0n3s@gmail.com> via python.org 
    à:	 disutils-sig <distutils-sig@python.org>
    date:	 10 juillet 2013 05:16
    objet:	 [Distutils] PEP 439 and pip bootstrap updated


[firstly, my apologies for posting the announcement yesterday of the pip bootstrap 
implementation and PEP updates to the pypa-dev list instead of distutils-sig... 
I blame PyCon AU exhaustion :-)]

Firstly, I've just made some additional changes to PEP 439 to include:

- installing virtualenv as well (so now pip, setuptools and virtualenv are installed)
- mention the possibility of inclusion in a future Python 2.7 release
- clarify the SSL certificate situation

The bootstrap code has also been updated to:

- not run the full pip command if it's "pip3 install setuptools" or either of 
  the other two packages it has just installed (thus preventing a possibly 
  confusing message to the user)
- also install virtualenv

The intention is that the pip, setuptools and actually all Python projects will 
promote a single bootstrap process:

    "pip3 install setuptools" or "pip3 install Django"

And then there's instructions for getting "pip" if it's not installed. 
Exact wording etc. to be determined :-)

The original message I sent to pypa-dev yesterday is below:

The bootstrap that I wrote at the PyCon AU sprints to implement PEP 439 has 
been added to pypa on bitbucket:

https://bitbucket.org/pypa/bootstrap

I've also updated the PEP with the following changes:

- mention current plans for HTTPS cert verification in Python 3.4+ (sans PEP 
  reference for now)
- remove setuptools note; setuptools will now be installed
- mention bootstrapping target (user vs. system) and command-line options
- mention python 2.6+ bootstrap possibility
- remove consideration of support for unnecessary installation options (beyond -i/--index-url)
- mention having pip default to --user when itself installed in ~/.local

What the last item alludes to is the idea that it'd be nice if pip installed in 
~/.local would default to installing packages also in ~/.local as though 
the --user switch had been provided. 

Otherwise the user needs to remember it every time they install a package.

Note that the bootstrapping uses two different flags to control where the pip 
implementation is installed: --bootstrap and --bootstrap-system (these were 
chosen to encourage user installs). 

It would be ideal if pip could support those flags, as the pip3 command currently 
must remove them before invoking pip main.

Once we're happy with the shape of pip3 we can fork it to Python 2 and use it 
as the canonical bootstrap script for installing pip and setuptools. 

I think we should also consider installing virtualenv in Python 2...

::

    > - installing virtualenv as well (so now pip, setuptools and virtualenv are installed)

    doesn't "PyEnv" which is bundled with Python 3.3+ replace virtualenv? 
    What's the purpose of including virtualenv in the bootstrap? 
    http://www.python.org/dev/peps/pep-0405/
    

::

    > I just talked to Carl. He basically said that for 3.3+ pyenv itself should 
    probably used and that "hopefully virtualenv will die in favor of of pyvenv".

    OK, thanks. I wonder whether virtualenv.org could mention pyvenv for Py3k users?  
    
    
::

    Carl Meyer <carl@oddbird.net> via python.org 
    à:	 distutils-sig@python.org
    date:	 10 juillet 2013 06:19
    objet:	 Re: [Distutils] PEP 439 and pip bootstrap updated
    
    >> doesn't "pyvenv" which is bundled with Python 3.3+ replace virtualenv? 
    What's the purpose of including virtualenv in the bootstrap? http://www.python.org/dev/peps/pep-0405/
    >
    > It's my understanding that people still install virtualenv in py3k.

    They certainly do today, but that's primarily because pyvenv isn't very
    useful yet, since the stdlib has no installer and thus a newly-created
    pyvenv has no way to install anything in it.

    The bootstrap should fix this very problem (i.e. make an installer
    available in every newly-created pyvenv) and thus encourage use of
    pyvenv (which is simpler, more reliable, and built-in) in place of
    virtualenv. I don't think it makes sense for the stdlib bootstrapper to
    install an inferior third-party tool instead of using a tool that is now
    built-in to the standard library on 3.3+.

    Certainly if the bootstrap is ever ported to 2.7 or 3.2, it would make
    sense for it to install virtualenv there (or, probably even better, for
    pyvenv to be backported along with the bootstrap).     
    
     
::

    Vinay Sajip <vinay_sajip@yahoo.co.uk> via python.org 
    à:	 Distutils-Sig@python.org
    date:	 10 juillet 2013 11:16
    objet:	 Re: [Distutils] PEP 439 and pip bootstrap updated
        
    Carl Meyer <carl <at> oddbird.net> writes:
    > They certainly do today, but that's primarily because pyvenv isn't very
    > useful yet, since the stdlib has no installer and thus a newly-created
    > pyvenv has no way to install anything in it.

    True, though I've provided a script to do that very thing:

    https://gist.github.com/vsajip/4673395

    Of course, that'll now need to be changed to install setuptools rather than
    distribute :-)

    https://bitbucket.org/pypa/setuptools/downloads/ez_setup.py
    
    
    Regards,         

Happy to clarify where needed and code review is welcome. It's been a looong 
four days here :-)


     Richard
     
     
