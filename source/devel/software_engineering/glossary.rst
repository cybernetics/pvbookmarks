
.. index::
   pair: Glossary ; Software Engineering
   pair: Software Engineering; DRY
   ! Glossary Software
   


.. _software_engineering_glossaty:

=============================
Sofware engineeering Glossary
=============================


.. glossary::


    Design Patterns
        In software engineering, a design pattern is a general reusable solution
        to a commonly occurring problem within a given context in software design.
        A design pattern is not a finished design that can be transformed directly
        into code.
        It is a description or template for how to solve a problem that can be
        used in many different situations.

        Object-oriented design patterns typically show relationships and
        interactions between classes or objects, without specifying the final
        application classes or objects that are involved.
        Many patterns imply object-orientation or more generally mutable state,
        and so may not be as applicable in functional programming languages, in
        which data is immutable or treated as such.


        .. seealso:: http://en.wikipedia.org/wiki/Design_pattern_%28computer_science%29

    DRY
    Don’t Repeat Yourself
        (a.k.a. DRY), which requires you to rigorously remove duplication in
        your code base
        
        .. seealso::
        
           - http://en.wikipedia.org/wiki/Don%27t_repeat_yourself


    Exigence
        une condition ou une capacité requise par un utilisateur pour résoudre
        un problème ou atteindre un objectif qui doit être tenu ou possédé par
        un système ou composant pour satisfaire à un contrat, standard, spécification
        ou autre document imposé formellement [d'après IEEE 610].

        .. seealso:: http://fr.wikipedia.org/wiki/Gestion_des_exigences

    Fluent interface
        In software engineering, a fluent interface (as first coined by Eric
        Evans and Martin Fowler) is an implementation of an object oriented API
        that aims to provide for more readable code.

        A fluent interface is normally implemented by using method chaining to
        relay the instruction context of a subsequent call (but a fluent
        interface entails more than just method chaining [1]). Generally, the
        context is

        - defined through the return value of a called method
        - self referential, where the new context is equivalent to the last context
        - terminated through the return of a void context.

        This style is marginally beneficial in readability due to its ability to
        provide a more fluid feel to the code[citation needed]. However, it can
        be detrimental to debugging, as a fluent chain constitutes a single
        statement for which debuggers may not allow setting up intermediate
        breakpoints, for instance.


        .. seealso:: http://en.wikipedia.org/wiki/Fluent_interface

    Interface Segregation Principle
        .. seealso:: http://www.objectmentor.com/resources/articles/isp.pdf


    IS0 9241
        ISO 9241 is a multi-part standard from the International Organization for
        Standardization (ISO), covering aspects of people working with computers.
        It was originally titled Ergonomic requirements for office work with visual
        display terminals (VDTs).
        The standards are being retitled to the more generic Ergonomics of Human
        System Interaction. As part of this change, ISO is renumbering the standard
        so that it can cover more topics. The first part to be renumbered was
        part 10, now renumbered to part 110.

        .. seealso::

           http://en.wikipedia.org/wiki/ISO_9241


    ISO 9241-110
        (formerly ISO9241-10, deprecated) Dialogue principles (2006)
        This part deals with general ergonomic principles which apply to the
        design of dialogues between humans and information systems:

        - suitability for the task,
        - suitability for learning,
        - suitability for individualisation,
        - conformity with user expectations,
        - self descriptiveness,
        - controllability, and
        - error tolerance.

        .. seealso::

           http://en.wikipedia.org/wiki/ISO_9241


    KISS
    Keep It Simple Stupid
        (a.k.a. KISS), a funny way of saying that the simplest solution is more
        than sufficient.

        .. seealso:: http://fr.wikipedia.org/wiki/Keep_it_Simple,_Stupid


    Law of Demeter
        The Law of Demeter (LoD) or Principle of Least Knowledge is a design
        guideline for developing software, particularly object-oriented programs.
        In its general form, the LoD is a specific case of loose coupling.
        The guideline was invented at Northeastern University towards the end of
        1987, and can be succinctly summarized in one of the following ways:

        - Each unit should have only limited knowledge about other units: only
          units "closely" related to the current unit.
        - Each unit should only talk to its friends; don't talk to strangers.
        - Only talk to your immediate friends.

        The fundamental notion is that a given object should assume as little
        as possible about the structure or properties of anything else
        (including its subcomponents).

        .. seealso:: http://en.wikipedia.org/wiki/Law_of_Demeter

    The Principle of Least Surprise
         Which means that you should choose a solution that does include any 
         things people might not understand, or put on the wrong track.

    Liskov Substitution Principle
        It should be possible to treat a derived object as if it were a base
        class object.
        This rule is one of the :term:`S.O.L.I.D.` principles

        .. seealso:: http://en.wikipedia.org/wiki/Liskov_substitution_principle

    Modularity
        the resulting software comprises well defined, independent components.
        That leads to better maintainability. The components could be then
        implemented and tested in isolation before being integrated to form a
        desired software system.
        This allows division of work in a software development project.

        .. seealso::

           - http://en.wikipedia.org/wiki/Modularity
           - http://en.wikipedia.org/wiki/Modular_programming


    Maintainability
        The software can be restored to a specified condition within a specified
        period of time.
        For example, antivirus software may include the ability to periodically
        receive virus definition updates in order to maintain the software's
        effectiveness

    Polymorphism
        Subtype polymorphism, almost universally called just polymorphism in the
        context of object-oriented programming, is the ability to create a variable,
        a function, or an object that has more than one form.
        The word derives from the Greek **πολυμορφισμός** meaning "having multiple forms".
        In principle, polymorphism can however arise in other computing contexts
        and it shares important similarities to the concept of degeneracy in biology.

        .. seealso:: http://en.wikipedia.org/wiki/Polymorphism_in_object-oriented_programming


    Portability
        Portability is one of the key concepts of high-level programming.
        Portability is the software codebase feature to be able to reuse the
        existing code instead of creating new code when moving software from an
        environment to another.
        The prerequirement for portability is the generalized abstraction
        between the application logic and system interfaces.
        When one is targeting several platforms with the same application,
        portability is the key issue for development cost reduction.

        .. seealso::

           - http://en.wikipedia.org/wiki/Software_portability


    principle of least surprise
    Principle of Least Surprise
        The Principle of Least Surprise (or Astonishment), which means that you
        should choose a solution that does include any things people might not
        understand, or put on the wrong track.

        .. seealso:: http://en.wikipedia.org/wiki/Principle_of_least_astonishment

    Single Responsibility Principle
    SRP
        This principle was described in the work of Tom DeMarco and Meilir
        Page-Jones. They called it ``cohesion``. As we’ll see in Chapter 21, we
        have a more specific definition of cohesion at the package level.

        However, at the class level the definition is similar.

        .. seealso:: 
        
           - http://www.objectmentor.com/resources/articles/srp.pdf
           - http://en.wikipedia.org/wiki/Single_responsibility_principle


    S.O.L.I.D.
        S.O.L.I.D. is a collection of best-practice object-oriented design principles
        that you can apply to your design to accomplish various desirable goals
        like loose-coupling, higher maintainability, intuitive location of
        interesting code, etc.
        S.O.L.I.D. is an acronym for the following principles

        .. seealso:: http://lostechies.com/chadmyers/2008/03/08/pablo-s-topic-of-the-month-march-solid-principles/


    Software Requirements Specification
    SRS
        a requirements specification for a software system – is a complete
        description of the behavior of a system to be developed.
        It includes a set of use cases that describe all the interactions the
        users will have with the software. In addition to use cases, the SRS
        also contains non-functional (or supplementary) requirements.
        Non-functional requirements are requirements which impose constraints
        on the design or implementation (such as performance engineering
        requirements, quality standards, or design constraints).

        .. seealso::

           - http://en.wikipedia.org/wiki/Requirements_management


    specification
        specification: A document that specifies, ideally in a complete, precise
        and verifiable manner, the requirements, design, behavior, or other
        characteristics of a component or system, and, often, the procedures for
        determining whether these provisions have been satisfied. [After IEEE 610]

    Spécification
        un document qui spécifie, idéalement de façon complète, précise et
        vérifiable, les exigences, conceptions, comportements et autres
        caractéristiques d’un composant ou système, et souvent, les procédures
        pour déterminer si ces stipulations ont été satisfaites. [d’après IEEE 610]

        .. seealso:: http://fr.wikipedia.org/wiki/Sp%C3%A9cification_%28informatique%29

        La phase de spécification doit être précédée par une étude préalable,
        qui décrit l'existant et les attentes et exigences générales exprimées
        par les utilisateurs pour le domaine à informatiser. Un exemple d'attente
        à prendre en compte à ce stade est la langue du logiciel, qui doit être
        adaptée à l'utilisateur.
        Les spécifications reprendront ces exigences pour les décrire plus en détail.

    YAGNI
    You Ain’t Gonne Need It
        (a.k.a. YAGNI), which tells you to create a solution for the current problem
        rather than the ones you think will happen later on (since when can you predict the future ?)
