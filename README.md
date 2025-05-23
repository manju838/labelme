<h1 align="center">
  <img src="labelme/icons/icon.png"><br/>labelme
</h1>

<h4 align="center">
  Image Polygonal Annotation with Python
</h4>

<div align="center">
  <a href="https://pypi.python.org/pypi/labelme"><img src="https://img.shields.io/pypi/v/labelme.svg"></a>
  <a href="https://pypi.org/project/labelme"><img src="https://img.shields.io/pypi/pyversions/labelme.svg"></a>
  <a href="https://github.com/wkentaro/labelme/actions"><img src="https://github.com/wkentaro/labelme/actions/workflows/ci.yml/badge.svg?branch=main&event=push"></a>
</div>

<div align="center">
  <a href="#installation"><b>Installation</b></a>
  | <a href="#usage"><b>Usage</b></a>
  | <a href="#examples"><b>Examples</b></a>
  <!-- | <a href="https://github.com/wkentaro/labelme/discussions"><b>Community</b></a> -->
  <!-- | <a href="https://www.youtube.com/playlist?list=PLI6LvFw0iflh3o33YYnVIfOpaO0hc5Dzw"><b>Youtube FAQ</b></a> -->
</div>

<br/>

<div align="center">
  <img src="examples/instance_segmentation/.readme/annotation.jpg" width="70%">
</div>

## Installation Setup by Manjunadh

Installation is done on Windows with gitbash. Usage on WSL2 failed due to some errors in PyQt5
```bash
conda create --name labelme python=3.9
conda activate labelme

git clone https://github.com/manju838/labelme.git
cd labelme

pip install -e . # Installation in executable/developer mode(changes made to repo will be reflected without reinstallation). Looks for setup.py in repo and creates a symbolic link between the development directory and site-packages in conda env.


pip install labelme2yolo==0.2.5 # Data annotated for object detection(bounding boxes) using labelme is not of YOLO format but rather "LabelMe JSON format"
```

## Add the different repository as a seperate branch of your forked repository

```
origin     -> your labelme fork (older version)
upstream   -> labelme repo version 5.8.1
upstream2  -> mberkay0’s automated-labelme repo
``` 

```bash
git remote add upstream2 <different repository url>
git fetch upstream2
git checkout -b <NEW_BRANCH>
git reset --hard upstream2/main (If main branch is the default)
git push origin <NEW_BRANCH>
```

## Directory Structure Description by Manjunadh

To get the directory structure for the current github repo:
```bash
npm i -g @jpwilliams/gitree
gitree
```

