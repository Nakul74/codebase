backup_folder_path=/home/nakul/projects

echo [$(date)]: "STARTING BACKUP"

echo [$(date)]: "CD into project folder"
cd $backup_folder_path
cd ..

echo [$(date)]: "Moving envs file"
mv $backup_folder_path/envs .

echo [$(date)]: "Zipping folder"
zip -r backup_$(date +"%d_%m_%Y").zip $backup_folder_path/

echo [$(date)]: "Moving envs file back"
mv ./envs $backup_folder_path/.

echo [$(date)]: "BACKUP FILE READY"