

.. index::
   pair: Seaborn ; Notebooks
   pair: Timeseries data ; Seaborn
   pair: Seaborn ; Notebooks (Timeseries data )


.. _seaborn_notebooks:

===========================================
Seaborn Notebooks
===========================================

.. seealso::

   - http://stanford.edu/~mwaskom/software/seaborn/tutorials.html
   - :ref:`notebooks_seaborn` 


.. contents::
   :depth: 3

Introduction
============

There are a few tutorial notebooks that offer some thoughts on visualizing 
statistical data in a general sense and show how to do it using the tools 
that are provided in seaborn. 

The notebooks are meant to be fairly, but not completely comprehensive; hopefully 
the docstrings for the specific functions will answer any additional questions.



Plotting statistical timeseries data
=====================================

.. seealso::

   - http://stanford.edu/~mwaskom/software/seaborn/timeseries_plots.html


This notebook focuses on the tsplot function, which can be used to plot 
statistical timeseries data. 

Timeseries data consists of values for some dependent variable that are observed 
at several timepoints. 
In general, these data are thought of as realizations from some continuous 
process, so the tsplot function makess the visualization of that process simple 
(though not strictly enforced). Importantly, the function is concerned with 
plotting statistical timecourses: the expected dataset is additionally structured 
into sets of observations for several sampling units, such as subjects or 
neurons. 
In the presentation of these data, the unit dimension is frequently collapsed 
across to plot some measure of central tendency along with a representation of 
the variability introduced by sampling and measurement error. tsplot is capable 
of representing that variabilty with several sophisticated methods that are 
appropriate in different circumstances.

