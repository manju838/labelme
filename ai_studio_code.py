import cv2
import numpy as np
import json
import os

def generate_labelme_json(image_path, boxes, label="detected_object"):
    """
    Creates a basic LabelMe JSON file from detected boxes.
    """
    img = cv2.imread(image_path)
    h, w = img.shape[:2]
    
    shapes = []
    for (x1, y1, x2, y2) in boxes:
        shape = {
            "label": label,
            "points": [[float(x1), float(y1)], [float(x2), float(y2)]],
            "group_id": None,
            "shape_type": "rectangle",
            "flags": {}
        }
        shapes.append(shape)

    data = {
        "version": "5.0.1",
        "flags": {},
        "shapes": shapes,
        "imagePath": os.path.basename(image_path),
        "imageData": None, # LabelMe can read the image from disk if this is null
        "imageHeight": h,
        "imageWidth": w
    }
    
    # Save json with same name as image
    json_path = os.path.splitext(image_path)[0] + ".json"
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved annotations to {json_path}")

def detect_objects(image_path, template_path, threshold=0.8):
    # 1. Load image and template
    img_rgb = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_path, 0)
    
    w, h = template.shape[::-1]
    
    detected_boxes = []

    # 2. Iterate through 4 rotations (0, 90, 180, 270)
    # Floor plan furniture is almost always orthogonal
    for angle in [0, 90, 180, 270]:
        
        # Rotate the template
        if angle == 0:
            rotated_temp = template
        else:
            rotated_temp = cv2.rotate(template, cv2.ROTATE_90_CLOCKWISE)
            # Update template for next iteration (cumulative rotation)
            template = rotated_temp 
            
        cur_w, cur_h = rotated_temp.shape[::-1]

        # 3. Perform Match Template
        res = cv2.matchTemplate(img_gray, rotated_temp, cv2.TM_CCOEFF_NORMED)
        
        # 4. Filter by threshold
        loc = np.where(res >= threshold)
        
        for pt in zip(*loc[::-1]):
            # Save (x1, y1, x2, y2)
            detected_boxes.append([pt[0], pt[1], pt[0] + cur_w, pt[1] + cur_h])

    # 5. Non-Maximum Suppression (NMS) to remove overlapping boxes
    # OpenCV's groupRectangles is a simple way to do this
    if len(detected_boxes) > 0:
        rects, weights = cv2.groupRectangles(np.array(detected_boxes).tolist(), 1, 0.2)
        return rects
    else:
        return []

# --- USAGE ---
# 1. Crop a desk or chair from your main image and save it as "template.png"
# 2. Run this script
image_file = "floorplan.jpg"   # Your big floorplan
template_file = "desk_crop.png" # Your single cropped example

boxes = detect_objects(image_file, template_file, threshold=0.7)

# Visualization (Optional)
debug_img = cv2.imread(image_file)
for (x, y, x2, y2) in boxes:
    cv2.rectangle(debug_img, (x, y), (x2, y2), (0, 0, 255), 2)
cv2.imwrite("result_debug.jpg", debug_img)

# Generate LabelMe JSON so you can edit it
generate_labelme_json(image_file, boxes, label="Workstation")