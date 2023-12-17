from celery.result import AsyncResult
from celery import Celery
import redis
import time

celery = Celery(__name__)
celery.conf.broker_url = "redis://localhost:6379/0"
celery.conf.result_backend = "redis://localhost:6379/1"
celery.conf.result_expires = 3600

@celery.task(name="create_task")
def create_task(task_type):
    time.sleep(int(task_type) + 10)
    return {'data':int(task_type)*10}

def delete_task_data_from_redis(task_id):
    redis_host = "localhost" 
    redis_port = 6379 
    redis_db = 1  
    
    r = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
    r.delete(f"celery-task-meta-{task_id}")
    
def run_task(task_type: int):
    task = create_task.delay(int(task_type))
    return {"task_id": task.id}

def get_status(task_id: str):
    task_result = AsyncResult(task_id,app=celery)
    
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    
    if task_result.result:
        delete_task_data_from_redis(task_id)
        print('task done')
    
    return result