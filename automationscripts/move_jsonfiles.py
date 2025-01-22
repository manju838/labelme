"""
Here's a script that takes the _door_labelmeformat folder as input, creates a labelme_json_dir folder inside it, and moves all the JSON files into the new folder.

This is for usage of labelme2yolo library
"""

import os
import shutil

def organize_json_files(input_folder):
    """
    Organizes JSON files in the input folder by moving them into a subdirectory named 'labelme_json_dir'.

    Args:
        input_folder (str): The folder containing images and JSON files.

    Returns:
        str: The path to the created 'labelme_json_dir' folder.
    """
    # Define the output directory for JSON files
    json_dir = os.path.join(input_folder, "labelme_json_dir")
    os.makedirs(json_dir, exist_ok=True)

    # List all files in the input folder
    files = os.listdir(input_folder)

    # Iterate over files and move JSON files to the new directory
    for file in files:
        if file.endswith(".json"):
            src_json_path = os.path.join(input_folder, file)
            dest_json_path = os.path.join(json_dir, file)
            shutil.move(src_json_path, dest_json_path)

    print(f"All JSON files have been moved to '{json_dir}'.")
    return json_dir


# Example usage
if __name__ == "__main__":
    input_folder = "./propall_floorplans1/propall_floorplans1_door_labelmeformat/"  # Replace with the path to the _door_labelmeformat folder
    organize_json_files(input_folder)
