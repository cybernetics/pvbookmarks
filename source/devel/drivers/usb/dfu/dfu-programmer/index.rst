

.. index::
   pair: dfu ; programmer


.. _atmel_dfu_programmer:

====================
ATMEL dfu-programmer
====================

.. seealso::

   - http://dfu-programmer.sourceforge.net/
   - https://lists.sourceforge.net/lists/listinfo/dfu-programmer-user


Why dfu-programmer
==================

The need for this tool came about when I needed to flash an at89c51snd1c chip that
had the USB bootloader on it, but the Atmel provided tool (FLIP) didn't support
USB flashing in linux.

After a few days of web searching and scrapping together a windows machine to do
the job, I found that Atmel provided a document describing the communications
protocol used.
I happily spent the next week hacking together the start of dfu-programmer.





