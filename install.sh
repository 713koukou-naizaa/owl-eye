#!/bin/bash

# 1. Navigate to /opt and clone repository
cd /opt
sudo git clone https://github.com/713koukou-naizaa/owl-eye

# 2. Change ownership to user to avoid using sudo inside project
sudo chown -R $USER:$USER /opt/owl-eye
cd owl-eye

# 3. Create .env file from example
cp .env.example .env

# 4. Open .env file to add credentials
# Required manual step.
echo "Please edit the .env file and fill in your credentials"
nano .env

# 5. Create Python virtual environment as user
python3 -m venv .venv

# 6. Activate virtual environment, install dependencies and deactivate
source .venv/bin/activate
pip install -r requirements.txt
deactivate

# 7. Set up systemd user service
# Create user systemd directory if doesn't exist
mkdir -p ~/.config/systemd/user/

# Copy service file to correct location
cp systemd/owl-eye.target.example ~/.config/systemd/user/owl-eye.target

# 8. Reload systemd for user, and enable service to start on login
systemctl --user daemon-reload
systemctl --user enable owl-eye.target

echo "Installation complete! The Owl-Eye service will start the next time you log in."
echo "You can start it manually for the current session with: systemctl --user start owl-eye.target"
