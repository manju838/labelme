from rfdetr import RFDETRLarge, RFDETRSmall
from PIL import Image
from typing import List, Tuple, Dict
import numpy as np
import os
import json
from pathlib import Path
import sys

# Get the directory where this propall_detect.py lives
_THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# Go one directory up
_PARENT_DIR = os.path.abspath(os.path.join(_THIS_DIR, os.pardir))

# Absolute paths to checkpoints
MODEL_PATH_LARGE = os.path.join(_PARENT_DIR, "model", "checkpoint_best_ema.pth")
MODEL_PATH_SMALL = os.path.join(_PARENT_DIR, "model", "commercial_128img_checkpoint_best_ema.pth")

# Default configurations for each model type
MODEL_CONFIGS: Dict[str, Dict] = {
    "RFDETRLarge": {
        "model_path": MODEL_PATH_LARGE,
        "class_names": {
            0: "bed",
            1: "commode",
            2: "diningtable",
            3: "door",
            4: "kitchencabinet",
            5: "singlesofa",
            6: "sofa",
            7: "wall",
            8: "wardrobe",
            9: "window"
        }
    },
    "RFDETRSmall": {
        "model_path": MODEL_PATH_SMALL,
        "class_names": {
            0: "bed",
            1: "cabintable",
            2: "circulartable",
            3: "commode",
            4: "conferencetable",
            5: "diningtable",
            6: "door",
            7: "kitchencabinet",
            8: "singlesofa",
            9: "sofa",
            10: "wall",
            11: "wardrobe",
            12: "window",
            13: "workstation"
        }
    }
}

# For backward compatibility and initial loading
DEFAULT_CONFIG = MODEL_CONFIGS["RFDETRLarge"]

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

# Load initial configuration (primarily for backward compatibility if needed)
config = load_config()

# Global model cache (singleton pattern for each model type)
_models: Dict[str, object] = {}

def _load_model(model_name: str = "RFDETRLarge"):
    global _models
    if model_name not in _models:
        if model_name == "RFDETRLarge":
            path = MODEL_CONFIGS["RFDETRLarge"]["model_path"]
            _models[model_name] = RFDETRLarge(pretrain_weights=path)
        elif model_name == "RFDETRSmall":
            path = MODEL_CONFIGS["RFDETRSmall"]["model_path"]
            _models[model_name] = RFDETRSmall(pretrain_weights=path)
        else:
            raise ValueError(f"Unknown model name: {model_name}")
    return _models[model_name]

def predict_on_image(image_path: str, model_name: str = "RFDETRLarge", threshold: float = 0.5) -> List[Tuple[np.ndarray, int, float]]:
    """
    Runs RFDeTR on the given image and returns bounding boxes.

    :param image_path: Path to input image.
    :param model_name: Name of the model to use ("RFDETRLarge" or "RFDETRSmall").
    :param threshold: Minimum confidence to keep a detection.
    :return: List of detections as (xyxy, class_id, confidence).
    """
    model = _load_model(model_name)

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

def get_class_name(class_id: int, model_name: str = "RFDETRLarge") -> str:
    configs = MODEL_CONFIGS.get(model_name, MODEL_CONFIGS["RFDETRLarge"])
    return configs["class_names"].get(class_id, f"class_{class_id}")

def get_all_model_class_names() -> Dict[str, List[str]]:
    """Returns all class names for all supported models."""
    return {name: list(cfg["class_names"].values()) for name, cfg in MODEL_CONFIGS.items()}

def get_all_class_names() -> List[str]:
    """Returns a unique list of all class names from all models."""
    all_names = set()
    for cfg in MODEL_CONFIGS.values():
        all_names.update(cfg["class_names"].values())
    return sorted(list(all_names))

