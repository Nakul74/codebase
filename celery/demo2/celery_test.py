import celery_demo
import time

task_type = 2
task_id = celery_demo.run_task(task_type)
print(task_id)
r = celery_demo.get_status(task_id['task_id'])
while (not r['task_result']):
    time.sleep(3)
    r = celery_demo.get_status(task_id['task_id'])
print(r)