

.. index::
   pair: Vincent; Charts 


.. _vincent_chart_library:

=========================
Vincent chart library
=========================

.. seealso::

   - https://vincent.readthedocs.org/en/latest/charts_library.html
   

.. contents::
   :depth: 3
   
      
Introduction
=============

   
Vincent provides a charts library that allows for rapid creation and iteration 
of different chart types, with data inputs from a number of Python data 
structures. 

This library is built using the Vincent API to construct Vega grammar, with 
some adding conveniences for simple data input.   

Concept
========

The data capabilities of Python. The visualization capabilities of JavaScript.

Vincent allows you to build Vega specifications in a Pythonic way, and performs 
type-checking to help ensure that your specifications are correct. 

It also has a number of convenience chart-building methods that quickly turn 
Python data structures into Vega visualization grammar, enabling graphical 
exploration. 

It allows for quick iteration of visualization designs via getters and setters 
on grammar elements, and outputs the final visualization to JSON.

Perhaps most importantly, Vincent has Pandas-Fu, and is built specifically to 
allow for quick plotting of DataFrames and Series.

