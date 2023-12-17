#!/bin/bash
cd /home/nakul74/Desktop/templates/linux/cronjob
/home/nakul/projects/envs/scrapper_env/bin/python -u app.py >> output.log 2>&1
echo "Script execution finished at $(date)" >> status.log