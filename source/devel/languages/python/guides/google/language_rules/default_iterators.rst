
.. index::
   pair: python ; Default Iterators


.. _python_default_Iterators:

================================
Default Iterators and Operators
================================

Use default iterators and operators for types that support them, like lists,
dictionaries, and files.

**Definition**
    Container types, like dictionaries and lists, define default iterators and
    membership test operators ("in" and "not in").

**Pros:**
    The default iterators and operators are simple and efficient. They express
    the operation directly, without extra method calls.
    A function that uses default operators is generic. It can be used with any
    type that supports the operation.

**Cons**
    You can't tell the type of objects by reading the method names
    (e.g. has_key() means a dictionary). This is also an advantage.

Decision
========

Use default iterators and operators for types that support them, like lists,
dictionaries, and files. The built-in types define iterator methods, too.
Prefer these methods to methods that return lists, except that you should
not mutate a container while iterating over it.

Yes::

    for key in adict: ...
    if key not in adict: ...
    if obj in alist: ...
    for line in afile: ...
    for k, v in dict.iteritems(): ...

No::

    for key in adict.keys(): ...
    if not adict.has_key(key): ...
    for line in afile.readlines(): ...
