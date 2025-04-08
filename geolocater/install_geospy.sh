#!/bin/bash

# ============================
# 🛰️ GeoStalker Elite Installer
# ============================

BANNER="
███████╗███████╗ ██████╗ ███████╗████████╗ █████╗ ██╗     ██╗  ██╗███████╗██████╗ 
██╔════╝██╔════╝██╔════╝ ██╔════╝╚══██╔══╝██╔══██╗██║     ██║ ██╔╝██╔════╝██╔══██╗
███████╗█████╗  ██║  ███╗█████╗     ██║   ███████║██║     █████╔╝ █████╗  ██████╔╝
╚════██║██╔══╝  ██║   ██║██╔══╝     ██║   ██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
███████║███████╗╚██████╔╝███████╗   ██║   ██║  ██║███████╗██║  ██╗███████╗██║  ██║
╚══════╝╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"

echo "$BANNER"
echo "🛡️ Starting GeoStalker Installation..."
echo ""

# ======================
# 1. Check for Python 3
# ======================
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install it first."
    exit 1
fi

# ======================
# 2. Check for pip
# ======================
if ! command -v pip &> /dev/null; then
    echo "❌ pip is not installed. Installing pip..."
    sudo apt install python3-pip -y || { echo "❌ Failed to install pip"; exit 1; }
fi

# ============================
# 3. Create Virtual Environment
# ============================
echo "📦 Creating virtual environment (env)..."
python3 -m venv env || { echo "❌ Failed to create virtual environment"; exit 1; }

# ============================
# 4. Activate & Install Deps
# ============================
echo "📡 Activating environment and installing dependencies..."
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt || { echo "❌ Failed to install dependencies"; exit 1; }

# ============================
# 5. Make CLI Executable
# ============================
echo "🔧 Setting CLI permissions..."
chmod +x geostalker

# ============================
# 6. Link CLI globally
# ============================
echo "🛰️ Linking CLI tool globally..."
sudo ln -sf "$(pwd)/geostalker" /usr/local/bin/geostalker

# ============================
# 7. Done!
# ============================
echo ""
echo "✅ GeoStalker deployed successfully!"
echo ""
echo "🎯 Run it like a real OSINT operator:"
echo "   geospy username <instagram_username>"
echo "   geospy ip <ip_address>"
echo ""
echo "🧪 Virtual env: To activate manually → source env/bin/activate"
echo "💣 Tool ready for Parrot, Kali, BlackArch, and beyond."

