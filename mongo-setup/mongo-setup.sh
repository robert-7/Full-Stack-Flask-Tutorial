#!/bin/bash

mongoimport --host mongodb \
            --db UTA_Enrollment \
            --collection user \
            --type json \
            --file /mongo-setup/users.json \
            --jsonArray

mongoimport --host mongodb \
            --db UTA_Enrollment \
            --collection course \
            --type json \
            --file /mongo-setup/courses.json \
            --jsonArray
