import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("baixar_modulo_PW.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["os", "ctypes", "sys"],
        include_files = [],
        excludes = []
)




setup(
    name = "baixar_modulo",
    version = "1.0",
    description = "Somente um complemento",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
