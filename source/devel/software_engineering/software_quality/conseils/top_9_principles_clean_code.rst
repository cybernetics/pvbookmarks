
.. index::
   pair: Quality; Clean code


.. _top_9_qualities_clean_code:

==================================
Top 9 qualities of clean code
==================================

.. seealso::

   - http://blog.goyello.com/2013/01/21/top-9-principles-clean-code/
   - http://www.goyello.com/


.. contents::
   :depth: 3

Introduction
============

How often do you express your disbelief when browsing through someone’s code 
saying out loud ``Omg, that’s real spaghetti code...`` ? Probably quite often. 

And how sure are you that no one thought the same when working with your code? 

In other words, how sure are you that your code is clean ? The truth is that you 
can only be sure if you fully know what clean code means.

It is hard to create a precise definition of clean code and probably there are 
as many definitions as developers. 

However, some principles that lead to a basic level of clean code apply. 
I have gathered the 9 most relevant ones and described them in short below.


.. _point1_quality:

1. Bad code does too much – Clean code is focused
=================================================

Each class, method or any other entity should remain undisturbed. 

SRP (Single Responsibility Principle)
--------------------------------------

.. seealso::

   - http://en.wikipedia.org/wiki/Single_responsibility_principle
   - http://www.developerfusion.com/profile/ralfw
   - http://www.developerfusion.com/article/137636/taking-the-single-responsibility-principle-seriously/

It should conform to :term:`SRP` (Single Responsibility Principle). 

Shortly speaking, we can say that SRP (according to some well-known definitions) 
is about making sure that if you can think of the reason for changing a class 
you should not be able to come up with more than one.

Though, I wouldn’t limit this definition only to the concept of classes. 

In his `latest article`_ Ralf Westphal presents a broader definition of 
Single Responsibility Principle. According to his definition::

    A functional unit on a given level of abstraction should only be responsible 
    for a single aspect of a system’s requirements. 
    An aspect of requirements is a trait or property of requirements, which can 
    change independently of other aspects.

If you would like to read more about the quoted thesis I advise you to dig into 
his article.

.. _`latest article`:  http://www.developerfusion.com/article/137636/taking-the-single-responsibility-principle-seriously/


.. _point2_quality:

2.  The language you wrote your code with should look like it was made for the problem
=======================================================================================


::

    It is not the language that makes a program look simple, but the programmer 
    who makes the language appear simple.

(quote from Robert C. Martin)

This means, for instance, that you shouldn’t use workarounds which make code and 
language usually look awkward. 

If you claim that something can only be done by means of a workaround, it usually 
means that you haven’t spent enough time on trying to find a good, clean solution.


.. _point3_quality:

3. It should not be redundant
==============================

DRY (Don’t Repeat Yourself)
----------------------------

.. seealso::

   - http://en.wikipedia.org/wiki/Don%27t_repeat_yourself

It should comply with the :term:`DRY` rule (Don’t Repeat Yourself). 

When the DRY principle has successfully been applied, the modification of any 
single element of a system doesn’t require a change in any other logically 
unrelated elements.


.. _point4_quality:

4. Reading your code should be pleasant
========================================

When  browsing through the code you should feel like reading Harry Potter 
(yeah I know that’s a slight exaggeration :) ). 

You should feel that it was made to be read by any developer easily without 
hours spent on digging into it.

KISS` principle (Keep It Simple, Stupid!) YAGNI principle (You Ain’t Gonna Need It)
------------------------------------------------------------------------------------

To achieve this you should try to comply with the :term:`KISS` principle 
(Keep It Simple, Stupid!) and YAGNI principle (You Ain’t Gonna Need It). 

The KISS principle states that most systems work best if they are kept simple 
rather than made complex.

Therefore, **simplicity** should be a key goal in design, and unnecessary 
complexity should be avoided. 

YAGNI is a practice encouraging to purely focus on the simplest things that make 
your software work.


.. _point5_quality:

5. Can be easily extended by any other developer
=================================================

You don’t write code for yourself , or worse -  for a compiler. 

You write code for other developers. Don’t be selfish – think about the others. 

Don’t torture other developers by producing a hardly maintainable and extendable 
code. 
Besides, in some months time you could be that “other developer” yourself.


.. _point6_quality:

6. It should have minimal dependencies
=======================================

.. seealso::

   - http://www.ndepend.com/

The more dependencies it has, the harder it is to maintain and change it in the 
future. 

You can always help yourself in achieving the goal of having minimal dependencies 
by using e.g. NDEPEND_ for checking potential incorrectness in the dependencies 
of your code.


.. _NDEPEND:  http://www.ndepend.com/

.. _point7_quality:

7. Smaller is better
====================

**Code should be minimal**. 

Both classes and methods should be short, preferably just a few lines of code. 

It should be well divided (also within one class). 

The better you divide your code the easier it becomes to read it. 

This principle might positively influence point 4 – it will make it easier for 
other developers to understand your code.


.. _point8_quality:

8. It should have unit and acceptance tests
============================================

.. seealso::

   - http://blog.goyello.com/2011/10/06/three-pillars-of-unit-tests/


How can we know that our code complies with the requirements if we don’t write 
tests ? 

How can we maintain and extend it without the fear that it will stop working ? 

**Code without tests is simply not clean**. 

If you would like to get to know more about the pillars of unit testing I advise 
you to read a very nice article Three Pillars of Unit Tests written by one of my 
colleagues.


9. It should be expressive
===========================

.. seealso::

   - http://c2.com/cgi/wiki?SelfDocumentingCode

Expressiveness of the code means that it has **meaningful names**. 

These names should express their intention. 

They should not mislead you. 

They should be distinctive. 

Expressiveness makes code document itself making the need for documentation 
less important. 

If you want to read more about the subject of self-documenting code I recommend 
you to go through this article.

So what is in fact the definition of clean code ?
==================================================

All in all there is one final quality that summarizes all the above::

    Clean code is a code that is written by someone who cares

quote from Michael Feathers

It is written by someone who has treated it as an art and paid attention to all 
details.

The subject of clean code is in fact very complex and goes far beyond the 
knowledge presented in this post. 

Therefore if you find any other characteristics that you think make code cleaner 
do not hesitate and share them with us !



