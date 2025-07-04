# CV and Drones 101 – Python Demo Code

This repository accompanies the **“CV and Drones 101”** workshop (Electrical Engineering Association,  
IIT Kanpur, Dec ’23 – Jan ’24).  
It contains **self‑contained Python scripts** that recreate each hands‑on activity covered:

| File | Topic |
|------|-------|
| `color_space_demo.py` | Color‑space conversions & pixel‑intensity transforms |
| `numpy_ops_demo.py` | NumPy indexing, slicing, flattening, appending, concatenation |
| `draw_shapes.py` | Array‑based rendering of lines & circles with OpenCV |
| `reversed_video.py` | Reverse a video (frame order) with OpenCV |
| `analog_clock.py` | Real‑time analog clock drawn purely from NumPy arrays |
| `bresenham_line.py` | Bresenham Line‑Drawing Algorithm (Line 4 & Line 8 variants) |
| `tello_pid_control.py` | Feedback‑based (PID) control loop for a DJI Tello drone |

> **Prerequisites**  
> ```bash
> pip install opencv-python numpy djitellopy
> ```
> `djitellopy` requires the drone and host to be on the same Wi‑Fi network.

Run any script with:

```bash
python <script_name.py>
```

Feel free to adapt these snippets for assignments or further exploration.