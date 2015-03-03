
.. index::
   pair: sphinx ; copypasta
   pair: collaborative ; editing


.. _copypasta:

=======================
copypasta and sphinx
=======================


.. seealso::

   - https://copypasta.credibl.es/
   - :ref:`django_ucomment`


Copypasta is a collaborative editing tool. Readers submit edits, authors approve
changes, everyone wins.


garlicsims and copypasta
========================

.. seealso:: http://blog.garlicsim.org/post/3897688973/garlicsims-documentation-is-now-user-editable


A while ago I stumbled upon a very cool tool by Kurt Mackey called Copypasta.

As the website describes it: “Copypasta is a collaborative editing tool.

Readers submit edits, authors approve changes, everyone wins.”

It’s still a young and experimental project, but it’s quite promising. It often
happens that I’m reading a friend’s blog post and I see something that I want
to fix, like a typo or a grammar mistake.

What I usually do is fire an email to that friend alerting him to the typo.
This is of course inefficient. Copypasta lets you edit the page yourself in the
browser, and then it shoots an email to the site owner with your proposed changes.

Currently it requires the site owner to put the Copypasta button on the website
for it to work; in the future Kurt might release a browser plugin that will let
you edit any site on the internet.

That will be really awesome.

So I decided to put Copypasta on the GarlicSim documentation site. (This is a
Sphinx-based documentation site.) Now anyone can offer fixes for GarlicSim’s docs!

Let me know if there are any bugs.

I hope that more Python package maintainers will do this for their projects’
documentation so we could all help to improve each other’s documentation.

Now what I want is a Sphinx backend for Copypasta which will be able to
automatically change the documentation source in the repository, possibly creating
a GitHub pull request with the changes to the docs source...

But now I’m fantasizing :)


comment from Henning
--------------------

You could also try :ref:`http://ucomment.org/  <django_ucomment>`


comment from Jonas Obrist (https://github.com/ojii/)
------------------------------------------------------


About the last paragraph, I implemented exactly that for :ref:`readthedocs.org <read_the_doc>`
unfortunately it's not 100% working yet, but stay tuned!


comment from Robert Kern
-------------------------

ou may want to give the Numpy Documentation Editor a look. It's a web
documentation editor for Sphinx documentation checked into a repository.

- http://docs.scipy.org/numpy/Front%20Page/
- :ref:`http://code.google.com/p/pydocweb/  <pydocweb>`


coolRR   1 day ago in reply to Robert Kern
++++++++++++++++++++++++++++++++++++++++++

Yeah, I remember I considered using it for the GarlicSim docs a few months ago
but decided against it, don't remember why.

Looking at it now I see that it's not very easy to use. I now got into the
NumPy docs and pressed "edit" and I got a confusing screen where I
don't understand how I'm supposed to edit anything. Possibly UX is the reason
why :ref:`Pydocweb` hasn't gained wide adoption in the Python world.


