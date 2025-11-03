# 🌊 MediaWater

A lightweight **Flask-based web application** for managing and downloading media files.  
MediaWater provides a clean interface to upload, view, and download project folders,  
with ZIP compression and in-memory streaming.

> ⚠️ **Note:** Currently, MediaWater transfers files **locally only** (within your device or LAN).  
> Internet and cloud-based file sharing will be added in a future update.

---

## 🚀 Features

- 📁 Upload and organize files into project folders  
- ⬇️ Download entire folders as ZIP archives  
- 🚫 Excludes unwanted system folders (`venv`, `__pycache__`, `.git`, etc.)  
- 💾 In-memory ZIP generation — no temp files written to disk  
- 🔒 Secure and minimal Flask backend  
- 🌐 Cloud upload and sharing **coming soon**

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)  
- **Frontend:** HTML + CSS (Jinja2 templates)  
- **Storage:** Local filesystem (`uploads/`)  
- **Libraries:** `os`, `io`, `zipfile`

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Basix-95/MediaWater.git
cd MediaWater
```

### 2️⃣ Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows
```

### 3️⃣ Install dependencies
```bash
pip install flask
```

### 4️⃣ Run the Flask app
```bash
python app.py
```

Then open your browser and visit:
```
http://127.0.0.1:5000
```

## 🧠 Troubleshooting

If you encounter a `FileNotFoundError` while downloading folders:
- Ensure the folder exists inside `uploads/`
- Exclude unnecessary directories such as `venv/`
- Use the updated `download_folder()` function with missing-file handling
