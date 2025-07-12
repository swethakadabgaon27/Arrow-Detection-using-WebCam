# 🧭 Arrow Orientation and Angle Detection using OpenCV

This project uses a webcam feed to **detect arrows in real-time** and analyze their:
- **Orientation** (UP, DOWN, LEFT, RIGHT)
- **Angle** (in degrees from the horizontal)

Built with **Python** and **OpenCV**, this system can assist in applications such as:
- Robotics navigation
- Visual indicators for automation
- Interactive computer vision systems
- STEM and image processing education

---

## 📌 Features (Detailed)

- ✅ **Live Webcam Arrow Detection**: Continuously monitors frames for arrow-like shapes.
- ✅ **Arrow Orientation Detection**: Identifies whether the arrow points **UP**, **DOWN**, **LEFT**, or **RIGHT** using geometric analysis.
- ✅ **Angle Calculation**: Computes the angle (in degrees) between the arrowhead and centroid, useful for fine-grained navigation or alignment.
- ✅ **Visual Annotation**: 
  - Detected arrows are outlined on the frame.
  - Arrowhead and center are marked with color-coded circles.
  - Angle and orientation labels are overlaid for real-time feedback.
- ✅ **Dual Frame Display**:
  - **Original Frame** with annotations
  - **White Background View** with only the arrow for clean visualization
- ✅ **Smoothing**: Arrowhead and centroid coordinates are smoothed using a moving average for stable angle readings.
- ✅ **Techniques Used**:
  - Canny edge detection
  - Contour analysis
  - Image moments
  - Vector math (Euclidean distance & angle calculation)

---

## 🧠 Working Principle (Step-by-Step)

### 1️⃣ Image Preprocessing
- **Grayscale Conversion**  
  - Converts the webcam image from color to grayscale using `cv2.cvtColor()`  
  - Removes color noise and simplifies processing
  
- **Gaussian Blur**  
  - Applies blur using `cv2.GaussianBlur()` to reduce high-frequency noise  
  - Helps improve edge clarity

- **Canny Edge Detection**  
  - Detects edges using `cv2.Canny()`  
  - Highlights arrow boundaries for contour detection

---

### 2️⃣ Contour Detection
- Uses `cv2.findContours()` to detect shapes in the edge-detected image
- Filters out small contours with area `< 1000` to ignore noise
- Keeps large shapes likely to be arrows

---

### 3️⃣ Feature Extraction

- **Centroid Calculation**  
  - Uses image moments: `cv2.moments()`  
  - Centroid = geometric center of contour (i.e., the arrow body)

- **Arrowhead Detection**  
  - Finds the **farthest point** from the centroid using:
    ```python
    np.linalg.norm(np.array(p) - np.array(center))
    ```
  - This point is assumed to be the arrowhead (the tip)

---

### 4️⃣ Orientation & Angle Analysis

- **Orientation Detection**
  - Compares the direction of the arrowhead relative to the centroid
  - Logic:
    ```python
    dx, dy = arrowhead - center
    if abs(dx) > abs(dy):
        direction = 'RIGHT' if dx > 0 else 'LEFT'
    else:
        direction = 'UP' if dy < 0 else 'DOWN'
    ```

- **Angle Calculation**
  - Measures the angle between the arrowhead-center line and horizontal axis:
    ```python
    angle = -math.degrees(math.atan2(dy, dx))
    ```
  - Produces angle in range `[-180°, 180°)`

---


## 📷 Demo

<img width="374" height="297" alt="image" src="https://github.com/user-attachments/assets/1f94d15f-4dd5-41c0-bc34-79e0f0167775" />
<img width="365" height="293" alt="image" src="https://github.com/user-attachments/assets/cde16dc2-96e8-4dba-b8fd-ece3841aa8d9" />
<img width="371" height="294" alt="image" src="https://github.com/user-attachments/assets/1779f8df-8645-45a5-9cd1-dbd14b0df9ce" />
<img width="363" height="298" alt="image" src="https://github.com/user-attachments/assets/33a05056-7015-432e-bac3-63f4e4de7d10" />
