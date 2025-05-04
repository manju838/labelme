<h1 align="center">
  <img src="labelme/icons/icon.png"><br/>labelme
</h1>

<h4 align="center">
  Image Polygonal Annotation with Python
</h4>

<div align="center">
  <a href="https://pypi.python.org/pypi/labelme"><img src="https://img.shields.io/pypi/v/labelme.svg"></a>
  <!-- <a href="https://pypi.org/project/labelme"><img src="https://img.shields.io/pypi/pyversions/labelme.svg"></a> -->
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

## Installation in Manjunadh:

```bash
conda create -n new_labelme python=3.10 -y
conda activate new_labelme

pip install uv
uv pip install -e .
```

## Notes by Manjunadh

### Basic Structural Concepts

1. Makefile: 

  * A Makefile is not Python-specific. It’s a general-purpose build automation tool file used by ```make```.
  * Purpose: It lets you define rules (like make install, make clean, etc.) that automate common tasks.

Targets (commands you can run):
| Target   | Purpose                                                                       |
| -------- | ----------------------------------------------------------------------------- |
| `help`   | Lists all available targets with descriptions.                                |
| `setup`  | Installs dev dependencies from `pyproject.toml` using `uv`. (`uv sync --dev`) [An extremely fast Python package and project manager, written in Rust. ```pip install uv```] |
| `format` | Formats code using `ruff format` and fixes lint errors automatically.         |
| `lint`   | Checks code formatting and linting errors without fixing.                     |
| `mypy`   | Runs type checking on the package.                                            |
| `check`  | Runs both `lint` and `mypy` (handy shortcut).                                 |
| `test`   | Runs the `pytest` test suite.                                                 |
| `build`  | Builds the package (for publishing or testing distribution).                  |

```$(call exec,command to run)``` uses a helper macro exec and is equivalent to 
```bash
echo "command to run"
command to run
```

2. pyproject.toml: 
  * It’s the modern standard file for Python projects.
  * It declares build system settings, dependencies, and project metadata.
  * Before pyproject.toml, people used setup.py and setup.cfg (as used in main branch which is fork of an old version of labelme repo). Today, most new projects use pyproject.toml because it’s flexible and tool-agnostic.

  Key Sections (First three are main ones):

  * [project]: Metadata about your project (name, version, dependencies).
  * [build-system]: Declares what tools to use for building the project. (Here, it’s saying to use setuptools).
  * [project.scripts]:
  Each line under this section creates an executable command. For example ```labelme = "labelme.__main__:main"``` creates a command labelme which executes main() fn. in labelme/__main__.py 
  * [tool.hatch.metadata.hooks.fancy-pypi-readme]
  * [dependency-groups]
  * [tool.pytest.ini_options] : ```qt_api = "pyqt5"``` Tells pytest to use PyQt5 for any Qt-based testing.
  * [tool.ruff.lint]: ```select = ["E", "F", "I"]``` Specifies what linting checks to enable for ruff (E=Errors, F=Flake8, I=Import sorting).
  * [tool.ruff.lint.isort]:
  ```force-single-line = true``` Forces every import to be on its own line (good for readability and merge conflicts).
  * [tool.mypy]: 

3. uv.lock
  * This file is specific to ```uv``` (a faster package manager alternative) to pip and virtualenv. 
  * It automatically locks versions of all your project’s dependencies and sub-dependencies into uv.lock. This is similar to package.lock in npm bundled projects.

If uv.lock is present in the repo, install the repo in editable mode (developer mode) using the following command:
```bash
pip install uv
uv pip install -e .
```
if there is any unseen error with the above way, you can also install using pip as follows:
```bash
pip install -e .
```

Comparison:
| File               | Purpose                                      |
| ------------------ | -------------------------------------------- |
| `requirements.txt` | Lists main dependencies (older method)       |
| `pyproject.toml`   | Lists main dependencies + build settings     |
| `uv.lock`          | Pins exact versions of all (sub)dependencies |

### Entrypoint and flow of code
















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


## How to build standalone executable

```bash
LABELME_PATH=./labelme
OSAM_PATH=$(python -c 'import os, osam; print(os.path.dirname(osam.__file__))')
pyinstaller labelme/labelme/__main__.py \
  --name=Labelme \
  --windowed \
  --noconfirm \
  --specpath=build \
  --add-data=$(OSAM_PATH)/_models/yoloworld/clip/bpe_simple_vocab_16e6.txt.gz:osam/_models/yoloworld/clip \
  --add-data=$(LABELME_PATH)/config/default_config.yaml:labelme/config \
  --add-data=$(LABELME_PATH)/icons/*:labelme/icons \
  --add-data=$(LABELME_PATH)/translate/*:translate \
  --icon=$(LABELME_PATH)/icons/icon.png \
  --onedir
```


## Acknowledgement

This repo is the fork of [mpitid/pylabelme](https://github.com/mpitid/pylabelme).
