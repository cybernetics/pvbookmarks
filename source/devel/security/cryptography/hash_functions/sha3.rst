

.. index::
   pair: hash ; SHA3
   pair: condensat ; SHA3


.. _sha3_keccak:

======================
SHA3 (Keccak)
======================


.. seealso::

   - http://keccak.noekeon.org/
   - http://en.wikipedia.org/wiki/SHA-3



.. contents::
   :depth: 3

Definitions
===========

Keccak (pronounced [kɛtʃak], like “ketchak”) is a cryptographic hash function
designed by Guido Bertoni, Joan Daemen, Michaël Peeters, and Gilles Van Assche,
building upon RadioGatún. On October 2, 2012, Keccak was selected as the winner
of the NIST hash function competition to select a SHA-3 algorithm.

The authors claim 12.5 cycles per byte on an Intel Core 2 CPU.

However, in hardware implementations it is notably faster than all other finalists.

Keccak uses the sponge construction in which message blocks are XORed into
the initial bits of the state, which is then invertibly permuted.

In its largest instance, the state consists of a 5×5 array of 64-bit words, 1600
bits total.

Reduced versions of the algorithm are defined for smaller power-of-2 word sizes
w down to 1 bit (25 bits total state).

While smaller state sizes can be used to test cryptanalytic attacks, intermediate
state sizes (e.g., from w=4, 100 bits, to w=32, 800 bits) also provide practical,
lightweight, alternatives.


NIST announce (October 2, 2012)
===============================

.. seealso:: http://www.nist.gov/itl/csd/sha-100212.cfm

The National Institute of Standards and Technology (NIST) today announced the
winner of its five-year competition to select a new cryptographic hash algorithm,
one of the fundamental tools of modern information security.

The winning algorithm, Keccak (pronounced “catch-ack”), was created by
Guido Bertoni, Joan Daemen and Gilles Van Assche of STMicroelectronics and
Michaël Peeters of NXP Semiconductors.

The team’s entry beat out 63 other submissions that NIST received after its open
call for candidate algorithms in 2007, when it was thought that SHA-2, the
standard secure hash algorithm, might be threatened.

**Keccak will now become NIST’s SHA-3 hash algorithm.**

Hash algorithms are used widely for cryptographic applications that ensure the
authenticity of digital documents, such as digital signatures and message
authentication codes.

These algorithms take an electronic file and generate a short "digest," a sort of digital fingerprint of the content. A good hash algorithm has a few vital characteristics. Any change in the original message, however small, must cause a change in the digest, and for any given file and digest, it must be infeasible for a forger to create a different file with the same digest.

The NIST team praised the Keccak algorithm for its many admirable qualities, including its elegant design and its ability to run well on many different computing devices. The clarity of Keccak’s construction lends itself to easy analysis (during the competition all submitted algorithms were made available for public examination and criticism), and Keccak has higher performance in hardware implementations than SHA-2 or any of the other finalists.

“Keccak has the added advantage of not being vulnerable in the same ways SHA-2 might be,” says NIST computer security expert Tim Polk. “An attack that could work on SHA-2 most likely would not work on Keccak because the two algorithms are designed so differently.”

Polk says that the two algorithms will offer security designers more flexibility. Despite the attacks that broke other somewhat similar but simpler hash algorithms in 2005 and 2006, SHA-2 has held up well and NIST considers SHA-2 to be secure and suitable for general use.

What then will SHA-3 be good for? While Polk says it may take years to identify all the possibilities for Keccak, it immediately provides an essential insurance policy in case SHA-2 is ever broken. He also speculates that the relatively compact nature of Keccak may make it useful for so-called “embedded” or smart devices that connect to electronic networks but are not themselves full-fledged computers. Examples include sensors in a building-wide security system and home appliances that can be controlled remotely.

“The Internet as we know it is expanding to link devices that many people do not ordinarily think of as being part of a network,” Polk says. “SHA-3 provides a new security tool for system and protocol designers, and that may create opportunities for security in networks that did not exist before.”


SHA3 competition
================

For more on the SHA3 competition, see http://csrc.nist.gov/groups/ST/hash/sha-3/index.html.




