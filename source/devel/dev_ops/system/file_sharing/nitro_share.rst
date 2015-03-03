
.. index::
   pair: Sharing; Nitroshare

===========
Nitro share
===========

.. seealso::

   - http://www.ubuntugeek.com/nitroshare-cross-platform-tool-for-sharing-files-across-a-local-network.html
   - http://quickmediasolutions.com/apps/14/nitroshare


NitroShare is a cross-platform tool for sharing files across a local network.

After completing the setup wizard, NitroShare discovers other machines on the
network running the tool and enables you to send files to them using the
application indicator or small widgets on the desktop.

A network file-sharing application that makes sending a file to another machine
on the local network as easy as dragging-and-dropping.

NitroShare is designed to be hassle-free in every aspect.

Just install the application on any machine running Ubuntu or Windows and
you're all set.

**Each machine should discover all of the other machines on the local network**

The application integrates with the operating system, using application i
ndicators on Ubuntu and the system tray on Windows.

NitroShare offers a number of other features, including:

- dynamic file compress during transfer to decrease transfer time and bandwidth
- CRC checksum generation to ensure file integrity during transfer
- full compatibility with clients running on other operating systems
- a helpful configuration wizard to guide you through setting up the application
  on your machines

Install nitroshare in ubuntu
============================

Open the terminal and run the following commands::


    sudo add-apt-repository ppa:george-edison55/nitroshare
    sudo apt-get update
    sudo apt-get install nitroshare
