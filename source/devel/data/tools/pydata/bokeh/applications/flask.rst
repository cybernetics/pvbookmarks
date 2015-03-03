

.. index::
   pair: Flask ; Bokeh



.. _bokeh_flask:

===================================================
Rendering Bokeh plots in Flask
===================================================


.. seealso::

   - https://github.com/rpazyaquian/bokeh-flask-tutorial/wiki/Rendering-Bokeh-plots-in-Flask
   - :ref:`flask_web_framework`
   
 
.. contents::
   :depth: 3
   
      
Introduction
=============

One thing I really wanted to do while working with Bokeh is to render my own 
plots and embed them in a template served by Flask. 

I've figured out how to do this, to a degree, so I've decided to create a 
tutorial on embedding Bokeh plots into HTML via Flask and its templating system. 

This tutorial assumes you know the basics of both Flask and Bokeh - not that 
you can't follow it otherwise, but once you're familiar with them the details 
make much more sense.

First of all, let's define the absolute basics you need for serving a Bokeh plot on a webpage:

- A plotting function that returns an HTML snippet.
- A basic Flask app that will render this HTML snippet.

With this, we should be able to serve a plot on a webpage without the need of 
bokeh-server. 

This is extremely useful if you want to integrate these plots into an app 
deployed onto Heroku, for example.

.. note:: I highly suggest that you type out the code snippets I share with you 
   instead of copying them. I feel that simply pasting the code into a text 
   editor doesn't let you understand how and why you are building the code.

   
