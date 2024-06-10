import sys
from cx_Freeze import setup, Executable
import pynput


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("main.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["os", "ctypes", "sys", "customtkinter","ttkthemes", "tkinter", "pynput", "pyaudio", "wave", "soundcard"],
        include_files = ['beck','diretorios.txt',"index_entry.txt", "index_out.txt", "rodar_s_ou_n.txt", "Design sem nome (10).png"],
        excludes = []
)




setup(
    name = "SilvaoAuds",
    version = "1.0",
    description = "Somente um complemento",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
