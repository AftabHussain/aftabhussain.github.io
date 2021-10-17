#!/bin/bash

TIME=$(echo "$(date "+%a"), $(date "+%d") $(date "+%B") $(date "+%Y")")

export POST_TIME=$TIME
python3 addpost.py "$1" "$2"

