#Directories and files

#Absolute path : The full path to a file or folder starting from the root directory.
#Relative path : The path to a file or folder based on the current working directory.

from pathlib import Path

path = Path()
print(path.exists()) #False

for file in path.glob('*.py'):
    print(file)                 #shows all .py files


