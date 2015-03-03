
.. index::
   javascript (multithreading) 
   html5 (workers)


.. _javascript_multithreading:

=========================
javascript multitreading
=========================

.. seealso:: 

   - http://david.blob.core.windows.net/html5/Introduction%20to%20the%20HTML5%20Web%20Workers%20the%20JavaScript%20multithreading%20approach.htm#firstwebworker
   - http://xebee.xebia.in/2010/11/02/multithreading-in-javascript-with-web-workers/
   - http://www.whatwg.org/specs/web-apps/current-work/complete/workers.html


Introduction to the HTML5 Web Workers: the JavaScript multithreading approach
=============================================================================

An HTML5 application is obviously written using JavaScript. 

But compared to other kind of development environments (like native one), 
JavaScript historically suffers from an important limitation: all its execution 
process remains inside a unique thread. This could be pretty annoying with 
today multi-cores processors like the i5/i7 containing up to 8 logical CPUs 
and even with the latest ARM mobile processors being dual or even quad-cores. 

Hopefully, we’re going to see that HTML5 offers to the web a way to better 
handle these new marvelous processors to help you embrace a new generation 
of web applications.



Before the workers
==================

.. seealso:: :ref:`technos_not_html5`

This JavaScript limitation implies that a long running processing will freeze 
the main window. We often say in our developers’ words that we’re blocking the 
“UI Thread”. This is the main thread in charge of handling all the visual 
elements and associated tasks: drawing, refreshing, animating, user inputs 
events, etc. We all know the bad consequences of overloading this thread: 
the page freezes and the user can’t interact anymore with your application. 

The user experience is then of course very bad and the user will probably 
decide to kill the tab or the browser instance. This is probably not something 
you’d like to see while using your application!  

To avoid that, the browsers have implemented a protection mechanism which 
alerts the user when a long-running suspect script occurs. Unfortunately, 
this protection mechanism can’t make the difference between a script not 
written correctly and a script which really needs more time to accomplish 
its work. Still, as it blocks the UI thread, it’s better to tell you that 
something wrong is maybe currently occurring. Here are some messages examples 
(from Firefox 5 & IE9).





