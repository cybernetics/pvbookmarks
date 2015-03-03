
.. index::
   pair: C♯;  Maintainability Guidelines

.. _csharp_maintainabilit_guidelines:

=============================
5 Maintainability Guidelines
=============================


AV1500 Methods should not exceed 7 statements
=============================================

A method that requires more than 7 statements is doing too much, or has too
many responsibilities.

It also requires the human mind to analyze the exact statements to understand
what the code is doing.

Break it down in multiple small and focused methods with self-explaining names.


AV1501 Make all members private and types internal by default
=============================================================

To make a more conscious decision on which members to make available to other
classes, explicitly set the scope of all new members to ``private`` and that of
a new type to ``internal``.

**Then carefully decide what to expose as a public member or type**.


AV1502 Avoid conditions with double negatives
=============================================

Although a property like customer.HasNoOrders make sense, avoid using it in a
negative condition like this::

    bool hasOrders = !customer.HasNoOrders;


Double negatives are more difficult to grasp than simple expressions, and people
tend to read over the double negative easily.


AV1505 Name assemblies after their contained namespace
======================================================

As an example, consider a group of classes organized under the namespace
``AvivaSolutions.Web.Binding`` exposed by a certain assembly.

According to this guideline, that assembly should be called
``AvivaSolutions.Web.Binding.dll``.

All DLLs should be named according to the pattern <Company>.<Component>.dll
where <Company> refers to your company’s name and <Component> contains one or
more dot-separated clauses. For example AvivaSolutions.Web.Controls.dll.

Exception If you decide to combine classes from multiple unrelated namespaces
into one assembly, consider post fixing the assembly with Core, but do not use
that suffix in the namespaces. For instance, AvivaSolutions.Consulting.Core.dll.


AV1506 Name a source file to the type it contains
=================================================

Also, use Pascal casing for naming the file and don’t use underscores.


AV1507 Limit the contents of a source code file to one type
===========================================================

Exception Nested types should, for obvious reasons, be part of the same file.


AV1508 Name a source file to the logical function of the partial type
=====================================================================

When using partial types and allocating a part per file, name each file after
the logical part that part plays. For example::

::

    // In MyClass.cs
    public partial class MyClass
    {...}


AV1510 Use using statements instead of fully qualified type names
==================================================================

Limit usage of fully qualified type names to prevent name clashing.

For example:

Don’t::

    var list = new System.Collections.Generic.List<string>();

Do::

    using System.Collections.Generic;
    var list = new List<string>();


If you do need to prevent name clashing, use a using directive to assign an
alias::

    using Label = System.Web.UI.WebControls.Label;


AV1515 Don’t use "magic numbers"
================================

Don’t use literal values, either numeric or strings, in your code other than to
define symbolic constants. For example::


    public class Whatever
    {
        public static readonly Color PapayaWhip = new Color(0xFFEFD5);
        public const int MaxNumberOfWheels = 18;
    }

Strings intended for logging or tracing are exempt from this rule. Literals
are allowed when their meaning is clear from the context, and not subject to
future changes, For example:::

    mean = (a + b) / 2; // okay WaitMilliseconds(waitTimeInSeconds * 1000); // clear enough


If the value of one constant depends on the value of another, do attempt to make
this explicit in the code. For example, don’t::

    public class SomeSpecialContainer
    {
        public const int MaxItems = 32;
        public const int HighWaterMark = 24; // at 75%
    }

but do::

    public class SomeSpecialContainer
    {
        public const int MaxItems = 32;
        public const int HighWaterMark = 3 * MaxItems / 4; // at 75%
    }


Note An enumeration can often be used for certain types of symbolic constants.

AV1520 Only use var when the type is very obvious
=================================================


Only use var as the result of a LINQ query, or if the type is very obvious from
the same statement and using it would improve readability.

Don't::

    var i = 3; // what type? int? uint? float?
    var myfoo = MyFactoryMethod.Create("arg"); // Not obvious what base-class or
    // interface to expect. Also difficult
    // to refactor if you can't search for
    // the class


Do::

    var q = from order in orders where order.Items > 10 and order.TotalValue > 1000;
    var repository = new RepositoryFactory.Get<IOrderRepository>();
    var list = new ReadOnlyCollection<string>();


In all of three above examples it is clear what type to expect.
For a more detailed rationale about the advantages and disadvantages of using
var, read `Eric Lippert’s Uses and misuses of implicit typing`_.


.. _`Eric Lippert’s Uses and misuses of implicit typing`: http://blogs.msdn.com/b/ericlippert/archive/2011/04/20/uses-and-misuses-of-implicit-typing.aspx


AV1521 Initialize variables at the point of declaration
=======================================================

