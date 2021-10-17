#!/bin/bash

TIME=$(echo "$(date "+%a"), $(date "+%d") $(date "+%B") $(date "+%Y")")

export POST_TIME=$TIME

echo "Enter text"
read text
echo "Enter link"
read link

python3 addpost.py "$text" "$link"

git add posts.html && git commit -m "post" && git push


