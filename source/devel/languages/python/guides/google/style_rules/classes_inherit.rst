
.. index::
   pair: python; classes inherit

.. _python_classes_inherit:

===============
Classes inherit
===============


If a class inherits from no other base classes, **explicitly inherit from object**.
This also applies to nested classes.

No::

    class SampleClass:
        pass


    class OuterClass:

        class InnerClass:
            pass

Yes::

     class SampleClass(object):
         pass


     class OuterClass(object):

         class InnerClass(object):
             pass


     class ChildClass(ParentClass):
         """Explicitly inherits from another class already."""

Inheriting from object is needed to make properties work properly, and it will
protect your code from one particular potential incompatibility with Python 3000.

It also defines special methods that implement the default semantics of objects
 including __new__, __init__, __delattr__, __getattribute__, __setattr__,
 __hash__, __repr__, and __str__.

