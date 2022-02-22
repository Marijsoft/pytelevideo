program avviatelevideo;

{$APPTYPE CONSOLE}

{$R *.res}

uses
  System.SysUtils,
  Winapi.Windows;

begin
  try
Winexec('pythonw Televideo.pyc',SW_NORMAL);
  except
    on E: Exception do
      Writeln(E.ClassName, ': ', E.Message);
  end;
end.
