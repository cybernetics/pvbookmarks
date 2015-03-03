

.. index::
   pair: Notebooks ; Pandas


.. _pandas_csv:

=======================================
Reading csv files with Pandas 
=======================================

::

    import pandas as pd
    d = pd.read_csv('example_1.csv')
    print d
    print type(d)
    

::

    
               Name        DOB  Years Degree Last Name First Name
    0   Alice Jones  12/1/1980      3     MS     Jones      Alice
    1     Bob Smith   1/1/1969      4     BS     Smith        Bob
    2     John Book   5/3/1980     11     BA      Book       John
    3  Billy Blanks   6/9/2000      8     AA    Blanks      Billy

    [4 rows x 6 columns]
    <class 'pandas.core.frame.DataFrame'>


Now, we have read the CSV file as a pandas DataFrame which is a super-structure 
that sits on top of numpy. 

Let's examine the columns of this DataFrame
