
.. index::
   pair: windows tools; proxycfg


.. _proxycfg_tool:

===============
proxycfg tool
===============


.. seealso::

   - http://msdn.microsoft.com/en-us/library/aa384069%28v=vs.85%29.aspx
   - http://www.processlibrary.com/fr/directory/files/proxycfg/28503/


http://msdn.microsoft.com/en-us/library/aa384069%28v=vs.85%29.aspx
==================================================================

This topic explains the use of the Microsoft Windows HTTP Services (WinHTTP)
proxy configuration tool, "ProxyCfg.exe".

There are two ways to access HTTP and Secure Hypertext Transfer Protocol (HTTPS)
servers through a proxy using Microsoft Windows HTTP Services (WinHTTP).

First, you can specify proxy settings from within your WinHTTP application.

Second, you can specify default proxy settings from outside your application
using the proxy configuration utility located in the %windir%\system32 directory.


::

    C:\>proxycfg  -u


::

    Outil de configuration du proxy par défaut WinHTTP Microsoft (R)
    Copyright (c) Microsoft Corporation. Tous droits réservés.

    Paramètres proxy mis à jour
    Paramètres proxy WinHTTP en cours sous :
      HKEY_LOCAL_MACHINE\
        SOFTWARE\Microsoft\Windows\CurrentVersion\InternetSetting \Connections\
          WinHttpSettings :

        Serveurs proxy :  http=gateway:3128
        Liste d'exception :  <local>