**Avoid the C and Visual Basic styles where all variables have to be defined at
the beginning of a block**, but rather define and initialize each variable at the
point where it is needed.




AV1523 Favor Object and Collection Initializers over separate statements
========================================================================


Instead of::

    var startInfo = new ProcessStartInfo(“myapp.exe”);
    startInfo.StandardOutput = Console.Output;
    startInfo.UseShellExecute = true;

Use Object Initializers::

    var startInfo = new ProcessStartInfo(“myapp.exe”)
    {
    StandardOutput = Console.Output,
    UseShellExecute = true
    };


Similarly, instead of::

    var countries = new List<string>();
    countries.Add(“Netherlands”);
    countries.Add(“United States”);


Use Collection Initializers::

    var countries = new List<string> { “Netherlands”, “United States” };


AV1525 Don’t make explicit comparisons to true or false
=======================================================

It is usually bad style to compare a bool-type expression to true or false.

For example::

    while (condition == false) // wrong; bad style while (condition != true) // also wrong

    while (((condition == true) == true) == true) // where do you stop? while (condition) // OK



AV1526 Use an enumeration instead of a list of strings if the list of values is finite
======================================================================================

If a variable can have a limited set of constant string values, use an
enumeration for defining the valid values.

Using the enumeration instead of a constant string allows compile-time checking
and prevents typos.


AV1530 Don’t change a loop variable inside a for or foreach loop
================================================================

Updating the loop variable within the loop body is generally considered
confusing, even more so if the loop variable is modified in more than one place.