```
.
├── .flake8
├── .github
│   ├── FUNDING.yml
│   ├── ISSUE_TEMPLATE
│   │   ├── 1.bug_report.yml
│   │   └── config.yml
│   └── workflows
│       ├── ci.yml
│       └── release.yml
├── .gitignore
├── .gitmodules
├── automationscripts
│   ├── isolate_labelmedata.py
│   ├── move_jsonfiles.py
│   ├── rescale_datasets.py
│   ├── restructure_yolodata.py
│   └── view_dataset.py
├── CITATION.cff
├── examples
│   ├── bbox_detection
│   │   ├── .readme
│   │   │   └── annotation.jpg
│   │   ├── data_annotated
│   │   │   ├── 2011_000003.jpg
│   │   │   ├── 2011_000003.json
│   │   │   ├── 2011_000025.jpg
│   │   │   └── 2011_000025.json
│   │   ├── data_dataset_voc
│   │   │   ├── Annotations
│   │   │   │   ├── 2011_000003.xml
│   │   │   │   └── 2011_000025.xml
│   │   │   ├── AnnotationsVisualization
│   │   │   │   ├── 2011_000003.jpg
│   │   │   │   └── 2011_000025.jpg
│   │   │   ├── class_names.txt
│   │   │   └── JPEGImages
│   │   │       ├── 2011_000003.jpg
│   │   │       └── 2011_000025.jpg
│   │   ├── labelme2voc.py
│   │   ├── labels.txt
│   │   └── README.md
│   ├── classification
│   │   ├── .readme
│   │   │   ├── annotation_cat.jpg
│   │   │   └── annotation_dog.jpg
│   │   ├── data_annotated
│   │   │   ├── 0001.jpg
│   │   │   ├── 0001.json
│   │   │   ├── 0002.jpg
│   │   │   └── 0002.json
│   │   ├── flags.txt
│   │   └── README.md
│   ├── instance_segmentation
│   │   ├── .readme
│   │   │   ├── annotation.jpg
│   │   │   ├── draw_label_png_class.jpg
│   │   │   └── draw_label_png_object.jpg
│   │   ├── data_annotated
│   │   │   ├── 2011_000003.jpg
│   │   │   ├── 2011_000003.json
│   │   │   ├── 2011_000025.jpg
│   │   │   └── 2011_000025.json
│   │   ├── data_dataset_coco
│   │   │   ├── annotations.json
│   │   │   ├── JPEGImages
│   │   │   │   ├── 2011_000003.jpg
│   │   │   │   └── 2011_000025.jpg
│   │   │   └── Visualization
│   │   │       ├── 2011_000003.jpg
│   │   │       └── 2011_000025.jpg
│   │   ├── data_dataset_voc
│   │   │   ├── class_names.txt
│   │   │   ├── JPEGImages
│   │   │   │   ├── 2011_000003.jpg
│   │   │   │   └── 2011_000025.jpg
│   │   │   ├── SegmentationClass
│   │   │   │   ├── 2011_000003.png
│   │   │   │   └── 2011_000025.png
│   │   │   ├── SegmentationClassNpy
│   │   │   │   ├── 2011_000003.npy
│   │   │   │   └── 2011_000025.npy
│   │   │   ├── SegmentationClassVisualization
│   │   │   │   ├── 2011_000003.jpg
│   │   │   │   └── 2011_000025.jpg
│   │   │   ├── SegmentationObject
│   │   │   │   ├── 2011_000003.png
│   │   │   │   └── 2011_000025.png
│   │   │   ├── SegmentationObjectNpy
│   │   │   │   ├── 2011_000003.npy
│   │   │   │   └── 2011_000025.npy
│   │   │   └── SegmentationObjectVisualization
│   │   │       ├── 2011_000003.jpg
│   │   │       └── 2011_000025.jpg
│   │   ├── labelme2coco.py
│   │   ├── labelme2voc.py
│   │   ├── labels.txt
│   │   └── README.md
│   ├── primitives
│   │   ├── primitives.jpg
│   │   └── primitives.json
│   ├── semantic_segmentation
│   │   ├── .readme
│   │   │   ├── annotation.jpg
│   │   │   └── draw_label_png.jpg
│   │   ├── data_annotated
│   │   │   ├── 2011_000003.jpg
│   │   │   └── 2011_000025.json
│   │   ├── data_dataset_voc
│   │   │   ├── class_names.txt
│   │   │   ├── JPEGImages
│   │   │   │   ├── 2011_000003.jpg
│   │   │   │   └── 2011_000025.jpg
│   │   │   ├── SegmentationClass
│   │   │   │   ├── 2011_000003.png
│   │   │   │   └── 2011_000025.png
│   │   │   ├── SegmentationClassNpy
│   │   │   │   ├── 2011_000003.npy
│   │   │   │   └── 2011_000025.npy
│   │   │   └── SegmentationClassVisualization
│   │   │       ├── 2011_000003.jpg
│   │   │       └── 2011_000025.jpg
│   │   ├── labelme2voc.py
│   │   ├── labels.txt
│   │   └── README.md
│   ├── tutorial
│   │   ├── .readme
│   │   │   ├── annotation.jpg
│   │   │   ├── draw_json.jpg
│   │   │   └── draw_label_png.jpg
│   │   ├── apc2016_obj3.jpg
│   │   ├── apc2016_obj3.json
│   │   ├── apc2016_obj3_json
│   │   │   ├── img.png
│   │   │   ├── label.png
│   │   │   ├── label_names.txt
│   │   │   └── label_viz.png
│   │   ├── load_label_png.py
│   │   └── README.md
│   └── video_annotation
│       ├── .readme
│       │   ├── 00000100.jpg
│       │   ├── 00000101.jpg
│       │   └── data_annotated.gif
│       ├── data_annotated
│       │   ├── 00000100.jpg
│       │   ├── 00000100.json
│       │   ├── 00000101.jpg
│       │   ├── 00000101.json
│       │   ├── 00000102.jpg
│       │   ├── 00000102.json
│       │   ├── 00000103.jpg
│       │   ├── 00000103.json
│       │   ├── 00000104.jpg
│       │   └── 00000104.json
│       ├── data_dataset_voc
│       │   ├── class_names.txt
│       │   ├── JPEGImages
│       │   │   ├── 00000100.jpg
│       │   │   └── 00000104.jpg
│       │   ├── SegmentationClass
│       │   │   ├── 00000100.npy
│       │   │   └── 00000104.npy
│       │   ├── SegmentationClassPNG
│       │   │   ├── 00000100.png
│       │   │   └── 00000104.png
│       │   └── SegmentationClassVisualization
│       │       ├── 00000100.jpg
│       │       └── 00000104.jpg
│       ├── labelme2voc.py
│       ├── labels.txt
│       └── README.md
├── labelme.desktop
├── labelme.spec
├── labelme
│   ├── __init__.py
│   ├── __main__.py
│   ├── ai
│   │   ├── __init__.py
│   │   ├── _utils.py
│   │   ├── efficient_sam.py
│   │   ├── segment_anything_model.py
│   │   └── text_to_annotation.py
│   ├── app.py
│   ├── cli
│   │   ├── __init__.py
│   │   ├── draw_json.py
│   │   ├── draw_label_png.py
│   │   ├── export_json.py
│   │   ├── json_to_dataset.py
│   │   └── on_docker.py
│   ├── config
│   │   ├── __init__.py
│   │   └── default_config.yaml
│   ├── icons
│   │   ├── cancel.png
│   │   ├── close.png
│   │   ├── color-line.png
│   │   ├── color.png
│   │   ├── copy.png
│   │   ├── delete.png
│   │   ├── done.png
│   │   ├── done.svg
│   │   ├── edit.png
│   │   ├── expert.png
│   │   ├── eye.png
│   │   ├── feBlend-icon.png
│   │   ├── file.png
│   │   ├── fit-width.png
│   │   ├── fit-window.png
│   │   ├── fit.png
│   │   ├── help.png
│   │   ├── icon.icns
│   │   ├── icon.ico
│   │   ├── icon.png
│   │   ├── labels.png
│   │   ├── labels.svg
│   │   ├── new.png
│   │   ├── next.png
│   │   ├── objects.png
│   │   ├── open.png
│   │   ├── open.svg
│   │   ├── prev.png
│   │   ├── quit.png
│   │   ├── save-as.png
│   │   ├── save-as.svg
│   │   ├── save.png
│   │   ├── save.svg
│   │   ├── undo-cross.png
│   │   ├── undo.png
│   │   ├── zoom-in.png
│   │   ├── zoom-out.png
│   │   └── zoom.png
│   ├── label_file.py
│   ├── shape.py
│   ├── testing.py
│   ├── translate
│   │   ├── empty.ts
│   │   ├── zh_CN.qm
│   │   └── zh_CN.ts
│   ├── utils
│   │   ├── __init__.py
│   │   ├── _io.py
│   │   ├── image.py
│   │   ├── qt.py
│   │   └── shape.py
│   └── widgets
│       ├── __init__.py
│       ├── ai_prompt_widget.py
│       ├── brightness_contrast_dialog.py
│       ├── canvas.py
│       ├── color_dialog.py
│       ├── escapable_qlist_widget.py
│       ├── file_dialog_preview.py
│       ├── label_dialog.py
│       ├── label_list_widget.py
│       ├── tool_bar.py
│       ├── unique_label_qlist_widget.py
│       └── zoom_widget.py
├── LICENSE
├── Makefile
├── MANIFEST.in
├── pytest.ini
├── README.md +2 -2
├── requirements-dev.txt
├── ruff.toml
├── setup.py
└── tests
    └── labelme_tests
        ├── __init__.py
        ├── data
        │   ├── annotated
        │   │   ├── 2011_000003.jpg
        │   │   ├── 2011_000003.json
        │   ├── annotated_with_data
        │   │   ├── apc2016_obj3.jpg
        │   │   └── apc2016_obj3.json
        │   └── raw
        │       ├── 2011_000003.jpg
        │       └── 2011_000006.jpg
        ├── test_app.py
        ├── utils_tests
        │   ├── __init__.py
        │   ├── test_image.py
        │   ├── test_shape.py
        │   └── util.py
        └── widgets_tests
            ├── __init__.py
            ├── test_label_dialog.py
            └── test_label_list_widget.py
```

