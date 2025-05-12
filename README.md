# Face-Detection

A simple OpenCV-powered toolkit to capture images, detect faces in real time, and visualize datasets for facial recognition projects.

## Features

* Capture face images directly from your webcam
* Real-time face detection with OpenCV
* Organize images into datasets for training or testing
* Visualize datasets and detected faces easily

## Project Structure

```
.
├── capture_images.py     # Capture images of a person and save to dataset
├── face_from_camera.py   # Real-time face detection using webcam
├── train_model.py        # Visualize and verify dataset images with face detection
└── dataset/              # Saved images organized by person
```

## Requirements

* Python 3.x
* OpenCV

Install dependencies:

```bash
pip install opencv-python
```

## Usage

### 1. Capture Images

Run to collect images of a person:

```bash
python capture_images.py
```

> **Important:** Edit the `person_name` variable inside `capture_images.py` before running to set the folder name.

Controls:
`S` – Save current frame
`Q` – Quit

### 2️. Detect Faces from Webcam

```bash
python face_from_camera.py
```

Press `Q` to quit.

### 3️. Visualize Dataset

```bash
python train_model.py
```

Displays all saved images with face detection bounding boxes. Useful to verify dataset quality.

## Notes

* All captured images are saved under `dataset/{person_name}`.
* Make sure to use clear, front-facing images for best face detection accuracy.
