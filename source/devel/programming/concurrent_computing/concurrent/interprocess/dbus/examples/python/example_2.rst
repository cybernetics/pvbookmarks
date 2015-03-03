


============================================================================================================
http://stackoverflow.com/questions/5109879/usb-devices-udev-and-d-bus
============================================================================================================

Just monitor udev directly (through libudev, through pyudev).


::


    import pyudev
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    observer = pyudev.pygtk.GUDevMonitorObserver(monitor)
    observer.connect('device-added', device_added_callback)
    observer.connect('device-changed', device_changed_callback)
    monitor.enable_receiving()
    mainloop = gobject.MainLoop()
    mainloop.run()



This is what I use to list already plugged flash sticks. You can modify script
to your needs::

    import dbus
    bus = dbus.SystemBus()

    proxy = bus.get_object("org.freedesktop.Hal", "/org/freedesktop/Hal/Manager")
    iface = dbus.Interface(proxy, "org.freedesktop.Hal.Manager")

    devices = iface.GetAllDevices ()

    for device in devices:
      try:
          proxy1 = bus.get_object("org.freedesktop.Hal", device)
          iface1 = dbus.Interface(proxy1, "org.freedesktop.Hal.Device")
          props = iface1.GetAllProperties()

          removable = iface1.GetProperty("storage.removable")
          usb = iface1.GetProperty("storage.bus")
          if usb== "usb":
            print "\n".join(("%s: %s" % (k, props[k]) for k in props)) # shows available properties
      except:
        pass



And this is what I use to see if any usb plugged::


    #!/usr/bin/python
    import dbus
    import gobject

    class DeviceAddedListener:
        def __init__(self):
            self.bus = dbus.SystemBus()
            self.hal_manager_obj = self.bus.get_object("org.freedesktop.Hal", "/org/freedesktop/Hal/Manager")
            self.hal_manager = dbus.Interface(self.hal_manager_obj,"org.freedesktop.Hal.Manager")
            self.hal_manager.connect_to_signal("DeviceAdded", self._filter)

        def _filter(self, udi):
            device_obj = self.bus.get_object ("org.freedesktop.Hal", udi)
            device = dbus.Interface(device_obj, "org.freedesktop.Hal.Device")
            self.do_something(device)

        def do_something(self, device):
            try:
                usb = device.GetProperty("storage.bus")
                info = device.GetProperty("info.product")
                removable = device.GetProperty("storage.removable")
                print info
            except:
                            pass#blah blah


    if __name__ == '__main__':
        from dbus.mainloop.glib import DBusGMainLoop
        DBusGMainLoop(set_as_default=True)
        loop = gobject.MainLoop()
        DeviceAddedListener()
        loop.run()
