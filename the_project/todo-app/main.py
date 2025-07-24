import os
from datetime import datetime, UTC
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.responses import HTMLResponse

import uvicorn

load_dotenv()

app = FastAPI(
    title="Todo App API",
    description="A simple todo application API",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now(UTC).isoformat(),
        "service": "todo-app"
    }

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <!DOCTYPE html>
    <html>
      <head>
        <title>Todo App</title>
      </head>
      <body>
        <h1>Welcome to the Todo App!</h1>
        <p>The API is running.</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
