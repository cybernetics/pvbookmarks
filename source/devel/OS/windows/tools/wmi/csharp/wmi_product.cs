/**
@file       wmi_product.cs
@author     $Author: pvergain $
@version    $Revision: 768 $
@date       $Date: 2012-09-28 10:22:37 +0200 (Fri, 28 Sep 2012) $
@brief      WMI product.
@details
 *

*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Management;  // Include this in references

namespace ReadSoftwareVersion
{
    // your own class name
    public class Software
    {
        // Method that will fetch the version of a given software
        public string GetSoftwateVersion(string softWareName)
        {
            string strVersion = string.Empty;
            try
            {
                var version = (object)null;
                //Query the system registery for the verion of the given software                
                var searcher = new ManagementObjectSearcher(
                  "SELECT * FROM Win32_Product where Name LIKE " + 
                  "'%" + softWareName + "%'");
                foreach (ManagementObject obj in searcher.Get())
                {
                    version = obj["Version"];
                }
                if (version != null)
                {
                    strVersion = (String)version;
                }
                // if given product is not found in list of installed products in control panel
                else
                {
                    strVersion = "Given Product is not found the list of Installed Programs";
                }
            }
            // Exception Handling
            catch (Exception e)
            {
                strVersion = "An Error occured while fetching Version" + 
                  " (" + e.Message + ")";
            }
            return strVersion;
        }
    }
}
