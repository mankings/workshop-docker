# Docker 101

## Install Docker

### Docker Engine (CLI based)

1. [Docker Engine Installation Guide](https://docs.docker.com/engine/install/)  
2. [Docker Install Script](https://github.com/docker/docker-install)
3. [Docker Engine Linux Post-Install](https://docs.docker.com/engine/install/linux-postinstall/)

### Docker Desktop (GUI based)

1. [Docker Desktop Installation Guide](https://docs.docker.com/desktop/)
2. [Portainer - Alternative to Docker Desktop GUI](https://www.portainer.io/)

## Examples

### 1 - Simple App

A basic FastAPI "Hello World" app packaged into a Docker image. Learn how to write a `Dockerfile`, build an image, and run a container.

```bash
cd 1-app
```

Build the image using the `Dockerfile` and run it locally (maps port 8080 on your machine to port 8080 in the container):
```bash
docker build . -t app
docker run -p 8080:8080 app
```

Open http://localhost:8080 in your browser to see the app.

To publish the image to a registry, tag it with a registry name and version, then push:

```bash
docker tag app <your-username>/app:v1
docker push <your-username>/app:v1
```

### 2 - Persistence

Same app, but now it serves static files (HTML + images) from a `www/` folder. A **bind mount** maps a folder on your host into the container, so changes you make to the files on your machine are immediately reflected inside the container — no rebuild needed.

```bash
cd 2-persistence
```

Build and run with a bind mount (`-v` links the local `www/` directory to `/app/www` inside the container):
```bash
docker build . -t app2
docker run -p 8080:8080 -v "$(pwd)"/www:/app/www app2
```

Open http://localhost:8080, then try editing `www/index.html` on your host and refresh the page.

### 3 - Compose

Introduces **Docker Compose** to run multiple containers together. This example sets up two services: the FastAPI app and an **Nginx** reverse proxy that forwards traffic to it. Compose handles building, networking, and starting both containers with a single command.

```bash
cd 3-compose
```

Start both services (Compose builds the images automatically on the first run):
```bash
docker compose up
```

Open http://localhost:8081 — the request hits Nginx, which proxies it to the app container. Notice how Compose creates a shared network so Nginx can reach the app by its service name (`app`).
```bash
docker network ls
```

Stop and remove the container services once you're done:
```bash
docker compose down
```

### 4 - Config

Builds on the previous example by adding **environment variables** and **Docker configs**. The app reads an env var (`KEY`) and injects its value into the HTML page. Nginx is configured using a Docker `configs` object instead of a custom Dockerfile.

```bash
cd 4-config
```

Start the services:
```bash
docker compose up
```
Open http://localhost:8081 — you should see the value of `my-env-variable` (``) rendered on the page. Try changing the value in `docker-compose.yml` and restarting to see the effect.

Stop and remove the container services once you're done:
```bash
docker compose down
```

### 5 - Secrets

Adds **SSL/TLS** to the setup using **Docker secrets** to securely provide certificates to the Nginx container. Secrets are mounted as files inside the container and are never exposed in image layers or environment variables.

```bash
cd 5-secrets
```

First, generate a self-signed certificate:
```bash
sh create_cert.sh
```

Then start the services:
```bash
docker compose up
```

Open https://localhost:4431 (your browser will warn about the self-signed certificate — that's expected). HTTP still works on http://localhost:8081.

Stop and remove the container services once you're done:
```bash
docker compose down
```

## Final tip

Cleanup your Docker system, removing all dangling containers, unused images, volumes and networks

```
docker system prune --all
```

## References

1. [Docker Docs](https://docs.docker.com/)
2. [Docker Compose Section](https://docs.docker.com/compose/)
3. Lab Docker do Prof. João Paulo Barraca