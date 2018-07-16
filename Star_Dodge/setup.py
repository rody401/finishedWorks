import sys
from cx_Freeze import setup, Executable


import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = None
if sys.platform == 'win64':
    base = 'Win64GUI'

executables = [
    Executable('Star Dodge.py', base=base)
]


options = {
    'build_exe': {
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            "Spaceship.png",
            "Dodged_object.png",
            "spacebackground.png"
         ],
    },
}


setup(name = 'Star Dodge',
      
      options = options,
      
      executables = executables
      )

