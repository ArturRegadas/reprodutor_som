import os
import ctypes
import sys

def run_as_admin():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        return False


if not run_as_admin():
    print("O script está sendo executado como administrador.")
    sys.exit()
else:
    print("O script está sendo executado como administrador.")

    os.system("powershell.exe Install-Module AudioDeviceCmdlets")
    