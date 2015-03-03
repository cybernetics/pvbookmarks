
.. index::
   pair: ffmpeg ; history:



.. _ffmpeg_history:

==============
ffmpeg history
==============

.. seealso:: :ref:`libav_history`

May 3, 2011
===========

FFmpeg now accesses x264 presets via libx264.

This extends functionality by introducing several new libx264 options including
-preset, -tune, and -profile.

You can read more detailed information about these options with "x264 --fullhelp".

The syntax has changed so be sure to update your commands.

Example::

    ffmpeg -i input -vcodec libx264 -preset fast -tune film -profile main -crf 22 -threads 0 output