Although this rule also applies to foreach loops, an enumerator will typically
detect changes to the collection the foreach loop is iteration over::

    for (int index = 0; index < 10; ++index) { if (some condition)
    {
        index = 11; // Wrong! Use ‘break’ or ‘continue’ instead. }
    }


AV1532 Don’t use nested loops in a method
=========================================

A method that nests loops is more difficult to understand than one with only a
single loop. In fact, in most cases having nested loops can be replaced with a
much simpler LINQ query that uses the from keyword twice or more to join the
data.


AV1535 Add a block after all flow control keywords, even if it is empty
=======================================================================

Please note that this also avoids possible confusion in statements of the form::

    if (b1)
        if (b2)
           Foo();
    else Bar(); // which ‘if’ goes with the ‘else’?


The right way::

    if (b1)
    {
         if (b2)
         {
             Foo();
         }
         else
         {
             Bar();
         }
    }


AV1536 Always add a default block after the last case in a switch statement
===========================================================================

Add a descriptive comment if the default block is supposed to be empty.

Moreover, if that block is not supposed to be reached throw an
InvalidOperationException to detect future changes that may fall through the
existing cases.

This ensures better code, because all paths the code can travel has been
thought about::

    void Foo(string answer)
    {
        switch (answer)
        {
            case "no": Console.WriteLine("You answered with No");
            break; case "yes": Console.WriteLine("You answered with Yes"); break;
            default: // Not supposed to end up here.
            throw new InvalidOperationException("Unexpected answer: " + answer);
        }
    }



AV1537 Finish every if-else-if statement with an else-part
===========================================================


The intention of this rule, which applies to else-if constructs, is the same as
the previous rule. For example::

    void Foo(string answer)
    {
        if (answer == "no")
        {
            Console.WriteLine("You answered with No");
        }
        else if (answer == "yes")
        {
            Console.WriteLine("You answered with Yes");
        }
        else
        {
            // What should happen when this point is reached? Ignored? If not, // throw an InvalidOperationException.
        }
    }



AV1540 Be reluctant with multiple return statements
===================================================

One entry, one exit is a sound principle and keeps control flow readable.

However, if the method is very small and complies with guideline AV1500 then
multiple return statements may actually improve readability over some central
Boolean flag that is updated at various points.



AV1545 Don’t use selection statements instead of a simple assignment or initialization
======================================================================================

Express your intentions directly. For example, rather than::

    bool pos;
    if (val > 0) { pos = true; } else { pos = false; }

write::

    bool pos = (val > 0); // initialization



AV1546 Prefer conditional statements instead of simple if-else constructs
=========================================================================


For example, instead of::

    string result;
    if (someString != null)
    {
        result = someString;
    }
    else
    {
         result = “Unavailable”;
    }
    return result;

write::

    return someString ?? “Unavailable”;


AV1547 Encapsulate complex expressions in a method or property
================================================================

Consider the following example::

    if (member.HidesBaseClassMember
    && (member.NodeType != NodeType.InstanceInitializer))
    {
        // do something
    }


In order to understand what this expression is about, you need to analyze its
exact details and all the possible outcomes. Obviously, you could add an
explanatory comment on top of it, but it is much better to replace this complex
expression with a clearly named method:::

    if (NonConstructorMemberUsesNewKeyword(member))
    {
        // do something
    }

    private bool NonConstructorMemberUsesNewKeyword(Member member)
    {
        return     (member.HidesBaseClassMember
                && (member.NodeType != NodeType.InstanceInitializer)
    }


You still need to understand the expression if you are modifying it, but the
calling code is now much easier to grasp.


AV1551 Call the most overloaded method from other overloads
===========================================================

This guideline only applies to overloads that are intended for providing
optional arguments. Consider for example the following code snippet::

    public class MyString
    {
        private string someText;
        public MyString(string text) { this.someText = text; }
        public int IndexOf(string phrase)
        {
            return IndexOf(phrase, 0, someText.Length);
        }

        public int IndexOf(string phrase, int startIndex)
        {
            return IndexOf(phrase, startIndex, someText.Length - startIndex );
        }

        public virtual int IndexOf(string phrase, int startIndex, int count)
        {
        return someText.IndexOf(phrase, startIndex, count);
        }
    }


The class MyString provides three overloads for the IndexOf method, but two of
them simply call the one with the most arguments. Notice that the same rule
applies to class constructors; implement the most complete overload and call
that one from the other overloads using the this() operator.

Also notice that the parameters with the same name should appear in the same
position in all overloads.

Important If you also want to allow derived classes to override these methods,
define the most complete overload as a protected virtual method that is called
by all overloads.



AV1553 Only use optional parameters to replace overloads
========================================================

The only valid reason for using C# 4.0’s optional parameters is to replace the
example from rule AV1551 with a single method like:::

    public virtual int IndexOf(string phrase, int startIndex = 0, int count = 0)
    {
    return someText.IndexOf(phrase, startIndex, count);
    }

If the optional parameter is a reference type then it can only have a default
value of null.

But since strings, lists and collections should never be null according to rule
AV1, you must use overloaded methods instead.

Note The default values of the optional parameters are stored at the caller
side.

As such, changing the default value without recompiling the calling code will
not apply the new default value propery.



AV1555 Avoid using named parameters
====================================


C# 4.0’s named parameters have been introduced to make it easier to call COM
components that are known for offering tons of optional parameters.

If you need named parameters to improve the readability of the call to a
method, that method is probably doing too much and should be refactored.

The only exception where named parameters improve readability is when a
constructor that yields a valid object is called like this::

    Person person = new Person
    (
        firstName: "John",
        lastName: "Smith",
        dateOfBirth: new DateTime(1970, 1, 1)
    );


AV1561 Avoid methods with more than three parameters
====================================================

If you end up with a method with more than three parameters, use a structure or
class for passing multiple parameters such as explained in the Specification
design pattern.

In general, the fewer the number of parameters, the easier it is to understand
the method.

Additionally, unit testing a method with many parameters requires many scenarios
to test.

AV1562 Don’t use ref or out parameters
======================================

Ref and out parameters make code less understandable and therefore may introduce
bugs. Prefer returning compound objects instead.


AV1564 Avoid methods that take a bool flag
==========================================

A flag parameter based on a bool is not self-explanatory. Consider the following
method signature::

    public Customer CreateCustomer(bool platinumLevel) {}

On first sight this signature seems perfectly fine, but when calling this method
you will lose this purpose completely::

    Customer customer = CreateCustomer(true);


Often, a method taking such a flag is doing more than one thing and needs to be
refactored into two or more methods. An alternative solution is to replace the
flag with an enumeration.

AV1668 Don’t use parameters as temporary variables
===================================================

Never use a parameter as a convenient variable for storing temporary state.

Even though the type of your temporary variable may be the same, the name
usually does not reflect the purpose of the temporary variable.

AV1570 Always check the result of an as operation
=================================================

If you use as to obtain a certain interface reference from an object, always
ensure that this operation does not return null.

Failure to do so may cause a NullReferenceException at a much later stage if
the object did not implement that interface.

AV1575 Don’t comment-out code
==============================

Never check-in code that is commented-out, but instead use a work item tracking
system to keep track of some work to be done.

Nobody knows what to do when they encounter a block of commented-out code.

- Was it temporarily disabled for testing purposes ?
- Was it copied as an example ?
- Should I delete it ?

AV1580 Consider abstracting an external dependency or 3rd party component
=========================================================================

If your code relies on some kind of external class, service or UI control,
consider wrapping that dependency in a lightweight wrapper that only exposes
the members that are really used.

Such a wrapper smoothens the changes required when replacing that dependency
with another, but can also be used to hide any undesired behavior or bugs
that you don’t have influence on.
