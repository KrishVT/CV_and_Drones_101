"""Draw basic shapes (lines, circles) on a blank canvas using OpenCV."""
import cv2
import numpy as np

canvas = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw a blue line from (50,50) to (350,50)
cv2.line(canvas, (50, 50), (350, 50), (255, 0, 0), 2)

# Draw a green circle with center (200,200) radius 100
cv2.circle(canvas, (200, 200), 100, (0, 255, 0), 2)

# Draw a red diagonal line
cv2.line(canvas, (50, 350), (350, 50), (0, 0, 255), 2)

cv2.imshow("Shapes", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()