


.. index::
   pair: Graddle ; Building tool
   ! Gradle 


.. _gradle_building_tool:
.. _gradle:

=======
Gradle
=======

.. figure:: gradle_logo.gif
   :align: center

.. seealso::

   - http://www.gradle.org/



.. contents::
   :depth: 3


What is Gradle ?
=================

Gradle is build automation evolved. 

Gradle can automate the building, testing, publishing, deployment and more of 
software packages or other types of projects such as generated static websites, 
generated documentation or indeed anything else.

Gradle combines the power and flexibility of Ant with the dependency management 
and conventions of Maven into a more effective way to build. 

Powered by a Groovy DSL and packed with innovation, Gradle provides a declarative 
way to describe all kinds of builds through sensible defaults. 

Gradle is quickly becoming the build system of choice for many open source 
projects, leading edge enterprises and legacy automation challenges.

Learn more about what makes Gradle a compelling choice for build automation or 
get started with Gradle right now.



http://gradle.org/overview
==========================

Declarative builds and build-by-convention

At the heart of Gradle lies a rich extensible Domain Specific Language (DSL)
based on Groovy. Gradle pushes declarative builds to the next level by providing
declarative language elements that you can assemble as you like. Those elements
also provide build-by-convention support for Java, Groovy, OSGi, Web and Scala
projects. Even more, this declarative language is extensible. Add your own new
language elements or enhance the existing ones. Thus providing concise,
maintainable and comprehensible builds.

Why Groovy ?
------------

.. seealso::

   - :ref:`groovy`


We think the advantages of an internal DSL (based on a dynamic language) over
XML are tremendous in case of build scripts. There are a couple of dynamic
languages out there. Why Groovy? The answer lies in the context Gradle
is operating in. Although Gradle is a general purpose build tool at its core,
its main focus are Java projects. In such projects obviously the team members
know Java. We think a build should be as transparent as possible to all team members.

You might argue why not using Java then as the language for build scripts. We
think this is a valid question. It would have the highest transparency for your
team and the lowest learning curve. But due to limitations of Java such a build
language would not be as nice, expressive and powerful as it could be.

Languages like Python, Groovy or Ruby do a much better job here. We have chosen
:ref:`Groovy <groovy>` as it offers by far the greatest transparency for Java people. 

Its base syntax is the same as Java's as well as its type system, its package 
structure and other things. 
Groovy builds a lot on top of that. But on a common ground with Java.

For Java teams which share also Python or Ruby knowledge or are happy to learn it,
the above arguments don't apply. The Gradle design is well-suited for creating
another build script engine in JRuby or Jython. It just doesn't have the highest
priority for us at the moment.
We happily support any community effort to create additional build script engines.


Gradle versions
===============

.. toctree::
   :maxdepth: 3
   
   versions/index
   
   
Used by 
===============

.. toctree::
   :maxdepth: 3
      
   used_by/index
   
   
   
   

