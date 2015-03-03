


================================================================
http://developer.qt.nokia.com/forums/viewthread/8595
================================================================


::


    QDBusConnection::systemBus().connect(
                             "org.freedesktop.Hal",
                             "/org/freedesktop/Hal/Manager",
                             "org.freedesktop.Hal.Manager",
                             "DeviceAdded",
                             this, SLOT(deviceAdded());
    QDBusConnection::systemBus().connect(
                             "org.freedesktop.Hal",
                             "/org/freedesktop/Hal/Manager",
                             "org.freedesktop.Hal.Manager",
                             "DeviceRemoved",
                             this, SLOT(deviceRemoved());

    void deviceAdded(){
                             qDebug() << "device added!";
    }

    void deviceRemoved(){
                             qDebug() << "device removed!";
    }
