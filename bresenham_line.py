"""Bresenham Line Algorithm demo (Line 4 & Line 8)."""
import cv2
import numpy as np

def bresenham(x0, y0, x1, y1):
    """Return list of points between (x0,y0) and (x1,y1) using Bresenham."""
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return points

canvas = np.ones((300, 300, 3), dtype=np.uint8) * 255
for p in bresenham(20, 20, 280, 200):
    canvas[p[1], p[0]] = (255, 0, 0)  # blue points

cv2.imshow("Bresenham Line", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()