from rfdetr import RFDETRLarge  # assuming you have this defined somewhere
from PIL import Image
from typing import List, Tuple
import numpy as np
import os
import json
from pathlib import Path
import sys

# Get the directory where this propall_detect.py lives
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# Go one directory up
_PARENT_DIR = os.path.abspath(os.path.join(_THIS_DIR, os.pardir))

# Absolute path to the checkpoint
MODEL_PATH = os.path.join(_PARENT_DIR, "model", "checkpoint_best_ema.pth")

# Default configuration
# DEFAULT_CONFIG = {
#     "model_path": MODEL_PATH,
#     "class_names": {
#         0: "bed",
#         1: "commode",
#         2: "diningtable",
#         3: "door",
#         4: "singlesofa",
#         5: "sofa",
#         6: "wall",
#         7: "window"
#     }
# }

DEFAULT_CONFIG = {
    "model_path": MODEL_PATH,
    "class_names": {
        0: "bed",
        1: "commode",
        2: "diningtable",
        3: "door",
        4: "kitchencabinet",
        5: "singlesofa",
        6: "sofa",
        7: "wall",
        8: "wall2",
        9: "wardrobe",
        10: "window"
    }
}

def get_config_path():
    """Get path to config file (next to executable or in user's home)"""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        app_dir = Path(sys.executable).parent
    else:
        # Running as script
        app_dir = Path(__file__).parent
    
    return app_dir / "config.json"

def load_config():
    """Load configuration from file or create default"""
    config_path = get_config_path()
    
    if config_path.exists():
        with open(config_path, 'r') as f:
            config = json.load(f)
    else:
        # Create default config file
        config = DEFAULT_CONFIG
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)
        print(f"Created default config at: {config_path}")
    
    return config

# Load configuration
config = load_config()
MODEL_PATH = config["model_path"]
CLASS_NAMES = {int(k): v for k, v in config["class_names"].items()}


# Map class IDs to human-readable labels

# CLASS_NAMES = {
#     0: "bed",
#     1: "commode",
#     2: "diningtable",
#     3: "door",
#     4: "singlesofa",
#     5: "sofa",
#     6: "wall",
#     7: "window"
# }

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

def get_all_class_names() -> list[str]:
    return list(CLASS_NAMES.values())

