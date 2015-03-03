

.. index::
   building tool (kook)


.. _kook_building_tool:

=====
Kook
=====

.. seealso::

   - http://www.kuwata-lab.com/kook/


Kook is software build tool similar to Rake, Ant, SCons or Cook.

Kook liken build process to cooking:

- Recipe -- Task or rule to generate output from input.
- Product -- Output from recipe.
- Ingredient -- Input for recipe.
- Method -- Steps (= a set of commands) to generate product from ingredients.
- Spice -- Additional argument (= command-line options) for recipe.
- Cookbook -- A file containing recipe definitions.

The most ineresting feature Kook has (and others doesn't) is that it 
introduced meta programming concept into task definition. 

.. warning:: Caution! pyKook is currently under experimental. It means that 
   the design and specification of pyKook may change without prior notice.

