# Cricket-Shot-Detection-and-Classification-using-YOLOv8

## Project Description

This project uses YOLOv8 (You Only Look Once) for detecting and classifying cricket shots such as:

* Cover Drive
* Pull Shot
* Defensive Shot

The model is trained on a custom dataset and can perform real-time detection using webcam.

---

## Features

* Image-based detection
* Real-time webcam detection
* Fast and efficient YOLOv8 model
* Custom dataset training

---

## Technologies Used

* Python
* YOLOv8 (Ultralytics)
* OpenCV

---

##  Dataset

The dataset consists of labeled cricket images divided into:

* Train set
* Validation set

---

## How to Run

### 1. Install dependencies

```bash
pip install ultralytics
```

### 2. Train model

```bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=20 imgsz=640
```

### 3. Predict on images

```bash
yolo detect predict model=runs/detect/train/weights/best.pt source=dataset/images/train
```

### 4. Real-time detection

```bash
yolo detect predict model=runs/detect/train/weights/best.pt source=0
```

---

##  Results

* Achieved real-time detection (~40–80 ms per frame)
* High accuracy for cover drive
* Moderate accuracy for pull shot and defensive shot

---

##  Conclusion

YOLOv8 provides efficient and fast object detection. Model performance depends on dataset quality and balance.

---

## 👨‍💻 Author

Anshu Raj
