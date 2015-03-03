
.. index::
   pair: Python; Speech recognition
   ! pygsr


.. _pygsr:

=================================
Pygsr
=================================

.. seealso::

   - https://pypi.python.org/pypi/pygsr/0.1


.. contents::
   :depth: 3

Presentation
=============

Simple way to access google api for speech recognition with python

Dependencies
=============

- **sox** - `apt-get install sox`
- **pyaudio** - `apt-get install python-pyaudio`

Install
========

::

    pip install pygsr

Example
=========

::

    from pygsr import Pygsr
    speech = Pygsr()
    speech.record(3) # duration in seconds (3)
    phrase, complete_response = speech.speech_to_text('es_ES') # select the language
    print phrase
