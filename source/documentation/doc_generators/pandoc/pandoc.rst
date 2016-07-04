
.. index::
   pair: Documentation ; Pandoc
   ! Pandoc

.. _pandoc:

=======================
Pandoc
=======================


.. seealso::

   - http://johnmacfarlane.net/pandoc/index.html
   - https://github.com/jgm/pandoc
   - https://raw.github.com/jgm/pandoc/master/README
   - :ref:`haskell_language`


.. contents::
   :depth: 3


Introduction
=============

If you need to convert files from one markup format into another, pandoc is your
swiss-army knife.

Pandoc can convert documents in markdown, reStructuredText, textile, HTML, DocBook,
LaTeX, or MediaWiki markup to:

- HTML formats: XHTML, HTML5, and HTML slide shows using Slidy, Slideous, S5, or
  DZSlides.
- Word processor formats: Microsoft Word docx, OpenOffice/LibreOffice ODT,
  OpenDocument XML
- Ebooks: EPUB version 2 or 3, FictionBook2
- Documentation formats: DocBook, GNU TexInfo, Groff man pages
- TeX formats: LaTeX, ConTeXt, LaTeX Beamer slides
- PDF via LaTeX
- Lightweight markup formats: Markdown, reStructuredText, AsciiDoc,
  `MediaWiki markup`_, Emacs Org-Mode, Textile



.. _`MediaWiki markup`:  http://www.mediawiki.org/wiki/Help:Formatting


.. seealso::

   - https://raw.github.com/jgm/pandoc/master/README


- [markdown]: http://daringfireball.net/projects/markdown/
- [reStructuredText]: http://docutils.sourceforge.net/docs/ref/rst/introduction.html
- [S5]: http://meyerweb.com/eric/tools/s5/
- [Slidy]: http://www.w3.org/Talks/Tools/Slidy/
- [Slideous]: http://goessner.net/articles/slideous/
- [HTML]:  http://www.w3.org/TR/html40/
- [HTML 5]:  http://www.w3.org/TR/html5/
- [XHTML]:  http://www.w3.org/TR/xhtml1/
- [LaTeX]: http://www.latex-project.org/
- [beamer]: http://www.tex.ac.uk/CTAN/macros/latex/contrib/beamer
- [ConTeXt]: http://www.pragma-ade.nl/
- [RTF]:  http://en.wikipedia.org/wiki/Rich_Text_Format
- [DocBook]:  http://www.docbook.org/
- [OPML]: http://dev.opml.org/spec2.html
- [OpenDocument]: http://opendocument.xml.org/
- [ODT]: http://en.wikipedia.org/wiki/OpenDocument
- [Textile]: http://redcloth.org/textile
- [MediaWiki markup]: http://www.mediawiki.org/wiki/Help:Formatting
- [groff man]: http://developer.apple.com/DOCUMENTATION/Darwin/Reference/ManPages/man7/groff_man.7.html
- [Haskell]:  http://www.haskell.org/
- [GNU Texinfo]: http://www.gnu.org/software/texinfo/
- [Emacs Org-Mode]: http://orgmode.org
- [AsciiDoc]: http://www.methods.co.nz/asciidoc/
- [EPUB]: http://www.idpf.org/
- [GPL]: http://www.gnu.org/copyleft/gpl.html "GNU General Public License"
- [DZSlides]: http://paulrouget.com/dzslides/
- [ISO 8601 format]: http://www.w3.org/TR/NOTE-datetime
- [Word docx]: http://www.microsoft.com/interop/openup/openxml/default.aspx
- [PDF]: http://www.adobe.com/pdf/
- [reveal.js]: http://lab.hakim.se/reveal-js/
- [FictionBook2]: http://www.fictionbook.org/index.php/Eng:XML_Schema_Fictionbook_2.1

Pandoc source code
==================

Pandoc has a publicly accessible git repository at github. To get a local copy
of the source::

    git clone git://github.com/jgm/pandoc.git

After cloning the repository (and in the future after pulling from it),
you should do::

      git submodule update --init

to pull in changes to the templates.

You can automate this by creating a file .git/hooks/post-merge with the contents::

    #!/bin/sh
    git submodule update --init

and making it executable::

    chmod +x .git/hooks/post-merge

The modules Text.Pandoc.Definition, Text.Pandoc.Builder, and Text.Pandoc.Generics
are in a separate package pandoc-types.

The code can be found in this repository_ (http://github.com/jgm/pandoc-types).

.. _repository:   http://github.com/jgm/pandoc-types


Versions
=========

.. toctree::
   :maxdepth: 3
   
   versions/versions
   
   

