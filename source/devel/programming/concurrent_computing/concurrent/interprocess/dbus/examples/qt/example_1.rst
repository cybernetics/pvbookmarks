


================================================================
http://www.qtcentre.org/threads/18311-Hot-plug-and-button-event
================================================================


.. seealso:: http://www.qtfr.org/viewtopic.php?pid=77299



::

    MainWindow::MainWindow(QWidget *parent)
        : QMainWindow(parent), ui(new Ui::MainWindow)
    {
        ui->setupUi(this);
        if (!QDBusConnection::systemBus().isConnected()) {
            qDebug() << "Cannot connect to system bus";
        }

        bool connected = QDBusConnection::systemBus().connect(
                "org.freedesktop.Hal",
                "/org/freedesktop/Hal/Manager",
                "org.freedesktop.Hal.Manager",
                "DeviceAdded",
                this, SLOT(deviceAdded()));
    }


    void MainWindow::deviceAdded()
    {
        qDebug() << "Device added";
    }

