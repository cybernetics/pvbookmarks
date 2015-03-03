

.. index::
   pair Boost ; System library
   pair: System ; C++


.. _boost_system_cplusplus_library:

============================
Boost system C++ library
============================

.. seealso::

   - http://www.boost.org/doc/libs/1_47_0/libs/system/doc/index.html


Error conditions originating from the operating system or other low-level
application program interfaces (API's) are typically reported via an integer
representing an error code.

When these low-level API calls are wrapped in portable code, such as in a
portable library, some users want to deal with the error codes in portable
ways. Other users need to get at the system specific error codes, so they can
eal with system specific needs.

The Boost System library provides simple, light-weight error_code objects that
encapsulate system-specific error code values, yet also provide access to more
abstract and portable error conditions via error_condition objects.
Because error_code objects can represent errors from sources other than the
operating system, including user-defined sources, each error_code and
error_condition has an associated error_category.

An exception class,  system_error, is provided. Derived from std::runtime_error,
it captures the underlying error_code for the problem causing the exception
so that this important information is not lost.

While exceptions are the preferred C++ default error code reporting mechanism,
users of libraries dependent on low-level API's often need overloads reporting
error conditions via error code arguments and/or return values rather than
via throwing exceptions. Otherwise, when errors are not exceptional occurrences
and must be dealt with as they arise, programs become littered with
try/catch blocks, unreadable, and very inefficient.

The Boost System library supports both error reporting by exception and by error code.

In addition to portable errors codes and conditions supported by the
error_code.hpp header, system-specific headers support the Cygwin, Linux, and
Windows platforms.
These headers are effectively no-ops if included for platforms other than their
intended target.


