
.. index::
   pair: cli ; Windows
   pair: cli ; wmic
   pair: Windows; Services
   pair: cli ; WMI

.. _wmic:

====
Wmic
====

.. seealso::

   - :ref:`wmi`
   - http://quux.wiki.zoho.com/WMIC-Snippets.html
   - http://timgolden.me.uk/python/wmi/cookbook.html


Exemple 1
==========
.. toctree::
   :maxdepth: 4

   example_1


List of Windows services
============================

::

    wmic service get name, state


Resultat
--------

::

    Z:\>wmic service get name, state
    Name                            State
    AdobeFlashPlayerUpdateSvc       Stopped
    Alerter                         Stopped
    ALG                             Running
    AppMgmt                         Stopped
    aspnet_state                    Stopped
    AudioSrv                        Running
    BITS                            Stopped
    Browser                         Stopped
    CiSvc                           Stopped
    ClipSrv                         Stopped
    clr_optimization_v2.0.50727_32  Stopped
    clr_optimization_v4.0.30319_32  Stopped
    COMSysApp                       Stopped
    CryptSvc                        Running
    DcomLaunch                      Running
    Dhcp                            Running
    DirMngr                         Stopped
    dmadmin                         Stopped
    dmserver                        Running
    Dnscache                        Running
    Dot3svc                         Stopped
    EapHost                         Stopped
    ERSvc                           Stopped
    Eventlog                        Running
    EventSystem                     Running
    FastUserSwitchingCompatibility  Stopped
    FontCache3.0.0.0                Stopped
    Gallio.Ambience                 Stopped
    gupdate                         Stopped
    gupdatem                        Stopped
    gusvc                           Stopped
    helpsvc                         Stopped
    HidServ                         Stopped
    hkmsvc                          Stopped
    HTTPFilter                      Stopped
    IDaAuditMonitor                 Running
    IDaSessionMonitor               Running
    IDriverT                        Stopped
    idsvc                           Stopped
    ImapiService                    Stopped
    JavaQuickStarterService         Running
    lanmanserver                    Running
    lanmanworkstation               Running
    LightScribeService              Stopped
    LmHosts                         Running
    MDM                             Stopped
    Messenger                       Running
    mnmsrvc                         Stopped
    MongoDB                         Stopped
    MozillaMaintenance              Stopped
    MSDTC                           Stopped
    MSIServer                       Stopped
    MSSQL$SQLEXPRESS                Stopped
    MSSQLServerADHelper             Stopped
    msvsmon90                       Stopped
    napagent                        Stopped
    Net Driver HPZ12                Running
    NetDDE                          Stopped
    NetDDEdsdm                      Stopped
    Netlogon                        Running
    Netman                          Running
    NetTcpPortSharing               Stopped
    Nla                             Running
    NtLmSsp                         Stopped
    NtmsSvc                         Running
    ose                             Stopped
    PhidgetWebservice21             Stopped
    PlugPlay                        Running
    Pml Driver HPZ12                Running
    PolicyAgent                     Running
    ProtectedStorage                Running
    RasAuto                         Stopped
    RasMan                          Running
    RDSessMgr                       Stopped
    RemoteAccess                    Stopped
    RemoteRegistry                  Running
    RpcLocator                      Stopped
    RpcSs                           Running
    RSVP                            Stopped
    SamSs                           Running
    SCardSvr                        Running
    Schedule                        Running
    seclogon                        Running
    SENS                            Running
    SharedAccess                    Running
    ShellHWDetection                Running
    Spooler                         Running
    SQLBrowser                      Stopped
    SQLWriter                       Running
    srservice                       Running
    SSDPSRV                         Running
    stisvc                          Running
    stllssvr                        Stopped
    SwPrv                           Stopped
    SysmonLog                       Stopped
    SystemExplorerHelpService       Running
    TapiSrv                         Running
    TermService                     Running
    Themes                          Stopped
    TlntSvr                         Stopped
    TrkWks                          Running
    upnphost                        Stopped
    UPS                             Stopped
    VSS                             Stopped
    W32Time                         Running
    WebClient                       Stopped
    winmgmt                         Running
    WinRM                           Stopped
    WmdmPmSN                        Stopped
    Wmi                             Stopped
    WmiApSrv                        Running
    WMPNetworkSvc                   Stopped
    WPFFontCache_v0400              Running
    wscsvc                          Stopped
    wuauserv                        Running
    WudfSvc                         Stopped
    WZCSVC                          Stopped
    xmlprov                         Stopped



Start/Stop a Windows service
============================

Start a service
-------------------

::

    wmic service where (name="SCardSvr") call startservice


::


    Z:\>wmic service where (name="SCardSvr") call startservice
    Exécution (\\machine\ROOT\CIMV2:Win32_Service.Name="SCardSvr")->startservice()
    Méthode exécutée.
    Paramètres de sortie:
    instance of __PARAMETERS
    {
            ReturnValue = 10;
    };

Stopping a service
-------------------

::

    wmic service where (name="SCardSvr") call stopservice


::

    Z:\>wmic service where (name="SCardSvr") call stopservice
    Exécution (\\machine\ROOT\CIMV2:Win32_Service.Name="SCardSvr")->stopservice()
    Méthode exécutée.
    Paramètres de sortie:
    instance of __PARAMETERS
    {
            ReturnValue = 0;
    };


State of a service
-------------------

::

    wmic service where (name="SCardSvr") call state


::

    Z:\>wmic service where (name="SCardSvr") get state
    State
    Stopped


Affiche la liste courte des processus en cours, toutes les 2 secondes
=====================================================================

.. seealso::

   - http://www.prod-info.fr/Windows/Windows-Commandes-WMIC.html


::

    wmic /node:<server_name> process list brief /every:2



