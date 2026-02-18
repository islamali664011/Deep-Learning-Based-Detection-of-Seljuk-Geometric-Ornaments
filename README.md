## Seljuk Geometric Pattern Detection

Deep Learning–Based Detection of Seljuk Geometric Ornaments in Iran and Anatolia

## Project Overview
1- This project presents a deep learning framework for the automatic detection and localization of Seljuk geometric ornaments in architectural images from Iran and Anatolia.
By leveraging YOLOv8 object detection architecture, the system accurately identifies whether an image contains Seljuk-style geometric patterns and precisely localizes them using bounding boxes.


2-  The project is designed as a research-oriented pipeline, contributing to the digital documentation and computational analysis of Islamic architectural heritage.


## Key Contributions
- Automated documentation of Seljuk architectural ornaments

- AI-assisted Islamic architectural analysis

- Intelligent geometric pattern classification

- Digital preservation of architectural heritage


## Objectives
Construct a custom annotated dataset of Seljuk geometric ornaments.


Train a high-performance YOLOv8 detection model.


Detect and localize Seljuk geometric patterns in real architectural images.


Provide a fully reproducible deep learning pipeline from raw data to inference.


## Dataset Description
The dataset consists of architectural images collected from historical Seljuk monuments across:
Iran
Anatolia (Turkey)
Each image is carefully manually annotated following the YOLO object detection format.

## class
0_ seljuk_shape


## Dataset Structure
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


## Model Architecture

Framework: YOLOv8 (Ultralytics)


Backbone: CSPDarknet


Neck: PAN-FPN


Input Resolution: 640 × 640


This architecture enables high-accuracy detection with real-time performance.


## Installation 
pip install ultralytics


## Training Pipeline
  ## Step 1 — Dataset Preparation


python scripts/01_prepare_dataset.py


## Step 2 — Dataset Splitting


python scripts/02_split_dataset.py


##  Step 3 — Model Training
python scripts/03_train_model.py

## Inference (Model Testing)

python scripts/04_inference.py --image path/to/image.jpg


## Experimental Results

The accuracy model is 40 % 
That because, It is a Baseline Model, It is dependent on 700 images 


## Architectural Applications

- Islamic geometric ornament classification
- Seljuk architectural heritage documentation
- AI-driven archaeological analysis
- Automated geometric feature extraction

 ## Author
 - Islam Ali Muhammed Muhammed
 - 
## Architect & AI Specialist


## Research interests include:

- Islamic architectural heritage
  
- Computer vision for archaeology

- Deep learning and cultural heritage AI
