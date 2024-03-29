import os

source = 'main.txt'
dest = 'newfile.txt'

try:
    
    os.rename(source, dest)
    print("Source path renamed to destination path successfully.")
except FileNotFoundError:
    print(f"Error: The file '{source}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied. Cannot rename '{source}'.")
except OSError as error:
    print(f"Error: {error}")
