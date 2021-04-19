#!/bin/bash

# Extracts frames for all videos in all datasets.
'''folder-path-of-bilibili-videos: 
'''
function main () {

  # Extract for bilibili dataset
  nohup ./extract_frames_all_videos.sh \
  "folder-path-of-bilibili-videos" \
  "dest-folder-path-of-bilibili-video-frames" > \
  "logs/bilibili_frame_generation.log" &

  ## Extract for youtube dataset
  # nohup ./extract_frames_all_videos.sh \
  # "folder-path-of-youtube-videos" \
  # "dest-folder-path-of-youtube-video-frames" > \
  # "logs/youtube_frame_generation.log" &
}

main
