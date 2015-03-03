

.. index::
   Heroku (cloud application platform)
   Cloud computing (Heroku)
   Instant Deployment
   Continuous Deployment
   Poka-yoke
   Application platform (heroku)


.. _heroku_cloud_application_platform:

Heroku cloud application platform
=================================

.. seealso:: http://www.heroku.com/


Agile deployment for Ruby, Node.js, Clojure, Java, Python and Scala.

Get up and running in minutes, and deploy instantly with :ref:`git`.
Focus 100% on your code, and never think about servers, instances, or VMs again.

Instant Deployment
------------------

Deploying an app is simple and easy. No special tools needed, just a plain
git push. Deployment is instant, whether your app is big or small.

Read more about `git deployment`_.

.. _`git deployment`: .. http://devcenter.heroku.com/articles/git

Continuous Deployment
---------------------

Easily create testing, staging, and production versions of your app and deploy
to and between them instantly. The `dyno manifold`_ insures all parts of your
app are updated and bounced gracefully, `routing`_ continues seamlessly, and
traffic is held for data migrations by custom maintenance controls.

.. _`dyno manifold`: http://www.heroku.com/how/deploy#
.. _`routing`:  http://devcenter.heroku.com/articles/http-routing

Poka-yoke
---------

Move quickly and with confidence: Heroku follows a poka-yoke (mistake-proof)
design philosophy, including role-based permissions, integrity checks during
push, and robust release management and rollback controls.

If in doubt, watch every detail of the deployment process in real-time with
`Logplex`_.

.. _Logplex:  http://www.heroku.com/how/deploy#

Bruce Heckel example
====================

.. seealso:: http://www.artima.com/weblogs/viewpost.jsp?thread=335549

Heroku is a cloud application platform. They seem to have the goal of making
cloud deployment of your app as easy as possible, and they also seem to be
trying to adapt to whatever technology you happen to be using.

Just today (September 30, 2011) they announced support for Python.
You can find a `walkthrough here`_ and there's specific information about using
it with Django `here`_.

.. _`walkthrough here`: http://devcenter.heroku.com/articles/python
.. _`here`: http://blog.heroku.com/archives/2011/9/28/python_and_django/

Because I've been preparing for this speaking trip to Europe, I have yet to
delve into the details of Heroku. My friend James Ward (who now works there)
asked to see the code for this article, and upon receiving it had it set up
in less than 30 minutes (even though he is a Python novice and hasn't
used Web.py).

Here are the steps he used (with the basic Heroku stuff already set up):

Create a new file in your src dir named "Procfile" containing:

web: python server.py ${PORT}

Create a new file in your src dir named "requirements.txt" containing:

web.py

Create the git repo, add the files to it, and commit them::

    git init
    git add .
    git commit -m init

Create the app on Heroku::

    heroku create -s cedar

Deploy the app::

    git push heroku master

It's kind of clever the way they use git as the deployment mechanism. I have
to say I'm pretty impressed by how quickly this could be deployed on Heroku.
I think it's a tribute to the simplicity of Web.py that there weren't any snags.

`Here is the app running under Heroku`_.

.. _`Here is the app running under Heroku`: http://blazing-rain-3960.herokuapp.com/


