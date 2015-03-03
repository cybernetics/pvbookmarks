

.. index::
   pair: Pandas ; Ggplot


.. _ggplot:

===========================================================================
Ggplot
===========================================================================

.. seealso::

   - https://github.com/yhat/ggplot
   - http://blog.yhathq.com/posts/ggplot-for-python.html
   - https://twitter.com/YhatHQ
   - https://github.com/yhat/DataGotham2013/


.. contents::
   :depth: 3
   
   
Concept
========

Analytical projects often begin w/ exploration--namely, plotting distributions 
to find patterns of interest and importance. 
And while there are dozens of reasons to add R and Python to your toolbox, it 
was the supperior visualization faculties that spurred my own investment in 
these tools.

``Excel`` makes some great looking plots, but I wouldn't be the first to say that 
creating charts in `Excel involves a lot of manual work`_. 
Data is messy, and exploring it requires considerable effort to clean it up, 
transform it, and rearrange it from one format to another. 
R and Python make these tasks easier, allowing you to visually inspect data in 
several ways quickly and without tons of effort.

The preeminent graphics packages for R and Python are ggplot2 and matplotlib 
respectively. Both are feature-rich, well maintained, and highly capable. 

Now, I've always been a ggplot2 guy for graphics, but I'm a Python guy for 
everything else. As a result, I'm constantly toggling between the two languages 
which can become rather tedious.


This is a post about ggplot2 and an attempt to bring it to Python.

Give me some ggplot
--------------------

There's no shortage of talk around improving the plotting capabilities of Python. 
Libraries like Bokeh, d3py are exciting or at least intruiging, but they aren't 
as accessible as either ggplot2 or matplotlib (yet, at least).

I don't know all that much about these two projects, but are they solving for 
interactivity and presentation or for every day data exploration? 
Most of the time, I just want to plot(X,y), see the results, and move on. 
matplotlib works, but it's not exactly the belle of the ball among contemporary 
graphics libraries. And let's get real for a second, matplotlib just stinks the 
big one from a usability perspective.




.. _`Excel involves a lot of manual work`:  http://learnr.wordpress.com/2009/03/16/ggplot2-split-data-range-into-multiple-chart-series/

   
   
Versions
========

.. toctree::
   :maxdepth: 3
   
   versions/index
   
      
