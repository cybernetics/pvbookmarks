
.. index::
   pair: hg ; matching


.. _hg_log_matching:

=====================
hg log -r "matching"
=====================


.. contents::
   :depth: 3


This keyword can be used to find revisions that "match" one or more fields of a
given set of revisions.

A revision matches another if all the selected fields (description, author,
files, date, parents and/or substate) match the corresponding values of those
fields on the source revision.

By default this keyword looks for revisions that whose metadata match
(description, author and date) making it ideal to look for duplicate revisions.

matching takes 2 arguments (the second being optional):

1. rev: a revset represeting a _single_ revision (e.g. tip, ., p1(.), etc)
2. field(s) to match]: an optional field or list of fields to match.
   By default matching will match the metadata fields (description, author and
   date). When matching more than one field, they must be input as a list. When
   matching a single field there is no need to surround it in () to make it a
   list.

Examples
========

1.- Look for revisions with the same metadata (author, description and date)
as the 11th revision:

hg log -r "matching(11)"

2.- Look for revisions with the same description as the 11th revision:

hg log -r "matching(11, description)"

You do not need to type the whole 'description' word. You could also use
'descript' or 'desc' but not 'd' because 'd' also matches 'date' and 'date'
takes prefecedence because fields are matched in alphabetical order.

3.- Look for revisions with the same author as the current revision:

hg log -r "matching(., author)"

You could use 'user' rather than 'author' to get the same result.

4.- Look for revisions with the same description _AND_ author as the tip of the
repository:

hg log -r "matching(tip, (author, desc))"

5.- Look for revisions touching the same files as the the tip of the repository

hg log -r "matching(tip, files)"

6.- Look for revisions whose subrepos are on the same state as the parent of the
tip of the repository

hg log -r "matching(p1(tip), substate)"

7.- Look for revisions whose author and files both match the tip or the parent
of the tip of the repository:

hg log -r "matching(p1(tip):tip, (a, f))"

