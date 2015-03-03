
.. index::
   pair: Compiler; Grako


.. _grako:

===============================
Grako (for *grammar compiler*)
===============================

.. seealso::

   - http://pypi.python.org/pypi/grako
   - https://bitbucket.org/apalala/grako
   - http://en.wikipedia.org/wiki/Ebnf
   - http://en.wikipedia.org/wiki/Parsing_expression_grammar


.. contents::
   :depth: 3


What ?
======

EBNF to PEG parser generator.

Introduction
============

Grako
=====

**Grako** (for *grammar compiler*) is a tool that takes grammars in a variation of EBNF_ as input, and outputs memoizing_ PEG_ parsers in Python_.

**Grako** is *different* from other PEG_ parser generators in that the generated parsers use Python_'s very efficient exception-handling system to backtrack. **Grako** generated parsers simply assert what must be parsed; there are no complicated *if-then-else* sequences for decison making or backtracking. *Possitive and negative lookaheads*, and the *cut* element allow for additional, hand-crafted optimizations at the grammar level.

**Grako**, the runtime support, and the generated parsers have measurably low `Cyclomatic complexity`_.  At around 2500 lines of Python_, it is possible to study all its source code in a single session. **Grako**'s only dependecies are on the Python_ 2.7, 3.x, or PyPy_ standard libraries.

.. _`Cyclomatic complexity`: http://en.wikipedia.org/wiki/Cyclomatic_complexity

**Grako** is feature complete and currently being used over very large grammars to parse and translate hundreds of thousands of lines of legacy_ code.

.. _KLOC: http://en.wikipedia.org/wiki/KLOC
.. _legacy: http://en.wikipedia.org/wiki/Legacy_code
.. _PyPy: http://pypy.org/


Rationale
---------

**Grako** was created to address recurring problems encountered over decades of working with parser generation tools:

