# Fastapi uvicorn run command

## uvicorn run command
```bash
uvicorn main:app --host 0.0.0.0 --port 1020 --reload
```
</br>

## uvicorn run command with nohup
```bash
rm -rf __public_logs__ log_dir && mkdir __public_logs__ && nohup uvicorn main:app --host 0.0.0.0 --port 8000 --reload >> __public_logs__/out 2>> __public_logs__/error & echo $! > task_id.txt
```
</br>

## uvicorn python commands
```bash
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info",reload=True)
```
```bash
python -u main.py
```
</br>

## Product ready server setup [fastapi-nginx-gunicorn](https://dylancastillo.co/fastapi-nginx-gunicorn/)
