

.. index::
   pair: C♯3 properties; automatic
   pair: C♯ properties; automatic


.. _csharp_automatic_properties:

======================================================================================================
"Auto-implemented properties" /"automatically implemented properties" / "Automatic properties"   (C♯3)
======================================================================================================

.. seealso::

   - http://msdn.microsoft.com/en-us/library/bb384054.aspx
   - http://csharpindepth.com/articles/general/bluffersguide3.aspx

.. versionadded:: 3
   The *automatic* properties.


Automatic properties are a simple way to write properties which just get and
set their values directly from/to a backing variable.

For example, this code::

    string name;
    public string Name
    {
        get { return name; }
        set { name = value; }
    }

can be written in C# 3 like this::


    public string Name { get; set; }

You can specify separate access levels for the getter and the setter, just like
in C♯2.




