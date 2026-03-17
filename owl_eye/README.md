# OwlEye

## Overview
**OwlEye** is a Python-based monitoring tool that automatically takes webcam photos and screenshots at regular intervals. It also collects system info such as IP address, MAC address, WiFi SSID, and geolocation, and sends this data via email. Designed to run in the background, it can help secure your device or log activity for legitimate purposes.

## Features
- Webcam photo capture every 15 seconds.
- Screenshot capture every 15 seconds.
- Collects IP, MAC, WiFi SSID, and geolocation.
- Sends captured data and attachments via email.
- Clean logging and temporary file management.

## File Architecture

```
owl_eye/
├── README.md                 # This file
├── main.py                   # Main application entry point and control loop
├── logger.py                 # Logging configuration and setup
├── requirements.txt          # Python dependencies
├── config/                   # Configuration files and settings
│   ├── config.py            # Main configuration loader and environment variables
│   ├── devices.yaml         # Device settings (webcam, audio)
│   ├── intervals.yaml       # Timing configurations
│   └── paths.yaml           # File path configurations
├── utils/                    # Utility modules
│   ├── capture.py           # Webcam photo and audio recording
│   ├── screenshot.py        # Screen capture functionality
│   ├── system_info.py       # System information collection
│   └── mailer.py            # Email sending functionality
└── systemd/                  # System service configuration
    └── auto-recorder.service
```

### Key Components

- **main.py**: Orchestrates the entire monitoring process, handles signals, and manages the main execution loop
- **config/**: Centralized configuration management using YAML files and environment variables
- **utils/**: Modular utilities for different capture and communication functions
- **logger.py**: Provides consistent logging across the application

## Application Workflow

1. **Initialization**
   - Load configuration from YAML files and environment variables
   - Set up logging system
   - Register signal handlers for graceful shutdown

2. **Main Loop** (runs continuously at configured intervals)
   - **Capture Phase**:
     - Take webcam photo using OpenCV
     - Record audio segment using sounddevice
     - Capture screen screenshot using flameshot
   
   - **Data Collection**:
     - Get external IP address via ifconfig.me
     - Retrieve geolocation data from ipinfo.io
     - Extract MAC address from network interface
     - Get current WiFi SSID
   
   - **Email Transmission**:
     - Compose email body with system information
     - Attach captured media files (photo, audio, screenshot)
     - Send email via SMTP with TLS encryption
   
   - **Cleanup**:
     - Remove temporary files after successful transmission
     - Handle errors and retry on failures

3. **Error Handling**
   - Graceful degradation when capture devices fail
   - Network timeout handling for external API calls
   - Email sending fallback and retry logic

4. **Shutdown Process**
   - Respond to SIGINT/SIGTERM signals
   - Clean up remaining temporary files
   - Log shutdown completion

## Configuration

The application uses a combination of YAML configuration files and environment variables:

- **Environment variables** (stored in `.env`): Email credentials and SMTP settings
- **YAML files**: Device settings, capture intervals, and file paths
- **Runtime behavior**: Configurable capture intervals and device selection

