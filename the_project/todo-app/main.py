import os
from datetime import datetime, UTC
from fastapi import FastAPI
from dotenv import load_dotenv
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

@app.get("/")
def root():
    return {"message": "Todo App API is running"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
