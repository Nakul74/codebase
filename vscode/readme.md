# vscode setup

## ssh config

```bash
Host aws-ec2
    HostName ec2-xx-xx-xx-xx.compute-1.amazonaws.com
    User ubuntu
    IdentityFile /home/nakul74/.ssh/ds@goglocal.pem
```
digitalocean
```bash
Host digital-ocean-droplet
    HostName xxx.xxx.xxx.xxx
    User ubuntu
    IdentityFile ~/.ssh/id_ed25519
```
</br>

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

## If you get "SSH Permission denied (publickey)" error use following steps
1. Make sure following ssh settings are applied to your local server
```bash
chmod 700 .ssh
chmod 700 .ssh/*
```
</br>
2. Make sure following ssh setting are applied to your remote server
```bash
chmod 700 .ssh
chmod 600 .ssh/authorized_keys
```
</br>

## create new user on instance [article link](https://github.com/GauriSP10/streamlit_login_auth_ui)
