

.. index::
   pair: Android (2014) ; CCID

.. _android_ccid_2014:

==================
Android CCID 2014
==================


::

    > I have to admit that I agree that I really don't like how hackish the
    > providing an FD approach is. I was trying to work out if there was a way to
    > avoid it all and keep the libusb APIs for opening devices as cross-platform
    > as possible.
    >
    > There are a couple of key problems. The first of these is that to invoke the
    > Java UsbManager methods in Android from native code requires having a JavaVM
    > pointer (or a JNIEnv, but they are per-thread, so JavaVM is more generic).
    > There would be no way to avoid adding some API to libusb such as
    > libusb_provide_jvm_handle(libusb_context* context, JavaVM* jvm), although
    > I'd probably go for having the JavaVM* as a void* to avoid libusb.h needing
    > to include the JNI header.


Maybe I completely missed the point of the new API.

If I am correct, the idea is that the permission asking and the
opening of the device is done _before_ the call to libusb in the Java
application.
libusb will get a Linux file descriptor and just use it. That is why i
proposed to NOT use "open" in the name of the new function. I proposed
libusb_create_from_descriptor() but libusb_create_from_handle() is
also fine.

> Personally I'd be very happy to have a go at writing this Android backend,

No new backend is needed. Just use the Linux one.

Some functions would return LIBUSB_ERROR_NOT_SUPPORTED since they
can't be used on Android (without a real Android backend, that may not
be needed)

- libusb_get_device_list
- libusb_open_device_with_vid_pid
- libusb_open
- libusb_hotplug


The motivation for this new API is to port already existing C-code
using libusb to Android. Of course a new code should just be written
directly in Java to avoid all the JNI complexity.
In my case the idea is to port my CCID driver [1] to Android.

Bye

[1] http://pcsclite.alioth.debian.org/ccid.html
