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

### Simple App

Build local image and run it 
```bash
docker build . -t app
docker run -p 8080:8080 app
```

Build local image, tag it with registry and version, and push it
```bash
docker build . -t app
docker tag app mankings/app:v1
docker push mankings/app:v1
```

### Persistence

```bash
docker build . -t persistence
docker run -p 8080:8080 -v "$(pwd)"/www:/app/www persistence
docker run -p 8080:8080 --mount type=bind,source="$(pwd)"/www,target=/app/www persistence # use a bind mount instead of a volume
```

### Compose

```bash
docker compose up
```

### Config

```bash
docker compose up
```

### Secrets

```bash
docker compose up
```

## Cheat Sheet

Remove all unused images, volumes and networks

```
docker system prune --all
```

## References

1. [Docker Docs](https://docs.docker.com/)
2. [Docker Compose Section](https://docs.docker.com/compose/)
3. Lab Docker do Prof. João Paulo Barraca