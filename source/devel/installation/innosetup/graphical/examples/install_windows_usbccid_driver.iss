; -- install_windows_ccid_driver.iss --
; install a ccid driver depending on :
; - the architectures (x86, x64,ia64)
; - the windows operating system (Windows XP, Vista, 7)
;

[Setup]
AppCopyright=Copyright 2009-2010 Orcanthus
AppName=Windows USB CCID Driver Install
AppVerName=USBCCID Driver Install
OutputDir=innosetup
DefaultDirName=c:\Tmp
DefaultGroupName=USBCCID_Driver
UninstallDisplayIcon={app}\USBCCID_Driver.exe
Compression=lzma
SolidCompression=yes
DisableStartupPrompt=yes

; OutputDir=userdocs:Inno Setup Examples Output
; "ArchitecturesInstallIn64BitMode=x64 ia64" requests that the install
; be done in "64-bit mode" on x64 & Itanium, meaning it should use the
; native 64-bit Program Files directory and the 64-bit view of the
; registry. On all other architectures it will install in "32-bit mode".
ArchitecturesInstallIn64BitMode=x64 ia64

[Files]
; Install the usbccid driver depending on the architectures ans windows operating systems
Source: x86\Livraison\XP\*.*; DestDir: "{app}";       Check:  IsOtherArch and IsWindowsXP
Source: x86\Livraison\Vista_7\*.*; DestDir: "{app}";  Check:  IsOtherArch and IsWindowsVista_or_7
Source: x64\Livraison\XP\*.*; DestDir: "{app}";       Check:  IsX64 and IsWindowsXP
Source: x64\Livraison\Vista_7\*.*; DestDir: "{app}";  Check:  IsX64 and IsWindowsVista_or_7

; Source: "MyProg.chm"; DestDir: "{app}"
; Source: "README.txt"; DestDir: "{app}"; Flags: isreadme

[Icons]
Name: {group}\Uninstall USBCCID_Driver; Filename: {uninstallexe}

[Run]
Filename: "{app}\install_usbccid_driver.bat"; Parameters: "{app}"; StatusMsg: "Installing USB CCID driver ..."


[Code]
function IsX64: Boolean;
begin
  Result := Is64BitInstallMode and (ProcessorArchitecture = paX64);
end;


function IsIA64: Boolean;
begin
  Result := Is64BitInstallMode and (ProcessorArchitecture = paIA64);
end;

function IsOtherArch: Boolean;
begin
  Result := not IsX64 and not IsIA64;
end;


function IsWindowsXP: Boolean;
var
  Version: TWindowsVersion;
  S: String;
begin
  GetWindowsVersionEx(Version);
  Result := Version.NTPlatform and (Version.Major = 5) and (Version.Minor = 1);
end;
     

function IsWindowsVista: Boolean;
var
  Version: TWindowsVersion;
  S: String;
begin
  GetWindowsVersionEx(Version);

  Result := Version.NTPlatform and (Version.Major= 6) and (Version.Minor = 0);

end;

function IsWindows7: Boolean;
var
  Version: TWindowsVersion;
  S: String;
begin
  GetWindowsVersionEx(Version);

  Result := Version.NTPlatform and (Version.Major = 6) and (Version.Minor = 1);

end;

function IsWindowsVista_or_7: Boolean;
var
  Version: TWindowsVersion;
  S: String;
begin
  GetWindowsVersionEx(Version);

  Result := Version.NTPlatform and (Version.Major = 6) and ((Version.Minor = 1) or (Version.Minor = 0));

end;
