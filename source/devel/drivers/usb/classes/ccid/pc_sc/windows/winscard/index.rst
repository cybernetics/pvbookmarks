


.. index::
   pair: PC/SC ; Winscard win32



.. _winscard_win32:

===============
Winscard win32
===============


The windows version of the :ref:`libpcsclite linux version <libpcsclite>`.


Winscard.h
==========


::

    /*++

    Copyright (c) 1996  Microsoft Corporation

    Module Name:

            WinSCard

    Abstract:

            This header file provides the definitions and symbols necessary for an
            Application or Smart Card Service Provider to access the Smartcard
            Subsystem.

    Environment:

            Win32

    Notes:

    --*/



    //
    ////////////////////////////////////////////////////////////////////////////////
    //
    //  Reader Control Routines
    //
    //      The following services provide for direct, low-level manipulation of the
    //      reader by the calling application allowing it control over the
    //      attributes of the communications with the card.
    //

    extern WINSCARDAPI LONG WINAPI
    SCardControl(
            IN      SCARDHANDLE hCard,
            IN      DWORD dwControlCode,
            IN      LPCVOID lpInBuffer,
            IN      DWORD nInBufferSize,
            OUT     LPVOID lpOutBuffer,
            IN      DWORD nOutBufferSize,
            OUT     LPDWORD lpBytesReturned);









