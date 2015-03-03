
.. index::
   pair: WMI ; Windows Management Instrumentation
   pair: WMI ; C examples
   pair: WMI ; Win32_SerialPort
   pair: WMI ; Win32_Product
   pair: WMI ; Win32_OperatingSystem
   ! WMI

.. _wmi:

========================================
WMI (Windows Management Instrumentation)
========================================

.. seealso::

   - :ref:`python_wmi`
   - :ref:`windows_power_shell`
   - http://en.wikipedia.org/wiki/Windows_Management_Instrumentation
   - http://quux.wiki.zoho.com/PowerShell-Snippets.html
   - http://quux.wiki.zoho.com/WMIC-Snippets.html (old page before powershell)
   - http://support.microsoft.com/servicedesks/webcasts/wc072402/listofsampleusage.asp
   - http://laurent-dardenne.developpez.com/articles/wmi-p1/
   - http://c.buguet.free.fr/infos2/spip.php?article106



.. contents::
   :depth: 3

Introduction
============

Windows Management Instrumentation (WMI) is a set of extensions to the Windows
Driver Model that provides an operating system interface through which
instrumented components provide information and notification.

WMI is Microsoft's implementation of the Web-Based Enterprise Management
(WBEM) and Common Information Model (CIM) standards from the Distributed Management
Task Force (DMTF).

WMI allows scripting languages like VBScript or Windows PowerShell to manage
Microsoft Windows personal computers and servers, both locally and remotely.
WMI is preinstalled in Windows 2000 and newer OSs.

It is available as a download for Windows NT, Windows 95 and Windows 98.

Microsoft also provides a command line interface to WMI called Windows Management
Instrumentation Command-line (WMIC)


Article de Charles Antoine Buguet sur WMI
=========================================

.. seealso:: http://c.buguet.free.fr/infos2/spip.php?article106



Avec de très nombreux scripts intéressants.


List of Win32 classes
=====================

.. seealso:: http://msdn.microsoft.com/en-us/library/aa394084


To display the classe's informations type the following command::

    wmic path Win32_OperatingSystem get /ALL /FORMAT:list



::

    wmic path Win32_PnPEntity get /?


::

    Propriété                               Type                    Opération
    ========                                ====                    =========
    Availability                            uint16                  Read
    Caption                                 string                  Read
    ClassGuid                               string                  Read
    ConfigManagerErrorCode                  uint32                  Read
    ConfigManagerUserConfig                 boolean                 Read
    CreationClassName                       string                  Read
    Description                             string                  Read
    DeviceID                                string                  Read
    ErrorCleared                            boolean                 Read
    ErrorDescription                        string                  Read
    InstallDate                             datetime                Read
    LastErrorCode                           uint32                  Read
    Manufacturer                            string                  Read
    Name                                    string                  Read
    PNPDeviceID                             string                  Read
    PowerManagementCapabilities             array of uint16         Read
    PowerManagementSupported                boolean                 Read
    Service                                 string                  Read
    Status                                  string                  Read
    StatusInfo                              uint16                  Read
    SystemCreationClassName                 string                  Read
    SystemName                              string                  Read


Win32_Desktop
-------------


::

    wmic path Win32_Desktop get /?

::

    Propriété                               Type                    Opération
    ========                                ====                    =========
    BorderWidth                             uint32                  Read
    Caption                                 string                  Read
    CoolSwitch                              boolean                 Read
    CursorBlinkRate                         uint32                  Read
    Description                             string                  Read
    DragFullWindows                         boolean                 Read
    GridGranularity                         uint32                  Read
    IconSpacing                             uint32                  Read
    IconTitleFaceName                       string                  Read
    IconTitleSize                           uint32                  Read
    IconTitleWrap                           boolean                 Read
    Name                                    string                  Read
    Pattern                                 string                  Read
    ScreenSaverActive                       boolean                 Read
    ScreenSaverExecutable                   string                  Read
    ScreenSaverSecure                       boolean                 Read
    ScreenSaverTimeout                      uint32                  Read
    SettingID                               string                  Read
    Wallpaper                               string                  Read
    WallpaperStretched                      boolean                 Read
    WallpaperTiled                          boolean                 Read

