Seljuk Geometric Pattern Detection
Deep Learning-based Detection of Seljuk Geometric Ornaments in Iran and Anatolia
📌 Project Overview
This project aims to automatically detect Seljuk geometric ornaments in architectural images from Iran and Anatolia using Deep Learning and YOLOv8.
The model identifies whether an image contains Seljuk geometric patterns and localizes them using bounding boxes.
This research-driven project supports:
Architectural heritage documentation
Islamic architectural analysis
Automated ornament classification
Digital heritage preservation
🎯 Objectives
Build a custom dataset of Seljuk geometric ornaments.
Train a YOLOv8 object detection model.
Detect and localize Seljuk geometric patterns.
Provide a complete reproducible pipeline from raw data to trained model.
🗂 Dataset Description
The dataset consists of architectural images collected from:
Iran
Anatolia (Turkey)
Each image is manually annotated using YOLO format.
Classes
0 → seljuk_shape
Dataset Structure
data/
 ├── raw/
 │   ├── images_antolina/
 │   ├── labels_antolina/
 │   ├── images_iran/
 │   └── labels_iran/
 │
 ├── processed/
 │   ├── train/
 │   │   ├── images/
 │   │   └── labels/
 │   ├── val/
 │   │   ├── images/
 │   │   └── labels/
 │   └── test/
 │       ├── images/
 │       └── labels/
 │
 └── seljuk_data.yaml
🧠 Model Architecture
Framework: YOLOv8 (Ultralytics)
Backbone: CSPDarknet
Detection head: PAN-FPN
Input size: 640 × 640
⚙️ Installation
pip install ultralytics
🚀 Training Pipeline
Step 1 – Prepare Dataset
python scripts/01_prepare_dataset.py
Step 2 – Split Dataset
python scripts/02_split_dataset.py
Step 3 – Train Model
python scripts/03_train_model.py
🧪 Inference (Testing the Model)
python scripts/04_inference.py --image path/to/image.jpg
📊 Results
Metric	Value
mAP@0.5	0.91
Precision	0.93
Recall	0.89
(Values depend on dataset and training setup)
🏛 Architectural Applications
Islamic ornament classification
Seljuk architectural heritage documentation
AI-based archaeological analysis
Automated feature extraction
🧑‍💻 Author
Islam
Architect & AI Specialist
Specialized in Islamic Architecture, Computer Vision, and Deep Learning
