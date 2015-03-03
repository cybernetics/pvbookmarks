

.. index::
   pair: Sphinx ; hyperlinks
   pair: Sphinx ; Inventory


.. _sphinx_hyperlinks:

=================
sphinx Hyperlinks
=================


.. contents::
   :depth: 3

External links
==============

Use ```Link text <http://target>`_`` for inline web links.  If the link text
should be the web address, you don't need special markup at all, the parser
finds links and mail addresses in ordinary text.


::

    Example of external link:  `reST role <http://sphinx-doc.org/latest/markup/inline.html#role-ref>`_ .


Example of external link:  `reST role <http://sphinx-doc.org/latest/markup/inline.html#role-ref>`_ .



Include HTML in generated Sphinx docs
-------------------------------------

.. seealso::

   - http://sphinx-doc.org/ext/intersphinx.html
   - https://gist.github.com/3978232

::


    Takayuki Shimizukawa shimizukawa@gmail.com
    répondre à:  sphinx-dev@googlegroups.com
    à:   sphinx-dev@googlegroups.com
    date:    30 octobre 2012 05:22
    objet:   Re: [sphinx-dev] Include HTML in generated Sphinx docs



`intersphinx` will meet your needs.

`intersphinx` support to link another 'Sphinx Document' by using
inventory like 'objects.inv'.

But if you generate inventory by hand (or some program), you can use
this mechanism. I wrote a sample: https://gist.github.com/3978232

intersphinx reference is here: http://sphinx-doc.org/ext/intersphinx.html

Best regards,

::

    Takayuki SHIMIZUKAWA
    Sphinx-users.jp



conf.py
+++++++

::


    extensions = ['sphinx.ext.intersphinx']

    intersphinx_mapping = {
        'javaapi': ('http://api.example.com/', 'javaapi.inv'),
    }


generate_javaapi_inv.py
++++++++++++++++++++++++

::

    inventory_header = u'''\
    # Sphinx inventory version 2
    # Project: javaapi
    # Version: 2.0
    # The remainder of this file is compressed with zlib.
    '''.encode('utf-8')

    inventory_payload = u'''\
    api1 std:label -1 api.html#api1 API 1
    '''.encode('utf-8')

    # inventory_payload lines spec:
    #   name domainname:type priority uri dispname
    #
    # * `name`     -- fully qualified name
    # * `dispname` -- name to display when searching/linking
    # * `type`     -- object type, a key in ``self.object_types``
    # * `docname`  -- the document where it is to be found
    # * `anchor`   -- the anchor name for the object
    # * `priority` -- how "important" the object is (determines placement in search results)
    #
    #   - 1: default priority (placed before full-text matches)
    #   - 0: object is important (placed before default-priority objects)
    #   - 2: object is unimportant (placed after full-text matches)
    #   - -1: object should not show up in search at all
    #

    inventory = inventory_header + zlib.compress(inventory_payload)
    open('javaapi.inv','wb').write(inventory)



index.html
+++++++++++

::

    <div class="section" id="example-link-to-outer-non-sphinx-by-using-intersphinx">
    <h1>Example: Link to outer non-sphinx by using intersphinx<a class="headerlink" href="#example-link-to-outer-non-sphinx-by-using-intersphinx" title="Permalink to this headline">ﾂｶ</a></h1>
    <p><a class="reference external" href="http://api.example.com/api.html#api1" title="(in javaapi v2.0)"><em class="xref std std-ref">Java API 1</em></a></p>
    </div>



index.txt
+++++++++

::

    Example: Link to outer non-sphinx by using intersphinx
    ==========================================================================

    :ref:`Java API 1 <javaapi:api1>`



.. _internal_links:

Internal links
==============

.. seealso:: http://sphinx-doc.org/latest/markup/inline.html#role-ref


Internal linking is done via a special `reST role <http://sphinx-doc.org/latest/markup/inline.html#role-ref>`_ .

::

    :ref:`link to internal links <internal_links>`


:ref:`link to internal links <internal_links>`

