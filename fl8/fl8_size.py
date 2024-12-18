import os


def get_size(directory):
    """Calculate the total size of all files in a directory (including subdirectories) and return size in MB."""
    total_size = 0
    
    # Walk through the directory
    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if os.path.isfile(file_path):  # Ensure it's a file
                total_size += os.path.getsize(file_path)
    
    # Convert bytes to MB
    size_in_mb = total_size / (1024 * 1024)
    return round(size_in_mb, 2)
