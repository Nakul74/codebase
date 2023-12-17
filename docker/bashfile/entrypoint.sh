#!/bin/bash
if [ "$1" == "celery" ]; then
    exec celery -A translation_app worker --loglevel=info
else
    mkdir -p log_dir/
    nohup celery -A translation_app worker --loglevel=info >> log_dir/out 2>> log_dir/error &
    python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
fi