#!/bin/bash
docker_compose_path=/home/nakul74/Desktop/templates/docker/docker_compose
logs_path_dir="$PWD"
bashfile_logs_dir="bashfile_logs"
fastapi_logs_dir="fastapi_logs"
selenium_logs_dir="selenium_logs"
user=nakul

echo [$(date)]: "START"

echo [$(date)]: "CD into docker compose folder path"
cd $docker_compose_path

echo "[$(date)]: Removing previous log file"
sudo rm -rf "$logs_path_dir"
sudo -u "$user" mkdir "$logs_path_dir"
sudo -u "$user" mkdir "$logs_path_dir/$bashfile_logs_dir"
sudo -u "$user" mkdir "$logs_path_dir/$fastapi_logs_dir"
sudo -u "$user" mkdir "$logs_path_dir/$selenium_logs_dir"


echo [$(date)]: "stopping already running docker compose"
if docker compose ps | grep projects; then
    echo "Stopping existing containers..."
    sudo docker compose down
    sudo docker images -a | grep projects | awk '{ print $3; }' | xargs docker rmi
    sudo rm -rf __docker_compose_logs__ 
    sudo -u $user mkdir __docker_compose_logs__ 
fi

echo [$(date)]: "starting docker compose"
sudo nohup docker compose up --remove-orphans --build >> __docker_compose_logs__/out 2>> __docker_compose_logs__/error & echo $! > task_id.txt

echo [$(date)]: "END"