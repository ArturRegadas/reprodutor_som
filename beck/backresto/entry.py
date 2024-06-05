import os
import ctypes
import sys
os.system("powershell.exe Get-AudioDevice -list")
def change_audio_input(device_index):
    powershell_command = f"Set-AudioDevice -Index {device_index}"
    os.system(f"powershell.exe -Command \"{powershell_command}\"")

device_id = input()

change_audio_input(device_id)
input()