
.. index::
   pair: BIOS ; Windows


=========================
System, BIOS, Motherboard
=========================

This first example shows a few variations of the most common WMI query.

We ask a WMI object (computersystem, or bios, or baseboard in the examples below)
to return the values for a few of its properties. It returns the results in its
default tabular format.

::

    wmic computersystem get domain, EnableDaylightSavingsTime, Manufacturer, Model, PartOfDomain, TotalPhysicalMemory, username


::


    Domain  EnableDaylightSavingsTime  Manufacturer     Model PartOfDomain                            TotalPhysicalMemory  UserName
    ID3GEN  TRUE                       Hewlett-Packard  HP Compaq dx2400 Microtower PC  TRUE          3479351296           ID3GEN\pvergain
