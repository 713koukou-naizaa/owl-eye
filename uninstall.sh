#!/bin/bash

echo "Starting the uninstallation of Owl-Eye..."

# 1. Stop systemd user service if running
echo "--> Stopping the Owl-Eye service..."
systemctl --user stop owl-eye.target

# 2. Disable systemd user service to prevent it from starting on boot/login
echo "--> Disabling the Owl-Eye service..."
systemctl --user disable owl-eye.target

# 3. Remove systemd service file from user's config directory
SERVICE_FILE=~/.config/systemd/user/owl-eye.target
if [ -f "$SERVICE_FILE" ]; then
    echo "--> Removing systemd service file: $SERVICE_FILE"
    rm -f "$SERVICE_FILE"
else
    echo "--> Systemd service file not found, skipping."
fi

# 4. Reload systemd user daemon to unregister service
echo "--> Reloading systemd user daemon..."
systemctl --user daemon-reload

# 5. Remove application directory from /opt
APP_DIR=/opt/owl-eye
if [ -d "$APP_DIR" ]; then
    echo "--> Removing application directory: $APP_DIR"
    sudo rm -rf "$APP_DIR"
else
    echo "--> Application directory not found, skipping."
fi

echo ""
echo "Owl-Eye has been successfully uninstalled."

