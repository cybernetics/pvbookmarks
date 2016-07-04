# -*- coding: utf-8 -*-
"""

Scan for win32 serial ports with win32com.client.


 - http://www.activexperts.com/admin/scripts/wmi/python/0358/


Launch of the program::

    python scan_with_win32com.py

result::

    Availability:2
    Binary:True
    Capabilities:
     null
    CapabilityDescriptions:
     null
    Caption:u'MEABOARD (COM5)'
    ConfigManagerErrorCode:0
    ConfigManagerUserConfig:False
    CreationClassName:u'Win32_SerialPort'
    Description:u'MEABOARD'
    DeviceID:u'COM5'
    MaxBaudRate:115200
    MaximumInputBufferSize:0
    MaximumOutputBufferSize:0
    Name:u'MEABOARD (COM5)'
    OSAutoDiscovered:True
    PNPDeviceID:u'USB\\VID_0B81&PID_8004\\00000000'
    PowerManagementCapabilities:
     1,
    PowerManagementSupported:False
    ProviderType:u'Modem Device'
    SettableBaudRate:True
    SettableDataBits:True
    SettableFlowControl:True
    SettableParity:True
    SettableParityCheck:True
    SettableRLSD:True
    SettableStopBits:True
    Status:u'OK'
    StatusInfo:3
    Supports16BitMode:False
    SupportsDTRDSR:True
    SupportsElapsedTimeouts:True
    SupportsIntTimeouts:True
    SupportsParityCheck:True
    SupportsRLSD:True
    SupportsRTSCTS:False
    SupportsSpecialCharacters:False
    SupportsXOnXOff:False
    SupportsXOnXOffSet:False
    SystemCreationClassName:u'Win32_ComputerSystem'
    SystemName:u'AGAVE'

"""

import win32com.client
def WMIDateStringToDate(dtmDate):
    strDateTime = ""
    if (dtmDate[4] == 0):
        strDateTime = dtmDate[5] + '/'
    else:
        strDateTime = dtmDate[4] + dtmDate[5] + '/'
    if (dtmDate[6] == 0):
        strDateTime = strDateTime + dtmDate[7] + '/'
    else:
        strDateTime = strDateTime + dtmDate[6] + dtmDate[7] + '/'
        strDateTime = strDateTime + dtmDate[0] + dtmDate[1] + dtmDate[2] + dtmDate[3] + " " + dtmDate[8] + dtmDate[9] + ":" + dtmDate[10] + dtmDate[11] +':' + dtmDate[12] + dtmDate[13]
    return strDateTime

strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")

objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_SerialPort")

