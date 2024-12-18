import os
from pathlib import Path

def find_by_ext(ext, directory):
    directory_path = Path(directory)  # Convert string to Path object
    if directory_path.exists() and directory_path.is_dir():
        files = list(directory_path.rglob(f"*.{ext}"))  # Use rglob to find files
        return files
    else:
        print(f'Error: {directory} doesn\'t exist or is not a valid directory!')

def find_by_name(name, directory):
    directory_path = Path(directory)  # Convert string to Path object
    if directory_path.exists() and directory_path.is_dir():
        files = list(directory_path.rglob(f"*{name}*"))  # Find files containing 'name' in their name
        return files
    else:
        print(f'Error: {directory} doesn\'t exist or is not a valid directory!')
