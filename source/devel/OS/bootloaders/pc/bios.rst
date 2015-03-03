
.. index::
   pair: bootloader; BIOS
   pair: bootloader; MBR (Master Boot Record)


.. _bios:

==================
Micrologiciel BIOS
==================

Dans le cas le plus simple, il n'y a qu'une seule partition du disque de boot :
le micrologiciel BIOS charge les 512 premiers octets de ce disque, ces 512
octets constituant le MBR.

À partir des informations du MBR, il détermine l'emplacement du chargeur d'amorçage.

Si le disque de boot a plusieurs partitions, le micrologiciel BIOS lit le MBR du
disque, puis le VBR de la partition (Volume Boot Record, voir (en) VBR).

À partir de ces informations, il peut déterminer l'emplacement du chargeur
d'amorçage et le lancer.

Si le support de boot est une disquette, c'est le VBR de cette disquette qui est
utilisé pour déterminer l'emplacement du chargeur d'amorçage.






