#!/usr/bin/env bash
HOST=mongodb            # Taken from docker-compose
DB=UTA_Enrollment       # Taken from config.py
MOUNT_PATH=/mongo-setup # Taken from docker-compose

# TODO: Re-add this. Broken with registration.
# collection="user"
# json_file_path="${MOUNT_PATH}/users.json"
# echo "Setting up ${DB} db with user collection from ${json_file_path}..."
# mongoimport --host "${HOST}" \
#             --db "${DB}" \
#             --collection "${collection}" \
#             --type json \
#             --file "${json_file_path}" \
#             --jsonArray
# echo "Done setting ${collection} collection."

collection="course"
json_file_path="${MOUNT_PATH}/courses.json"
echo "Setting up ${DB} db with user collection from ${json_file_path}..."
mongoimport --host "${HOST}" \
            --db "${DB}" \
            --collection "${collection}" \
            --type json \
            --file "${json_file_path}" \
            --jsonArray
echo "Done setting ${collection} collection."
