
.. index::
   pair: python; access_control

.. _python_access_control:

===============
Access Control
===============

If an accessor function would be trivial you should use public variables instead
of accessor functions to avoid the extra cost of function calls in Python.

When more functionality is added you can use property to keep the syntax
consistent.

On the other hand, if access is more complex, or the cost of accessing the
variable is significant, you should use function calls (following
the :ref:`Naming guidelines <python_naming_guideline>`) such as get_foo() and
set_foo().

If the past behavior allowed access through a property, do not bind the new
accessor functions to the property.

Any code still attempting to access the variable by the old method should break
visibly so they are made aware of the change in complexity.
