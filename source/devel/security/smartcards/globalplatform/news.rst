

.. index::
   GlobalPlatform news

===================
globalplatform news
===================


::

    de  Martin Paljak <martin@martinpaljak.net>
    heure de l'expéditeur   Envoyé à 09:33 (GMT+02:00). Heure locale : 11:40. ✆
    répondre à  MUSCLE <muscle@lists.musclecard.com>
    à   MUSCLE <muscle@lists.musclecard.com>
    date    25 mars 2011 09:33
    objet   Re: [Muscle] GlobalPlatform Library & GPShell documentation now online



Hello,


::

    > There are two issues that I find interesting, but I'm not sure
    > if you want to put information about these in the wiki:
    > a) where can people get javacard cards at reasonable price?

I used to buy a bunch of Oberthur Cosmos V7 cards from smartcardfocus.com [1]
but they seem to be unavailable at the moment.
cryptoshop.com seem to sell JCOP 41 v2.3.1 cards but I've not ordered from them
before (should try though).

There are probably other sources as well, if you find them, OpenSC FAQ has an entry "Where can I buy smart cards?"  [2]

Why shouldn't this information be in a wiki?

::

    > b) what about the standards of the javacards, e.g. JCOP?
    >   as far as I know there is some functionality you can't access
    >   once you get the finished card (e.g. change ATR, UID etc.).
    >   IIRC the documentation is closed under NDA, but if anyone
    >   found a copy available on the net, that would be interesting...

JCOP is not a standard, it is an implementation of a JavaCard platform by
IBM / NXP. There are other vendors as well.

JavaCard specs as well as GlobalPlatform specs and API-s are freely available.
Both can be downloaded as .zip files but extracted versions are also available
from google:

- http://www.win.tue.nl/pinpasjc/docs/apis/jc222/
- http://www.win.tue.nl/pinpasjc/docs/apis/gp211/

[1] http://www.smartcardfocus.com/shop/ilp/id~407/Cosmo_V7_128K/p/index.shtml
[2] http://www.opensc-project.org/opensc/wiki/FrequentlyAskedQuestions#Q:WherecanIbuysmartcards


::

    de  Sébastien Lorquet <squalyl@gmail.com>
    heure de l'expéditeur   Envoyé à 11:00 (GMT+01:00). Heure locale : 12:57. ✆
    répondre à  MUSCLE <muscle@lists.musclecard.com>
    à   MUSCLE <muscle@lists.musclecard.com>
    date    25 mars 2011 11:00
    objet   Re: [Muscle] GlobalPlatform Library & GPShell documentation now online



::

    There are two issues that I find interesting, but I'm not sure
    if you want to put information about these in the wiki:
    a) where can people get javacard cards at reasonable price?
    b) what about the standards of the javacards, e.g. JCOP?
      as far as I know there is some functionality you can't access
      once you get the finished card (e.g. change ATR, UID etc.).
      IIRC the documentation is closed under NDA, but if anyone
      found a copy available on the net, that would be interesting...


You're talking about not initialized cards. First, it's near impossible to
find cards in this state, so the doc would be useless, and second, the commands
available in these modes are generally secret and not even available with NDAs
outside the manufacturer. In these initialization states, cards are not
javacards yet, they are totally proprietary objects, as you might already know.

Aditionnaly, please avoid talking about "JCOP" when referring to Java Card,
JCOP is a (not so good for all applications) NXP product, and fortunately,
there are bunch of other manufacturers and cards, such as the Oberthur Cosmo,
the Gemalto GXP/GCX and some others at G&D, for example.

All of these cards follow a single standard, namely Java Card.

Sebastien





