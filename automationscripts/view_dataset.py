import os
from pathlib import Path
import cv2

def overlay_bounding_boxes(train_dir: str):
    """
    Takes in a split directory(train/test/val) that has 2 subdirectories: images and labels. This directory has YOLO style datasets and saves the bounding box overlay image.
    Args:
        train_dir (str): Path to the split directory(train/test/valid) containing images and labels in YOLO bounding box style.

    Returns:
        None
    """
    
    
    # Define paths
    train_dir = Path(train_dir)
    images_dir = train_dir / "images"
    labels_dir = train_dir / "labels"
    output_dir = train_dir.parent / f"{train_dir.name}_overlayed"  # Create a sibling directory with _overlayed suffix
    output_images_dir = output_dir

    # Create output directories
    output_images_dir.mkdir(parents=True, exist_ok=True)

    # Iterate through images
    for image_file in images_dir.glob("*.png"):  # Assuming images are PNG
        # Corresponding label file
        label_file = labels_dir / (image_file.stem + ".txt")

        # Read the image
        image = cv2.imread(str(image_file))
        if image is None:
            print(f"Failed to read image: {image_file}")
            continue

        # Check if label file exists
        if not label_file.exists():
            print(f"Label file not found for image: {image_file}")
            continue

        # Read label file and overlay bounding boxes
        with open(label_file, "r") as f:
            for line in f.readlines():
                # Parse the label line: "class x_center y_center width height"
                class_id, x_center, y_center, width, height = map(float, line.strip().split())
                img_height, img_width, _ = image.shape

                # Convert normalized coordinates to pixel coordinates
                x1 = int((x_center - width / 2) * img_width)
                y1 = int((y_center - height / 2) * img_height)
                x2 = int((x_center + width / 2) * img_width)
                y2 = int((y_center + height / 2) * img_height)

                # Draw the bounding box on the image
                color = (0, 255, 0)  # Green color for the box
                thickness = 2
                cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)

                # Optionally add a label
                label_text = f"Class {int(class_id)}"
                cv2.putText(image, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)

        # Save the overlayed image
        output_image_path = output_images_dir / image_file.name
        cv2.imwrite(str(output_image_path), image)

    print(f"Overlayed images saved to: {output_images_dir}")

if __name__ == "__main__":
    # Path to the train directory
    train_dir = "./propall_floorplans1/propall_floorplans1_door_yoloformat/train"
    overlay_bounding_boxes(train_dir)