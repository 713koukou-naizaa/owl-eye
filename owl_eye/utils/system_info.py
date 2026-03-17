import requests
import subprocess

def get_ip_address():
    try:
        return requests.get("https://ifconfig.me").text.strip()
    except Exception:
        return "Unknown"

def get_geolocation():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()
        return f"{data.get('city')}, {data.get('region')}, {data.get('country')}"
    except Exception:
        return "Unknown"

def get_mac_address():
    interface = subprocess.run(["ip", "route", "show", "default"], capture_output=True, text=True).stdout.split()[4]
    try:
        result = subprocess.run(["cat", f"/sys/class/net/{interface}/address"], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception:
        return "Unknown"

def get_wifi_ssid():
    try:
        result = subprocess.run(["iwgetid", "-r"], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception:
        return "Unknown"
