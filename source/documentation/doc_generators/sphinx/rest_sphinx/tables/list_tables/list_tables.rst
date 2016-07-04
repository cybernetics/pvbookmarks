

.. index::
   pair: Sphinx ; list-table
   ! list-table


.. _list_tables:
.. _list_table:

===========
list-table
===========

.. seealso::

   - http://sfepy.org/doc-devel/developer_guide.html#sfepy-directory-structure
   - :ref:`petl_examples`
   - :ref:`rest_tables`


.. contents::
   :depth: 3

Description
============

Bulleted lists can sometimes be cumbersome and hard to follow.

When dealing with a **long list of items**, use ``list-tables``.


Exemple
========

.. seealso::

   - http://sfepy.org/doc-devel/developer_guide.html#sfepy-directory-structure


Exemple 1
----------

For example, to talk about a list of options, create a table that looks like this:

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Shapes
     - Description
   * - Square
     - Four sides of equal length, 90 degree angles
   * - Rectangle
     - Four sides, 90 degree angles

This is done with the following code::

   .. list-table::
      :widths: 20 80
      :header-rows: 1

      * - Shapes
        - Description
      * - Square
        - Four sides of equal length, 90 degree angles
      * - Rectangle
        - Four sides, 90 degree angles

Example 2
-------------------------------------


.. list-table::
   :widths: 33 33 33
   :header-rows: 1

   * - 
     - 
     - 
     
   * - .. image:: image_selection/up_image1.png
     - .. image:: image_selection/up_image2.png
     - .. image:: image_selection/up_image3.png
     
   * - .. image:: image_selection/down_image4.png
     - .. image:: image_selection/down_image5.png
     - .. image:: image_selection/down_image6.png



This is done with the following code::

    .. list-table::
       :widths: 33 33 33
       :header-rows: 1

       * - 
         - 
         - 
         
       * - .. image:: image_selection/up_image1.png
         - .. image:: image_selection/up_image2.png
         - .. image:: image_selection/up_image3.png
         
       * - .. image:: image_selection/down_image4.png
         - .. image:: image_selection/down_image5.png
         - .. image:: image_selection/down_image6.png
         
 
Example 3
-------------------------

.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - Error type
     - Definition
     - Impact

   * - False Match
     - Comparison decision of “match” for a biometric probe and a biometric 
       reference that are from different fingers
     - System security lack
     
   * - False Non-Match
     - Comparison decision of “non-match” for a biometric probe and a biometric 
       reference that are from the same finger
     - User inconvenience    
     
This is done with the following code::

    .. list-table::
       :widths: 20 60 20
       :header-rows: 1

       * - Error type
         - Definition
         - Impact

       * - False Match
         - Comparison decision of “match” for a biometric probe and a biometric 
           reference that are from different fingers
         - System security lack
         
       * - False Non-Match
         - Comparison decision of “non-match” for a biometric probe and a biometric 
           reference that are from the same finger  
         - User inconvenience            
              

         
