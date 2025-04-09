import os
import re

def batch_rename(directory, pattern, format_string):
    """
    Renames files in a directory based on a pattern and format string.

    Args:
        directory (str): The path to the directory containing the files.
        pattern (str): A regular expression pattern to match filenames.
        format_string (str): A format string to construct new filenames, 
                           using {} as a placeholder for matched groups.
    """
    for filename in os.listdir(directory):
        match = re.search(pattern, filename)
        if match:
            new_name = format_string.format(*match.groups())
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_name}'")

# Example usage:
directory = "/path/to/your/files" 
pattern = r"^(image)-(\d+)\.jpg$" # Matches "image-1.jpg", "image-2.jpg" etc.
format_string = "photo_{}.jpg"   # Rename to "photo_1.jpg", "photo_2.jpg" etc.

batch_rename(directory, pattern, format_string)
