


.. index::
   pair: python; Packages

.. _python_packages:

========
Packages
========

Import each module using the full pathname location of the module.

**Pros**
    Avoids conflicts in module names. Makes it easier to find modules.

**Cons**
    Makes it harder to deploy code because you have to replicate the package
    hierarchy.

Decision
========

All new code should import each module by its full package name.

Imports should be as follows::

    # Reference in code with complete name.
    import sound.effects.echo

    # Reference in code with just module name (preferred).
    from sound.effects import echo
