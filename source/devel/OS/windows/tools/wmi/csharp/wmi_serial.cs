/**
@file       wmi_serial.cs
@author     $Author: pvergain $
@version    $Revision: 768 $
@date       $Date: 2012-09-28 10:22:37 +0200 (Fri, 28 Sep 2012) $
@brief      WMI serial port.
@details
 *

*/

using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using System.Reflection;
using System.Management; // WMI


namespace VideoCell
{
    internal class ProcessConnection
    {
        public static ConnectionOptions ProcessConnectionOptions()
        {
            ConnectionOptions options = new ConnectionOptions();
            options.Impersonation = ImpersonationLevel.Impersonate;
            options.Authentication = AuthenticationLevel.Default;
            options.EnablePrivileges = true;

            return options;
        }

        public static ManagementScope ConnectionScope(string machineName, ConnectionOptions options, string path)
        {
            ManagementScope connectScope = new ManagementScope();

            connectScope.Path = new ManagementPath(@"\\" + machineName + path);
            connectScope.Options = options;
            connectScope.Connect();
            return connectScope;
        }
    }

    /*
     * Résultat de la commande: wmic path win32_serialport get /ALL /FORMAT:list

    Availability=2
    Binary=TRUE
    Capabilities=
    CapabilityDescriptions=
    Caption=Videocell (COM5)
    ConfigManagerErrorCode=0
    ConfigManagerUserConfig=FALSE
    CreationClassName=Win32_SerialPort
    Description=Videocell
    DeviceID=COM5
    ErrorCleared=
    ErrorDescription=
    InstallDate=
    LastErrorCode=
    MaxBaudRate=115200
    MaximumInputBufferSize=0
    MaximumOutputBufferSize=0
    MaxNumberControlled=
    Name=Videocell (COM5)
    OSAutoDiscovered=TRUE
    PNPDeviceID=USB\VID_0B81&amp;PID_8009&amp;MI_00\6&amp;7FC829C&amp;0&amp;0000
    PowerManagementCapabilities={1}
    PowerManagementSupported=FALSE
    ProtocolSupported=
    ProviderType=Modem Device
    SettableBaudRate=TRUE
    SettableDataBits=TRUE
    SettableFlowControl=TRUE
    SettableParity=TRUE
    SettableParityCheck=TRUE
    SettableRLSD=TRUE
    SettableStopBits=TRUE
    Status=OK
    StatusInfo=3
    Supports16BitMode=FALSE
    SupportsDTRDSR=TRUE
    SupportsElapsedTimeouts=TRUE
    SupportsIntTimeouts=TRUE
    SupportsParityCheck=TRUE
    SupportsRLSD=TRUE
    SupportsRTSCTS=FALSE
    SupportsSpecialCharacters=FALSE
    SupportsXOnXOff=FALSE
    SupportsXOnXOffSet=FALSE
    SystemCreationClassName=Win32_ComputerSystem
    SystemName=AGAVE
    TimeOfLastReset= */

    public class CWin32SerialPort
    {
        static string VIDEOCELL_VendorID  = "0B81"; // id3 Technologies
        static string VIDEOCELL_ProductID = "8009"; // Carte VIDEOCELL, CEA


        public string Name { get; set; }
        public string Description { get; set; }
        public string Caption { get; set; }
        public string DeviceID { get; set; }
        public string PNPDeviceID { get; set; }

        /// <summary>
        /// Constructeur
        /// </summary>
        public CWin32SerialPort()
        {
        }

        /// <summary>
        /// Constructeur
        /// </summary>
        public CWin32SerialPort(string _Name, string _Description, string _DeviceID, string _Caption, string _PNPDeviceID)
        {
            Name = _Name;
            Description = _Description;
            DeviceID = _DeviceID;
            Caption = _Caption;
            PNPDeviceID = _PNPDeviceID;
        }


