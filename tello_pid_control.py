"""Simple PID‑based altitude hold for DJI Tello using djitellopy.

**Make sure:**
  * Laptop & Tello are on same Wi‑Fi.
  * Run: pip install djitellopy
"""
import time
from djitellopy import Tello

class PID:
    def __init__(self, kp, ki, kd):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.prev_error = 0
        self.integral = 0

    def __call__(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt if dt > 0 else 0
        self.prev_error = error
        return self.kp*error + self.ki*self.integral + self.kd*derivative

def main(target_height_cm=120):
    drone = Tello()
    drone.connect()
    print("Battery:", drone.get_battery(), "%")

    pid = PID(0.4, 0.0, 0.2)

    drone.takeoff()
    try:
        last_time = time.time()
        while True:
            height = drone.get_height()
            error = target_height_cm - height
            now = time.time()
            dt = now - last_time
            last_time = now

            correction = pid(error, dt)
            correction = max(min(correction, 20), -20)  # clamp speed
            drone.send_rc_control(0, 0, int(correction), 0)

            print(f"Height: {height} cm | Error: {error:.1f} | Thrust: {correction:.1f}")
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        drone.send_rc_control(0, 0, 0, 0)
        drone.land()
        drone.end()

if __name__ == "__main__":
    main()