__author__ = 'Edinei'
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
targetName = None
if sys.platform == "win32":
    base = "Win32GUI"
    targetName = "DarumaFramework_Python_Qt.exe"
else:
    targetName = "darumaframework_python_qt"

setup(  name = "darumaframework_python_qt",
        version = "1.0",
        description = "Exemplo Daruma Multiplataforma em Python",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py",
                                  base=base,
                                  targetName = targetName,)])
