.. module:: PythonWmiWindows
    :synopsis: Python wmi Windows


.. index::
   pair: Python ; wmi
   pair: Python ; registry


.. _python_wmi:

==========
Python wmi
==========

.. seealso::

   - :ref:`wmi`
   - :ref:`wmi_csharp`



.. contents::
   :depth: 4



Introduction
============

Windows Management Instrumentation (WMI) is Microsoft’s implementation of
Web-Based Enterprise Management (WBEM), an industry initiative to provide
a Common Information Model (CIM) for pretty much any information
about a computer system.

The Python WMI module is a lightweight wrapper on top of the pywin32
extensions, and hides some of the messy plumbing needed to get Python
to talk to the WMI API. It’s pure Python and has been tested against
all versions of Python from 2.4 to 3.2. It should work with
any recent version of pywin32.


.. seealso::

   - http://timgolden.me.uk/python/wmi/index.html
   - http://timgolden.me.uk/python/wmi/tutorial.html
   - http://timgolden.me.uk/python/wmi/cookbook.html




python wmi registry
===================


.. seealso::

   - http://timgolden.me.uk/python/wmi/cookbook.html#list-registry-keys
   - http://timgolden.me.uk/python-on-windows/programming-areas/registry.html
   - http://code.google.com/p/python-on-windows-docs/source/browse/#svn/trunk/programming-areas/registry


delete the registry
-------------------

The requirement: To delete one or more keys from the registry,
including all their values.

The standard registry API, exposed in Python by the _winreg module,
only allows keys to be deleted which have no subkeys. The Windows
shell API does offer a recursive key delete but that function isn’t
exposed neither by the Python stdlib nor by the pywin32 extensions.

The first example below uses the _winreg module to delete keys one
at a time. For simplicity, this example knows the layout of subtrees
it needs to delete. It would be possible to adapt the registry
walker example to go depth first and delete subtrees from the
bottom up. The second example uses ctypes to invoke the shell
API function which will delete an entire tree in one go.


.. seealso:: http://timgolden.me.uk/python-on-windows/programming-areas/registry/delete-the-registry.html


Deleting with _winreg
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import _winreg

    root = _winreg.HKEY_CURRENT_USER
    keypaths = [
      r"Software\PySoft\PyApp",
      r"Software\PySoft\PyThing",
      r"Software\PySoft\PyTool",
      r"Software\PySoft",
    ]

    for keypath in keypaths:
      keys = keypath.split ("\\")
      mainkey, subkey = "\\".join (keys[:-1]), keys[-1]
      key = _winreg.OpenKey (root, mainkey, 0, _winreg.KEY_ALL_ACCESS)
      _winreg.DeleteKey (key, subkey)
      print "Deleted", keypath





Deleting with Shell API
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import _winreg
    import ctypes
    from ctypes import wintypes
    import win32api
    import win32con

    shlwapi = ctypes.windll.shlwapi
    SHDeleteKey = shlwapi.SHDeleteKeyW

    root, keypath = wintypes.HKEY (_winreg.HKEY_CURRENT_USER), ur"Software\PySoft"
    result = SHDeleteKey (root, keypath)
    if result:
      raise RuntimeError (
        win32api.FormatMessageW (win32con.FORMAT_MESSAGE_FROM_SYSTEM, None, result, 0, [])
      )




serial ports
============

.. seealso:: http://www.activexperts.com/admin/scripts/wmi/python/0358/


.. literalinclude:: scan_with_wmi.py
   :language: python











