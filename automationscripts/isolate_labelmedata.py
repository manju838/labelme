import os
import shutil

# Input folder containing images and JSON files
input_folder = "propall_floorplans1/"

# Output folder for filtered images
output_folder = os.path.join(input_folder, f"{os.path.basename(os.path.normpath(input_folder))}_door_labelmeformat")
os.makedirs(output_folder, exist_ok=True)

def filter_images_with_json(input_folder, output_folder):
    # List all files in the input folder
    files = os.listdir(input_folder)
    
    # Specify image extension
    image_extensions = {".jpg", ".jpeg", ".png"}
    
    """
    ## Some useful path handling fns.
    
    path1 = "dir1/dir2/file.txt"
    path2 = "/home/user/temp/../Documents/"

    print(os.path.splitext(path1)[0]) # dir1/dir2/file
    print(os.path.splitext(path1)[1]) # .txt
    print(os.path.basename(path1))    # file.txt
    print(os.path.normpath(path2))    # /home/user/temp/Documents
    
    """
    
    # Get Json filepath roots
    json_filepath_roots = {os.path.splitext(file)[0] for file in files if file.endswith(".json")} # Split Extension splits path into root and ext
    
    # Iterate through all files and extract images corresponding to json files
    for file in files:
        file_root, file_ext = os.path.splitext(file)
        
        # Check if it's an image with a corresponding JSON file
        if file_ext.lower() in image_extensions and file_root in json_filepath_roots:
            
            # Copy the image to the output folder
            src_img_path = os.path.join(input_folder, file)
            dest_img_path = os.path.join(output_folder, file)
            shutil.copy(src_img_path, dest_img_path)
    
            # Copy json file to the output folder
            src_json_path = os.path.join(input_folder, f"{file_root}.json")
            dest_json_path = os.path.join(output_folder, f"{file_root}.json")
            shutil.copy(src_json_path, dest_json_path)
    
    print(f"Filtered images and JSON files saved to {output_folder}")
    


# Run the function
filter_images_with_json(input_folder, output_folder)
