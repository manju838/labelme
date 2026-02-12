import json
import os
from pathlib import Path

def fix_label_in_json(json_path, old_label, new_label):
    """
    Fix mislabelled class names in a labelme JSON file.
    
    Args:
        json_path: Path to the JSON file
        old_label: The incorrect label to replace
        new_label: The correct label to use
    
    Returns:
        Number of labels changed in this file
    """
    try:
        # Read the JSON file
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        changes_made = 0
        
        # Check if 'shapes' key exists
        if 'shapes' in data:
            # Iterate through all shapes and fix labels
            for shape in data['shapes']:
                if shape.get('label') == old_label:
                    shape['label'] = new_label
                    changes_made += 1
        
        # Only write back if changes were made
        if changes_made > 0:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"✓ {json_path.name}: Changed {changes_made} label(s)")
        
        return changes_made
    
    except json.JSONDecodeError as e:
        print(f"✗ Error reading {json_path.name}: Invalid JSON - {e}")
        return 0
    except Exception as e:
        print(f"✗ Error processing {json_path.name}: {e}")
        return 0


def fix_labels_in_folder(folder_path, old_label="toilet", new_label="commode"):
    """
    Fix mislabelled class names in all JSON files in a folder.
    
    Args:
        folder_path: Path to the folder containing JSON files
        old_label: The incorrect label to replace (default: "toilet")
        new_label: The correct label to use (default: "commode")
    """
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Error: Folder '{folder_path}' does not exist!")
        return
    
    if not folder.is_dir():
        print(f"Error: '{folder_path}' is not a directory!")
        return
    
    # Find all JSON files
    json_files = list(folder.glob("*.json"))
    
    if not json_files:
        print(f"No JSON files found in '{folder_path}'")
        return
    
    print(f"Found {len(json_files)} JSON file(s)")
    print(f"Replacing '{old_label}' with '{new_label}'...\n")
    
    total_changes = 0
    files_modified = 0
    
    # Process each JSON file
    for json_file in json_files:
        changes = fix_label_in_json(json_file, old_label, new_label)
        total_changes += changes
        if changes > 0:
            files_modified += 1
    
    # Summary
    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"  Total files processed: {len(json_files)}")
    print(f"  Files modified: {files_modified}")
    print(f"  Total labels changed: {total_changes}")
    print(f"{'='*50}")


if __name__ == "__main__":
    # USAGE: Update the folder path below
    folder_path = "C:/Users/manju/Downloads/final_training_dataset/final_training_dataset/val"
    
    # Optional: customize the labels to replace
    # old_label = "toilet"
    # new_label = "commode"
    
    fix_labels_in_folder(folder_path, old_label="dinningtable", new_label="diningtable")