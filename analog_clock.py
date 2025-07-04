"""Draw a live analog clock using only NumPy & OpenCV."""
import cv2
import numpy as np
import math
import datetime

size = 400
center = size // 2
radius = size // 2 - 20

while True:
    canvas = np.ones((size, size, 3), dtype=np.uint8) * 255
    now = datetime.datetime.now()
    # Draw clock circle
    cv2.circle(canvas, (center, center), radius, (0, 0, 0), 2)

    # Markers
    for i in range(12):
        angle = i * math.pi / 6
        x1 = int(center + (radius - 10) * math.cos(angle - math.pi/2))
        y1 = int(center + (radius - 10) * math.sin(angle - math.pi/2))
        x2 = int(center + radius * math.cos(angle - math.pi/2))
        y2 = int(center + radius * math.sin(angle - math.pi/2))
        cv2.line(canvas, (x1, y1), (x2, y2), (0, 0, 0), 2)

    # Hands
    sec_angle = (now.second / 60) * 2 * math.pi
    min_angle = (now.minute / 60) * 2 * math.pi + sec_angle/60
    hr_angle  = ((now.hour % 12) / 12) * 2 * math.pi + min_angle/12

    def draw_hand(angle, length, thickness, color):
        x = int(center + length * math.cos(angle - math.pi/2))
        y = int(center + length * math.sin(angle - math.pi/2))
        cv2.line(canvas, (center, center), (x, y), color, thickness)

    draw_hand(hr_angle, 0.5*radius, 6, (0,0,0))
    draw_hand(min_angle, 0.8*radius, 4, (0,0,255))
    draw_hand(sec_angle, 0.9*radius, 2, (255,0,0))

    cv2.imshow("Analog Clock", canvas)
    if cv2.waitKey(1000) & 0xFF == 27:  # ESC to quit
        break

cv2.destroyAllWindows()