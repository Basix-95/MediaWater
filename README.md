🌊 MediaWater

A lightweight Flask-based web application for managing and downloading media files.
MediaWater provides a clean interface to upload, view, and download project folders, with ZIP compression and in-memory streaming.

Features

Upload and organize files into project folders

Download entire folders as ZIP archives

Excludes unwanted system folders (like venv and pycache) during downloads

In-memory ZIP generation (no temporary files)

Simple and secure Flask backend

Tech Stack

Backend: Flask (Python)

Frontend: HTML + CSS (Jinja templates)

Storage: Local file system (uploads/)

Tools: zipfile, io, os

Installation & Setup

Clone the repository
git clone https://github.com/Basix-95/MediaWater.git


Note:
Currently, MediaWater works for local file transfers only (within your device or local network).
Internet and cloud-based access will be added in a future update.
