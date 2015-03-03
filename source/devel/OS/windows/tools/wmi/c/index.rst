
.. index::
   pair: WMI ; C C++)

.. _wmi_c:

===================
Use WMI  in C/C++
===================

.. seealso::

   - http://cboard.cprogramming.com/c-programming/60299-hd-serial-number.html
   - http://disphelper.sourceforge.net/
   - http://msdn.microsoft.com/en-us/library/aa390418%28v=vs.85%29.aspx



.. contents::
   :depth: 3



.. _using_disphelper:

Using Disphelper in a Qt project with MINGW
===========================================

We have to link with the


The windows source files
------------------------

::

    win32 {
        SOURCES += \
            ../disphelper/samples_cpp/wmi_test_drive.cpp \
            ../disphelper/source/dh_invoke.c \
            ../disphelper/source/dh_init.c \
            ../disphelper/source/dh_extra.c \
            ../disphelper/source/dh_exceptions.c \
            ../disphelper/source/dh_enum.c \
            ../disphelper/source/dh_create.c \
            ../disphelper/source/dh_core.c \
            ../disphelper/source/convert.c

        HEADERS += \
            ../disphelper/source/convert.h \
            ../disphelper/source/disphelper.h
    }



Link with WMI (-lole32 -loleaut32 -luuid)
-----------------------------------------


::

    win32 {
        DEFINES += WIN32
        DEFINES += _WIN32_WINNT=0x0501
        INCLUDEPATH += "C:/boost_1_47_0"
        # see C:/boost_1_47_0/stage/lib
        LIBS += -LZ:/PDEV1V160_CodesRousseau/Soft/PC/test_boost/lib/windows
    #static
    # see https://svn.boost.org/trac/boost/ticket/4614
    #    DEFINES += BOOST_THREAD_USE_LIB # pour l'edition de liens statique
    #    LIBS += -static -lpthread   # for static linking
    #    LIBS += libboost_system-mgw44-mt-s-1_47
    #    LIBS += libboost_thread-mgw44-mt-s-1_47
    #dynamic
        LIBS += libboost_system-mgw44-mt-1_47
        LIBS += libboost_thread-mgw44-mt-1_47 # pour l'exemple 3_async
        LIBS += -lws2_32 # WSAStartUp@8  WSACleanup@0
        LIBS += -lole32 -loleaut32 -luuid  #WMI

    # Future use
        # INCLUDEPATH += "C:/zeromq-2.1.9/include"
        # LIBS += -LC:/zeromq-2.1.9/lib  libzmq
    }
