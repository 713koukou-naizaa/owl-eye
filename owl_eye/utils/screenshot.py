import subprocess
import os
from datetime import datetime
from owl_eye.config.config import TEMP_DIR

def timestamped_filename(prefix, ext):
    return os.path.join(TEMP_DIR, f"{prefix}-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.{ext}")

def take_screenshot():
    filename = os.path.join(TEMP_DIR, f"screenshot-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.png")
    try:
        subprocess.run(["flameshot", "full", "-p", filename], check=True)
        return filename
    except Exception:
        return None
