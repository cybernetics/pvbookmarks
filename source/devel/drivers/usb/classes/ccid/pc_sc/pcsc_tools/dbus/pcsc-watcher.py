#!/usr/bin/env python

"""
pcsc-watcher.py
(c) 2011 by Florian "floe" Echtler <floe@butterbrot.org>
"""

import gobject

import dbus
import dbus.service 

from dbus.mainloop.glib import DBusGMainLoop

from smartcard.CardMonitoring import *
from smartcard.util import *


# dbus stuff

service = None

interface = "org.debian.alioth.pcsclite" # also used as bus name
path = "/org/debian/alioth/pcsclite/reader0/slot0"

# very simple DBus service class with one signal
class PCSC_DBus_Service(dbus.service.Object):
	def __init__(self,object_path):
		bus_name = dbus.service.BusName(interface, bus=dbus.SessionBus())
		dbus.service.Object.__init__(self, bus_name, object_path)

	@dbus.service.signal(interface)
	def CardPresenceChanged(self, atr, added):
		pass


# smartcard stuff

# simple card observer class which calls the DBus service
class PCSC_Card_Observer(CardObserver):
	def update(self, observable, (addedcards, removedcards)):
		for card in addedcards:
			service.CardPresenceChanged(toHexString(card.atr),True)
		for card in removedcards:
			service.CardPresenceChanged(toHexString(card.atr),False)


# main

DBusGMainLoop(set_as_default=True)
gobject.threads_init() # very important to avoid starving the PCSC thread

service = PCSC_DBus_Service(path)

cardmonitor = CardMonitor()
cardobserver = PCSC_Card_Observer()
cardmonitor.addObserver(cardobserver)

gobject.MainLoop().run()

