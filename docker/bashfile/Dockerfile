FROM python:3.10.6

RUN apt-get update && apt-get upgrade -y && apt-get clean
RUN apt-get install sudo -y

RUN apt update && apt upgrade -y && apt clean
RUN apt install lsof

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x entrypoint.sh

ENTRYPOINT ["bash","entrypoint.sh"]