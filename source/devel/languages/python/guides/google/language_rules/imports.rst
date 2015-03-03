.. index::
   pair: python; Imports


.. _python_imports:


=====================================
Imports for packages and modules only
=====================================

Use imports for packages and modules only.

**Definition**
    Reusability mechanism for sharing code from one module to another.

**Pros**
    The namespace management convention is simple. The source of each identifier
    is indicated in a consistent way; x.Obj says that object Obj is defined in
    module x.

**Cons**
    Module names can still collide. Some module names are inconveniently long.

Decision
========

Use import x for importing packages and modules.


Use from x import y where x is the package prefix and y is the module name with
no prefix.

Use from x import y as z if two modules named y are to be imported or if y is
an inconveniently long name.

For example the module sound.effects.echo may be imported as follows:::

    from sound.effects import echo
    ...
    echo.EchoFilter(input, output, delay=0.7, atten=4)

Do not use relative names in imports.

Even if the module is in the same package, use the **full package name**.

This helps prevent unintentionally importing a package twice.


