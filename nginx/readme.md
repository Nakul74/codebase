## Nginx 

#### Product ready server setup [fastapi-nginx-gunicorn](https://dylancastillo.co/fastapi-nginx-gunicorn/)

## Nginx without ssl

```bash
sudo echo "server {
    listen 8014;
    server_name $(curl icanhazip.com);
    location / {
        proxy_pass http://127.0.0.1:8015;
    }
}" > /etc/nginx/sites-enabled/fastapi_nginx
```
* Here listen is nginx port and proxy_pass is port where api is running
</br>


## Nginx with openssl

```bash
server {
    listen 80;
    listen 443 ssl;
    ssl on;
    ssl_certificate /etc/nginx/ssl/server.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;
    server_name 18.116.199.161;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```
* [blog link](https://lcalcagni.medium.com/deploy-your-fastapi-to-aws-ec2-using-nginx-aa8aa0d85ec7)
</br>

#### nginx alternative [caddy2](https://stribny.name/blog/caddy-config/)

#### Gunicorn + Nginx + SSL [article link](https://dev.to/chand1012/how-to-host-a-flask-server-with-gunicorn-and-https-942)

#### Fastsapi + Nginx + SSL + ec2 [article link](https://lcalcagni.medium.com/deploy-your-fastapi-to-aws-ec2-using-nginx-aa8aa0d85ec7)