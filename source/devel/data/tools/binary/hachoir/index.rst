

.. index::
   pair: Hachoir ; Binary


.. _hachoir:

========================
Hachoir
========================


.. seealso::

   - https://bitbucket.org/haypo/hachoir/wiki/Home

.. contents::
   :depth: 4

Introduction
=============

Hachoir is a Python library that allows to view and edit a binary stream field
by field.

In other words, Hachoir allows you to "browse" any binary stream just like you
browse directories and files.

A file is split in a tree of fields, where the smallest field is just one bit.

There are other fields types: integers, strings, bits, padding types, floats,
etc.

Hachoir is the French word for a meat grinder (meat mincer), which is used by
butchers to divide meat into long tubes;

Hachoir is used by computer butchers to divide binary files into fields.

Hachoir is composed of the parser core (hachoir-core), various file format
parsers (hachoir-parser), and other peripheral programs.
For example, you can use hachoir-metadata to extract information from your
favourite photos or videos.

Hachoir also allows you to edit files (of supported formats) without the
original (often proprietary) program that was used to create them.
