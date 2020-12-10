import sys
from cx_Freeze import setup, Executable
import math

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("Baskara.py", base=base)
]

buildOptions = dict(
        packages = [math],
        includes = [],
        include_files = [],
        excludes = []
)




setup(
    name = "Baskara",
    version = "1.0",
    description = "Baskara",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
