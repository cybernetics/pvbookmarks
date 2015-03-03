
.. index::
   pair: Sphinx; Templates (Tip 1)


.. _sphinx_custom_title_page_1:

============================================================
Custom title page (1)
============================================================


.. seealso::

   - https://bitbucket.org/birkenfeld/sphinx/src/tip/doc/conf.py 
   - http://sphinx-doc.org/config.html#confval-html_additional_pages
   - https://bitbucket.org/birkenfeld/sphinx/src/tip/doc/_templates/



On Fri, Apr 4, 2014 at 1:58 PM, Julia Evans <jwevans01@gmail.com> wrote::

    I'm new to Sphinx, and I'd like to create a custom title page. I have 
    figured out how I can suppress the title page by adding 'maketitle': ' ', 
    in the conf.py file, but how do I replace it with a custom cover page? 
    And If I can, what format doe sit have to be in? 

    I'm using the "howto" sphinx template.


Sphinx uses its own custom front page in https://bitbucket.org/birkenfeld/sphinx/src/tip/doc/conf.py by doing;

   html_sidebars = {'index': ['indexsidebar.html', 'searchbox.html']}
   html_additional_pages = {'index': 'index.html'}

documented at http://sphinx-doc.org/config.html#confval-html_additional_pages 
and http://sphinx-doc.org/config.html#confval-html_sidebars]

where index.html and indexsidebar.html are in https://bitbucket.org/birkenfeld/sphinx/src/tip/doc/_templates/

It also uses:

   master_doc = 'contents'

to rename the Sphinx generated main file.
