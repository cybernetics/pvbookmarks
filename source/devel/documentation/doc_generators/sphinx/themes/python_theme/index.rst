
.. index::
   pair: Sphinx Theme; Python

.. _python_theme:

=============================
Python doc Theme
=============================

.. seealso::

   - http://hg.python.org/cpython/file/22e88355acd6/Doc/tools/sphinxext



Where can I find a sphinx theme used in Python official documentation site ?
=============================================================================

::

    Sujet:  Re: [sphinx-users] Where can I find a sphinx theme used in Python official documentation site?
    Date :  Sat, 1 Feb 2014 04:52:34 -0800 (PST)
    De :    Hiroki Watanabe <hwatanabe.japan@gmail.com>
    Répondre à :    sphinx-users@googlegroups.com
    Pour :  sphinx-users@googlegroups.com



Hello,

Thank you very much !

I tried it. It worked well except color of sidebar's collapse button.

The followings are things I tried.

# Searching good themes, I noticed an extension theme,
# 'sphinxjp.themes.basicstrap' was also excellent.
# For while, I will use it for my purpose.

Things I tried
==============

1. Go the following site:
   http://hg.python.org/cpython/file/22e88355acd6/Doc/tools/sphinxext/pydoctheme

2. Download a pydoctheme as a zip archive by clicking a "zip" link
   where you can see left side of the site.

3. Unzip the archive under sphinx's source folder like this:
   source/_themes/pydoctheme/theme.conf

4. Edit conf.py like this::

    sys.path.append(os.path.abspath('_themes'))
    html_theme_path = ['_themes']
    html_theme = 'pydoctheme'

5. Execute 'make html'
   You will notice that you can not see a collapse button on the sidebar. So,

6. Add 'collapsiblesidebar' option and its color to conf.py::

        html_theme_options = {
           'collapsiblesidebar': True,
           'sidebarbtncolor': '#eeeeee',
        }

A problem still exists. When you hover the collapse button, it will disappear 
due to it having the same color of background. 

I don't know how to solve this problem, maybe some CSS knowledge is required.

Best regards,


2014年2月1日土曜日 13時54分21秒 UTC+9 Takayuki SHIMIZUKAWA::

    Hi,

    I think this is the one:
    http://hg.python.org/cpython/file/22e88355acd6/Doc/tools/sphinxext
    <http://hg.python.org/cpython/file/22e88355acd6/Doc/tools/sphinxext>
    However, I have not used it.

    Regards,
    -- 
    Takayuki SHIMIZUKAWA
    http://about.me/shimizukawa
