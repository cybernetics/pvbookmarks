
.. index::
   Sagrada (Web)


===============
Sagrada project
===============

.. seealso:: http://tarekziade.wordpress.com/2011/09/22/sagrada-creation-and-hosting-of-web-services/

The bottom line is that web services can be described in a Domain Specific 
Language (DSL) that can be used to generate the documentation automatically 
(and it stays accurate and up to date) but also to set up in the server things 
we usually do on the code side: the request dispatching.

And if we hide the DSL behind a nice user interface developers can use to build 
their apps, that’s even better. That’s what’s happening in the screencast 
I’ve recorded. The forms generate portions of DSL.

A web service DSL
=================

Back to our DSL. When you write a web service, it’s always the same story no 
matter what framework you’re using, you’re basically doing these steps 
(I am over-simplying for now)::

    Define a route for your service on the server
    Build the response
    Send back the response

These steps can be described in a simple DSL.

Here’s a basic example::

    path hello_world (
     description "Simplest application: Hello World!",
     method GET,
     url /hello,
     use python:somemodule.hello
     );

With a function hello located in somemodule that can look like this::

	def hello(request):
		return 'Hello World'

   
The application in that case is composed of:

- a DSL file
- a Python file with a single function

It’s easy from there with the proper DSL parser to:

- deploy those two files in our infrastructure
- run the app
- provide auto-generated documentation for the service

Architecture

The prototype I’ve written for the demo does the following:

- The tool is a web application that provides forms to create Service Containers
- Each Service Container has a unique root on the server
- In each container you can add web services.
- For each container, the DSL is built on the fly, then the corresponding AST 
  is kept in memory. The web UI allow users to modify it on the fly
- When a request comes in, it’s rooted to the right Service Container depending 
  on the beginning of the path, then the AST is used to find out what 
  function(s) should be used. The function is then executed in a sandbox.

The prototype also provides a command-line tool to start a server by loading 
an arbitrary DSL file.

The DSL Parser
==============

I will not go in to great details here, you can look at my previous posts 
mentioning RedBarrel.

The current DSL is implemented with PLY and can be found here_.

:download:`download parser.py <parser.py>`

.. _here: https://bitbucket.org/tarek/redbarrel/src/9f466fd5c2eb/redbarrel/dsl/parser.py




