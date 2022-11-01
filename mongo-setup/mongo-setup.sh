#!/usr/bin/env bash
echo "Setting up UTA_Enrollment db with user collection..."
mongoimport --host mongodb \
            --db UTA_Enrollment \
            --collection user \
            --type json \
            --file /mongo-setup/users.json \
            --jsonArray
echo "Done setting user collection."

echo "Setting up UTA_Enrollment db with course collection... "
mongoimport --host mongodb \
            --db UTA_Enrollment \
            --collection course \
            --type json \
            --file /mongo-setup/courses.json \
            --jsonArray
echo "Done setting course collection."
