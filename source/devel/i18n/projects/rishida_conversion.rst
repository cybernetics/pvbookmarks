


.. index::
   i18n rishida conversion


========================
rishida conversion tool
========================

.. seealso::

   - http://rishida.net/tools/conversion/
   - http://rishida.net/blog/?p=547


Exemple: http://rishida.net/tools/conversion/?q=Cr%C3%AApes


http://rishida.net/blog/?p=547
==============================

It has always been possible to pass a string to the converter in the URI, but
that was never documented.

Now it is, and you can pass a string using the q parameter. For example,
http://rishida.net/tools/conversion/?q=Crêpes. You can also pass a string with
escapes in it, but you will need to be especially careful to percent escape
characters such as &, + and # which affect the URI syntax.
For example, http://rishida.net/tools/conversion/?q=CrU%2B00EApes.