* To deal with programming languages in which important statement words (can't call them keywords) may be used as identifiers in programs, the parser must be able to lead the lexer. The parser must also lead the lexer to parse languages in which the meaning of input symbols may change with context, like Ruby_.

* When ambiguity is the norm in the parsed language (as is the case in several legacy_ ones), an LL or LR grammar becomes contaminated with miriads of lookaheads. PEG_ parsers address ambiguity from the onset. Memoization, and relying on the exception-handling system makes backtracking very efficient.

* Semantic actions, like `Abstract Syntax Tree`_ (AST_) creation or transformation, *do not*  belong in the grammar. Semantic actions in the grammar create yet another programming language to deal with when doing parsing and translation: the source language, the grammar language, the semantics language, the generated parser's language, and translation's target language.

* Pre-processing (like dealing with includes, fixed column formats, or Python_'s structure through indentation) belong in well-designed program code, and not in the grammar.

* It is easy to recruit help knowledged about a mainstream programming language (Python_ in this case); it is not so for grammar description languages. As a grammar language becomes more complex, it becomes increasingly difficult to find who can maintain a parser. **Grako** grammars are in the spirit of a *Translators and Interpreters 101* course (if something's hard to explain to an university student, it's probably too complicated).

* Generated parsers should be humanly-readable and debuggable. Looking at the generated source code is sometimes the only way to find problems in a grammar, the semantic actions, or in the parser generator itself. It's inconvenient to trust generated code that you cannot understand.

* Python_ is a great language for working in language parsing and translation.

.. _`Abstract Syntax Tree`: http://en.wikipedia.org/wiki/Abstract_syntax_tree
.. _AST: http://en.wikipedia.org/wiki/Abstract_syntax_tree
.. _ASTs: http://en.wikipedia.org/wiki/Abstract_syntax_tree
.. _EBNF: http://en.wikipedia.org/wiki/Ebnf
.. _memoizing: http://en.wikipedia.org/wiki/Memoization
.. _PEG: http://en.wikipedia.org/wiki/Parsing_expression_grammar
.. _Python: http://python.org
.. _Ruby: http://www.ruby-lang.org/

The Generated Parsers
---------------------

A **Grako** generated parser consists of the following classes:

* A root class derived from ``Parser`` which implements the parser using one method for each grammar rule. The per-rule methods are named enclosing the rule's name with underscores to emphasize that they should not be tampered with (called, overriden, etc)::

    def _myrulename_(self):

* An *abstract* parser class that inherits from the root parser and verifies at runtime that there's a semantic method (see below) for every rule invoked. This class is useful as a parent class when changes are being made to the grammar, as it will throw an exception if there are missing semantic methods.

* An base class with one semantic method per grammar rule. Each method receives as its single parameter the `Abstract Syntax Tree`_ (AST_) built from the rule invocation.::

    def myrulename(self, ast):
        return ast

The methods in the base parser class return the same AST_ received as parameter, but derived classes can override the methods to have them return anything (for example, a `Semantic Graph`_). The base class can be used as a template for the final parser.

By default, and AST_ is either a list (for *closures*), or dict-derived object that contains one item for every named element in the grammar rule. Items can be accessed through the standard dict syntax, ``ast['key']``, or as attributes, ``ast.key``.

AST_ entries are single values if only one item was associated with a name, or lists if more than one item was matched. There's a provision in the grammar syntax (see below) to force an AST_ entry to be a list even if only one element was matched. The value for named elements that were not found during the parse (perhaps because they are optional) is ``None``.

.. _`Semantic Graph`: http://en.wikipedia.org/wiki/Abstract_semantic_graph



License
-------

**Grako** is Copyright 2012-2013 by `ResQSoft Inc.`_ and  `Juancarlo AÃ±ez`_

.. _`ResQSoft Inc.`:  http://www.resqsoft.com/
.. _ResQSoft:  http://www.resqsoft.com/
.. _`Juancarlo AÃ±ez`: mailto:apalala@gmail.com

You may use the tool under the terms of the `GNU General Public License (GPL) version 3`_ as described in the enclosed **LICENSE.txt** file.

.. _`GNU General Public License (GPL) version 3`:  http://www.gnu.org/licenses/gpl.html

**If your project requires different licensing** please contact
`info@resqsoft.com`_.

.. _`info@resqsoft.com`: mailto:info@resqsoft.com


Contact
-------

For queries and comments about **Grako**, please use the `Grako Forum`_.

.. _`Grako Forum`:  https://groups.google.com/forum/?fromgroups#!forum/grako


Credits
-------

The following must be mentioned as contributors of thoughts, ideas, code, *and funding* to the **Grako** project:

* **Niklaus Wirth** was the chief designer of the programming languages Euler, Algol W, Pascal, Modula, Modula-2, Oberon, Oberon-2, and Oberon-07. In the last chapter of his 1976 book `Algorithms + Data Structures = Programs`_, Wirth_ creates a top-down, descent parser with recovery for the Pascal_-like, `LL(1)`_ programming language `PL/0`_. The structure of the program is that of a PEG_ parser, though the concept of PEG_ wasn't formalized until 2004.

* **Bryan Ford** introduced_ PEG_ (parsing expression grammars) in 2004.

* Other parser generators like `PEG.js`_ by **David Majda** inspired the work in **Grako**.

* **William Thompson** inspired the use of context managers with his `blog post`_ that I knew about through the invaluable `Python Weekly`_ nesletter, curated by **Rahul Chaudhary**

* **Terence Parr** created ANTLR_, probably the most solid and professional parser generator out there. Ter, *ANTLR*, and the folks on the *ANLTR* forums helped me shape my ideas about **Grako**.

* **JavaCC** (originally Jack_) looks like an abandoned project. It was the first parser generator I used while teaching.

* **Guido van Rossum** created and has lead the development of the Python_ programming environment for over a decade. A tool like **Grako**, at under three thousand lines of code, would not have been possible without Python_.

* **My students** at UCAB_ inspired me to think about how grammar-based parser generation could be made more approachable.

* **Gustavo Lau** was my professor of *Language Theory* at USB_, and he was kind enough to be my tutor in a thesis project on programming languages that was more than I could chew.

* **Manuel Rey** led me through another, unfinished thesis project that taught me about what languages (spoken languages in general, and programming languages in particular) are about.

* **Grako** would not have been possible without the funding provided by **Thomas Bragg** through ResQSoft_.

.. _Wirth: http://en.wikipedia.org/wiki/Niklaus_Wirth
.. _Pascal: http://en.wikipedia.org/wiki/Pascal_(programming_language)
.. _`PL/0`: http://en.wikipedia.org/wiki/PL/0
.. _`LL(1)`: http://en.wikipedia.org/wiki/LL(1)
.. _`Algorithms + Data Structures = Programs`: http://www.amazon.com/Algorithms-Structures-Prentice-Hall-Automatic-Computation/dp/0130224189/
.. _`blog post`: http://dietbuddha.blogspot.com/2012/12/52python-encapsulating-exceptions-with.html
.. _`Python Weekly`: http://www.pythonweekly.com/
.. _introduced: http://dl.acm.org/citation.cfm?id=964001.964011
.. _`PEG.js`: http://pegjs.majda.cz/
.. _UCAB: http://www.ucab.edu.ve/
.. _USB: http://www.usb.ve/
.. _ANTLR: http://www.antlr.org/
.. _Jack: http://en.wikipedia.org/wiki/Javacc

Versions
========

.. toctree::
   :maxdepth: 3
   
   versions/index
   



