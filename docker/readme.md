# Docker commands

## List images

```bash
docker images
```
</br>

## List running containers

```bash
docker ps
```
</br>

## List all containers (running + stopped)

```bash
docker ps -a
```
</br>

## Build image

```bash
docker build -t image_name .
```
</br>

## Build container (remove -d if not want to run container in detach mode)

```bash
docker run --name container_name -d -p host_port:container_port image_name
```
</br>

## Build container with volume logs map

```bash
docker run --name container_name -d -p host_port:container_port -v $(pwd)/logs:/app/logs image_name
```
</br>

## copy file from container to host

##### copy file
```bash
docker cp <containerId>:/path/to/file /path/on/host
```
##### copy directory
```bash
docker cp -r <containerId>:/path/to/directory /path/on/host
```
</br>

## copy file from host to container

##### copy file
```bash
docker cp /path/on/host <containerId>:/path/to/file 
```
##### copy directory
```bash
docker cp -r /path/on/host <containerId>:/path/to/directory 
```
</br>


## Build container with volume logs map

```bash
docker run --name container_name -d -p host_port:container_port -v $(pwd)/logs:/app/logs image_name
```
</br>

## Build container with host network

```bash
docker run --name container_name --network="host" -d -p host_port:container_port image_name
```
</br>

## Remove untagged (None) or unused images

##### Remove all unused images (including "none" tagged)
```bash
docker images -f "dangling=true" -q | xargs -r docker rmi -f
```
##### Remove only "none" tagged images
```bash
docker images -a | grep none | awk '{ print $3; }' | xargs docker rmi
```
</br>

## Remove all images

```bash
docker rmi $(docker images -q)
```
</br>

## Remove all containers

```bash
docker rm -vf $(docker ps -a -q)
```
</br>

## Save Docker images as tar

```bash
docker save -o file.tar image_name
```
</br>

## Load Docker image from .tar

```bash
docker load -i file.tar
```
</br>

## Inside Docker container

```bash
docker exec -it container_id /bin/bash
```
</br>

## Docker logs

```bash
docker logs container_id
```
</br>

## Build Docker Compose

```bash
docker compose up
```
or
```bash
rm -rf __docker_compose_logs__ && mkdir __docker_compose_logs__ && nohup docker compose up --remove-orphans --build >> __docker_compose_logs__/out 2>> __docker_compose_logs__/error & echo $! > task_id.txt
```
</br>

## Down Docker Compose

```bash
docker compose down
```
</br>

## Clean Docker cache

```bash
docker builder prune -a --filter until=24h
```

## Install docker linux [article link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04)
</br>

## Install docker compose linux [article link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-22-04)