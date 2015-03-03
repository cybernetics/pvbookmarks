

.. index::
   pair: Home ; Assistant


.. _home_assistant:

=================
Home assistant
=================


.. seealso::

   - https://github.com/balloob/home-assistant


Description
============

This is the source for Home Assistant. 

For installation instructions, tutorials and the docs, please see 
[https://home-assistant.io](https://home-assistant.io). 

For a functioning demo frontend of Home Assistant, [click here](https://home-assistant.io/demo/).

Home Assistant is a home automation platform running on Python 3. 

The goal of Home Assistant is to be able to track and control all devices at 
home and offer a platform for automating control.

It offers the following functionality through built-in components:

* Track if devices are home by monitoring connected devices to a wireless router 
  (supporting [OpenWrt](https://openwrt.org/), [Tomato](http://www.polarcloud.com/tomato), 
  [Netgear](http://netgear.com))
* Track and control [Philips Hue](http://meethue.com) lights
* Track and control [WeMo switches](http://www.belkin.com/us/Products/home-automation/c/wemo-home-automation/)
* Track and control [Google Chromecasts](http://www.google.com/intl/en/chrome/devices/chromecast)
* Track running services by monitoring `ps` output
* Track and control [Tellstick devices and sensors](http://www.telldus.se/products/tellstick)
* Turn on the lights when people get home after sun set
* Turn on lights slowly during sun set to compensate for light loss
* Turn off all lights and devices when everybody leaves the house
* Offers web interface to monitor and control Home Assistant
* Offers a [REST API](#API) for easy integration with other projects ([see related projects for Android and Ruby support](#related_projects))
* [Ability to have multiple instances of Home Assistant work together](#connected_instances)

Home Assistant also includes functionality for controlling HTPCs:

* Simulate key presses for Play/Pause, Next track, Prev track, Volume up, Volume Down
* Download files
* Open URLs in the default browser
