

.. index::
   ! Endianness
   pair: mixed ; endian
   pair: big ; endian
   pair: little ; endian
   pair: boutisme; endianness


.. _endianness:

==================================
Endianness
==================================


.. seealso::

   - http://en.wikipedia.org/wiki/Endianness
   - http://fr.wikipedia.org/wiki/Endianness


.. figure:: Endianessmap.svg.png
   :align:  center

   Endianness

.. contents::
   :depth: 3


Définition en français
======================

En informatique, certaines données telles que les nombres entiers peuvent être
représentées sur plusieurs octets.

L'ordre dans lequel ces octets sont organisés en mémoire ou dans une
communication est appelé endianness (mot anglais traduit par « boutisme » 1 ou
par « endianisme »).

De la même manière que certains langages humains s'écrivent de gauche à droite,
et d'autres s'écrivent de droite à gauche2, il existe une alternative majeure à
l'organisation des octets représentant une donnée : l'orientation big-endian et
l'orientation little-endian.

Ces expressions sont parfois traduites par gros-boutiste et petit-boutiste ou
par grand-boutien et petit-boutien.

Les expressions byte order, d’ordre des octets ou de byte sex sont également
utilisées (bien qu’ordre des octets fasse référence à l'unité d’une base numérale
précise sur 8 bits, que les autres termes plus généraux ne traduisent pas).

L'endianness qualifie aussi bien un fichier (dans lequel ce sont les bytes qui
sont ordonnés différemment) qu'un processeur (dans lequel la gestion des bits
a aussi un ordre).


Étymologie
==========

Les termes big-endian et little-endian ont été popularisés dans le domaine
informatique par Dany Cohen, en référence aux Voyages de Gulliver, roman
satirique de Jonathan Swift. En 1721, Swift décrit comment de nombreux habitants
de Lilliput refusent d'obéir à un décret obligeant à manger les œufs à la coque
par le petit bout.

La répression pousse les rebelles, dont la cause est appelée big-endian, à se
réfugier dans l'empire rival de Blefuscu ce qui entretient une guerre longue et
meurtrière entre les deux empires.

En 1980, Cohen publie « une tentative pour arrêter une guerre», celle qui oppose
les partisans big-endian et little-endian au sein du groupe qui travaille sur
les protocoles réseau qui conduiront à Internet.
Dans sa note technique, il indique qu'aucune argumentation logique ne peut
montrer la supériorité d'une convention sur l'autre ; cependant, dans le domaine
informatique, un choix doit être fait pour éviter l'anarchie.

La première traduction en français du roman de Swift utilise le terme gros-boutien.

L'Office québécois de la langue française préconise gros-boutiste et petit-boutiste,
ce qui conduit au nom **boutisme** adopté par au moins un ouvrage d'informatique pour
traduire endianness.

En informatique, le suffixe -iste est employé de préférence à -ien


Introdution
===========

In computing, the term endian or endianness refers to the ordering of individually
addressable sub-components within the representation of a larger data item as
stored in external memory (or, sometimes, as sent on a serial connection).

Each sub-component in the representation has a unique degree of significance,
like the place value of digits in a decimal number. These sub-components are
typically 16-, 32- or 64-bit words, 8-bit bytes, or even bits.

Endianness is a difference in data representation at the hardware level and may
or may not be transparent at higher levels, depending on factors such as the
type of high level language used.

The most common cases refer to how bytes are ordered within a single 16-, 32-,
or 64-bit word, and endianness is then the same as byte order.

The usual contrast is whether the most significant or least significant byte is
ordered first—i.e., at the lowest byte address—within the larger data item.

**A big-endian machine stores the most significant byte first, and a little-endian
machine stores the least significant byte first**.

In these standard forms, the bytes remain ordered by significance. However, mixed
forms are also possible where the ordering of bytes within a 16-bit word may
differ from the ordering of 16-bit words within a 32-bit word, for instance.

Although rare, such cases do exist and may sometimes be referred to as mixed-endian
or middle-endian.

Endianness is important as a low-level attribute of a particular data format.

For example, the order in which the two bytes of a UCS-2 character are stored in
memory is of considerable importance in network programming where two computers
with different byte orders may be communicating with each other.

Failure to account for a varying endianness across architectures when writing
code for mixed platforms leads to failures and **bugs that can be difficult to detect**.


The Intel x86 family and Digital Equipment Corporation architectures
(PDP-11, VAX, Alpha) are representatives of Little-Endian, while the Sun SPARC,
IBM 360/370, and Motorola 68000 and 88000 architectures are Big-Endians.

Still, other architectures such as PowerPC, MIPS, and Intel’s 64 IA-64 are
Bi-Endian, i.e. they are capable of operating in either Big-Endian or
Little-Endian mode.

Endianess is also referred to as the NUXI problem. Imagine the word UNIX stored
in two 2-byte words.

In a Big-Endian system, it would be stored as UNIX. In a little-endian system,
it would be stored as NUXI


Windows (on x86, x64) and Linux (on x86, x64) are both little-endian operating
systems.

Big endian
==========

.. figure:: Big-Endian.svg.png
   :align: center

   Big endian


The most significant byte (MSB) value, which is 0Ah in our example, is stored at
the memory location with the lowest address, the next byte value in
significance, 0Bh, is stored at the following memory location and so on.

This is akin to Left-to-Right reading in hexadecimal order.


Little endian
=============


.. figure:: Little-Endian.svg.png
   :align: center

   Little endian


Tutorials
=========

.. toctree::
   :maxdepth: 3

   tutorials/index


Source
======

.. toctree::
   :maxdepth: 3

   source/index






