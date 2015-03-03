
.. index::
   pair: Innosetup ; Examples
   pair: Innosetup ; WMI



.. _innosetup_examples_graph:

==============================
Innosetup examples (.iss file)
==============================


.. contents::
   :depth: 3



install_windows_usbccid_driver
==============================

.. literalinclude:: install_windows_usbccid_driver.iss



install_python_app
==============================

.. literalinclude:: install_python_app.iss


WMI examples IsAppRunning
=========================

How to check with inno-setup, if a process is running at a windows 2008 r2 64bit ?
----------------------------------------------------------------------------------


::

    function IsAppRunning(const FileName : string): Boolean;
    var
        FSWbemLocator: Variant;
        FWMIService   : Variant;
        FWbemObjectSet: Variant;
    begin
        Result := false;
        FSWbemLocator := CreateOleObject('WBEMScripting.SWBEMLocator');
        FWMIService := FSWbemLocator.ConnectServer('', 'root\CIMV2', '', '');
        FWbemObjectSet := FWMIService.ExecQuery(Format('SELECT Name FROM Win32_Process Where Name="%s"',[FileName]));
        Result := (FWbemObjectSet.Count > 0);
        FWbemObjectSet := Unassigned;
        FWMIService := Unassigned;
        FSWbemLocator := Unassigned;
    end;


Determine if a Processor is AMD64 or Intel64 ?
----------------------------------------------

.. seealso:: http://stackoverflow.com/questions/10492484/determine-if-a-processor-is-amd64-or-intel64


You can use the Win32_Processor WMi class, from inno setup you can execute a WMI
query without problems. check this sample::


    var
      FSWbemLocator : Variant;
      FWMIService   : Variant;
      FWbemObject   : Variant;
    begin
    FSWbemLocator := CreateOleObject('WBEMScripting.SWBEMLocator');
    FWMIService   := FSWbemLocator.ConnectServer('', 'root\CIMV2', '', '');
    FWbemObject   := FWMIService.Get('Win32_Processor');
    if FWbemObject.Architecture=9 then //is a 64 bits processor
      if  FWbemObject.Family=131 then  //all 64-bit AMD processors are identified by using a Family attribute value of 0x83 (131).



