 # Todo App

A simple todo application API built with FastAPI.

## Build, Run, and Deploy with k3d

1. **Build the Docker image:**
   ```bash
   docker build -t todo-app:latest todo-app
   ```

2. **Create a k3d cluster:**
   ```bash
   k3d cluster create todo-app-cluster
   ```

3. **Import the image into the k3d cluster:**
   ```bash
   k3d image import todo-app:latest -c todo-app-cluster
   ```

4. **Set kubectl context to the new cluster:**
   ```bash
   kubectl config use-context k3d-todo-app-cluster
   ```

5. **Deploy the application using the manifest:**
   ```bash
   kubectl apply -f todo-app/manifest/deployment.yaml
   ```

6. **Check the logs:**
   ```bash
   kubectl logs -f deployment/todo-app-dep
   ```

## API Endpointss

- `GET /` - Root endpoint
- `GET /health` - Health check endpoint

The application will be available at `http://localhost:8000` (if exposed via a service).