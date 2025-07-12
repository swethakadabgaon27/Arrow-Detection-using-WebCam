import cv2
import numpy as np
import math

class Smoother:
    def __init__(self, size):
        self.size = size
        self.values = []

    def add(self, value):
        self.values.append(value)
        if len(self.values) > self.size:
            self.values.pop(0)
        return np.mean(self.values, axis=0) if len(self.values) > 0 else value

def find_arrowhead_and_center(contour):
    moments = cv2.moments(contour)
    if moments['m00'] == 0:
        return None, None
    center = (int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00']))
    extreme_points = [tuple(point[0]) for point in contour]
    farthest_point = max(extreme_points, key=lambda p: np.linalg.norm(np.array(p) - np.array(center)))
    return farthest_point, center

def get_orientation(center, arrowhead):
    dx, dy = np.array(arrowhead) - np.array(center)
    if abs(dx) > abs(dy):
        return 'RIGHT' if dx > 0 else 'LEFT'
    return 'UP' if dy < 0 else 'DOWN'

def process_frame(frame, smoother_center, smoother_arrowhead):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(cv2.GaussianBlur(gray, (5, 5), 0), 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    white_background = np.ones_like(frame) * 255
    text_y = 30
    text_padding = 30

    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue

        arrowhead, center = find_arrowhead_and_center(contour)
        if arrowhead is None or center is None:
            continue

        smoothed_center = smoother_center.add(center)
        smoothed_arrowhead = smoother_arrowhead.add(arrowhead)

        orientation = get_orientation(smoothed_center, smoothed_arrowhead)
        dx, dy = np.array(smoothed_center) - np.array(smoothed_arrowhead)
        angle = -math.degrees(math.atan2(dy, dx))

        cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
        cv2.circle(frame, tuple(map(int, smoothed_center)), 5, (0, 0, 255), -1)
        cv2.circle(frame, tuple(map(int, smoothed_arrowhead)), 5, (255, 0, 0), -1)

        cv2.drawContours(white_background, [contour], -1, (0, 255, 0), 2)
        cv2.circle(white_background, tuple(map(int, smoothed_center)), 5, (0, 0, 255), -1)
        cv2.circle(white_background, tuple(map(int, smoothed_arrowhead)), 5, (255, 0, 0), -1)

        angle_text = f'Angle: {angle:.2f} degrees'
        orientation_text = f'Orientation: {orientation}'

        cv2.putText(frame, angle_text, (10, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(frame, orientation_text, (10, text_y + text_padding), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        text_y += text_padding * 2
        if text_y > frame.shape[0] - 50:
            text_y = 30

    return frame, white_background

def divide_arrows_from_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    smoother_center = Smoother(size=5)
    smoother_arrowhead = Smoother(size=5)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame, arrows_frame = process_frame(frame, smoother_center, smoother_arrowhead)

        cv2.imshow('Processed Frame', processed_frame)
        cv2.imshow('White Background with Arrows', arrows_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the application
divide_arrows_from_webcam()
