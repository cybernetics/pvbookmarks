

.. index::
   video (pywatchvideo)
   Qt4 applications (watchvideo)


.. _watchvideo:

===========
watchvideo
===========


.. seealso::

   - http://pypi.python.org/pypi/WatchVideo
   - http://qt-apps.org/content/show.php/WatchVideo?content=128368.


A small application to play or download videos from various YouTube-like sites.

WatchVideo is an application to watch videos from many popular Flash based sites
using an external player like VLC.


For both GUI and CLI interface
==============================

- Python 2.5/2.6/2.7 (tested with Python 2.6 and 2.7)
- GetMediumURL 0.0a2 or later
- simplejson if using Python 2.5 (python-simplejson)

The installation script will automatically install GetMediumURL if it is not
available.

It requires lxml which should be installed from distribution package before
(in Debian-based GNU/Linux distributions it is named python-lxml).

For GUI only
============

- PyQt4 (python-qt4) or PySide
- libVLC version 1.1 (optional, required for built-in player)
- python-notify (optional) – uses the system’s default mechanism to show
  notification messages
- FFmpeg (optional) – needed for all operations related with video conversion,
  ripping or the built-in player.
- FFmpeg2theora (optional) – needed to convert videos to Ogg Vorbis or Theora,
  but not for ripping audio

For installation
=================

Distribute (python-setuptools)

If you downloaded through Subversion
=====================================

- pyqt4-dev-tools (pylupdate4, pyrcc4, pyuic4)
- libqt4-dev (lrelease)
- Inkscape
- OptiPNG (optional)

PyQt4 is used by default. When it is not found, PySide is used but there are
known bugs when using it.

Set the environment variable WATCHVIDEO_QT to a space-separated sequence of
package names tried to use a different package (e.g. WATCHVIDEO_QT=PySide to use
PySide on systems where PyQt4 is installed).



