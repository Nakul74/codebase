import time
from celery import Celery,chord

celery = Celery(__name__)
celery.conf.broker_url = "redis://localhost:6379/0"
celery.conf.result_backend = "redis://localhost:6379/1"
celery.conf.result_expires = 3600

def join_list(s):
    return ','.join(s)

@celery.task(ignore_result=True)
def fun3(l):
    print(join_list(l))

@celery.task
def fun2(country_list):
    country_list = [i.split('_')[0] for i in country_list]
    return country_list
    
@celery.task
def fun1(country,timeout):
    time.sleep(timeout)
    print(country)
    return country + '_' + country
    
@celery.task(ignore_result=True)
def create_task(countries,filter=True):
    timeout = len(countries)
    tasks = [fun1.s(country,timeout) for country in countries]
    if filter:
        chord(tasks)(fun2.s() | fun3.s())
    else:
        chord(tasks)(fun3.s())