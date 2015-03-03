


.. index::
   pair: ORM ; Peewee

.. _peewee:

====================
Peewee
====================


.. seealso::

   - https://peewee.readthedocs.org/en/latest/index.html


.. figure:: peewee.png
   :align: center

.. contents::
   :depth: 3


Introduction
=============

* a small, expressive orm
* written in python (2.6+, 3.2+)
* built-in support for sqlite, mysql and postgresql and special extensions like 
  `hstore <http://peewee.readthedocs.org/en/latest/peewee/playhouse.html#postgresql-hstore>`_

For flask integration, including an admin interface and RESTful API, check
out `flask-peewee <https://github.com/coleifer/flask-peewee/>`_.

For notes on the upgrade from 1.0 to 2.0, check out `the upgrade docs <http://peewee.readthedocs.org/en/latest/peewee/upgrading.html>`_.

Check out the `quickstart IPython notebook <http://nbviewer.ipython.org/d3faf30bbff67ce5f70c>`_.

Example queries::

    # a simple query selecting a user
    User.get(User.username == 'charles')

    # get the staff and super users
    editors = User.select().where(
        (User.is_staff == True) |
        (User.is_superuser == True)
    )

    # get tweets by editors ("<<" maps to IN)
    Tweet.select().where(Tweet.user << editors)

    # how many active users are there?
    User.select().where(User.active == True).count()

    # paginate the user table and show me page 3 (users 41-60)
    User.select().order_by(User.username).paginate(3, 20)

    # order users by number of tweets
    User.select().annotate(Tweet).order_by(
        fn.Count(Tweet.id).desc()
    )

    # a similar way of expressing the same
    tweet_ct = fn.Count(Tweet.id)
    (User
      .select(User, tweet_ct.alias('ct'))
      .join(Tweet)
      .group_by(User)
      .order_by(tweet_ct.desc()))

    # do an atomic update
    Counter.update(count=Counter.count + 1).where(
        Counter.url == request.url
    )


Check out the `quick start <http://peewee.readthedocs.org/en/latest/peewee/quickstart.html>`_ for more!



Articles
=========

.. toctree::
   :maxdepth: 3
   
   articles/index
   
   