win32_serialport
----------------

::

    wmic path win32_serialport get /?


::

    Propriété                               Type                    Opération
    ========                                ====                    =========
    Availability                            uint16                  Read
    Binary                                  boolean                 Read
    Capabilities                            array of uint16         Read
    CapabilityDescriptions                  array of string         Read
    Caption                                 string                  Read
    ConfigManagerErrorCode                  uint32                  Read
    ConfigManagerUserConfig                 boolean                 Read
    CreationClassName                       string                  Read
    Description                             string                  Read
    DeviceID                                string                  Read
    ErrorCleared                            boolean                 Read
    ErrorDescription                        string                  Read
    InstallDate                             datetime                Read
    LastErrorCode                           uint32                  Read
    MaxBaudRate                             uint32                  Read
    MaxNumberControlled                     uint32                  Read
    MaximumInputBufferSize                  uint32                  Read
    MaximumOutputBufferSize                 uint32                  Read
    Name                                    string                  Read
    OSAutoDiscovered                        boolean                 Read
    PNPDeviceID                             string                  Read
    PowerManagementCapabilities             array of uint16         Read
    PowerManagementSupported                boolean                 Read
    ProtocolSupported                       uint16                  Read
    ProviderType                            string                  Read
    SettableBaudRate                        boolean                 Read
    SettableDataBits                        boolean                 Read
    SettableFlowControl                     boolean                 Read
    SettableParity                          boolean                 Read
    SettableParityCheck                     boolean                 Read
    SettableRLSD                            boolean                 Read
    SettableStopBits                        boolean                 Read
    Status                                  string                  Read
    StatusInfo                              uint16                  Read
    Supports16BitMode                       boolean                 Read
    SupportsDTRDSR                          boolean                 Read
    SupportsElapsedTimeouts                 boolean                 Read
    SupportsIntTimeouts                     boolean                 Read
    SupportsParityCheck                     boolean                 Read
    SupportsRLSD                            boolean                 Read
    SupportsRTSCTS                          boolean                 Read
    SupportsSpecialCharacters               boolean                 Read
    SupportsXOnXOff                         boolean                 Read
    SupportsXOnXOffSet                      boolean                 Read
    SystemCreationClassName                 string                  Read
    SystemName                              string                  Read
    TimeOfLastReset                         datetime                Read


Win32_PnPSignedDriver
---------------------

::

    wmic path Win32_PnPSignedDriver get /?

::

    Propriété                               Type                    Opération
    ========                                ====                    =========
    Caption                                 string                  Read
    ClassGuid                               String                  Read
    CompatID                                String                  Read
    CreationClassName                       string                  Read
    Description                             String                  Read
    DevLoader                               String                  Read
    DeviceClass                             String                  Read
    DeviceID                                String                  Read
    DeviceName                              String                  Read
    DriverDate                              datetime                Read
    DriverName                              String                  Read
    DriverProviderName                      String                  Read
    DriverVersion                           String                  Read
    FriendlyName                            String                  Read
    HardWareID                              String                  Read
    InfName                                 String                  Read
    InstallDate                             datetime                Read
    IsSigned                                Boolean                 N/A
    Location                                String                  Read
    Manufacturer                            String                  Read
    Name                                    string                  Read
    PDO                                     String                  Read
    Signer                                  String                  Read
    StartMode                               string                  Read
    Started                                 boolean                 Read
    Status                                  string                  Read
    SystemCreationClassName                 string                  Read
    SystemName                              string                  Read


Win32_Processor
---------------

::

    wmic path Win32_Processor get /?

