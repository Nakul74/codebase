# Linux commands

## create multiple nested folder or create folder only if doen't exists

```bash
mkdir -p /path/to/your/nested/folders
```
</br>

## check root file storage

```bash
df -h
```
</br>

## check size of directory

```bash
du -sh /path/to/directory
```
</br>

## check size of directory + its contents

```bash
du -ah /path/to/directory
```
</br>

## Get absolute path of a folder or file

```bash
realpath -s file_or_folder_path
```
</br>

## Get path of installed package

```bash
which google-chrome
```
</br>

## Get version of installed package

```bash
google-chrome --version
```
</br>

## Go to your previous working directory.

```bash
cd -
```
</br>

## Go to your home directory.

```bash
cd ~
```
</br>

## zip folder or file

```bash
zip -r example.zip folder_path
```
</br>

## unzip folder or file

```bash
unzip example.zip -d /path/to/destination
```
</br>

## pypi grep

```bash
pip list | grep langchain
```
</br>

## scp from ec2 to local

```bash
scp -i ~/.ssh/id_ed25519 -r nakul@ec2-xx-xx-xx-xx.compute-1.amazonaws.com:/home/nakul/projects.zip /home/nakul74/Desktop/scrapper/ec2/projects/.
```
</br>

## scp from local to ec2

```bash
scp -i ~/.ssh/id_ed25519 -r /home/nakul74/Desktop/scrapper/ec2/projects/projects.zip nakul@ec2-xx-xx-xx-xx.compute-1.amazonaws.com:/home/nakul/.
```
</br>


## change owner and group of folder and its subfolders recursively

```bash
sudo chown -R new_owner:new_group folder_name
```
</br>

## nohup command examples

```bash
rm -rf __public_logs__ log_dir && mkdir __public_logs__ && nohup python -u app.py >> __public_logs__/out 2>> __public_logs__/error & echo $! > task_id.txt
```
</br>

## kill nohup process

```bash
kill -9 nohup_process_id
```
or
```bash
kill -9 `cat task_id.txt`
```
</br>

## Get used port details

```bash
sudo netstat -ltup | grep 8111
```
or
```bash
sudo netstat -nlp | grep :8111
```
</br>

## Get host ip address

```bash
curl icanhazip.com
```
</br>

## kill port

```bash
sudo kill -9 $(lsof -i:8000 -t)
```
</br>

## Open crontab file

```bash
sudo crontab -e
```
</br>

## Command to run bash file every hour

```bash
0 * * * * sudo bash /home/nakul74/Desktop/templates/linux/cronjob/cron_script.sh
```
</br>

## Command to run python file every hour

```bash
0 * * * * /home/nakul/projects/envs/scrapper_env/bin/python -u /path/to/app.py >> /path/to/logfile.log 2>&1
```
or
```bash
0 * * * * cd /home/nakul/projects/cronjob_email && conda ../envs/ && python -u app.py >> logs.txt 2>&1
```
</br>


## Linux instance create new user and ssh [aws article link](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-users.html) or [website article link](https://phoenixnap.com/kb/add-user-to-linux-group)

## ssh and scp [aws article link](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-ssh.html)


## create user for ssh
```bash
sudo adduser new_user 
```
or
```bash
sudo adduser new_user --disabled-password
```
```bash
sudo usermod -aG sudo new_user
```
```bash
sudo su - new_user
```
```bash
mkdir .ssh
```
```bash
chmod 700 .ssh
```
```bash
echo "ssh-pub-key" > .ssh/authorized_keys
```
```bash
chmod 600 .ssh/authorized_keys
```
</br>