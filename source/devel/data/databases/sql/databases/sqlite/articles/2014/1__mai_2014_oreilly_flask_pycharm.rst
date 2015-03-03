
.. index::
   pair: Flask ; Sqlite
   pair: SQLAlchemy; Sqlite

.. _sqlite_pycharm_mai_2014:

========================================================
Building ReSTful APIs with Flask in PyCharm (may 2014)
========================================================


.. seealso::

   - programming.oreilly.com/2014/05/building-restful-apis-with-flask-in-pycharm.html
   - https://github.com/johnlindquist/oreilly-article
   - http://flask.pocoo.org/
   - https://flask-restless.readthedocs.org/en/latest/
   - http://pythonhosted.org/Flask-SQLAlchemy/


Building APIs can be easier than you think. Say you’ve developed a product or 
service and would like to provide developer access via a ReSTful API quickly, 
with minimal effort and overhead. 

The lightweight Flask Python Web framework lets you easily build extendible 
APIs fast, without the bloat and ceremony of similar tools. 

Add to this the comprehensive workflow of a modern integrated development 
environment like PyCharm and you’ll be up and running posthaste.

We’ll start with installing a few prerequisites and set up our working 
environment so that testing, debugging, and extending the API can happen 
without too much hopping around. 

Afterward, we’ll move on to connecting to our database with SQLAlchemy, a Python 
SQL toolkit and object-relational mapper. 

We’ll finish up by creating the ReSTful API with Flask-Restless, a Flask 
extension that provides the simple generation of ReSTful JSON APIs for database 
models defined by SQLAlchemy. 


