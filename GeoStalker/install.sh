#!/bin/bash
echo "[*] Installing GeoStalker..."
sudo apt update && sudo apt install tor python3-pip libatlas-base-dev -y

echo "[*] Installing Python requirements..."
pip3 install -r requirements.txt

echo "[*] Cloning Sherlock (for optional use)..."
git clone https://github.com/sherlock-project/sherlock.git || true
cd sherlock && pip3 install -r requirements.txt && cd ..

echo "[*] Setup complete."