

.. index::
   ! OpenSL_ES


.. _OpenSL_ES:

=================
OpenSL ES 
=================

.. seealso:: 

   - http://en.wikipedia.org/wiki/OpenSL_ES

.. contents::
   :depth: 3
   
Introduction
============
   
OpenSL ES (Open Sound Library for Embedded Systems) is a royalty-free, 
cross-platform, hardware-accelerated, C-language audio API for 2D and 3D audio. 

It provides access to features such as 3D positional audio and MIDI playback. 

It is made for developers in the mobile and gaming industry and is working 
toward allowing for easy porting of applications across multiple platforms.

The OpenSL ES API has five major features:

- Basic audio playback and recording
- 3D audio effects including 3D positional audio
- Music experience enhancing effects including bass boost and environmental 
  reverb
- Interactive music and ringtones using SP-MIDI, Mobile DLS, Mobile XMF
- Buffer Queues
- The features of Audio Playback and Recording and Basic MIDI are common with 
  OpenMAX AL.

Design
=======

OpenSL ES utilizes an object oriented design to give application developers 
access to the audio functionality. The object model is shared with OpenMAX AL, 
and a device manufacturer can choose to implement one or both of the APIs. 

Together the two APIs give access to a wide range of functionality of the 
device's multimedia engine.

The design goal of OpenSL ES is to give application developers access to 
advanced audio features such as 3D positional audio and MIDI playback while 
striving for easy application porting between manufacturers and platforms. 

It is developed primarily for application developers in the mobile and gaming 
industry.

Profiles
========

To avoid fragmentation, OpenSL ES is divided up into three profiles:

- Phone
- Music
- Game

Each profile is designed for the respective device needs with a specific set of 
audio functionalities. A vendor can choose to be conformant with only one or 
with any combination of profiles.


An application can query the OpenSL ES implementation to find out which 
profiles are supported. The application developer can then design their 
application to either work with only the common parts of the profiles, or 
adapt to the available functionality as given by the profiles in the device 
it is running on. 

An application developer can also specify both the minimum and the optimal 
profile requirements.
