

.. index::
   pair: Time; Pandas (timeseries)
   pair: Time Series; Pandas
   

.. _pandas_timeseries:

========================
Pandas timeseries
========================

.. seealso::

   - http://pandas.pydata.org/pandas-docs/version/0.13.0/timeseries.html


.. contents::
   :depth: 3



What ?
=======

``pandas`` has proven very successful as a tool for working with time series data, 
especially in the financial data analysis space. 

With the 0.8 release, we have further improved the time series API in pandas 
by leaps and bounds. 

Using the new NumPy datetime64 dtype, we have consolidated a large number of 
features from other Python libraries like scikits.timeseries as well as 
created a tremendous amount of new functionality for manipulating time series 
data.

In working with time series data, we will frequently seek to:

- generate sequences of fixed-frequency dates and time spans
- conform or convert time series to a particular frequency
- compute “relative” dates based on various non-standard time increments 
  (e.g. 5 business days before the last business day of the year), or “roll” 
  dates forward or backward

pandas provides a relatively compact and self-contained set of tools for 
performing the above tasks.


Pandas notebook
================


.. seealso::

   - http://nbviewer.ipython.org/urls/bitbucket.org/hrojas/learn-pandas/raw/master/lessons/01%20-%20Lesson.ipynb
   
   
