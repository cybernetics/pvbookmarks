
.. index::
   pair: C♯; naming guideline


.. _csharp_naming_guideline:

===================
6 Naming Guidelines
===================


AV1701 Use proper US-English
===============================

All identifiers should be named using words from the American English language.

- Choose easily readable identifier names. For example, HorizontalAlignment is
  more readable than AlignmentHorizontal.
- Favor readability over brevity. The property name CanScrollHorizontally is
  better than ScrollableX (an obscure reference to the X-axis).
- Avoid using identifiers that conflict with keywords of widely used programming
  languages.


Exception In most projects, you will use words and phrases from your domain and
names specific to your company.

Visual Studio’s Static Code Analysis will perform a spelling check on all code,
so you may need to add those terms to a Custom Code Analysis Dictionary.

AV1702 Use proper casing for members
====================================


AV1704 Don’t include numbers in identifiers
============================================

Numbers in names of fields, variables or members are very rarely needed.
In fact, in most cases they are a lazy excuse for not defining a clear and
intention-revealing name.

AV1705 Don’t prefix member fields
=================================

Don’t use a prefix for field names. For example, Don’t use ``g_`` or ``s_`` to
distinguish static versus non-static fields.

In general, a method in which it is difficult to distinguish local variables
from member fields, is too big.

Examples of incorrect identifier names are: _currentUser, mUserName, m_loginTime.


AV1706 Don’t use abbreviations
==============================

**Don’t use abbreviations or acronyms as parts of identifier names**.

For example, use OnButtonClick rather than OnBtnClick. Avoid single character
variable names, such as i or q. Use index or query instead.

**Exceptions**
    Use well-known abbreviations that are widely accepted or well-known within
    the domain you work. For instance, use UI instead of UserInterface.



AV1707 Name an identifier according its meaning and not its type
================================================================

- Use semantically interesting names rather than language-specific keywords for
  type names. For example, GetLength is a better name than GetInt.
- Don’t use terms like Enum, Class or Struct in a name.
- Identifiers that refer to an array or collection should have a plural name.


AV1708 Name types using nouns, noun phrases or adjective phrases
================================================================

Bad examples include SearchExamination (a page for searching for examinations),
Common (does not end with a noun, and does not explain its purpose) and
SiteSecurity (although the name is technically okay, it does not say anything
about its purpose).

Good examples include BusinessBinder, SmartTextBox, or EditableSingleCustomer.

Don’t include terms like Utility or Helper in classes. Classes with a name like
that are usually static classes and are introduced without considering the
object-oriented principles.


AV1709 Name generic type parameters with descriptive names
==========================================================


The following guidelines cover selecting the correct names for generic type
parameters.

- Name generic type parameters with descriptive names, unless a single-letter
  name is completely self explanatory and a descriptive name would not add value.
  For example: IDictionary is an example of an interface that follows this guideline.
- Use the letter T as the type parameter name for types with one single-letter
  type parameter.
- Prefix descriptive type parameter names with the letter T.
- Consider indicating constraints placed on a type parameter in the name of
  parameter. For example, a parameter constrained to ISession may be called TSession.


AV1710 Don’t repeat the name of a class or enumeration in its members
=====================================================================

::

    class Employee
    {
        // Wrong!
        static GetEmployee() {}
        DeleteEmployee() {}
        // Right
        static Get() {...}
        Delete() {...}
        // Also correct.
        AddNewJob() {...}
        RegisterForMeeting() {...}
    }

AV1711 Name members similarly to members of .NET Framework classes
===================================================================


Stay close to the naming philosophy of the .NET Framework.

Developers are  already accustomed to the naming patterns .NET Framework classes
use, so following this same pattern helps them find their way in your classes
as well.

For instance, if you define a class that behaves like a collection, provide
members like Add, Remove and Count instead of AddItem, Delete or NumberOfItems.


AV1712 Avoid short names or names that can be mistaken with other names
=======================================================================

Although technically allowed, the following statement is quite confusing.

::

    bool b001 = (lo == l0) ? (I1 == 11) : (lOl != 101);


AV1715 Properly name properties
===============================


- Do name properties with nouns, noun phrases, or occasionally adjective phrases.
- Do name boolean properties with an affirmative phrase. E.g. CanSeek instead
  of CantSeek.
- Consider prefixing Boolean properties with Is, Has, Can, Allows, or Supports.
- Consider giving a property the same name as its type. When you have a property
  that is strongly typed to an enumeration, the name of the property can be the
  same as the name of the enumeration. For example, if you have an enumeration
  named CacheLevel, a property that returns one of its values can also be named
  CacheLevel.



AV1720 Name methods using verb-object pair
==========================================

Name methods using a verb-object pair such as ShowDialog. A good name should
give a hint on the what of a member, and if possible, the why. Also, don’t
include And in the name of the method. It implies that the method is doing more
than one thing, which violates the single responsibility principle.

::

    interface IEmployeeRepository
    {
        Employee[] First() { } // Wrong: What does first mean? How many?
        Employee[] GetFirstFive() {} // Better
        Employee[] GetFiveMostRecent(){} // Best: self-describing
        void Add(Employee employee) {} // Although not using verb-object pair; // the type name is clear enough
    }


AV1725 Name namespaces according a well-defined pattern
========================================================

All namespaces should be named according to the pattern::

    <Company>.(<Product>|<Technology>)[.<Feature>][.<Subnamespace>]


For instance: Microsoft.WindowsMobile.DirectX.


.. note::  Don’t use the same name for a namespace and a type in that namespace.
   For example, don’t use Debug for a namespace name and also provide a class
   named Debug in the same namespace.


AV1735 Use a verb or verb phrase to name an event
=================================================

Name events with a verb or a verb phrase. For example: Click, Deleted, Closing,
Minimizing, and Arriving. For example, the declaration of the Search event may
look like this:

    public event SearchEventHandler Search;


AV1737 Use -ing and -ed to express pre-events and post-events
=============================================================

Give event names a concept of before and after, using the present and past tense.
For example, a close event that is raised before a window is closed would be
called Closing and one that is raised after the window is closed would be called
Closed.

Don’t use Before or After prefixes or suffixes to indicate pre and post events.
Suppose you want to define events related to the deletion process of an object.
Avoid defining the Deleting and Deleted events as BeginDelete and EndDelete.

Define those events as follows:

- Deleting: Occurs just before the object is getting deleted
- Delete: Occurs when the object needs to be deleted by the event handler.
- Deleted: Occurs when the object is already deleted.

AV1738 Prefix an event handler with On
======================================

It is good practice to prefix the method that handles an event with On.
For example, a method that handles the Closing event could be named OnClosing.

AV1745 Group extension methods in a class suffixed with Extensions
==================================================================

If the name of an extension method conflicts with another member or extension
method, you must prefix the call with the class name. Having them in a dedicated
class with the Extensions suffix improves readability.






