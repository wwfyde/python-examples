import os
from pathlib import Path
from lib_workspace import hello

print(os.getcwd())
print(Path(__file__))
print(Path(".").resolve())
print(Path(__file__).resolve())
print(hello())
