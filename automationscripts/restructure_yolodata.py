import os
import shutil

def restructure_yolo_format(input_folder, output_folder):
    """
    Restructure the YOLO dataset from labelme2yolo format to the standard format.

    Args:
        input_folder (str): Path to the labelme2yolo output folder.
        output_folder (str): Path to the desired dataset format.

    Desired Format:
    dataset/
    |__train/
        |__images/
        |__labels/
    |__test/
        |__images/
        |__labels/
    |__valid/
        |__images/
        |__labels/
    |__data.yaml
    """
    # Create train, test, valid directories with images and labels subfolders
    for split in ["train", "test", "valid"]:
        os.makedirs(os.path.join(output_folder, split, "images"), exist_ok=True)
        os.makedirs(os.path.join(output_folder, split, "labels"), exist_ok=True)

    # Move files to the appropriate directories
    for split in ["train", "test", "val"]:  # Note 'val' will map to 'valid'
        images_src = os.path.join(input_folder, "images", split)
        labels_src = os.path.join(input_folder, "labels", split)
        split_dest = "valid" if split == "val" else split  # Map 'val' to 'valid'

        images_dest = os.path.join(output_folder, split_dest, "images")
        labels_dest = os.path.join(output_folder, split_dest, "labels")

        # Copy images
        if os.path.exists(images_src): # This check is necessary to avoid code breakage if test or val folders are absent
            for file in os.listdir(images_src):
                shutil.copy(os.path.join(images_src, file), images_dest)

        # Copy labels
        if os.path.exists(labels_src):
            for file in os.listdir(labels_src):
                shutil.copy(os.path.join(labels_src, file), labels_dest)

    # Copy the dataset.yaml file, mapping dataset.yaml to data.yaml
    data_yaml_src = os.path.join(input_folder, "dataset.yaml")
    data_yaml_dest = os.path.join(output_folder, "data.yaml")
    if os.path.exists(data_yaml_src):
        shutil.copy(data_yaml_src, data_yaml_dest)

    print(f"Dataset restructured and saved to '{output_folder}'.")

# Example usage
if __name__ == "__main__":
    labelme2yolo_output = "propall_floorplans1/propall_floorplans1_door_labelmeformat/YOLODataset"
    desired_dataset_format = "propall_floorplans1/propall_floorplans1_door_yoloformat"
    restructure_yolo_format(labelme2yolo_output, desired_dataset_format)
