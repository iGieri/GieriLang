# Script to compile your personal GieriLang compiler

import subprocess
import sys
from os import system

if __name__ == '__main__':
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    system("pyinstaller -F gieri.py")
