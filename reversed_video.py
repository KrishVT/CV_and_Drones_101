"""Reverse a video file by reading all frames then writing in reverse order."""
import sys
import cv2

def reverse_video(src: str, dst: str) -> None:
    cap = cv2.VideoCapture(src)
    if not cap.isOpened():
        raise FileNotFoundError(src)

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(dst, fourcc, 30, (frames[0].shape[1], frames[0].shape[0]))
    for frame in reversed(frames):
        out.write(frame)
    out.release()
    print("Saved reversed video to", dst)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python reversed_video.py <input.mp4> <output.mp4>")
        sys.exit(1)
    reverse_video(sys.argv[1], sys.argv[2])