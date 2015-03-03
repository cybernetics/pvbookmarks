
.. index::
   pair: FAQ; Async 


.. _async_csharp_faq:

==============================
Async C♯ FAQ 
==============================

.. seealso::

   - http://blogs.msdn.com/b/pfxteam/archive/2012/04/12/async-await-faq.aspx



Miguel de Icaza
===============

.. seealso 

   - http://tirania.org/blog/archive/2013/Aug-15.html
   
   
Today I had the chance to field a few questions, and I wanted to address those 
directly on my blog:

Q: Does async use a new thread for each operation ?
----------------------------------------------------

When you use Async methods, the operation that you requested is encapsulated 
in a Task (or Task<T>) object. Some of these operations might require a 
separate thread to run, some might just queue an event for your runloop, 
some might use kernel asynchronous APIs with notifications. 
You do not really know what an Async method is using behind the scenes, that is 
something that the author of each user will pick.

Q: It seems like you no longer need to use InvokeOnMainThread when using Async, why ?
--------------------------------------------------------------------------------------

When a task completes, the default is for execution to be resumed on the current 
synchronization context. This is a thread-local property that points to a specific 
implementation of a SynchronizationContext.

On iOS and Android, we setup a synchronization context on the UI thread that 
will ensure that code resumes execution on the main thread. 
Microsoft does the same for their platforms.

In addition, on iOS, we also have a DispatchQueue sync context, so by default 
if you start an await call on a Grand Central Dispatch queue, then execution is 
resumed on that queue.

You can of course customize this. 
Use SynchronizationContext and ConfigureAwait for this. 

