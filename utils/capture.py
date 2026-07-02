import os
import cv2
import sounddevice as sd
import soundfile as sf
from datetime import datetime
from config.config import settings

os.makedirs(settings.TEMP_DIR, exist_ok=True)

def timestamped_filename(prefix, ext):
    return os.path.join(settings.TEMP_DIR, f"{prefix}-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.{ext}")

def take_photo():
    cap = cv2.VideoCapture(settings.WEBCAM_DEVICE, cv2.CAP_V4L2)
    ret, frame = cap.read()
    if ret:
        filename = timestamped_filename("photo", "jpg")
        cv2.imwrite(filename, frame)
        cap.release()
        return filename
    cap.release()
    return None

def record_audio(duration=settings.AUDIO_DURATION):
    filename = timestamped_filename("audio", "wav")
    try:
        recording = sd.rec(int(duration * 44100), samplerate=44100, channels=2, device=settings.AUDIO_DEVICE_INDEX)
        sd.wait()
        sf.write(filename, recording, 44100)
        return filename
    except Exception:
        return None
