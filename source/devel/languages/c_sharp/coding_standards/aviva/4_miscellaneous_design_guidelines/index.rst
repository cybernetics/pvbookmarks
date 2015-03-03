
.. index::
   pair: error; exception

=================================
4 Miscellaneous Design Guidelines
=================================


AV1200 Throw exceptions rather than returning some kind of status value
=======================================================================

A code base that uses return values for reporting the success or failure tends
to have nested if-statements sprinkled all over the code.

Quite often, a caller forgets to check the return value anyhow.

Structured exception handling has been introduced to allow you to throw
exceptions and catch or replace exceptions at a higher layer.

In most systems it is quite common to throw exceptions whenever an unexpected
situations occurs.

AV1202 Provide a rich and meaningful exception message text
===========================================================

The message should explain the cause of the exception and clearly describe what
needs to be done to avoid the exception.

AV1205 Throw the most specific exception that is appropriate
=============================================================


For example, if a method receives a null argument, it should throw
ArgumentNullException instead of its base type ArgumentException.

AV1210 Don’t swallow errors by catching generic exceptions
==========================================================


Avoid swallowing errors by catching non-specific exceptions, such as Exception,
SystemException, and so on, in application code.

Only top-level code, such as a Last-Chance Exception Handler, should catch a
non-specific exception for logging purposes and a graceful shutdown of the
application.


AV1220 Always check an event handler delegate for null
======================================================


An event that has no subscribers is null, so before invoking, always make sure
that the delegate list represented by the event variable is not null.

Furthermore, to prevent conflicting changes from concurrent threads, use a
temporary variable to prevent concurrent changes to the delegate::

    event EventHandler<NotifyEventArgs> Notify;

    void RaiseNotifyEvent(NotifyEventArgs args)
    {
        EventHandler<NotifyEventArgs> handlers = Notify;
        if (handlers != null)
        {
            handlers(this, args);
        }
    }

Tip You can prevent the delegate list from being empty altogether.

Simply assign an empty delegate like this::

    event EventHandler<NotifyEventArgs> Notify = delegate {};


AV1225 Use a protected virtual method to raise each event
=========================================================

Complying with this guideline allows derived classes to handle a base class
event by overriding the protected method. The name of the protected virtual
method should be the same as the event name prefixed with On.

For example, the protected virtual method for an event named TimeChanged is
named OnTimeChanged.

Important Derived classes that override the protected virtual method are not
required to call the base class implementation.

The base class must continue to work correctly even if its implementation is
not called.


AV1230 Consider providing property-changed events
=================================================

Consider providing events that are raised when certain properties are changed.
Such an event should be named PropertyChanged, where Property should be replaced
with the name of the property with which this event is associated.

Note If your class has many properties that require corresponding events,
consider implementing the INotifyPropertyChanged interface instead.

It is often used in the Presentation Model and Model-View-ViewModel patterns.

AV1235 Don’t pass null as the sender parameter when raising an event
====================================================================

Often, an event handler is used to handle similar events from multiple senders.
The sender argument is then used to get to the source of the event. Always pass
a reference to the source (typically this) when raising the event.

Furthermore don’t pass null as the event data parameter when raising an event.
If there is no event data, pass EventArgs.Empty instead of null.
Exception On static events, the sender parameter should be null.

AV1240 Use generic constraints if applicable
============================================

Instead of casting to and from the object type in generic types or methods, use
where contraints or the as operator to specify the exact characteristics of the
generic parameter. For example::

    class SomeClass {}
    // Don't class MyClass<T>
    {
        void SomeMethod(T t)
        {
            object temp = t; SomeClass obj = (SomeClass) temp;
        }
    }
    // Do class MyClass<T> where T : SomeClass
    {
        void SomeMethod(T t)
        {
            SomeClass obj = t;
        }
    }


AV1245 Don’t add extension methods to the same namespace as the extended class
==============================================================================

Even though it may seem convenient to add extension methods related to the
String class in the System namespace, this may cause conflicts with future
versions of the .NET Framework.


AV1250 Evaluate the result of a LINQ expression before returning it
====================================================================

Consider the following code snippet::

    public IEnumerable<GoldMember> GetGoldMemberCustomers()
    {
        const decimal GoldMemberThresholdInEuro = 1000000;
        var q = from customer in db.Customers
                where customer.Balance > GoldMemberThresholdInEuro
                select new GoldMember(customer.Name, customer.Balance);
        return q;
    }

Since LINQ queries use deferred execution, returning q will actually
return the expression tree representing the above query. Each time the caller
evaluates this result using a foreach or something similar, the entire query
is re-executed resulting in new instances of GoldMember every time.

Consequently, you cannot use the == operator to compare multiple GoldMember
instances. Instead, always explicitly evaluate the result of a LINQ query
using ToList(), ToArray() or similar methods.


