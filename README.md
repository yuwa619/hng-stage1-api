# HNG Stage 1 - Personal API

This is a backend DevOps project for HNG Stage 1. It is a minimal API built with FastAPI and Python, deployed on an AWS EC2 Amazon Linux instance. The deployment utilizes Nginx as a reverse proxy and `systemd` to ensure the application runs persistently in the background.

## Live Deployment
**Live URL:** http://98.84.182.27

## Endpoints

### 1. Root Endpoint
- **GET** `/`
- **Response:**
  ```json
  {
    "message": "API is running"
  }

### 2. Health Check
- **GET** `/health`
- **Response:**
  ```json
  {
    "message": "healthy"
  }

### 3. Personal Details
- **GET** `/me`
- **Response:**
  ```json
  {
    "name": "Your Full Name",
    "email": "you@example.com",
    "github": "[https://github.com/yourusername](https://github.com/yourusername)"
  }

## How to Run Locally

### Prerequisites
* Python 3 installed
* Git

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone [YOUR_GITHUB_REPO_LINK]
   cd hng-stage1-api

2. Create and activate a virtual environment:

3. Install the required dependencies:

4. Run the development server:

5. The API will be available at `http://127.0.0.1:8000`.
