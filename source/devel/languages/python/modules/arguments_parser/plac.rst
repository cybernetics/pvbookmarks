


.. _python_plac_parser:

===================
plac
===================

.. seealso::

   - http://plac.googlecode.com/hg/doc/plac.html
   - http://pypi.python.org/pypi/plac
   - :ref:`python_pep_0389`



There is no want of command line arguments parsers in the Python world. The standard
library alone contains three different modules: getopt (from the stone age), optparse
(from Python 2.3) and argparse (from Python 2.7). All of them are quite powerful and
especially argparse is an industrial strength solution; unfortunately, all of them
feature a non-zero learning curve and a certain verbosity.
They do not scale down well, at least in my opinion.


It should not be necessary to stress the importance scaling down; nevertheless,
a lot of people are obsessed with features and concerned with the possibility of
scaling up, forgetting the equally important issue of scaling down.

This is an old meme in the computing world: programs should address the common
cases simply and simple things should be kept simple, while at the same keeping
difficult things possible. plac adhere as much as possible to this philosophy
and it is designed to handle well the simple cases, while retaining the ability
to handle complex cases by relying on the underlying power of argparse.

Technically plac is just a simple wrapper over argparse which hides most of its
complexity by using a declarative interface: the argument parser is inferred
rather than written down by imperatively. Still, plac is surprisingly scalable
upwards, even without using the underlying argparse. I have been using Python
for 8 years and in my experience it is extremely unlikely that you will ever
need to go beyond the features provided by the declarative interface of plac:
they should be more than enough for 99.9% of the use cases.

