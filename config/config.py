from dotenv import load_dotenv
from pathlib import Path
import os
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(dotenv_path=PROJECT_ROOT/".env")

class Config:
    def __init__(self):
        self.ROOT = PROJECT_ROOT
        self.CONFIG_DIR = self.ROOT / "config"

        # Load YAML configurations
        paths_cfg = self._load_yaml("paths.yaml")
        devices_cfg = self._load_yaml("devices.yaml")
        intervals_cfg = self._load_yaml("intervals.yaml")

        # Set attributes from YAML files
        self.CAPTURE_INTERVAL = intervals_cfg["intervals"]["capture_interval"]
        self.AUDIO_DURATION = intervals_cfg["intervals"]["audio_duration"]
        
        self.TEMP_DIR = self.ROOT / os.path.normpath(paths_cfg["paths"]["temp_dir"])
        self.LOG_FILE = self.ROOT / os.path.normpath(paths_cfg["paths"]["log_file"])

        self.WEBCAM_DEVICE = devices_cfg["devices"]["webcam_device"]
        self.AUDIO_DEVICE_INDEX = devices_cfg["devices"]["audio_device_index"]

        # Set attributes from environment variables with better error handling
        self.EMAIL_RECIPIENT = self._get_env_var("EMAIL_RECIPIENT")
        self.EMAIL_SENDER = self._get_env_var("EMAIL_SENDER")
        self.SMTP_SERVER = self._get_env_var("SMTP_SERVER")
        self.SMTP_PORT = int(self._get_env_var("SMTP_PORT"))
        self.SMTP_USERNAME = self._get_env_var("SMTP_USERNAME")
        self.SMTP_PASSWORD = self._get_env_var("SMTP_PASSWORD")

    def _load_yaml(self, name: str) -> dict:
        with open(self.CONFIG_DIR / name, "r") as f:
            return yaml.safe_load(f)

    def _get_env_var(self, var_name: str) -> str:
        value = os.getenv(var_name)
        if value is None:
            raise ValueError(f"Configuration error: Environment variable '{var_name}' is not set.")
        return value

settings = Config()