## Data Preparation

The files for processing are found at "automationscripts" directory

1. LabelMe Annotated directory ==> ./propall_floorplans1/
2. Filter Img-Label Pairs ==> ./propall_floorplans1/propall_floorplans1_door_labelmeformat (Use isolate_labelmedata.py)
3. Isolate json files from labelmeformat folder ==> ./propall_floorplans1/propall_floorplans1_door_labelmeformat/labelme_json_dir (Use move_jsonfiles.py)
4. Convert labelme format to YOLO format using the below command:

```bash
labelme2yolo --json_dir propall_floorplans1/propall_floorplans1_door_labelmeformat/ --test_size 0 --val_size 0 --output_format bbox
```
[Tutorial video to do the same](https://www.youtube.com/watch?v=bTUG82UaPdQ)

5. Restructure labelme2yolo output to YOLO format ==> ./propall_floorplans1/propall_floorplans1_door_yoloformat(Use restructure_yolodata.py)

Final_YOLOdataset format
|____images
    |__train
    |__test
    |__val
|____labels
    |__train
    |__test
    |__val
|____data.yaml

labelme2yolo_output format
|__train
    |__images
    |__labels
|__test
    |__images
    |__labels
|__valid
    |__images
    |__labels
|__data.yaml

6. Check data.yaml file as sometimes the paths generated by labelme2yolo have wierd characters like "?" and correct any paths

## Training Method:

Objective: Train YOLO model with 80 epochs(depending on dataset size) with crossvalidation and MLflow included













## Description

Labelme is a graphical image annotation tool inspired by <http://labelme.csail.mit.edu>.  
It is written in Python and uses Qt for its graphical interface.

<img src="examples/instance_segmentation/data_dataset_voc/JPEGImages/2011_000006.jpg" width="19%" /> <img src="examples/instance_segmentation/data_dataset_voc/SegmentationClass/2011_000006.png" width="19%" /> <img src="examples/instance_segmentation/data_dataset_voc/SegmentationClassVisualization/2011_000006.jpg" width="19%" /> <img src="examples/instance_segmentation/data_dataset_voc/SegmentationObject/2011_000006.png" width="19%" /> <img src="examples/instance_segmentation/data_dataset_voc/SegmentationObjectVisualization/2011_000006.jpg" width="19%" />  
<i>VOC dataset example of instance segmentation.</i>

<img src="examples/semantic_segmentation/.readme/annotation.jpg" width="30%" /> <img src="examples/bbox_detection/.readme/annotation.jpg" width="30%" /> <img src="examples/classification/.readme/annotation_cat.jpg" width="35%" />  
<i>Other examples (semantic segmentation, bbox detection, and classification).</i>

<img src="https://user-images.githubusercontent.com/4310419/47907116-85667800-de82-11e8-83d0-b9f4eb33268f.gif" width="30%" /> <img src="https://user-images.githubusercontent.com/4310419/47922172-57972880-deae-11e8-84f8-e4324a7c856a.gif" width="30%" /> <img src="https://user-images.githubusercontent.com/14256482/46932075-92145f00-d080-11e8-8d09-2162070ae57c.png" width="32%" />  
<i>Various primitives (polygon, rectangle, circle, line, and point).</i>


## Features

- [x] Image annotation for polygon, rectangle, circle, line and point. ([tutorial](examples/tutorial))
- [x] Image flag annotation for classification and cleaning. ([#166](https://github.com/wkentaro/labelme/pull/166))
- [x] Video annotation. ([video annotation](examples/video_annotation))
- [x] GUI customization (predefined labels / flags, auto-saving, label validation, etc). ([#144](https://github.com/wkentaro/labelme/pull/144))
- [x] Exporting VOC-format dataset for semantic/instance segmentation. ([semantic segmentation](examples/semantic_segmentation), [instance segmentation](examples/instance_segmentation))
- [x] Exporting COCO-format dataset for instance segmentation. ([instance segmentation](examples/instance_segmentation))


## Installation

There are 2 options to install labelme:

### Option 1: Using pip

For more detail, check ["Install Labelme using Pip"](https://www.labelme.io/docs/install-labelme-pip).

```bash
pip install labelme
```

### Option 2: Using standalone executable (Easiest)

If you're willing to invest in the convenience of simple installation without any dependencies (Python, Qt),
you can download the standalone executable from ["Install Labelme as App"](https://www.labelme.io/docs/install-labelme-app).

It's a one-time payment for lifetime access, and it helps us to maintain this project.


## Usage

Run `labelme --help` for detail.  
The annotations are saved as a [JSON](http://www.json.org/) file.

```bash
labelme  # just open gui

# tutorial (single image example)
cd examples/tutorial
labelme apc2016_obj3.jpg  # specify image file
labelme apc2016_obj3.jpg -O apc2016_obj3.json  # close window after the save
labelme apc2016_obj3.jpg --nodata  # not include image data but relative image path in JSON file
labelme apc2016_obj3.jpg \
  --labels highland_6539_self_stick_notes,mead_index_cards,kong_air_dog_squeakair_tennis_ball  # specify label list

# semantic segmentation example
cd examples/semantic_segmentation
labelme data_annotated/  # Open directory to annotate all images in it
labelme data_annotated/ --labels labels.txt  # specify label list with a file
```

### Command Line Arguments
- `--output` specifies the location that annotations will be written to. If the location ends with .json, a single annotation will be written to this file. Only one image can be annotated if a location is specified with .json. If the location does not end with .json, the program will assume it is a directory. Annotations will be stored in this directory with a name that corresponds to the image that the annotation was made on.
- The first time you run labelme, it will create a config file in `~/.labelmerc`. You can edit this file and the changes will be applied the next time that you launch labelme. If you would prefer to use a config file from another location, you can specify this file with the `--config` flag.
- Without the `--nosortlabels` flag, the program will list labels in alphabetical order. When the program is run with this flag, it will display labels in the order that they are provided.
- Flags are assigned to an entire image. [Example](examples/classification)
- Labels are assigned to a single polygon. [Example](examples/bbox_detection)

### FAQ

- **How to convert JSON file to numpy array?** See [examples/tutorial](examples/tutorial#convert-to-dataset).
- **How to load label PNG file?** See [examples/tutorial](examples/tutorial#how-to-load-label-png-file).
- **How to get annotations for semantic segmentation?** See [examples/semantic_segmentation](examples/semantic_segmentation).
- **How to get annotations for instance segmentation?** See [examples/instance_segmentation](examples/instance_segmentation).


## Examples

* [Image Classification](examples/classification)
* [Bounding Box Detection](examples/bbox_detection)
* [Semantic Segmentation](examples/semantic_segmentation)
* [Instance Segmentation](examples/instance_segmentation)
* [Video Annotation](examples/video_annotation)

## How to develop

```bash
git clone https://github.com/wkentaro/labelme.git
cd labelme

# Install anaconda3 and labelme
curl -L https://github.com/wkentaro/dotfiles/raw/main/local/bin/install_anaconda3.sh | bash -s .
source .anaconda3/bin/activate
pip install -e .
```


### How to build standalone executable

Below shows how to build the standalone executable on macOS, Linux and Windows.  

```bash
# Setup conda
conda create --name labelme python=3.9
conda activate labelme

# Build the standalone executable
pip install .
pip install 'matplotlib<3.3'
pip install pyinstaller
pyinstaller labelme.spec
dist/labelme --version
```


### How to contribute

Make sure below test passes on your environment.  
See `.github/workflows/ci.yml` for more detail.

```bash
pip install -r requirements-dev.txt

ruff format --check  # `ruff format` to auto-fix
ruff check  # `ruff check --fix` to auto-fix
MPLBACKEND='agg' pytest -vsx tests/
```


## Acknowledgement

This repo is the fork of [mpitid/pylabelme](https://github.com/mpitid/pylabelme).
