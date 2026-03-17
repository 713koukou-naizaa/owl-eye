from dotenv import load_dotenv
from pathlib import Path
import os
import yaml

load_dotenv()

ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT / "config"

def load_yaml(name: str) -> dict:
    with open(CONFIG_DIR / name, "r") as f:
        return yaml.safe_load(f)

paths_cfg = load_yaml("paths.yaml")
devices_cfg = load_yaml("devices.yaml")
intervals_cfg = load_yaml("intervals.yaml")

CAPTURE_INTERVAL = intervals_cfg["intervals"]["capture_interval"]
AUDIO_DURATION = intervals_cfg["intervals"]["audio_duration"]

EMAIL_RECIPIENT = os.environ["EMAIL_RECIPIENT"]
EMAIL_SENDER = os.environ["EMAIL_SENDER"]
SMTP_SERVER = os.environ["SMTP_SERVER"]
SMTP_PORT = int(os.environ["SMTP_PORT"])
SMTP_USERNAME = os.environ["SMTP_USERNAME"]
SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]

TEMP_DIR = paths_cfg["paths"]["temp_dir"]
LOG_FILE = paths_cfg["paths"]["log_file"]

WEBCAM_DEVICE = devices_cfg["devices"]["webcam_device"]
AUDIO_DEVICE_INDEX = devices_cfg["devices"]["audio_device_index"]
