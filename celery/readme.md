# celery command

## Celery run command with logs in terminal

```bash
celery -A file_name worker --loglevel=info
```
</br>

## Celery run command with logs in log_dir folder
```bash
rm -rf log_dir && mkdir log_dir && celery -A file_name worker --loglevel=info --logfile=log_dir/celery.log
```
</br>

## Celery run command with nohup
```bash
rm -rf log_dir && mkdir log_dir && nohup celery -A file_name worker --loglevel=info --logfile=log_dir/celery.log >> log_dir/out 2>> log_dir/error & echo $! > task_id.txt
```
</br>

## Flower run command
```bash
celery -A file_name flower --port=5001
```
</br>

## Flower run command with nohup
```bash
rm -rf log_dir && mkdir log_dir && nohup celery -A file_name flower --port=5001 --loglevel=info --logfile=log_dir/celery.log >> log_dir/out 2>> log_dir/error & echo $! > task_id.txt
```
</br>

## Celery chain,group and chord [article link](https://sayari3.com/articles/18-chains-groups-and-chords-in-celery/)
</br>
</br>
</br>

## Install redis linux [article link](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-22-04)

## Install rabbit-mq linux [article link](https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-rabbitmq#installing-on-ubuntu-13-debian-7-based-systems)

## Important Celery Points

1. **Default Core Utilization:**
   - Celery automatically leverages all available CPU cores by default, ensuring efficient parallel processing.

2. **Data Type Considerations:**
   - When passing data to Celery functions, it's advisable to use small data types such as strings, lists, and dictionaries. Avoid using heavy objects like dataframes.
   - Tip: If you need to work with dataframes, consider uploading the data to the cloud and specify the cloud path as an input parameter to the Celery function. The function can then read the data from the cloud during execution.

3. **Avoiding `.get` Method:**
   - Avoid using the `.get` method within a Celery task function. Instead, store results in a suitable storage mechanism. Celery tasks are designed to be asynchronous and do not support synchronous operations like blocking calls to retrieve results directly.

4. **Concurrency Configuration:**
   - Adjust the number of worker processes using the `--concurrency` or `-c` option when starting the Celery worker. This value influences parallel task processing and can be set based on the available CPU cores or specific workload requirements.