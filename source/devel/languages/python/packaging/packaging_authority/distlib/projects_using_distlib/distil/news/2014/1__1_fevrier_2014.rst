

.. _distil_news_1_fevrier_2014:

==========================
Distil news 1 fevrier 2014
==========================


::

    Sujet: Re: [Distutils] PEX at Twitter (re: PEX - Twitter's multi-platform executable archive format for Python)
    Date : Sat, 1 Feb 2014 10:49:15 +0000 (GMT)
    De : Vinay Sajip <vinay_sajip@yahoo.co.uk>
    Pour : Nick Coghlan <ncoghlan@gmail.com>
    Copie à : DistUtils mailing list <distutils-sig@python.org>

On Sat, 1/2/14, Nick Coghlan <ncoghlan@gmail.com> wrote:


::

    > I'm talking about easing the cognitive burden on developers.
    > The pip/virtualenv model is that once an environment is
    > activated, developers don't need to think about it anymore -
    > they're in that environment until they explicitly switch it off.

But distil deals with this::

    $ pyvenv-3.3 /tmp/venv
    $ source /tmp/venv/bin/activate
    (venv) $ distil --ve
    [...]
    Python: 3.3
    [...]

So, distil is using the venv's Python. Let's deactivate and try
again::

    (venv) $ deactivate
    $ distil --ve
    [...]
    Python: 2.7
    [...]

So we're now using the system python - so far, so good.
 
::
 
    > By installing pip *into* the environment, then it is automatically
    > affected by the same settings as all other Python components,
    > so "pip install library" inside an activated virtual environment
    > *just does the right thing*, and it does it in a way that doesn't
    > require any additional custom machinery or testing.

Likewise, with distil::

    $ source /tmp/venv/bin/activate
    (venv) $ distil list
    (venv) $ distil install sarge
    Checking requirements for sarge (0.1.3) ... done.
    The following new packages will be downloaded and installed:
        sarge (0.1.3)
    Downloading sarge-0.1.3.tar.gz to /tmp/tmpn01ls2
    [...]
    Building sarge (0.1.3) ...
    [...]
    Installing sarge (0.1.3) ...
    [...]
        Installation completed.
    (venv) $ distil list
    sarge 0.1.3
    (venv) $

So, I am at a loss to see your point.

::

    > Making any installer automatically respect an activated
    > virtual environment without installing it into that environment
    > is no doubt *feasible*, but just installing the installer *into* the
    > environment has the same effect with requiring any additional
    > engineering or testing effort.

Not only feasible, there needing to be no doubt about it ;-), but
also not rocket science, and demonstrated above. Distil isn't
doing anything especially clever, so I don't understand what you
mean by "any additional engineering or testing effort". 

ISTM you're making things seem more scary than they are. 

Of course, if you find some specific *installation* scenario that distil doesn't
cover, I'll be all ears.

I emphasised *installation* to distinguish from building - distil
eschews running setup.py during installation, since if it did that
then it would be no different from pip in that respect, so there'd
be no point to it. So, "distil install" can't deal with cases of
substantive logic in setup.py - but that's not to say that distil
can't deal with setup.py at all. Instead, that functionality is
provided in other distil commands which deal with building
wheels from sdists. They could be relatively easily merged
into an install command that works like pip, but I thought the
point was to separate building from installation, so that's why
distil is like it is at the moment.

Regards,

Vinay Sajip
