# 🛰️ GeoStalker

**GeoStalker** is a tactical OSINT recon tool for Linux systems like **Kali**, **Parrot OS**, and **BlackArch**.  
It helps you map **Instagram usernames** (from public post metadata) and geolocate **IP addresses** using terminal commands and slick browser-based maps.

> 🛡️ For educational and ethical red team ops only. Respect privacy laws.

---

## ⚔️ Features

- 🔎 Scan public Instagram accounts for geotag data
- 🌍 Geolocate IP addresses with high accuracy
- 🗺️ Render data as interactive HTML maps
- 🧠 Intelligent CLI commands
- 🎯 Runs fully offline (except IP geolocation lookups)
- ☠️ “Military-grade” Python backend

---

## 🛠️ Installation

### 1. Clone the Repo

```bash
git clone https://github.com/Muhile33/Geolocator.git
cd GeoStalker
```
### 2. Make the Installer Executable
```bash
chmod +x install_geostalker.sh
```

### 3. Run the Installer
```bash
./install_geostalker.sh
```

### This will

* Create a Python virtual environment

* Install all requirements

* Symlink geostalker globally to /usr/local/bin

### 🚀 Usage
```bash
geostalker username <instagram_username>
geostalker ip <ip_address>
```

### ✅ Examples
```bash
geostalker username nasa
geostalker ip 1.1.1.1
```
📍 A browser window will open showing a map with coordinates.

### 📁 Project Structure
```pgsql
geostalker-cli/
├── geostalker             ← CLI wrapper (executable)
├── geostalkermain.py      ← Main OSINT engine (functions)
├── install_geostalker.sh  ← Setup script
├── requirements.txt
```
> The geostalker script adds its folder to sys.path so geostalkermain.py is imported <br>
> cleanly. <br>
> No module import errors anymore.

### 📛 Disclaimer
GeoStalker is intended for legal & educational purposes only.

❌ Do NOT use this to harass or track people.

✅ Use it in CTFs, pentests, recon, threat intel, bug bounty, and OSINT projects.

### Ignore 
- geolocater directory go for Geostalker
- geolocater.html

### 🧠 Author
Created by [@Muhile33] <br>
Built with 💻 Python + ☕ coffee + 📡 recon mindset. <br>
Stay stealthy. Stay smart. Stay sharp.

## 📝 License

This project is licensed under the [MIT License](CreateLICENSE).


### 💣 Final Words
> The quieter you become, the more you can hear.” <br>
> ― Tactical wisdom
