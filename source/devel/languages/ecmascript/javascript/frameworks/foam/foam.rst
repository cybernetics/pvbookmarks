

.. index::
   pair: Javascript frameworks ; FOAM 
   pair: Coding Style; Javascript
   pair: Polymer ; FOAM
   ! FOAM 


.. _foam:

=========================================
FOAM (Feature Oriented Active Modeler)
=========================================

.. seealso::

   - http://foam-framework.github.io/foam/foam/apps/docs/docbrowser.html#developerDocs.Welcome
   - http://foam-framework.github.io/foam/
   - https://github.com/foam-framework/foam
   - https://github.com/tastejs/todomvc/pull/1085
   - https://github.com/tastejs/todomvc/issues/913#issuecomment-66909798
   - https://github.com/foam-framework/foam/wiki/CodingStyle

.. contents::
   :depth: 3


Welcome to FOAM
================

Congratulations on choosing the Feature Oriented Active Modeler. 

This guide will walk you through the first steps of getting to know FOAM, and 
how concepts from traditional programming languages map into FOAM.

Also see the other overviews:

- Context and Dependency Injection
- Reactive Events and Binding
- Views and HTML


Design Patterns
================

.. seealso::

   - https://github.com/foam-framework/foam/wiki/DesignPatterns

Demos
=====

.. seealso::

   - http://foam-framework.github.io/foam/foam/demos/DemoCat.html?q=mobile
   
   
ComparedToPolymer
=================

.. seealso::

   - https://github.com/foam-framework/foam/wiki/ComparedToPolymer

Polymer is a "Web Component" technology being created by Google.
FOAM is a Component technology, mostly for the Web, being created by Google.

Clearly, the two are very similar.

All mature engineering disciplines are based on components. 

Automotive, construction, electronics, etc. are all based on the heavy use of 
ready-made components. 

Without such components, every new project would need to start from scratch, 
and as a result, would cost orders of magnitude more money and time to complete, 
and the results would be of a lower quality. 

Both Polymer and FOAM realize this and are trying to bring to advantages of 
components to the web, which until this point, has not been what you would 
call a "mature engineering discipline".

However, there are some differences in the approaches taken by the two systems. 

Polymer says that it provides "Web Components", but what it really means is 
"DOM Components". 
It lets you create components which are encapsulated as new types of DOM elements.

FOAM, on the other hand, lets you create components which are not necessarily 
tied to DOM elements. Polymer is a DOM-only component model, whereas FOAM 
components can transparently be either DOM, Canvas, WebGL, SVG, non-visual, or 
even remote. 

However, there's a lot more to the Web than DOM; there's also Canvas, WebGL, 
SVG, and Javascript, as well as the server/network aspects. 

But with Polymer, you're DOM only, and even non-visual components still need 
to be added to the DOM as invisible components (just like was popular with 
Visual Basic twenty+ years ago). 

FOAM offers a unified component model that lets you use the same type of 
components for DOM, Canvas, WebGL, SVG, Javascript, Database, and Network 
objects. 

This makes it easier to create graphically rich UI's without having to learn 
and then bridge between entirely separate component, event, animation, and 
composition models

Why should you have to use two components in completely different ways, just 
because one is written using a Canvas and one is written using DOM? 

You may need to use several of the technologies available in the browser to 
make a complete app, and why should you have to code differently against each 
underlying technology? 

If you look at the average iPhone or Android app, they almost always have 
some graphical components. 

Why should you have a component model which doesn't include such a common 
aspect of modern application development? 

When you program against a DAO, you don't know what underlying technology is 
being used to implement it; it could be local-storage, IndexedDB, a simple 
array, a network REST service, etc. You don't know, and you don't care. 
That's polymorphism. 

The same should be true of Views. You should be able to get/set a View's 
properties, call its methods, add a listener, add it to a parent, add children, 
animate it, etc., all without knowing how it's implemented.






   
