# 🧭 Arrow Orientation and Angle Detection using OpenCV

This project detects **arrows** in real-time using your webcam feed and analyzes their **orientation** (UP, DOWN, LEFT, RIGHT) and **angle** (in degrees). It is built using Python and OpenCV and designed for practical use in navigation, robotics, and visual input systems.

---

## 📌 Features

- Real-time arrow detection from a webcam
- Calculates:
  - **Arrow orientation** (UP/DOWN/LEFT/RIGHT)
  - **Angle in degrees**
- Annotates detected arrows on the video frame
- Shows both original and white-background visualization
- Uses **contour analysis**, **Canny edge detection**, and **image moments**

---

## 📷 Demo

<img width="374" height="297" alt="image" src="https://github.com/user-attachments/assets/1f94d15f-4dd5-41c0-bc34-79e0f0167775" />
<img width="365" height="293" alt="image" src="https://github.com/user-attachments/assets/cde16dc2-96e8-4dba-b8fd-ece3841aa8d9" />
<img width="371" height="294" alt="image" src="https://github.com/user-attachments/assets/1779f8df-8645-45a5-9cd1-dbd14b0df9ce" />
<img width="363" height="298" alt="image" src="https://github.com/user-attachments/assets/33a05056-7015-432e-bac3-63f4e4de7d10" />


## 🧠 Working Principle

### 1. **Image Preprocessing**
- **Grayscale conversion**: Simplifies image
- **Gaussian blur**: Reduces noise
- **Canny edge detection**: Detects edges

### 2. **Contour Detection**
- Finds external contours (possible arrows)
- Filters small/noisy contours

### 3. **Feature Extraction**
- **Centroid**: Calculated using image moments
- **Arrowhead**: The farthest point from the centroid

### 4. **Orientation and Angle**
- Orientation is inferred by comparing `arrowhead - center` vector
- Angle calculated using:
  ```python
  angle = -math.degrees(math.atan2(dy, dx))
