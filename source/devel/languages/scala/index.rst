
.. index::
   pair: Language ; Scala
   ! Scala


.. _scala_language:

===================
Scala 
===================

.. figure:: scala_logo.png
   :align: center

.. figure:: scala_EPFL.jpg
   :align: center
   

.. seealso::

   - http://www.scala-lang.org/
   - http://typesafe.com/
   - http://www.scala-lang.org/faq
   - http://www.scala-lang.org/node/1658 (Scala in the enterprise)
   - http://fr.wikipedia.org/wiki/Scala_%28langage%29
   - http://neopythonic.blogspot.com/2008/11/scala.html (Guido van Rossum)
   - http://prezi.com/fb0vqbuqk33a/why-scala/
   - http://www.artima.com/weblogs/viewpost.jsp?thread=328540 (Scala: The Static Language that Feels Dynamic)


.. contents::
   :depth: 3

Introduction
=============

Scala est un langage de programmation multi-paradigme conçu à l'École
polytechnique fédérale de Lausanne (EPFL) pour exprimer les modèles de
programmation courants dans une forme concise et élégante. Son nom vient de
l'anglais Scalable language qui signifie à peu près **langage adaptable**
ou **langage qui peut être mis à l'échelle** Il peut en effet être vu comme un métalangage.

Scala intègre les paradigmes de programmation orientée objet et de programmation
fonctionnelle, avec un typage statique. Il concilie ainsi ces deux paradigmes
habituellement opposés (à de rares exceptions près, telle que le langage OCaml)
et offre au développeur la possibilité de choisir le paradigme le plus approprié
à son problème.

Il est prévu pour être compilé en bytecode Java (exécutable sur la JVM), ou .Net.
Ces deux plateformes sont supportées officiellement par l'EPFL, mais d'autres
plateformes pourront potentiellement être supportées dans le futur.


Download
========

.. seealso:: http://www.scala-lang.org/downloads/distrib/files/scala-2.9.1.final-installer.jar

Akka
====

.. seealso::

   - http://www.typesafe.com/technology/akka
   - http://akka.io/


Akka is the platform for the next generation event-driven, scalable and
fault-tolerant architectures on the JVM.

We believe that writing correct concurrent, fault-tolerant and scalable
applications is too hard. Most of the time it's because we are using the
wrong tools and the wrong level of abstraction.

Akka is here to change that.

Using the Actor Model together with Software Transactional Memory we raise the
abstraction level and provide a better platform to build correct concurrent
and scalable applications.

For fault-tolerance we adopt the "Let it crash" / "Embrace failure" model which
have been used with great success in the telecom industry to build applications
that self-heal, systems that never stop.

Actors also provides the abstraction for transparent distribution and the basis
for truly scalable and fault-tolerant applications.

Akka is Open Source and available under the Apache 2 License.



Akka and 0mq
------------

https://github.com/gruggiero/zeromq-scala-examples
++++++++++++++++++++++++++++++++++++++++++++++++++

is a Scala port of ZeroMQ guide samples.


https://github.com/zcox/akka-zeromq-java
++++++++++++++++++++++++++++++++++++++++

Examples of using Akka and 0MQ in Java, separately and together.



