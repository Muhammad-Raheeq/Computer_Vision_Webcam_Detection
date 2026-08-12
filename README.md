# Real-Time Object Instance Segmentation with YOLO & OpenCV

A lightweight Python application for **real-time object instance segmentation** using your laptop's webcam. Powered by **Ultralytics YOLO** and **OpenCV**, this application detects objects, generates pixel-level segmentation masks, and displays colored boundaries with object names and confidence scores on live video.

## ✨ Features

- 🎯 **Real-Time Instance Segmentation**
  - Detects and outlines exact pixel-level boundaries of objects.
  - Provides more precise results than simple bounding boxes.

- 🏷️ **Automatic Labeling**
  - Displays detected object names.
  - Shows confidence percentages for each prediction.

- ⚡ **CPU-Friendly**
  - Uses the lightweight YOLO Nano segmentation model.
  - Designed to run on consumer laptops without requiring a dedicated GPU.

- 📷 **Live Webcam Detection**
  - Supports integrated laptop webcams.
  - Supports external USB cameras.

- 🎨 **Colored Segmentation Masks**
  - Displays colored masks over detected objects.
  - Makes individual objects easy to identify.

- 🔌 **Simple Integration**
  - Uses OpenCV for webcam capture and video rendering.
  - Uses Ultralytics YOLO for object detection and segmentation.

---

## 🧠 How It Works

The application follows this pipeline:

```text
Webcam
   ↓
OpenCV Video Capture
   ↓
YOLO Segmentation Model
   ↓
Object Detection
   ↓
Pixel-Level Segmentation Masks
   ↓
Labels + Confidence Scores
   ↓
Live Segmented Video