::

    Propriété                               Type                    Opération
    ========                                ====                    =========
    AddressWidth                            uint16                  Read
    Architecture                            uint16                  Read
    Availability                            uint16                  Read
    Caption                                 string                  Read
    ConfigManagerErrorCode                  uint32                  Read
    ConfigManagerUserConfig                 boolean                 Read
    CpuStatus                               uint16                  Read
    CreationClassName                       string                  Read
    CurrentClockSpeed                       uint32                  Read
    CurrentVoltage                          uint16                  Read
    DataWidth                               uint16                  Read
    Description                             string                  Read
    DeviceID                                string                  Read
    ErrorCleared                            boolean                 Read
    ErrorDescription                        string                  Read
    ExtClock                                uint32                  Read
    Family                                  uint16                  Read
    InstallDate                             datetime                Read
    L2CacheSize                             uint32                  Read
    L2CacheSpeed                            uint32                  Read
    LastErrorCode                           uint32                  Read
    Level                                   uint16                  Read
    LoadPercentage                          uint16                  Read
    Manufacturer                            string                  Read
    MaxClockSpeed                           uint32                  Read
    Name                                    string                  Read
    NumberOfCores                           uint32                  Read
    NumberOfLogicalProcessors               uint32                  Read
    OtherFamilyDescription                  string                  Read
    PNPDeviceID                             string                  Read
    PowerManagementCapabilities             array of uint16         Read
    PowerManagementSupported                boolean                 Read
    ProcessorId                             string                  Read
    ProcessorType                           uint16                  Read
    Revision                                uint16                  Read
    Role                                    string                  Read
    SocketDesignation                       string                  Read
    Status                                  string                  Read
    StatusInfo                              uint16                  Read
    Stepping                                string                  Read
    SystemCreationClassName                 string                  Read
    SystemName                              string                  Read
    UniqueId                                string                  Read
    UpgradeMethod                           uint16                  Read
    Version                                 string                  Read
    VoltageCaps                             uint32                  Read

Win32_OperatingSystem
---------------------

::

    wmic path Win32_OperatingSystem get /?

::

    Propriété                               Type                    Opération
    ========                                ====                    =========
    BootDevice                              string                  Read
    BuildNumber                             string                  Read
    BuildType                               string                  Read
    CSCreationClassName                     string                  Read
    CSDVersion                              string                  Read
    CSName                                  string                  Read
    Caption                                 string                  Read
    CodeSet                                 string                  Read
    CountryCode                             string                  Read
    CreationClassName                       string                  Read
    CurrentTimeZone                         sint16                  Read/Write
    DataExecutionPrevention_32BitApplications       boolean                 Read
    DataExecutionPrevention_Available       boolean                 Read
    DataExecutionPrevention_Drivers         boolean                 Read
    DataExecutionPrevention_SupportPolicy   uint8                   Read
    Debug                                   boolean                 Read
    Description                             string                  Read/Write
    Distributed                             boolean                 Read
    EncryptionLevel                         uint32                  Read
    ForegroundApplicationBoost              uint8                   Read/Write
    FreePhysicalMemory                      uint64                  Read
    FreeSpaceInPagingFiles                  uint64                  Read
    FreeVirtualMemory                       uint64                  Read
    InstallDate                             datetime                Read
    LargeSystemCache                        uint32                  Read
    LastBootUpTime                          datetime                Read
    LocalDateTime                           datetime                Read
    Locale                                  string                  Read
    Manufacturer                            string                  Read
    MaxNumberOfProcesses                    uint32                  Read
    MaxProcessMemorySize                    uint64                  Read
    Name                                    string                  Read
    NumberOfLicensedUsers                   uint32                  Read
    NumberOfProcesses                       uint32                  Read
    NumberOfUsers                           uint32                  Read
    OSLanguage                              uint32                  Read
    OSProductSuite                          uint32                  Read
    OSType                                  uint16                  Read
    Organization                            string                  Read
    OtherTypeDescription                    string                  Read
    PlusProductID                           string                  Read
    PlusVersionNumber                       string                  Read
    Primary                                 boolean                 Read
    ProductType                             uint32                  Read
    QuantumLength                           uint8                   Read/Write
    QuantumType                             uint8                   Read/Write
    RegisteredUser                          string                  Read
    SerialNumber                            string                  Read
    ServicePackMajorVersion                 uint16                  Read
    ServicePackMinorVersion                 uint16                  Read
    SizeStoredInPagingFiles                 uint64                  Read
    Status                                  string                  Read
    SuiteMask                               uint32                  Read
    SystemDevice                            string                  Read
    SystemDirectory                         string                  Read
    SystemDrive                             string                  Read
    TotalSwapSpaceSize                      uint64                  Read
    TotalVirtualMemorySize                  uint64                  Read
    TotalVisibleMemorySize                  uint64                  Read
    Version                                 string                  Read
    WindowsDirectory                        string                  Read

