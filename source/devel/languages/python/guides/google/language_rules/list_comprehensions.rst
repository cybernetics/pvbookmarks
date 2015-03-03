.. index::
   pair: python; List Comprehensions


.. _python_List_comprehensions_g:

==================================================
List Comprehensions: okay to use for simple cases
==================================================
.

**Definition**
    List comprehensions and generator expressions provide a concise and
    efficient way to create lists and iterators without resorting to the use of
    map(), filter(), or lambda.

**Pros**
    Simple list comprehensions can be clearer and simpler than other list
    creation techniques.
    Generator expressions can be very efficient, since they avoid the creation
    of a list entirely.

**Cons**
    Complicated list comprehensions or generator expressions can be hard to read.

Decision
=========

Okay to use for simple cases.

Each portion must fit on one line: mapping expression, for clause,
filter expression.

Multiple for clauses or filter expressions are not permitted.

Use loops instead when things get more complicated.

No::

  result = [(x, y) for x in range(10) for y in range(5) if x * y > 10]

  return ((x, y, z)
          for x in xrange(5)
          for y in xrange(5)
          if x != y
          for z in xrange(5)
          if y != z)

Yes::

  result = []
  for x in range(10):
      for y in range(5):
          if x * y > 10:
              result.append((x, y))

  for x in xrange(5):
      for y in xrange(5):
          if x != y:
              for z in xrange(5):
                  if y != z:
                      yield (x, y, z)

  return ((x, complicated_transform(x))
          for x in long_generator_function(parameter)
          if x is not None)

  squares = [x * x for x in range(10)]

  eat(jelly_bean for jelly_bean in jelly_beans
      if jelly_bean.color == 'black')
