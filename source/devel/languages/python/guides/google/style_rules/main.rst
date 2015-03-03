
.. index::
   pair: python; main


.. _python_main:

====
Main
====

Even a file meant to be used as a script should be importable and a mere import
should not have the side effect of executing the script's main functionality.

The main functionality should be in a main() function.

In Python, pychecker, pydoc, and unit tests require modules to be importable.

Your code should always check if __name__ == '__main__' before executing your
main program so that the main program is not executed when the module is imported.


::

    def main():
          ...

    if __name__ == '__main__':
        main()

All code at the top level will be executed when the module is imported.

Be careful not to call functions, create objects, or perform other operations
that should not be executed when the file is being pychecked or pydoced.
