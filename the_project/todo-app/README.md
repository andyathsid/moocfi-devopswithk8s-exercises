# Todo App

A simple todo application API built with FastAPI.

## Getting Started

### Prerequisites
- Python 3.11 or higher
- Docker

### Setup and Run

1. **Navigate to the project directory:**
   ```bash
   cd the_project/todo-app
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   ```bash
   # On Linux/macOS
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   ```bash
   # Create .env file (already exists with PORT=8000)
   # Or set environment variable manually:
   export PORT=8000
   ```

6. **Run the application:**
   ```bash
   # Option 1: Using uvicorn 
   uvicorn main:app --host 0.0.0.0 --port 8000
   
   # Option 2: Using fast api dev server
   fastapi dev main.py
   ```

### Docker Setup

1. **Build the Docker image:**
   ```bash
   docker build -t todo-app:latest .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 todo-app:latest
   ```

### API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check endpoint

The application will be available at `http://localhost:8000`