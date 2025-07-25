print("hi")
import pyautogui
import time
import pyautogui

# Safety: move the mouse to the top-left corner to abort.
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1  # tiny pause after each PyAutoGUI call

INTERVAL = 10          # seconds between clicks
REPEATS = 10           # how many left/right pairs to do (set to None for infinite)
POSITION = None        # (x, y) to click at; leave None to use current cursor position

print("Starting in 3 seconds... move mouse to top-left to abort.")
time.sleep(3)

def do_click(button):
    if POSITION is None:
        pyautogui.click(button=button)
    else:
        pyautogui.click(POSITION[0], POSITION[1], button=button)

try:
    i = 0
    while True:
        # Left click
        do_click('left')
        print(f"[{time.strftime('%H:%M:%S')}] Left click")
        time.sleep(INTERVAL)

        # Right click
        do_click('right')
        print(f"[{time.strftime('%H:%M:%S')}] Right click")
        time.sleep(INTERVAL)

        i += 1
        if REPEATS is not None and i >= REPEATS:
            break

    print("Done.")
except pyautogui.FailSafeException:
    print("Stopped via PyAutoGUI fail-safe (mouse to top-left).")
except KeyboardInterrupt:
    print("Stopped by user (Ctrl+C).")
import time
import pyautogui

INTERVAL = 10  # seconds

print(f"Sampling mouse position every {INTERVAL}s. Press Ctrl+C to stop.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')}  X={x}  Y={y}")
        time.sleep(INTERVAL)
except KeyboardInterrupt:
    print("\nStopped.")
import time
import pyautogui

print(f"Sampling mouse position every {INTERVAL}s. Press Ctrl+C to stop.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')}  X={x}  Y={y}")
        time.sleep(10)
except KeyboardInterrupt:
    print("\nStopped.")
import time
import pyautogui
# Interval time (in seconds)
INTERVAL = 10  

print(f"Tracking mouse position every {INTERVAL} seconds. Press Ctrl+C to stop.")

try:
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()
        print(f"Mouse Position -> X: {x}, Y: {y}")
        
        # Wait 10 seconds before the next reading
        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print("\nStopped tracking mouse position.")
