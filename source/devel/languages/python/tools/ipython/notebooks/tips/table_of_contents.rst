

.. index::
   pair: Notebook; Table of contents   


.. _table_of_contents_ipython:

================================
table_of_contents_ipython
================================


.. seealso::

   - http://nbviewer.ipython.org/github/rasbt/python_reference/blob/master/tutorials/table_of_contents_ipython.ipynb



custom.js
==========

.. seealso::

   - http://nbviewer.ipython.org/gist/smoskwa/c3a642e59f0539f1faa7


The javascript can be placed in a custom.js file rather than polluting your 
actual notebooks !

::

    In [1]:
    %%javascript
    IPython.toolbar.add_buttons_group([
    {
         'label'   : 'Create TOC',
         'icon'    : 'icon-list', 
         'callback': function(){
             IPython.notebook.insert_cell_at_index('code',0);
             var toc = "Table of Contents\n\n"
             
             for (var i = 0; i < IPython.notebook.ncells(); i++) { 
                 var curr = IPython.notebook.get_cell(i)
                 if (curr.hasOwnProperty('level')) {
                     toc += Array(curr.level*2).join(' ')+ '* ['+curr.get_text()+'](#'+curr.get_text()+')\n\n'
                 }
                    
             }
             
             IPython.notebook.get_cell(0).set_text(toc);
             IPython.notebook.to_markdown(0);
             IPython.notebook.get_cell(0).execute();
             IPython.notebook.scroll_to_top();
        }
    }]);



