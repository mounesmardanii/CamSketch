# CamSketch 🎨

**CamSketch** is a simple Python project that captures an image from your webcam and transforms it into a pencil sketch using OpenCV.  
It’s a fun and practical way to learn the basics of image processing with live camera input.

---

## 🛠️ Technologies & Libraries Used

- **Python 3.x**
- **OpenCV (`cv2`)** – for webcam capture and image processing  
- **NumPy** – for array operations and image manipulation  
- **sys** – for system-level functions (optional)  
- **random** – for generating random values or filenames (optional)

```python
import cv2  
import numpy as np  
import sys  
import random
````

---

## 🎯 Features

* Capture real-time image from webcam
* Convert photo to grayscale sketch
* Instantly display or save the result
* Lightweight and easy to use
* Great for beginners in computer vision

---

## 🚀 How to Run

1. Make sure Python and the required libraries are installed:

   ```bash
   pip install opencv-python numpy
   ```

2. Run the script:

   ```bash
   python sketch_cam.py
   ```

3. Your webcam will activate and capture an image.
   The sketch version of the image will open in a pop-up window.

---

## 📂 Project Structure

```
CamSketch/
│
├── sketch_cam.py           # Main script file
├── output/                 # (Optional) folder for saved sketches
└── README.md               # Project documentation
