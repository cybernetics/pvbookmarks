

==========================
9 Documentation Guidelines
==========================

AV2301 Write comments and documentation in US English
=====================================================


AV2305 Use XML tags for documenting types and members
=====================================================

Document all public types and members of types using the built-in XML comment
functionality of Visual Studio.

Documenting your code allows Visual Studio to pop-up the documentation when your
class is used somewhere else.

Furthermore, by properly documenting your classes, tools can generate
professionally looking class documentation.


AV2306 Write XML documentation with the caller in mind
======================================================

Write the documentation of your class with the class user in mind. Assume the
user will not have access to the source code and try to explain how to get the
most out of the functionality of your class.


AV2307 Write MSDN-style documentation
=====================================

Following the MSDN on-line help style and word choice helps the developer to
find its way through your documentation more easily.

Tip The tool GhostDoc can generate a starting point for documenting code with
a shortcut key.


AV2310 Avoid inline comments
============================

If you feel the need to explain a block of code using a comment, consider
replacing that block with a method having a clear name.


AV2315 Don’t use / * / for comments
======================================


AV2316 Only write comments to explain complex algorithms or decisions
=====================================================================

Try to focus comments on the why and what of a code block and not the how.

Avoid explaining the statements in words, but instead help the reader understand
why you chose a certain solution or algorithm and what you are trying to
achieve.

If applicable, also mention that you chose an alternative solution because you
ran into a problem with the obvious solution.


AV2318 Don’t use comments for tracking work to be done later
============================================================

Annotating a block of code or some work to be done using a TODO or similar
comment may seem a reasonable way of tracking work-to-be-done.

But in reality, nobody really searches for comments like that. Use a work item
tracking system such as Team Foundation Server to keep track of left overs.