Win32_ComputerSystem
--------------------

::

    wmic path Win32_ComputerSystem get /?

::

    Propriété                               Type                    Opération
    ========                                ====                    =========
    AdminPasswordStatus                     uint16                  Read
    AutomaticResetBootOption                boolean                 Read/Write
    AutomaticResetCapability                boolean                 Read
    BootOptionOnLimit                       uint16                  Read
    BootOptionOnWatchDog                    uint16                  Read
    BootROMSupported                        boolean                 Read
    BootupState                             string                  Read
    Caption                                 string                  Read
    ChassisBootupState                      uint16                  Read
    CreationClassName                       string                  Read
    CurrentTimeZone                         sint16                  Read/Write
    DaylightInEffect                        boolean                 Read
    Description                             string                  Read
    Domain                                  string                  Read
    DomainRole                              uint16                  Read
    EnableDaylightSavingsTime               boolean                 Write
    FrontPanelResetStatus                   uint16                  Read
    InfraredSupported                       boolean                 Read
    InitialLoadInfo                         array of string         Read
    InstallDate                             datetime                Read
    KeyboardPasswordStatus                  uint16                  Read
    LastLoadInfo                            string                  Read
    Manufacturer                            string                  Read
    Model                                   string                  Read
    Name                                    string                  Read
    NameFormat                              string                  Read
    NetworkServerModeEnabled                boolean                 Read
    NumberOfLogicalProcessors               uint32                  Read
    NumberOfProcessors                      uint32                  Read
    OEMLogoBitmap                           array of uint8          Read
    OEMStringArray                          array of string         Read
    PartOfDomain                            boolean                 Read
    PauseAfterReset                         sint64                  Read
    PowerManagementCapabilities             array of uint16         Read
    PowerManagementSupported                boolean                 Read
    PowerOnPasswordStatus                   uint16                  Read
    PowerState                              uint16                  Read
    PowerSupplyState                        uint16                  Read
    PrimaryOwnerContact                     string                  Read
    PrimaryOwnerName                        string                  Read
    ResetCapability                         uint16                  Read
    ResetCount                              sint16                  Read
    ResetLimit                              sint16                  Read
    Roles                                   array of string         Read/Write
    Status                                  string                  Read
    SupportContactDescription               array of string         Read
    SystemStartupDelay                      uint16                  Read/Write
    SystemStartupOptions                    array of string         Read/Write
    SystemStartupSetting                    uint8                   Read/Write
    SystemType                              string                  Read
    ThermalState                            uint16                  Read
    TotalPhysicalMemory                     uint64                  Read
    UserName                                string                  Read
    WakeUpType                              uint16                  Read
    Workgroup                               string                  Read/Write


Win32_Product
--------------------


.. seealso::

   - http://www.codeproject.com/Tips/701941/Get-Version-of-a-Software-using-Csharp


::

    wmic path Win32_Product get /?
    
    

Using WMI
=========

.. toctree::
   :maxdepth: 4

   c/index
   csharp/index



