

.. index::
   pair: C♯ ; Configuration
   pair: Configuration; ini-parser

.. _csharp_ini_parser:

==========================
C♯ ini-parser modules
==========================


.. seealso:: http://code.google.com/p/ini-parser/

This library allows to read or create INI data programaticly.

An implementation for reading / writing INI data to and from streams, files and
strings is included.

Really simple to use::

    // Load ini file

    FileIniDataParser parser = new FileIniDataParser();


    IniData data = parser.LoadFile("TestIniFile.ini");

    // Retrieve value for key 'fullscreen' inside a config section
    string useFullScreen? = data["ConfigSection"]["fullscreen"];

    // Modify the value
    data["ConfigSection"]["fullscreen"] = true;

    // save new ini file
    parser.SaveFile("NewTestIniFile.ini");




