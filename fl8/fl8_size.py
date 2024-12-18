import os

def get_size(path):
    """Calculate the size of a single file or all files in a directory (including subdirectories) in MB."""
    if os.path.isfile(path):
        # If the path is a file, return its size in MB
        size_in_mb = os.path.getsize(path) / (1024 * 1024)
        return round(size_in_mb, 2)
    elif os.path.isdir(path):
        # If the path is a directory, calculate the total size of all files
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                if os.path.isfile(file_path):
                    total_size += os.path.getsize(file_path)
        size_in_mb = total_size / (1024 * 1024)
        return round(size_in_mb, 2)
    else:
        raise ValueError(f"Error: {path} is not a valid file or directory!")
