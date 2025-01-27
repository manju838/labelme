import os
import cv2
import shutil
from pathlib import Path


def resize_image_and_labels(image_path: str, label_path: str, output_image_path: str, output_label_path: str, target_size: int):
    """
    Resizes an image to a fixed size and adjusts the bounding box annotations.

    Args:
        image_path (str): Path to the input image file.
        label_path (str): Path to the input YOLO label file corresponding to the image.
        output_image_path (str): Path to save the resized image.
        output_label_path (str): Path to save the resized label annotations.
        target_size (int): The target size for both width and height of the image.

    Returns:
        None
    """
    # Read the image
    image = cv2.imread(image_path)
    h, w, _ = image.shape

    # Calculate scaling factors
    scale_x = target_size / w
    scale_y = target_size / h

    # Resize the image
    resized_image = cv2.resize(image, (target_size, target_size))

    # Save the resized image
    cv2.imwrite(output_image_path, resized_image)

    # Adjust and save the labels
    if os.path.exists(label_path):
        with open(label_path, 'r') as f:
            lines = f.readlines()

        resized_labels = []
        for line in lines:
            class_id, x_center, y_center, box_width, box_height = map(float, line.strip().split())
            
            # Denormalize coordinates to the original image dimensions
            x_center *= w
            y_center *= h
            box_width *= w
            box_height *= h
            
            # Scale to the target size
            x_center *= scale_x
            y_center *= scale_y
            box_width *= scale_x
            box_height *= scale_y

            # Normalize coordinates to the new image dimensions
            x_center /= target_size
            y_center /= target_size
            box_width /= target_size
            box_height /= target_size

            resized_labels.append(f"{class_id} {x_center} {y_center} {box_width} {box_height}\n")

        # Save adjusted labels
        with open(output_label_path, 'w') as f:
            f.writelines(resized_labels)


def process_dataset(dataset_path: str, acceptable_img_formats:dict ,target_size: int = 640):
    """
    Processes a YOLO dataset by resizing all images and scaling their annotations to a fixed size.
    
    Args:
        dataset_path (str): Path to the root directory of the YOLO dataset. 
                            The dataset should have the following structure:
                            dataset/
                            ├── train/
                            │   ├── images/
                            │   ├── labels/
                            ├── test/ (optional)
                            │   ├── images/
                            │   ├── labels/
                            ├── valid/ (optional)
                            |   ├── images/
                            |   ├── labels/
                            ├── data.yaml
        acceptable_img_formats (dict): Define acceptable image formats with dot prefixed (Example: {'.jpg', '.jpeg', '.png'})
        target_size (int): The target size for both width and height of the images.

    Returns:
        None
    """
    parent_path = Path(dataset_path).parent
    rescaled_dataset_dir = os.path.join(parent_path, "rescaled")
    # Create a folder for the rescaled dataset
    os.makedirs(rescaled_dataset_dir, exist_ok=True)

    for split in ['train', 'test', 'valid']:
        src_images_dir = Path(dataset_path) / split / 'images'
        src_labels_dir = Path(dataset_path) / split / 'labels'
        dest_images_dir = Path(rescaled_dataset_dir) / split / 'images'
        dest_labels_dir = Path(rescaled_dataset_dir) / split / 'labels'

        if not src_images_dir.exists() or not src_labels_dir.exists():
            print(f"Skipping {split} as the directory does not exist.")
            continue

        # Create destination directories
        os.makedirs(dest_images_dir, exist_ok=True)
        os.makedirs(dest_labels_dir, exist_ok=True)

        # Process each image and its corresponding label
        for file_name in os.listdir(src_images_dir):
            root, ext = os.path.splitext(file_name)
            if ext.lower() in acceptable_img_formats:
                image_path = src_images_dir / file_name
                label_path = src_labels_dir / f"{root}.txt"
                output_image_path = dest_images_dir / file_name
                output_label_path = dest_labels_dir / f"{root}.txt"

                # Resize and save image and labels
                resize_image_and_labels(str(image_path), str(label_path), str(output_image_path), str(output_label_path), target_size)

    # Copy `data.yaml` to the rescaled dataset directory
    data_yaml_src = Path(dataset_path) / 'data.yaml'
    data_yaml_dst = Path(rescaled_dataset_dir) / 'data.yaml'
    if data_yaml_src.exists():
        shutil.copy(data_yaml_src, data_yaml_dst)
    print(f"Rescaled dataset saved at: {rescaled_dataset_dir}")

if __name__=='__main__':
    # Define the dataset path
    dataset_path = "propall_floorplans1_door_yoloformat/"
    
    # Set the target image size
    TARGET_SIZE = 640
    
    # Define acceptable image formats
    acceptable_img_formats = {'.jpg', '.jpeg', '.png'}
    
    # Process the dataset
    process_dataset(dataset_path, acceptable_img_formats, TARGET_SIZE)
    