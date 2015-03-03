


.. _API_design_is_ui:

===============================
api-design-is-ui-for-developers
===============================

.. contents::
   :depth: 3

.. seealso::

   - http://shkspr.mobi/blog/index.php/2012/03/api-design-is-ui-for-developers/


Introduction
============

So, here are my hastily scribbled thoughts on what an API needs at a minimum to
entice the busy developer.

I don’t think any of these are Earth-shattering, but it’s amazing how many APIs
fail to meet even these basic requirements.


Easy Access
===========

- Don’t make me register, set up an account, or fill in a load of forms – I just
  want to see what I can do with you before I make a commitment.
- Don’t give me absurd key signing requirement – I should be able to call the
  API from a web browser just by typing stuff in.
- Do make it as easy as possible for me to get started – get your CEO
  (or similar) and see how long it takes her to set up an account & launch her
  first call. If it’s more than 5 minute, go back to the drawing board.

Example Code
============

Documentation
=============

I need to know what I can do, how I can do it, why I should do it a certain way,
and what response to expect.

Full Enumeration of Responses
==============================

A good example is Twitter’s “retweet_count”, the documentation used to imply
that the response would always be an integer.

However, it would occasionally respond with a string of “100+”. Naturally, this
meant developers would write code expecting ints which would fail whenever a
string was encountered. If you can’t tell me what responses to expect – how can
I code something which handles those responses correctly?

Variety of Response Language
=============================

The customer is always right. If the customer (developer) wants JSON, XML,
PHPobject, or just plain text – you should give it to them.

It’s the API designer’s job to make life easy for developers – so reply in
whatever formats the developer wants.

Human Readable Response
=======================

Developers are humans! Yes! It’s true! And they can’t all pretty-print JSON in
their heads. Give them something they can read without resorting to external tools.

Unless you have a very good reason not to – all your responses should be
pretty-printed. It helps with debugging and makes life just that little bit
easier for a struggling developer.

Human Readable Requests
=======================

Developers are humans! Yes! It’s true! And they can’t all remember every
little acronym in their heads. Give them something they can read without
resorting to documentation.

Unchanging
==========

Consistency is a virtue. If you have two similar APIs (say, search & read) they
should take the same parameters and produce identically formatted responses.

If you have to change the way your API responds, or the way it accepts request,
that’s fine – but use versioning so that developers don’t have to update their
code if they don’t want to.

Never deprecate anything! Once an embedded device has had its firmware burned,
it’s unlikely to ever be updated. If people or services rely on you, it’s simply
unacceptable to kill something off.

Remember, not every developer or end user can update their software.

Simplicity
==========

Try to explain what you’re doing in a single sentence. If you can’t – it’s
probably too complicated.

Libraries
=========

I’m sure you’re very proud that your community has created some libraries – but
they’re not good enough.

Detailed Errors
================

Do you really need to throw an error? Can your API take a “best” guess at what
the user was trying to do? Be generous in what you accept.

Feedback
========

Provide a mechanism where people can feed back what they think is broken, poorly
implemented, missing, or just plain confusing.

So What ?
=========

There is nothing new in this post to the seasoned developer.

But as Matt Gemmell reminded me recently – some people just don’t know the basics.

If you’re interested in making your API useful for developers, you have to treat
it like any other product.

You have to consider HCI factors, you have to do product testing, design, and
planning.

Your API is a product.

Treat your developers as you would your most profitable users.

Further Reading
===============

There are many books on this subject – the two I recommend are:

- `Basics of the Unix Philosophy`_ (free).
- `The Design of Everyday Things`_ (paper or ebook).



.. _`Basics of the Unix Philosophy`:  http://www.faqs.org/docs/artu/ch01s06.html
.. _`The Design of Everyday Things`:  http://www.amazon.co.uk/gp/product/0465067107/ref=as_li_ss_tl?ie=UTF8&tag=shkspr-21&linkCode=as2&camp=1634&creative=19450&creativeASIN=0465067107



