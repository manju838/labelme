from rfdetr import RFDETRLarge  # assuming you have this defined somewhere
from PIL import Image
from typing import List, Tuple
import numpy as np
import os

# Get the directory where this propall_detect.py lives
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# Go one directory up
_PARENT_DIR = os.path.abspath(os.path.join(_THIS_DIR, os.pardir))

# Absolute path to the checkpoint
MODEL_PATH = os.path.join(_PARENT_DIR, "model", "checkpoint_best_ema.pth")

# Map class IDs to human-readable labels
CLASS_NAMES = {
    0: "door",
    1: "wall",
    2: "window",
    3: "bed"
}

# Initialize model only once (singleton pattern)
_model = None

def _load_model():
    global _model
    if _model is None:
        _model = RFDETRLarge(pretrain_weights=MODEL_PATH)
    return _model

def predict_on_image(image_path: str, threshold: float = 0.5) -> List[Tuple[np.ndarray, int, float]]:
    """
    Runs RFDeTR on the given image and returns bounding boxes.

    :param image_path: Path to input image.
    :param threshold: Minimum confidence to keep a detection.
    :return: List of detections as (xyxy, class_id, confidence).
    """
    model = _load_model()

    image = Image.open(image_path).convert("RGB")

    raw_detections = model.predict(image, threshold=threshold)

    detections = []
    for pred in raw_detections:
        if len(pred):
            xyxy = np.array(pred[0], dtype=float)  # [x1, y1, x2, y2]
            confidence = float(pred[2])
            class_id = int(pred[3])
            detections.append((xyxy, class_id, confidence))

    return detections

def get_class_name(class_id: int) -> str:
    return CLASS_NAMES.get(class_id, f"class_{class_id}")
