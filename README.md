# 🎞️ Video Encoder App

A containerized microservice-based video processing application built with FastAPI, Celery, and FFmpeg. This app allows users to upload videos, which are then automatically encoded in the background using asynchronous task queues.

---

## 🚀 Features

- 📁 Upload and store video files via API
- 🧵 Asynchronous processing using Celery
- 🎬 Video encoding via FFmpeg
- 🧠 Background task management with Redis
- 🗃️ PostgreSQL support (future-ready)
- 🐳 Fully containerized with Docker and Docker Compose
- 🔒 CVE scanning and image hardening with Docker Scout

---

## 🧰 Tech Stack

| Component     | Technology         |
|---------------|--------------------|
| Web API       | FastAPI            |
| Task Queue    | Celery             |
| Message Broker| Redis              |
| Video Encoding| FFmpeg             |
| Database      | PostgreSQL         |
| Containerization | Docker, Docker Compose |

---

## 📂 Project Structure

video-encoder-app/
│
├── app/
│ ├── main.py # FastAPI app
│ ├── tasks.py # Celery task definitions
│ ├── utils.py # FFmpeg encoding logic
│ └── uploads/ # Uploaded and encoded video files
│
├── worker/
│ └── worker.py # Celery worker entry point
│
├── Dockerfile # Base image for both services
├── docker-compose.yml # Multi-service orchestration
└── requirements.txt # Python dependencies

---

## How to run Locally 

# Step 1: Clone the repository
git clone https://github.com/SwarajWadkar/video-encoder-app.git


cd video-encoder-app

# Step 2: Build and start services
docker-compose up --build

# Step 3: Upload a video via CURL 
curl -F "file=@/path/to/your/video.mp4" http://localhost:8000/upload

---

## Docker Images (Published)

| Service | Docker Image                        |
| ------- | ----------------------------------- |
| Web API | `swarajwadkar/video-encoder-web`    |
| Worker  | `swarajwadkar/video-encoder-worker` |


---

## Use Docker Scout to scan for vulnerabilities:

docker scout cves swarajwadkar/video-encoder-worker

---



