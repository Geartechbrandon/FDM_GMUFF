import sys
from cx_Freeze import setup, Executable

setup(name = "FDM_GMUFF" ,
      version = "1.0.0" ,
      description = "A tool to edit gcode. Gcode Modification Unit For Fabric." ,
      executables = [Executable("FDM_Fabric_Mod.py")])