#!/bin/bash
app_port=8003
project_path=/home/nakul/projects/PROD/un_comtrade_api
env_path=/home/nakul/projects/envs/selenium_scrapper/bin/activate
url_file_path=/home/nakul/projects/PROD/app_urls.txt
user=nakul

echo [$(date)]: "START"

echo [$(date)]: "CD into project folder"
cd $project_path

echo [$(date)]: "Activate ENV"
source $env_path

echo [$(date)]: "Removing previous logs"
sudo rm -rf __public_logs__/
sudo -u $user mkdir __public_logs__/

echo [$(date)]: "Killing app port ${app_port}"
sudo kill -9 $(lsof -i:${app_port} -t)

echo [$(date)]: "Starting uvicorn service"
nohup uvicorn main:app --host 0.0.0.0 --port $app_port --reload >> __public_logs__/out 2>> __public_logs__/error &

echo [$(date)]: "App started"
echo "UN-COMTRADE:http://$(curl icanhazip.com):$app_port" >> $url_file_path

echo [$(date)]: "END"