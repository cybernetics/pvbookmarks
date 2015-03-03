/**
@file       carte_leds_usb_serial.cs
@author     $Author: pvergain $
@version    $Revision: 1157 $
@date       $Date: 2014-04-24 10:07:50 +0200 (jeu. 24 avr. 2014) $
@brief      Carte LEDs USB serial port.
@details    
 * 
 * 
La carte LEDs 96 bits apparait comme un port "USB série".

Elle n'apparait pas dans la commande wmic path win32_serialport get /ALL /FORMAT:list

*/

using System;
using System.IO;
using System.IO.Ports;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using System.Reflection;
using System.Text;

using VideoCell;



namespace VideoCell
{
    public class CCarteLEDs_USBSerial
    {
        public string _nom_com_port;
        public string NomCOMPort
        {
            get { return _nom_com_port; }
        }

        private SerialPort  _serial_port_leds;
        // Accesseur public
        public SerialPort SerialPortLEDs
        {
            get { return _serial_port_leds; }
        }

        /// <summary>
        /// Constructeur
        /// </summary>
        public static bool COMPortExist(string name_com_port)
        {
            bool com_port_exit = false;
            List<string> list_ports = GetAllPorts();

            IEnumerable<string> filter = Enumerable.Where(list_ports, p => p.Contains(name_com_port));

            if (filter.Count() == 1)
                com_port_exit = true;

            return com_port_exit;
        }

        /// <summary>
        /// Constructeur
        /// </summary>
        public CCarteLEDs_USBSerial(string name_com_port) 
        {
            _nom_com_port = name_com_port;
            _serial_port_leds = new SerialPort(name_com_port);

            /*
	            res = GetCommState(hComm, &dcb);
	            dcb.BaudRate = 115200;
	            dcb.ByteSize = 8;
	            dcb.Parity = NOPARITY;
	            dcb.StopBits = ONESTOPBIT;
	            dcb.fRtsControl = RTS_CONTROL_DISABLE;
	            dcb.fOutX = FALSE;
	            dcb.fInX = FALSE;
	            dcb.XonChar = 0;
	            dcb.XoffChar = 0;
	            if (res)
		            res = SetCommState(hComm, &dcb);
             * */

            _serial_port_leds.BaudRate = 115200;        // dcb.BaudRate = 115200;
                                                        // dcb.ByteSize = 8;
            _serial_port_leds.Parity = Parity.None;     // dcb.Parity = NOPARITY;
            _serial_port_leds.StopBits = StopBits.One;  // dcb.StopBits = ONESTOPBIT;
                                                        // dcb.fRtsControl = RTS_CONTROL_DISABLE;
                                                        // dcb.fOutX = FALSE;
                                                        // dcb.fInX = FALSE;
                                                        // dcb.XonChar = 0;
                                                        // dcb.XoffChar = 0;
        }

        /// <summary>
        /// Est-ce que le port USB serial est ouvert ? 
        /// </summary>
        public bool IsOpen()
        {
            return _serial_port_leds.IsOpen;
        }

        /// <summary>
        /// Ouverture du port USB serial 
        /// </summary>
        public void Open()
        {
            try
            {
                if (!IsOpen())
                    _serial_port_leds.Open();
            }
            catch (Exception ex)
            {
            }
        }

        /// <summary>
        /// Ouverture du port USB serial 
        /// </summary>
        public void Close()
        {
            try
            {
                if (IsOpen())
                {
                    _serial_port_leds.Close();
                }
            }
            catch (Exception ex)
            {
            }
        }


        /// <summary>
        /// Envoi d'une commande pour allumer ou éteindre une LED correspondant à un puits
        /// <param name="nom_du_puits">Le nom du puits de la forme :[A01, A12, B01..B12...H01, H12]</param>
        /// <param name="courant_ma">Le courant appliqué en milli-ampères.</param>/// 
        /// </summary>
        public void EnvoyerCommande(string nom_du_puits, int courant_ma, bool log_gui= false)
        {
            if (!IsOpen())
            {
                Open();
                if (!IsOpen())
                {
                    // Log.Write("Can't open COM LED port", false);
                    return;
                }
            }

            // Exemples: 
            // - A07 150
            // - A07 0

            string commande = string.Format("{0} {1:000}\n", nom_du_puits, courant_ma);

            if (log_gui)
            {
                string message = string.Format("Well: {0} Command LED:<{1}>  COM port:<{2}> Courant:<{3}>"
                                              , nom_du_puits
                                              , commande
                                              , NomCOMPort
                                              , courant_ma);
                Log.Write(message, true);
            }

            byte[] array_command = Encoding.ASCII.GetBytes(commande);

            /*
	        /* Envoi de la commande en langage C
            sprintf(cmd, "%c%02d %03d\n", lig, col, val);

            res = WriteFile(hComm, cmd, strlen(cmd), &size, NULL);
            if ((!res) || (size != strlen(cmd)))
            {
                printf("Impossible d'envoyer la commande de led sur le port %s.\r\n", argv[1]);
                return 1;
            }*/

            // Ecriture de la commande sur la liaison série
            _serial_port_leds.Write(array_command, 0, array_command.Length);

            // Fermeture de la communication
            Close();
        }

        /// <summary>
        /// Allumer la LED du puits
        /// <param name="nom_du_puits">Le nom du puits de la forme :[A01, A12, B01..B12...H01, H12]</param>
        /// <param name="courant_ma">Le courant appliqué en milli-ampères.</param>/// 
        /// </summary>
        public void AllumerPuits(string nom_du_puits, int courant_ma, bool log_gui = false)
        {
            EnvoyerCommande(nom_du_puits, courant_ma, log_gui);
        }


        /// <summary>
        /// Eteindre la LED du puits
        /// <param name="nom_du_puits">Le nom du puits de la forme :[A01, A12, B01..B12...H01, H12]</param>
        /// <param name="courant_ma">Le courant appliqué en milli-ampères.</param>/// 
        /// </summary>
        public void EteindrePuits(string nom_du_puits, bool log_gui = false)
        {
            EnvoyerCommande(nom_du_puits, 0, log_gui);
        }

        /// <summary>
        /// Retourne l'ensemble des ports
        /// </summary>
        static public List<string> GetAllPorts()
        {
            List<String> allPorts = new List<String>();
            foreach (String portName in System.IO.Ports.SerialPort.GetPortNames())
            {
                allPorts.Add(portName);
            }
            return allPorts;
        }

    } // CCarteLEDs_USBSerial

} // namespace VideoCell
