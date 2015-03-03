
.. index::
   pair: Qt4 applications ; Face recognition


.. _qt_face:

===================================================
The Face Recognition System based on QT and OpenCV
===================================================

.. seealso::

   - https://github.com/sun11/QTFaceRec/wiki/The-Face-Recognition-System-based-on-QT-and-OpenCV



An essay that imitate the format of intel cup: The Face Recognition System based
on QT and OpenCV

Related downloads： http://min.us/m1m2L9JOr The files in this package are suited
to FriendlyARM's Tiny6410,it contains OpenCV2.3 and QT4.7.3,it has been compiled
and can be used directly.Please put the files in opencv-lib in folder /lib,and
uncompress qt4.7.3.tgz to /opt.It also contains ORL face database which i scaled
to 70x80,and some xml files.

faceRec is for command-line training in this project(it can also used for
command-line recognition).

This project used FriendlyARM's Tiny6410,actually PC's program is much simpler
and faster.This program can train and recognize human face.It uses common USB
camera to capture images through v4l2,and detect face with AdaBoost algorithm,
and then recognize face in PCA method. If it recognized a face in the face
database,it will send character '1' to RS232,if a person stand in front of
the camera for about a minute and not logged in,then it will send '2'.

The speed is not ideal,about 1 frame per second. As for desktop linux,you can
just change the device name and complie the desktop version of OpenCV lib,that's
enough. Welcome to fork.

Specially thanks to Shervin Emami's article:http://www.shervinemami.info/faceRecognition.html
I'm trying to translate it into Chinese,but it still doesn't reach 50%,I hope
more people will participate it. [译]人脸检测与人脸识别简介

(I will still improve the wiki,and i hope Computer Vision lovers will continue
the project...)

You are free:

- to Share — to copy, distribute and transmit the work to Remix — to adapt the
  work Under the following conditions:

- Attribution You must attribute the work in the manner specified by the author
  or licensor (but not in any way that suggests that they endorse you or your use
  of the work).

- Noncommercial — You may not use this work for commercial purposes.

- Share Alike — If you alter, transform, or build upon this work, you may
  distribute  the resulting work only under the same or similar license to this one.
