
.. index::
   pair: Psychological ; Elements (architecture)
   ! Software Architecture


.. _psy_architectuer:

===============================================
Psychological Elements of Software Architecture
===============================================


.. seealso:: http://unprotocols.org/blog:8


.. contents::
   :depth: 3

Introduction
============


Dirkjan Ochtman pointed me to Wikipedia's definition of `Software Architecture`_
as "the set of structures needed to reason about the system, which comprise
software elements, relations among them, and properties of both". It's a good
example of how miserably little we understand about what actually makes a
successful large scale software architecture.

I'll argue that the core elements of software architecture are psychological,
not technical. Primarily, our inability to understand complexity, and our desire
to work together to divide and conquer large problems.

It doesn't matter how much jargon you use, or how elegant your data structures
are, if you can't understand and work with the human brains that make, and use,
the software.

So here is my short list of the Psychological Elements of Software Architecture:


Stupidity
=========

Mental bandwidth is limited, so we're all stupid at some point.
The architecture has to be simple to understand. This is the number one rule:
**simplicity beats functionality, every time**. If you can't understand an
architecture at 7am before coffee, it's too complex.

Selfishness
===========

we act only out of self-interest, so the architecture must create space and
opportunity for selfish acts that benefit the whole.
Selfishness is often indirect and subtle. For example I'll spend hours helping
someone else understand something because that could be worth days to me later.

Laziness
========

We make lots of assumptions, many of which are wrong. We are happiest when we
can spend the least effort to get a result, so the architecture has to make this
possible. Specifically, that means simplicity and leverage. Exploit the paths of least resistance and challenge assumptions.

Jealousy
========

we're jealous of others, which means we'll overcome our stupidity and laziness
to prove others wrong, and beat them in competition.
The architecture thus has to create space for public competition based on fair
rules that anyone can understand.

Reciprocity
===========

we'll work hard to punish cheats and enforce fair rules. The architecture should
be heavily rule based, telling people how to work together, but not what to work on.

Pride
=====

we're intensely aware of our social status, and we'll work hard to avoid looking
stupid or incompetent in public. The architecture has to make sure every piece
has someone's name on it, so that person will wake up at 4am with nightmares
about people laughing over the implementation.

Greed
=====

we're ultimately economic animals (see selfishness), so the architecture has to
give us economic incentive to invest in making it happen. Maybe it's polishing
our reputation as experts, maybe it's literally making money from some skill or
component. Think of architecture as a market place, not an engineering design.

Conformity
==========

we're happiest to conform, out of fear and laziness, which can be good but is
mostly a problem. The architecture should encourage diversity of thought and
action. The only conformity that's needed is adherence to rules on remixing and ownership.

Fear
====

we're unwilling to take risks, especially if it makes us look stupid.
Fear of failure is a major reason people conform and follow the group in mass
stupidity.
The architecture should make silent experimentation easy and cheap, giving
people opportunity for success without punishing failure.


And yes, I'm as stupid, selfish, fearful, greedy, and proud as anyone.



.. _`Software Architecture`: http://en.wikipedia.org/wiki/Software_architecture
