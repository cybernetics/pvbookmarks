wmic /OUTPUT:C:\Proclist.htm path Win32_Process get Name, CommandLine, Description, Handle, Priority, ProcessId, WorkingSetSize, VirtualSize /format:hform.xsl

pause

