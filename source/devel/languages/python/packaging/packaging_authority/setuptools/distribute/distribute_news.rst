

======================
Python distribute news
======================

.. seealso::

   - :ref:`python_packaging_24_avril_2013`

.. contents::
   :depth: 3


Dear Pyramid, help Python Packaging  (mer. 12 septembre 2012)
=============================================================

.. seealso::

   - http://blog.ziade.org/2012/09/12/dear-pyramid-help-python-packaging/


Brett Cannon 11 septembre 2012
====================================

- https://plus.google.com/u/0/115362263245161504841/posts/UcBQK8P4jw3


Dear Django, help Python Packaging 10 septembre 2012
====================================================

.. seealso::

   - http://blog.ziade.org/2012/09/10/dear-django-help-python-packaging/



At least one package management tool for 2.7
============================================

::

    from    anatoly techtonik <techtonik@gmail.com>
    to  Python-Dev <python-dev@python.org>
    date    Wed, Mar 24, 2010 at 10:59 AM
    subject [Python-Dev] At least one package management tool for 2.7


    I wonder if there are many people here who don't use some kind of
    "easy_install" package for package management in their Python /
    virtualenv installations? I propose to include at least one such
    package that is capable to auto-update itself in Python 2.7

    C:\~env\Python27>python.exe -m easy_install
    C:\~env\Python27\python.exe: No module named easy_install

    C:\~env\Python27>python.exe -m pip
    C:\~env\Python27\python.exe: No module named pip


    It bugs me when I have to troubleshoot things on yet another machine
    that doesn't have some kind of `setuptools` installed. Or when I have
    to test some bug in my package on different Python version with a
    clean install and need some dependencies.


::


    from    Tarek Ziadé <ziade.tarek@gmail.com>
    to  anatoly techtonik <techtonik@gmail.com>
    cc  distutils-sig <distutils-sig@python.org>,
    Python-Dev <python-dev@python.org>
    date    Wed, Mar 24, 2010 at 11:26 AM
    subject Re: [Python-Dev] At least one package management tool for 2.7
    mailing list    python-dev.python.org Filter messages from this mailing list

    We are working on distutils2 right now to improve the situation, and
    Ian has proposed to work on the possible inclusion of virtualenv in
    the stldib as well.

    I'll talk for distutils2 :

    The plan is to provide a distutils2 standalone version that can be
    installed from 2.4 to 3.x, and that will provide a basic
    installer/uninstaller via -m.

    Distutils2 is planned to be reintegrated in the stdlib in Python 3.3,
    and my goal is to release it when Python 2.7 final is released.

    The open question is: do we want to include a full installer that
    takes care of installing / removing dependencies as well ?

    I think not. Pip already provides this feature on the top of distutils
    (and distutils2 later I guess) and is not hard to install on the top
    of Python.

    But the "auto-update" story seems interesting, can you expand on this ?

    Tarek



::


    from    anatoly techtonik <techtonik@gmail.com>
    to  Tarek Ziadé <ziade.tarek@gmail.com>
    cc  distutils-sig <distutils-sig@python.org>,
    Python-Dev <python-dev@python.org>
    date    Wed, Mar 24, 2010 at 12:20 PM
    subject Re: [Python-Dev] At least one package management tool for 2.7
    mailing list    python-dev.python.org Filter messages from this mailing list

    On Wed, Mar 24, 2010 at 12:26 PM, Tarek Ziadé <ziade.tarek@gmail.com> wrote:
    >
    > Distutils2 is planned to be reintegrated in the stdlib in Python 3.3,
    > and my goal is to release it when Python 2.7 final is released.

    Does that means "after" Python 2.7, because I meant it to be "before"
    or at least "with"?

    > The open question is: do we want to include a full installer that
    > takes care of installing / removing dependencies as well ?

    If there is a risk to get nothing at all in 2.7 distribution, because
    it just won't be ready/accepted by that time, then I it is certainly
    optional.

    > But the "auto-update" story seems interesting, can you expand on this ?

    Sure. Package management tool should have an ability to update itself
    when required regardless of Python release. For example::

       python.exe -m easy_install setuptools

    This will get you new version of `setuptools` and `easy_install`
    module from it automagically. You do not need to install new version
    of `setuptools` manually or copy files from SVN if you want to see
    fixes before next Python release. The stuff you would likely need to
    do with distutils bugs, which I personally find awkward.

    Package management is orthogonal to Python releases, and it is more
    oriented at Python users who don't like to wait or follow PEPs. That's
    why package management tool such as 'easy_install' has shorter
    development cycle, and it should faster react to user feedback. What
    can be one of the reasons that no package management tool is included
    with Python.

    In various README you may often see "requires setuptools > 0.6c9" or
    similar. I can't see why package management tool can not detect this
    dependency and propose to update itself.

    If it is impossible to ship the whole package management system then
    at least Python distribution may carry small bootstrap script for it.
    When user tries to execute package management tools, it warns him that
    these are not installed and gives a hint where to get them

    > python -m easy_install bla-bla-bla

    Error: easy_install module is not shipped with this Python release.
    Please execute the following command to install the latest version.

    python -m easy_bootstrap




