
.. index::
   pair: C♯ coding standard; code project


================================
C♯ code project coding standards
================================


Naming Conventions
==================

.NET standards do not recommend using Hungarian prefixes, so avoid them.

To refer to member field inside class member function, use this word ``this.memberVariable``.

You use lower case for variables and function parameters, all the rest go with
capitals::

    SomeClass { ... };
    SomeEnum { Item1, Item2, ... };
    SomeProperty { get; set }

    double someVariable;
    int someFunctionParameter;
    const char SomeConstantVariable;

    static readonly SomeReadOnlyStaticVariable;

    Exception SomeNameException;

    Attribute SomeNameAttribute;

    Button cancelButton;

    TextBox nameTextBox;

    PictureBox namePictureBox;


Class Layout
============

It is recommended to declare class internals in that order:

- Fields
- Constructors
- Nested enums, structs, classes
- Properties
- Methods

Miscellaneous
=============

One class per source file (SomeName class should be declared in somename.cs file).

Private members are private by default in class, **avoid explicit private**.

For a single statement get/set property use that construction::

    public int Foo
    {
            get { return this.foo; }
            set { this.foo = value; }
    }


Use {} for if, else, for, while even if single lined::

    if (someVar == true)
    {
            foo++;
    }

Use @ instead of escape sequencies in strings - @"c:\somepath\file.txt"

Use override instead of new::

    class SomeParent
    {
            //...
            public int DoWork();
            //...
    }

    class SomeOverride
    {
            //...
            public override int DoWork();
            //...
    }


Initialize string to String.Empty rather than assigning it "".

Use StringBuilder for composing complex strings rather than using string class
operators.

Document if the method returns copy of reference type.

Do not compare to true or false use if(condition).

Provide private constructor if only static fields are in the class or declare
static class.

Const objects in class are static by default.

Struct may have constructor with parameters only.


.. _documenting_csharp_code:

Documenting
===========

Consider documenting your code so you will not be trying to recall what the
method is supposed to do after some days have gone::

    /// <summary>
    /// Save trimmed text
    /// </summary>
    /// <param name="fileName">Trimmed text file name</param>
    /// <returns>zero upon success</returns>
    public int SaveText(String fileName)
    {
    //...
    }





