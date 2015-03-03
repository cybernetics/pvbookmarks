
.. index::
   pair: Libusbx ; 1.0.14


.. _libusbx_1.0.14:

============================
libusbx 1.0.14 (2012-09-26)
============================


.. seealso::

   - http://sourceforge.net/projects/libusbx/files/releases/1.0.14/




* Reverts the previous API change with regards to bMaxPower.
  If this doesn't matter to you, you are encouraged to keep using v1.0.13,
  as it will use the same attribute as v2.0, to be released soon.
* Note that LIBUSBX_API_VERSION is *decreased* to 0x010000FF and the previous
  guidelines with regards to concurent use of MaxPower/bMaxPower still apply.
