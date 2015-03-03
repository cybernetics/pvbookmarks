
===============
1 Introduction
===============

.. seealso::

   - http://twitter.com/ddoomen
   - dennis.doomen @ avivasolutions.nl
   - http://www.csharpcodingguidelines.com
   - http://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882



1.1 What is this ?
==================


This document attempts to provide useful and pragmatic guidelines for programming
in C# 3.0 and C# 4.0 that we at Aviva Solutions already use in our day-to-day work.

Coding guidelines, or coding standards if you will, are documents consisting of
rules and recommendations on the use of C# in enterprise systems.

They deal with code layout, naming guidelines, the proper use of the
.NET Framework, tips on writing useful comments and XML documentation, and
often also include guidance on proper object-oriented design.

Visual Studio’s Static Code Analysis (a.k.a. FxCop) and StyleCop can
automatically verify a majority of those rules and recommendations by analyzing
the compiled assemblies. You can configure to do that at compile time or as part
of a continuous or daily build.

This document adds additional rules and recommendations and its companion site,
http://www.csharpcodingguidelines.com provides a list of Code Analysis rules
that are applicable for Line-of-Business applications and frameworks.


1.2 Why are guidelines necessary ?
==================================

Because not every developer:

- is aware of the potential pitfalls of certain constructions in C#.
- is introduced into certain conventions when using the .NET Framework
  (e.g. ``IDisposable``)
- is aware of the impact of using (or neglecting to use) particular solutions
  on aspects like security, performance, multi-language support, etc.
- knows that not every developer is as capable in understanding an elegant, but
  abstract, solution as the original developer.

Although complying with coding guidelines may seem to appear as undesired
overhead or may limit creativity, this approach has already proven its value for
many years. Also beware of the fact that not all coding guidelines have a clear
rationale. Some of them are simply choices we made at Aviva Solutions.

1.3 Basic Principles
====================

There are many unexpected things I run into during my work as a consultant,
each deserving at least one guideline.

Unfortunately, I’m still trying to keep this document within a reasonable size.

But unlike to what some junior developers believe, **that doesn’t mean that when
something is not mentioned in this guidelines it must be okay**.

In general, if I have a discussion with a colleague about a smell that this
document does not provide absolution for, I’ll refer back to a set of basic
principles that apply to all situations, regardless of context. These include:

- :term:`The Principle of Least Surprise` (or Astonishment), which means that
  you should choose a solution that does include any things people might not
  understand, or put on the wrong track.
- :term:`Keep It Simple Stupid` (a.k.a. KISS), a funny way of saying that the
  simplest solution is more than sufficient.
- :term:`You Ain’t Gonne Need It` (a.k.a. YAGNI), which tells you to create a
  solution for the current problem rather than the ones you think will happen
  later on (since when can you predict the future?)
- :term:`Don’t Repeat Yourself` (a.k.a. DRY), which requires you to rigorously
  remove duplication in your code base

Regardless of the elegancy of somebody’s solution, if it’s too complex for the
ordinary developer, or exposes unusual behavior, or tries to solve many possible
future issues, it is very likely the wrong solution and needs redesign.

1.4 How do I get started ?
==========================

- Ask all developers to carefully read this document at least once. This will
  give them a sense of the kind of guidelines the document contains.
- Make sure there are always a few hard copies of the Quick Reference close
  at hand.
- Include the most critical coding guidelines on your Project Checklist and
  verify the remainder as part of your Peer Review.
- Decide which CA rules are applicable for your project and write these down
  somewhere, such as your TFS team site, or create a custom Visual Studio
  2010 Rule Set. The companion site offers Visual Studio 2010 rule sets for
  both Line-of-Business applications and more generic code like frameworks
  and class libraries.
- Add a custom Code Analysis Dictionary containing your domain- or
  company-specific terms, names and concepts. If you don’t, Static Analysis will
  report warnings for (parts of) phrases that are not part of its internal
  dictionary.
