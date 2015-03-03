
.. index::
   pair: python; True/False


.. _python_true_false:

======================
True/False evaluations
======================

Use the "implicit" false if at all possible.

**Definition**
    Python evaluates certain values as false when in a boolean context.
    A quick "rule of thumb" is that all "empty" values are considered false so 0,
    None, [], {}, "" all evaluate as false in a boolean context.

**Pros**
    Conditions using Python booleans are easier to read and less error-prone.
    In most cases, they're also faster.

**Cons**
    May look strange to C/C++ developers.

Decision
========

Use the "implicit" false if at all possible, e.g., if foo: rather than
if foo != []:. There are a few caveats that you should keep in mind though:

- Never use == or != to compare singletons like None. Use is or is not.
- Beware of writing if x: when you really mean if x is not None:—e.g., when
  testing whether a variable or argument that defaults to None was set to some
  other value. The other value might be a value that's false in a boolean context!
- Never compare a boolean variable to False using ==. Use if not x: instead.
  If you need to distinguish False from None then chain the expressions, such
  as if not x and x is not None:.
- For sequences (strings, lists, tuples), use the fact that empty sequences are
  false, so if not seq: or if seq: is preferable to if len(seq): or if not len(seq):.
- When handling integers, implicit false may involve more risk than benefit
  (i.e., accidentally handling None as 0). You may compare a value which is
  known to be an integer (and is not the result of len()) against the integer 0.

Yes::

     if not users:
         print 'no users'

     if foo == 0:
         self.handle_zero()

     if i % 10 == 0:
         self.handle_multiple_of_ten()


No::

     if len(users) == 0:
         print 'no users'

     if foo is not None and not foo:
         self.handle_zero()

     if not i % 10:
         self.handle_multiple_of_ten()

Note that '0' (i.e., 0 as string) evaluates to true.
