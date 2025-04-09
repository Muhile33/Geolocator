# 🛰️ GeoStalker

> Real-time OSINT recon tool for stalking... I mean **tracking** 👀  
> Instagram users, email addresses, webcams, geotags & more — built for **hunters**.

---

## ⚔️ Features

- 📸 **Instagram Recon**: Public profile scraping, bio, photos
- 🌍 **Geo-Photo Analysis**: Extracts EXIF geolocation from images
- 🧠 **Face/Scene Matching**: AI-powered vision matching with OpenCV + Torch
- 🛰️ **Webcam Tracer**: Real-time tracking via public webcams
- 🛡️ **Tor Proxy Integration**: All ops can be routed anonymously
- 📧 **Email Intelligence**: HIBP + domain scanner
- 📄 **PDF/HTML Report Generator**
- 🧪 **Planned**: Cross-platform username scan, Discord/Telegram deep scrapes

---

## ⚙️ Installation
```bash
git clone https://github.com/Muhile33/Geolocator.git
cd Geolocator
```
### 📦 Requirements

- Python 3.8+
- pip
- git

### 🔧 Setup

```bash
# Clone the repo
git https://github.com/Muhile33/Geolocator.git
cd GeoStalker
```
# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt


### 📁 Project Structure
```pgsql
GeoStalker/
├── geostalker.py        # Main CLI entry point
├── requirements.txt     # Dependencies
├── README.md            # You're here
│
├── modules/             # Core logic
│   ├── ig_lookup.py
│   ├── geo_photo.py
│   ├── webcam_trace.py
│   ├── email_recon.py
│   ├── vision_match.py
│   ├── tor_proxy.py
│   ├── report_gen.py
│   ├── utils.py
│   └── __init__.py
│
├── output/              # Reports, traces, photos
│   ├── traces/
│   ├── reports/
│   └── images/
│
├── data/                # Static data
│   ├── user_agents.txt
│   └── platforms.json

└── docs/                # Usage examples & docs
    └── usage_examples.md
```
> The geostalker script adds its folder to sys.path so geostalkermain.py is imported <br>
> cleanly. <br>
> No module import errors anymore.

### 📛 Disclaimer
GeoStalker is intended for legal & educational purposes only.

❌ Do NOT use this to harass or track people.

✅ Use it in CTFs, pentests, recon, threat intel, bug bounty, and OSINT projects.


## 🧠 Legal Notice
GeoStalker is a tool built for ethical, educational, and red-team use only. <br>
⚠️ Do not use this software to stalk, harass, or violate the privacy of others. <br>
By using this tool, you agree to use it legally and responsibly.

### 🧠 Author
Created by [@Muhile33] <br>
Built with 💻 Python + ☕ coffee + 📡 recon mindset. <br>
Stay stealthy. Stay smart. Stay sharp.

## 📝 License

This project is licensed under the [MIT License](CreateLICENSE).

Go to releases for more information


### 💣 Final Words
> The quieter you become, the more you can hear.” <br>
> ― Tactical wisdom