- Configure Visual Studio to verify the selected CA rules as part of the
  Release build. Then they won’t interfere with normal developing and debugging
  activities, but still can be run by switching to the Release configuration.
- Add the verification of the CA rules part of your Continuous or Daily Build.
- Add a rule to your team that the first one who comes in the office in the
  morning will check the build for CA warning and will make sure somebody
  (not necessarily himself) solves it as soon as possible.
- Add an item to your project checklist to make sure all new code is verified
  against CA violations, or use the corresponding Check-in Policy if you want
  to prevent any code from violating CA rules at all.
- ReSharper has an intelligent code inspection engine that, with some
  configuration, already supports many aspects of the Coding Guidelines.
  It will automatically highlight any code that does not match the rules for
  naming members (e.g. Pascal or Camel casing), detect dead code, and many
  other things. One click of the mouse button (or the corresponding keyboard
  shortcut) is usually enough to fix it.
- ReSharper also has a File Structure window that shows an overview of the
  members of your class or interface and allows you to easily rearrange them
  using a simple drag-and-drop action.
- Using GhostDoc you can generate XML comments for any member using a keyboard
  shortcut. The beauty of it, is that it closely follows the MSDN-style of
  documentation. However, you have to be careful not to misuse this tool, and
  use it as a starter only.
- Consider reading the book `Clean Code: A Handbook of Agile Software Craftsmanship`_
  by Robert C. Martin. It provides excellent guidance on writing
  elegant and simple code that is easy to maintain and to extend.
  His ideas have evolved into a new quality standard maintained by many
  well-known community members, and had a lot of influence on this document.


.. _`Clean Code: A Handbook of Agile Software Craftsmanship`:  http://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882

1.5 Why did you create it ?
===========================

The idea started in 2002 when Vic Hartog (Philips Medical Systems) and I were
assigned the task of writing up a coding standard for C# 1.0.

Since then, I've regularly added, removed and changed rules based on experiences,
feedback from the community and new tooling support such as offered by
Visual Studio 2010.

Additionally, after reading Robert C. Martin’s book Clean Code: A Handbook of
Agile Software Craftsmanship, I became a big fan of his ideas and decided to
include some of his smells and heuristics as guidelines.

Notice though that this document is in no way a replacement for his book. I
sincerely recommend that you read his book to gain a solid understanding of the
rationale behind his recommendations.

I’ve also decided to include some design guidelines in addition to simple
coding guidelines. They are too important to ignore and have a big influence
in reaching high quality code.

1.6 Is this a coding standard ?
===============================

The document does not state that projects must comply with these guidelines,
neither does it say which guidelines are more important than others.

However, we encourage projects to decide themselves what guidelines are
important, what deviations a project will use, who is the consultant in
case doubts arise, and what kind of layout must be used for source code.

Obviously, you should make these decisions before starting the real coding work.

To help you in this decision, I’ve assigned a level of importance to each
guideline:

- Guidelines that you should never skip and should be applicable to all
  situations
- Strongly recommended guidelines
- Recommended guidelines that may not be applicable in all situations

In general, generated code should not need to comply with coding guidelines.

However, if it is possible to modify the templates used for generation, try to
make them generate code that complies as much as possible.

1.7 Feedback and disclaimer
===========================


This document has been compiled using many contributions from (former)
colleagues, sources from the Internet, and many years of developing in C#.

If you have questions, comments or suggestions, just let me know by sending
me an email at ``dennis.doomen@avivasolutions.nl`` or tweet me at
http://twitter.com/ddoomen.

I will try to revise and republish this document with new insights, experiences
and remarks on a regular basis.

Notice though that it merely reflects my view on proper C# code so
Aviva Solutions will not be liable for any direct or indirect damages caused by
applying the guidelines of this document.

It is allowed to copy, adapt, and redistribute this document and its companion
quick reference guide for non-commercial purposes or internal usage.

However, you may not republish this document, or publish or distribute any
adaptation of this document for commercial use without first obtaining express
written approval from Aviva Solutions.


