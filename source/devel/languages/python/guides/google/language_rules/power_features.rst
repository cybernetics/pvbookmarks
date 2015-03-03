.. index::
   pair: python; Power Features


.. _python_power_features:

======================================
Power Features : avoid these features
======================================

.

**Definition**
    Python is an extremely flexible language and gives you many fancy features
    such as metaclasses, access to bytecode, on-the-fly compilation, dynamic
    inheritance, object reparenting, import hacks, reflection, modification
    of system internals, etc.

**Pros**
    These are powerful language features. They can make your code more compact.

**Cons**
    It's very tempting to use these "cool" features when they're not absolutely
    necessary. It's harder to read, understand, and debug code that's using
    unusual features underneath.
    It doesn't seem that way at first (to the original author), but when
    revisiting the code, it tends to be more difficult than code that is longer
    but is straightforward.

Decision
========

Avoid these features in your code.
