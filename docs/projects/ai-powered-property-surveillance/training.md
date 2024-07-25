---
title: Training YOLOv8 on Labeled Data from Label Studio
description: A step-by-step guide to training YOLOv8 on labeled data from Label Studio.
authors: [harmindersinghnijjar]
date: 2023-12-10
tags: [YOLOv8, Label Studio, Object Detection, Computer Vision, Python]
toc: true
comments: true
---

# Training YOLOv8 on Labeled Data from Label Studio

## YOLOv8 Training Data for Varied Conditions

### Images

- Collect a diverse dataset comprising several thousand annotated images for each of the DVR camera views.
- Include images that represent different times of day, seasons, weather conditions, and lighting scenarios.
- Ensure a range of backgrounds and object poses to enhance model generalization.

### Labels

- Annotate each image with bounding boxes to accurately mark objects for detection.
- Create labels for each object, considering variations in appearance under different conditions.

**Note:** Adequate representation of diverse conditions is crucial for robust object detection. Refer to YOLOv8 documentation for specific recommendations and guidelines.


## 1. Prepare Your Dataset

### Export Your Dataset

Export your dataset from Label Studio in the YOLO format. This will generate a .zip file containing the images and annotations in the required format.

### Organize Your Dataset

Ensure your dataset is properly organized. Each image in the `images` folder should have a corresponding annotation file in the `labels` folder.

### Dataset Structure

- `project-1-at-2023-12-10-11-21-cc95541c`
  - `images`: Contains all the .bmp image files.
  - `labels`: Contains corresponding .txt files for each image in YOLO format.

### Prepare Label Files

Each label file should have the following format:

- One line per object.
- Each line: `<class_index> <x_center> <y_center> <width> <height>`, normalized to [0,1].

### Create a train, val, and test split

Create a train, val, and test split of your dataset. The train set should contain 70% of the images, the val set should contain 15% of the images, and the test set should contain 15% of the images. This is the recommended split, but you can adjust it according to your needs.

Before running a Python script to split your dataset, ensure you have the necessary directory structure:

```bash
project-1-at-2023-12-10-11-21-cc95541c
├─ images
└─ labels
```

```python
import os
import shutil
import random

# Set the seed for reproducibility

random.seed(42)

# Paths

base_path = 'project-1-at-2023-12-10-11-21-cc95541c'
images_path = os.path.join(base_path, 'images')
labels_path = os.path.join(base_path, 'labels')

# Split Ratios

train_ratio = 0.70
val_ratio = 0.15
test_ratio = 0.15

# Create directories for train, val, and test sets

for set_type in ['train', 'val', 'test']:
for content_type in ['images', 'labels']:
os.makedirs(os.path.join(base_path, set_type, content_type), exist_ok=True)

# Get all image filenames

all_files = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]
random.shuffle(all_files)

# Calculate split indices

total_files = len(all_files)
train_end = int(train_ratio _ total_files)
val_end = train_end + int(val_ratio _ total_files)

# Split files

train_files = all_files[:train_end]
val_files = all_files[train_end:val_end]
test_files = all_files[val_end:]

# Function to copy files

def copy_files(files, set_type):
for file in files: # Copy image
shutil.copy(os.path.join(images_path, file), os.path.join(base_path, set_type, 'images')) # Copy corresponding label
label_file = file.rsplit('.', 1)[0] + '.txt'
shutil.copy(os.path.join(labels_path, label_file), os.path.join(base_path, set_type, 'labels'))

# Copy files to respective directories

copy_files(train_files, 'train')
copy_files(val_files, 'val')
copy_files(test_files, 'test')

print("Dataset successfully split into train, val, and test sets.")

```

Make sure to adjust the base_path to the correct path where your project-1-at-2023-12-10-11-21-cc95541c folder is located.

**How to Run the Script**

1. Save the script as a .py file, e.g., `split_dataset.py`.
2. Run the script using Python from your command line or terminal.
3. The script will create train, val, and test folders with images and labels subdirectories, and distribute your dataset accordingly.


## 2. Training YOLOv8 on Custom Dataset


### Create a Data Configuration File

Create a YAML file (e.g., `data.yaml`) with the following content:

```yaml
train: ./project-1-at-2023-12-10-11-21-cc95541c/images # Training images path
val: ./path-to-validation-set # Validation images path

nc: <number_of_classes> # Number of classes
names: ['class1', 'class2', ...] # Class names
```
Replace <number_of_classes> with the actual number of classes and ['class1', 'class2', ...] with your class names.

Example:

```yaml
train: ./project-1-at-2023-12-10-11-21-cc95541c/train/images # Path to training images
val: ./project-1-at-2023-12-10-11-21-cc95541c/val/images # Path to validation images
test: ./project-1-at-2023-12-10-11-21-cc95541c/test/images # Path to test images (optional)

nc: 7 # Number of classes
names:

- Car
- Closed Glass Door
- Dog
- Metal Roofing
- Open Glass Door
- Person
- Semi Truck

```

Make sure to adjust the paths to your train and val sets accordingly.

### Configure Training Parameters

Create a YAML file (e.g., `train.yaml`) with the following content:

```yaml
batch: 16 # Batch size
epochs: 100 # Number of epochs
weights: yolov5s.pt # Pretrained weights
img-size: 640 # Image size
```

### Train the Model

Run the following script to train the model using Python:

```python
from ultralytics import YOLO

# Load a new or pre-trained model

model = YOLO('path/to/model.yaml') # For a new model

# model = YOLO('path/to/pretrained_model.pt') # For a pre-trained model

# Train the model

model.train(
data='path/to/dataset.yaml',
epochs=100,
imgsz=640,
device='cuda', # or 'cpu', or a list of devices like [0, 1]
batch_size=16
)
```

Make sure to adjust the paths to your data.yaml file and the number of epochs accordingly.





