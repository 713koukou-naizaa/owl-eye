import logging
import os
from config.config import settings

def setup_logger():
    if not os.path.exists(settings.LOG_FILE):
        with open(settings.LOG_FILE, 'w'): pass

    logger = logging.getLogger("owl-eye")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # File handler
    fh = logging.FileHandler(settings.LOG_FILE)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
