
.. index::
   pair: python; Exceptions


.. _python_exceptions:

=================================================
Exceptions are allowed but must be used carefully
=================================================


**Definition**
    Exceptions are a means of breaking out of the normal flow of control of a
    code block to handle errors or other exceptional conditions.

**Pros**
    The control flow of normal operation code is not cluttered by error-handling
    code. It also allows the control flow to skip multiple frames when a
    certain condition occurs, e.g., returning from N nested functions in one
    step instead of having to carry-through error codes.

**Cons**
    May cause the control flow to be confusing. Easy to miss error cases when
    making library calls.

Decision
========

Exceptions must follow certain conditions:

Raise exceptions like this::

    raise MyException("Error message") or raise MyException.

Do not use the two-argument form (raise MyException, "Error message") or
deprecated string-based exceptions (raise "Error message").

Modules or packages should define their own domain-specific base exception
class, which should inherit from the built-in Exception class.

The base exception for a module should be called Error::.

    class Error(Exception):
        pass

Never use catch-all except: statements, or catch Exception or StandardError,
unless you are re-raising the exception or in the outermost block in your
thread (and printing an error message).

Python is very tolerant in this regard and except: will really catch
everything including Python syntax errors. It is easy to hide real bugs
using except:.

Minimize the amount of code in a try/except block. The larger the body of
the try, the more likely that an exception will be raised by a line of code
that you didn't expect to raise an exception. In those cases, the try/except
block hides a real error.

Use the finally clause to execute code whether or not an exception is raised
in the try block. This is often useful for cleanup, i.e., closing a file.