for objItem in colItems:
    if objItem.Availability != None:
        print "Availability:" + ` objItem.Availability`
    if objItem.Binary != None:
        print "Binary:" + ` objItem.Binary`
    print "Capabilities:"
    strList = " "
    try :
        for objElem in objItem.Capabilities :
            strList = strList + `objElem` + ","
    except:
        strList = strList + 'null'
    print strList
    print "CapabilityDescriptions:"
    strList = " "
    try :
        for objElem in objItem.CapabilityDescriptions :
            strList = strList + `objElem` + ","
    except:
        strList = strList + 'null'
    print strList
    if objItem.Caption != None:
        print "Caption:" + ` objItem.Caption`
    if objItem.ConfigManagerErrorCode != None:
        print "ConfigManagerErrorCode:" + ` objItem.ConfigManagerErrorCode`
    if objItem.ConfigManagerUserConfig != None:
        print "ConfigManagerUserConfig:" + ` objItem.ConfigManagerUserConfig`
    if objItem.CreationClassName != None:
        print "CreationClassName:" + ` objItem.CreationClassName`
    if objItem.Description != None:
        print "Description:" + ` objItem.Description`
    if objItem.DeviceID != None:
        print "DeviceID:" + ` objItem.DeviceID`
    if objItem.ErrorCleared != None:
        print "ErrorCleared:" + ` objItem.ErrorCleared`
    if objItem.ErrorDescription != None:
        print "ErrorDescription:" + ` objItem.ErrorDescription`
    if objItem.InstallDate != None:
        print "InstallDate:" + WMIDateStringToDate(objItem.InstallDate)
    if objItem.LastErrorCode != None:
        print "LastErrorCode:" + ` objItem.LastErrorCode`
    if objItem.MaxBaudRate != None:
        print "MaxBaudRate:" + ` objItem.MaxBaudRate`
    if objItem.MaximumInputBufferSize != None:
        print "MaximumInputBufferSize:" + ` objItem.MaximumInputBufferSize`
    if objItem.MaximumOutputBufferSize != None:
        print "MaximumOutputBufferSize:" + ` objItem.MaximumOutputBufferSize`
    if objItem.MaxNumberControlled != None:
        print "MaxNumberControlled:" + ` objItem.MaxNumberControlled`
    if objItem.Name != None:
        print "Name:" + ` objItem.Name`
    if objItem.OSAutoDiscovered != None:
        print "OSAutoDiscovered:" + ` objItem.OSAutoDiscovered`
    if objItem.PNPDeviceID != None:
        print "PNPDeviceID:" + ` objItem.PNPDeviceID`
    print "PowerManagementCapabilities:"
    strList = " "
    try :
        for objElem in objItem.PowerManagementCapabilities :
            strList = strList + `objElem` + ","
    except:
        strList = strList + 'null'
    print strList
    if objItem.PowerManagementSupported != None:
        print "PowerManagementSupported:" + ` objItem.PowerManagementSupported`
    if objItem.ProtocolSupported != None:
        print "ProtocolSupported:" + ` objItem.ProtocolSupported`
    if objItem.ProviderType != None:
        print "ProviderType:" + ` objItem.ProviderType`
    if objItem.SettableBaudRate != None:
        print "SettableBaudRate:" + ` objItem.SettableBaudRate`
    if objItem.SettableDataBits != None:
        print "SettableDataBits:" + ` objItem.SettableDataBits`
    if objItem.SettableFlowControl != None:
        print "SettableFlowControl:" + ` objItem.SettableFlowControl`
    if objItem.SettableParity != None:
        print "SettableParity:" + ` objItem.SettableParity`
    if objItem.SettableParityCheck != None:
        print "SettableParityCheck:" + ` objItem.SettableParityCheck`
    if objItem.SettableRLSD != None:
        print "SettableRLSD:" + ` objItem.SettableRLSD`
    if objItem.SettableStopBits != None:
        print "SettableStopBits:" + ` objItem.SettableStopBits`
    if objItem.Status != None:
        print "Status:" + ` objItem.Status`
    if objItem.StatusInfo != None:
        print "StatusInfo:" + ` objItem.StatusInfo`
    if objItem.Supports16BitMode != None:
        print "Supports16BitMode:" + ` objItem.Supports16BitMode`
    if objItem.SupportsDTRDSR != None:
        print "SupportsDTRDSR:" + ` objItem.SupportsDTRDSR`
    if objItem.SupportsElapsedTimeouts != None:
        print "SupportsElapsedTimeouts:" + ` objItem.SupportsElapsedTimeouts`
    if objItem.SupportsIntTimeouts != None:
        print "SupportsIntTimeouts:" + ` objItem.SupportsIntTimeouts`
    if objItem.SupportsParityCheck != None:
        print "SupportsParityCheck:" + ` objItem.SupportsParityCheck`
    if objItem.SupportsRLSD != None:
        print "SupportsRLSD:" + ` objItem.SupportsRLSD`
    if objItem.SupportsRTSCTS != None:
        print "SupportsRTSCTS:" + ` objItem.SupportsRTSCTS`
    if objItem.SupportsSpecialCharacters != None:
        print "SupportsSpecialCharacters:" + ` objItem.SupportsSpecialCharacters`
    if objItem.SupportsXOnXOff != None:
        print "SupportsXOnXOff:" + ` objItem.SupportsXOnXOff`
    if objItem.SupportsXOnXOffSet != None:
        print "SupportsXOnXOffSet:" + ` objItem.SupportsXOnXOffSet`
    if objItem.SystemCreationClassName != None:
        print "SystemCreationClassName:" + ` objItem.SystemCreationClassName`
    if objItem.SystemName != None:
        print "SystemName:" + ` objItem.SystemName`
    if objItem.TimeOfLastReset != None:
        print "TimeOfLastReset:" + WMIDateStringToDate(objItem.TimeOfLastReset)





