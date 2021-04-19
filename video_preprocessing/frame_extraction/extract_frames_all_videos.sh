#!/bin/bash

# Extracts frames from all videos in $1, puts them into directories in $2.
for FILE_PATH in "$1"/*; do
  FILE_NAME=$(basename "${FILE_PATH}")
  FILE_NAME="${FILE_NAME%.*}"
  DESTINATION="$2/${FILE_NAME}";
  mkdir -p "$2/${FILE_NAME}";
  ffmpeg -i "${FILE_PATH}" "${DESTINATION}/frame-%d.png";
done
