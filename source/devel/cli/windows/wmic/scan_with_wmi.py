# -*- coding: utf-8 -*-
"""
Scan for win32 serial ports with WMI.


 - http://timgolden.me.uk/python/wmi/cookbook.html

Launch of the program::

    python scan_with_wmi.py

result::

    instance of Win32_SerialPort
    {
            Availability = 2;
            Binary = TRUE;
            Caption = "MEABOARD (COM5)";
            ConfigManagerErrorCode = 0;
            ConfigManagerUserConfig = FALSE;
            CreationClassName = "Win32_SerialPort";
            Description = "MEABOARD";
            DeviceID = "COM5";
            MaxBaudRate = 115200;
            MaximumInputBufferSize = 0;
            MaximumOutputBufferSize = 0;
            Name = "MEABOARD (COM5)";
            OSAutoDiscovered = TRUE;
            PNPDeviceID = "USB\\VID_0B81&PID_8004\\00000000";
            PowerManagementCapabilities = {1};
            PowerManagementSupported = FALSE;
            ProviderType = "Modem Device";
            SettableBaudRate = TRUE;
            SettableDataBits = TRUE;
            SettableFlowControl = TRUE;
            SettableParity = TRUE;
            SettableParityCheck = TRUE;
            SettableRLSD = TRUE;
            SettableStopBits = TRUE;
            Status = "OK";
            StatusInfo = 3;
            Supports16BitMode = FALSE;
            SupportsDTRDSR = TRUE;
            SupportsElapsedTimeouts = TRUE;
            SupportsIntTimeouts = TRUE;
            SupportsParityCheck = TRUE;
            SupportsRLSD = TRUE;
            SupportsRTSCTS = FALSE;
            SupportsSpecialCharacters = FALSE;
            SupportsXOnXOff = FALSE;
            SupportsXOnXOffSet = FALSE;
            SystemCreationClassName = "Win32_ComputerSystem";
            SystemName = "AGAVE";
    };

"""


import wmi

c = wmi.WMI()

def list_serial_port():
    wql = "SELECT * FROM Win32_SerialPort"
    for info in c.query(wql):
      print info



if __name__ == '__main__':
    list_serial_port()
