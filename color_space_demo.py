Color‑space conversion & pixel‑level intensity transform demo.
Requires: opencv‑python, numpy.

Usage:
    python color_space_demo.py <image_path>
Outputs:
    * Displays original, HSV, and grayscale images.
    * Saves a brightness‑boosted copy as 'bright_<image_path>'.

import sys
import cv2
import numpy as np

def main(path: str) -> None:
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(path)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Brightness boost (value channel)
    hsv_bright = hsv.copy()
    hsv_bright[:, :, 2] = np.clip(hsv_bright[:, :, 2] * 1.3, 0, 255)
    bright = cv2.cvtColor(hsv_bright, cv2.COLOR_HSV2BGR)
    cv2.imwrite(f"bright_{os.path.basename(path)}", bright)

    cv2.imshow("Original (BGR)", img)
    cv2.imshow("HSV", hsv)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("Brightness boosted", bright)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python color_space_demo.py <image>")
        sys.exit(1)
    import os
    main(sys.argv[1])