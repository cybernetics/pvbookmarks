
.. index::
   pair: python; Properties


.. _python_properties_g:

==========
Properties
==========

Use properties for accessing or setting data where you would normally have
used simple, lightweight accessor or setter methods.

**Definition**
    A way to wrap method calls for getting and setting an attribute as
    a standard attribute access when the computation is lightweight.

**Pros**
    Readability is increased by eliminating explicit get and set method calls
    for simple attribute access.

    Allows calculations to be lazy.

    Considered the Pythonic way to maintain the interface of a class. In terms
    of performance, allowing properties bypasses needing trivial accessor
    methods when a direct variable access is reasonable.
    This also allows accessor methods to be added in the future without breaking
    the interface.

**Cons**
    - Properties are specified after the getter and setter methods are declared,
      requiring one to notice they are used for properties farther down in the
      code (except for readonly properties created with the :ref:`@property decorator <function_decorators_g>`).
    - Must inherit from object.
    - Can hide side-effects much like operator overloading.
    - Can be confusing for subclasses.

Decision
========

Use properties in new code to access or set data where you would normally have
used simple, lightweight accessor or setter methods.

**Read-only properties should be created with the @property decorator**

Inheritance with properties can be non-obvious if the property itself is not
overridden.

Thus one must make sure that accessor methods are called indirectly to ensure
methods overridden in subclasses are called by the property (using the
Template Method DP).

Yes::


     import math

     class Square(object):
         """A square with two properties: a writable area and a read-only perimeter.

         To use:
         >>> sq = Square(3)
         >>> sq.area
         9
         >>> sq.perimeter
         12
         >>> sq.area = 16
         >>> sq.side
         4
         >>> sq.perimeter
         16
         """

         def __init__(self, side):
             self.side = side

         def __get_area(self):
             """Calculates the 'area' property."""
             return self.side ** 2

         def ___get_area(self):
             """Indirect accessor for 'area' property."""
             return self.__get_area()

         def __set_area(self, area):
             """Sets the 'area' property."""
             self.side = math.sqrt(area)

         def ___set_area(self, area):
             """Indirect setter for 'area' property."""
             self.__set_area(area)

         area = property(___get_area, ___set_area,
                         doc="""Gets or sets the area of the square.""")

         @property
         def perimeter(self):
             return self.side * 4
