
.. index::
   pair: python; classes comment

.. _python_classes_comment_g:

================================
Classes should have a doc string
================================

Classes should have a doc string below the class definition describing the class.

If your class has public attributes, they should be documented here in an
Attributes section and follow the same formatting as a function's Args section.

::

	class SampleClass(object):
		"""Summary of class here.

		Longer class information....
		Longer class information....

		Attributes:
			likes_spam: A boolean indicating if we like SPAM or not.
			eggs: An integer count of the eggs we have laid.
		"""

		def __init__(self, likes_spam=False):
			"""Inits SampleClass with blah."""
			self.likes_spam = likes_spam
			self.eggs = 0

		def public_method(self):
			"""Performs operation blah."""




