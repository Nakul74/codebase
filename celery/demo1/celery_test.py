import celery_demo

countries = ['ind','aus','pak','china','japan']
celery_demo.create_task.delay(countries,filter=True)
celery_demo.create_task.delay(countries,filter=False)
