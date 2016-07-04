

.. index::
   Sphinx ; Substitution
   ! Substitution


.. _sphinx_substitution:

================================
Substitution 
================================


.. contents::
   :depth: 3

Substitutions
=============

Substitutions syntax is ::

    .. |biohazard| image:: biohazard.png

    The |biohazard| symbol must be used on containers used to dispose of medical waste.


Or if you want to do a literal text replacement use::

    .. |doctest| replace:: :mod:`doctest`

    I really like |doctest|.



Which renders like this:

.. |biohazard| image:: biohazard.png

The |biohazard| symbol must be used on containers used to dispose of medical waste.

.. |doctest| replace:: :mod:`doctest`

I really like |doctest|.

.. note::

   Substitutions are really useful, especially when put into a ``global.rst``
   and included at the top of every file.  See :ref:`Includes <sphinx_include>` for more.


