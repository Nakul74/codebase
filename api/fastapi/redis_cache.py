import redis
import os
from dotenv import load_dotenv
load_dotenv('.env')

#Here we can change databse with db parameter for eg. db=0 or db=1 or db=2
redis_client = redis.StrictRedis(host=os.environ.get("REDIS_HOST"), port=os.environ.get("REDIS_POST"), db=0)

def get_cached_data(cache_key: str) -> str:
    return redis_client.get(cache_key)

def set_cached_data(cache_key: str, data: str, expire_time: int = 5) -> None:
    redis_client.setex(cache_key, expire_time, data)