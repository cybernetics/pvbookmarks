

.. index::
   pair: python; Deprecated Language Features


.. _python_deprecated_language_features:


============================
Deprecated Language Features
============================

- Use string methods instead of the string module where possible.
- Use function call syntax instead of apply.
- Use list comprehensions and for loops instead of filter, map, and reduce.

**Definition**
    Current versions of Python provide alternative constructs that people find
    generally preferable.

**Decision**
    We do not use any Python version which does not support these features, so
    there is no reason not to use the new styles.

No::

     words = string.split(foo, ':')
     map(lambda x: x[1], filter(lambda x: x[2] == 5, my_list))
     apply(fn, args, kwargs)

Yes::

     words = foo.split(':')
     [x[1] for x in my_list if x[2] == 5]
     fn(*args, **kwargs)
