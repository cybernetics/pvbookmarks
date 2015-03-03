
.. index::
   pair: python; Indentation


.. _python_indentation:

===========
Indentation
===========

Indent your code blocks with 4 spaces.

.. warning:: Never use tabs or mix tabs and spaces.

In cases of implied line continuation, you should align wrapped elements:

- either vertically, as per the examples in the line length section;
- or using a  hanging indent of 4 spaces, in which case there should be no
  argument on the first line.

Yes::

       # Aligned with opening delimiter
       foo = long_function_name(var_one, var_two,
                                var_three, var_four)

       # 4-space hanging indent; nothing on first line
       foo = long_function_name(
           var_one, var_two, var_three,
           var_four)

No::

       # Stuff on first line forbidden
       foo = long_function_name(var_one, var_two,
           var_three, var_four)

       # 2-space hanging indent forbidden
       foo = long_function_name(
         var_one, var_two, var_three,
         var_four)