        /// <summary>
        /// Clone
        /// </summary>
        public CWin32SerialPort Clone()
        {
            CWin32SerialPort win32SerialPort = new CWin32SerialPort(Name, Description, DeviceID, Caption, PNPDeviceID);

            return win32SerialPort;
        }

        /// <summary>
        /// Ecrit les informations sur le port série
        /// </summary>
        public void PrintInfo()
        {
            string info = string.Format("Name:{0}\nDescription:{1}\nDeviceID:{2}\nCaption:{3}\nPNPDeviceID:{4}\n"
                                        , Name
                                        , Description
                                        , DeviceID
                                        , Caption
                                        , PNPDeviceID);


            Console.WriteLine(info);
        }


        /// <summary>
        /// Retourne la liste des ports série win32
        /// </summary>
        public static List<CWin32SerialPort> GetListWin32SerialPort()
        {
            ConnectionOptions options = ProcessConnection.ProcessConnectionOptions();
            ManagementScope connectionScope = ProcessConnection.ConnectionScope(Environment.MachineName, options, @"\root\CIMV2");
            ObjectQuery objectQuery = new ObjectQuery("SELECT * FROM win32_serialport ");
            ManagementObjectSearcher win32SerialPortSearcher = new ManagementObjectSearcher(connectionScope, objectQuery);

            // Liste des ports série
            List<CWin32SerialPort> win32SerialPortList = null;

            using (win32SerialPortSearcher)
            {
                foreach (ManagementObject obj in win32SerialPortSearcher.Get())
                {
                    if (win32SerialPortList == null)
                    {
                        win32SerialPortList = new List<CWin32SerialPort>();
                    }
                    // Création du port
                    CWin32SerialPort win32SerialPort = new CWin32SerialPort();

                    win32SerialPort.Name = obj["Name"].ToString();
                    win32SerialPort.Description = obj["Description"].ToString();
                    win32SerialPort.Caption = obj["Caption"].ToString();
                    win32SerialPort.DeviceID = obj["DeviceID"].ToString();
                    win32SerialPort.PNPDeviceID = obj["PNPDeviceID"].ToString();

                    // Ajout à la liste des ports série
                    win32SerialPortList.Add(win32SerialPort);
                }
            }

            return win32SerialPortList;

        } // public static List<CWin32SerialPort> GetListWin32SerialPort()


        /// <summary>
        /// Retourne la liste des ports série win32 VIDEOCELL
        /// </summary>
        public static List<CWin32SerialPort> GetListWin32SerialPortVIDEOCELL()
        {
            List<CWin32SerialPort> win32SerialPortList = CWin32SerialPort.GetListWin32SerialPort();
            if (win32SerialPortList == null)
                return null;

            // Création de la liste des ports série
            List<CWin32SerialPort> win32SerialPortVideoCellList = null;

            foreach (CWin32SerialPort win32SerialPort in win32SerialPortList)
            {
                if (   (win32SerialPort.PNPDeviceID.IndexOf(VIDEOCELL_VendorID) != -1)
                    && (win32SerialPort.PNPDeviceID.IndexOf(VIDEOCELL_ProductID) != -1))
                {
                    if (win32SerialPortVideoCellList == null)
                    {
                        win32SerialPortVideoCellList = new List<CWin32SerialPort>();
                    }

                    // Ajout à la liste des ports série
                    CWin32SerialPort win32PortVidecell = win32SerialPort.Clone();
                    win32SerialPortVideoCellList.Add(win32PortVidecell);
                }
            }

            return win32SerialPortVideoCellList;
        }


        /// <summary>
        /// Retourne la liste des ports série win32 VIDEOCELL
        /// </summary>
        public static CWin32SerialPort GetVideocellSerialPort()
        {
            List<CWin32SerialPort> win32SerialPortVideoCellList = GetListWin32SerialPortVIDEOCELL();

            if (win32SerialPortVideoCellList == null)
                return null;

            CWin32SerialPort winPort = win32SerialPortVideoCellList[0].Clone();

            return winPort;
        }
    }

} // namespace VideoCell
