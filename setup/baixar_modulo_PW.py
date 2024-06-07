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
    x=0
    sys.exit()
else:
    x=1
    print(x)

    os.system("powershell.exe Install-Module AudioDeviceCmdlets")
