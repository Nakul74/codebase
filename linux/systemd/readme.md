# Linux systemd commands

## cd to systemd path and create file for eg."fastapi.service"

```bash
cd /etc/systemd/system/
sudo nano fastapi.service
```
</br>

## Use below template in "fastapi.service" file

```bash
[Unit]
Description=uvicorn
After=network.target

[Service]
User=nakul
WorkingDirectory=/home/nakul/projects/chatgptbot
ExecStart=/home/nakul/projects/envs/scrapper_env/bin/uvicorn main:app --host 0.0.0.0 --port 8010
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```
</br>

## start "fastapi.service" service

```bash
sudo systemctl daemon-reload
sudo systemctl enable fastapi.service
sudo systemctl start fastapi.service
```
</br>

## check "fastapi.service" status and logs

```bash
sudo systemctl status fastapi.service
sudo journalctl -u fastapi.service -f
```
</br>

## Restart "fastapi.service"

```bash
sudo systemctl restart fastapi.service
```
</br>

## systemctl commands [article link](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)