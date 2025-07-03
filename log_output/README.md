# Log Output Application

A simple Python application that generates a random UUID string on startup and outputs it every 5 seconds with a timestamp.

## Build, Run, and Deploy with k3d

1. **Build the Docker image:**
   ```bash
   docker build -t log-output:latest .
   ```

2. **Create a k3d cluster:**
   ```bash
   k3d cluster create log-output-cluster
   ```

3. **Import the image into the k3d cluster:**
   ```bash
   k3d image import log-output:latest -c log-output-cluster
   ```

4. **Set kubectl context to the new cluster:**
   ```bash
   kubectl config use-context k3d-log-output-cluster
   ```

5. **Deploy the application using the manifest:**
   ```bash
   kubectl apply -f manifest/deployment.yaml
   ```

6. **Check the logs:**
   ```bash
   kubectl logs -f deployment/log-output-dep
   ```

## Expected Output

```
2020-03-30T12:15:17.705Z: 8523ecb1-c716-4cb6-a044-b9e83bb98e43
2020-03-30T12:15:22.705Z: 8523ecb1-c716-4cb6-a044-b9e83bb98e43
2020-03-30T12:15:27.705Z: 8523ecb1-c716-4cb6-a044-