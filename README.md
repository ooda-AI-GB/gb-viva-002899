# Daily List Web Application

A mobile-first and desktop-synced daily list application built with FastAPI and Python.

## Features

- Mobile-first interface for instant capture.
- Synced desktop view to keep your list updated.
- Minimalist daily list format.
- Health check endpoint at `/health`.

## Setup Instructions

### Prerequisites

- Python 3.11+
- pip
- Docker (optional, for containerized deployment)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Locally

```bash
python main.py
```

The application will be available at `http://0.0.0.0:8000`.

### 3. Run with Docker

1. Build the Docker image:

```bash
docker build -t daily-list-app .
```

2. Run the Docker container:

```bash
docker run -p 8000:8000 daily-list-app
```

The application will be available at `http://localhost:8000`.

## API Endpoints

- `GET /`: The main application page for viewing and adding tasks.
- `POST /add_task`: Endpoint to add a new task.
- `GET /health`: Health check endpoint. Returns "OK" if the application is running.
