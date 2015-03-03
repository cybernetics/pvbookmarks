
.. index::
   RFC 5646
   RFC 5645
   BCP 47


=============================
Best of Practice 47 (BCP_47)
=============================

.. seealso::

   - https://secure.wikimedia.org/wikipedia/en/wiki/BCP_47
   - http://www.loc.gov/standards/iso639-2/php/English_list.php


IETF_ language tags are abbreviated language codes; for examples, "en" for English
or "en-CA" for Canadian English.


They are defined by the `BCP_ 47`_ standard track, which is currently composed of
normative `RFC 5646`_ and `RFC 4647`_ (also referencing the related informational `RFC 5645`_),
along with the normative content of the IANA Language Subtag Registry regulated
by these RFCs.

.. _IETF: https://secure.wikimedia.org/wikipedia/en/wiki/Internet_Engineering_Task_Force
.. _BCP: https://secure.wikimedia.org/wikipedia/en/wiki/Best_Current_Practice
.. _`RFC 5646`: http://tools.ietf.org/html/rfc5646
.. _`RFC 4647`: http://tools.ietf.org/html/rfc4647
.. _`RFC 5645`: http://tools.ietf.org/html/rfc5645
.. _`BCP_ 47`: https://secure.wikimedia.org/wikipedia/en/wiki/BCP_47

Relations to ISO 639-3 (individual languages and macro-languages) and some parts of ISO 639-1
=============================================================================================

The obsoleted RFC 4646 (as well as its current successor RFC 5646), unlike its
predecessors, defined the concept of an "extended language subtag", although it
still did not permit the registration of such subtags.

However, in the newer RFC 5645 and RFC 5646, all individual languages and
macro-languages of ISO 639-3 were finally registered as (primary) language subtags,
with a new language matching algorithm that allows a resource whose localization
is missing in an individual language to be looked for in its macro-language,
whose code is now present in the IANA database along with other classification
information coming from ISO 639-3 (and also ISO 639-5 for language families).

.. seealso:: http://www.loc.gov/standards/iso639-2/php/English_list.php



