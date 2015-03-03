

.. index::
   pair: ORM ; Sandman
   pair; Django-style ; Admin
   ! Sandman


.. _sandman:

===============================================
Sandman
===============================================

.. seealso::

   - https://sandman.readthedocs.org/en/latest/index.html
   - https://raw.github.com/jeffknupp/sandman/develop/README.md


Introduction
============

**sandman** "makes things REST". Have an existing database you'd like to expose via
a REST API? Normally, you'd have to write a ton of boilerplate code for
the ORM you're using, then integrate that into some web framework. 

I don't want to write boilerplate.

Here's what's required to create a RESTful API service from an existing database using
**sandman**::

    from sandman import app, db

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chinook'

    from sandman.model import register, Model

    class Artist(Model):
        __tablename__ = 'Artist'

    class Album(Model):
        __tablename__ = 'Album'

    class Playlist(Model):
        __tablename__ = 'Playlist'

    register((Artist, Album, Playlist))

    app.run()



Let's start our new service and make a request::


::

    > python runserver.py &
    * Running on http://127.0.0.1:5000/


:


    > curl GET http://localhost:5000/artists


::

    {
        "ArtistId": 273,
        "Name": "C. Monteverdi, Nigel Rogers - Chiaroscuro; London Baroque; London Cornett & Sackbu",
        "links": [
        {
            "rel": "self",
            "uri": "/artists/ArtistId"
        }
        ]
    },
    {
        "ArtistId": 274,
        "Name": "Nash Ensemble",
        "links": [
        {
            "rel": "self",
            "uri": "/artists/ArtistId"
        }
        ]
    },
    {
        "ArtistId": 275,
        "Name": "Philip Glass Ensemble",
        "links": [
        {
            "rel": "self",
            "uri": "/artists/ArtistId"
        }
        ]
    }


Django-style admin
==================


Oh, that's not enough? You also want a Django-style admin interface built
automatically? Fine. Add one more line to the list of models to get access to
this:


RESTful API
===========

With **sandman**, (almost) zero boilerplate code is required. Your existing database
structure and schema is introspected and your database tables magically get a
RESTful API and admin interface. For each table, Sandman creates:

* proper endpoints 
* support for a configurable set of HTTP verbs 
    * GET
    * POST
    * PATCH
    * PUT
    * DELETE
* responses with appropriate `rel` links automatically
* custom validation by simply defining `validate_<METHOD>` methods on your Model
* explicitly list supported methods for a Model by setting the `__methods__` attribute
* customize a Models endpoint by setting the `__endpoint__` method
* essentially a HATEOAS-based service sitting in front of your database

*Warning: Sandman is still very much a work in progress. Use it at your own risk. 
It's also often changing in backwards incompatible ways.*


