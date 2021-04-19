
## Frame & Face Extraction for Deepfake Detection

To detect deepfake videos, a common approach is to
1. Extract all frames from the video 
2. Extract all detectable faces from each frame
3. Run a specific deepfake detection scheme on each face image
3. Make either video-level or frame-level decisions using the results of your specific scheme. 

In this directory, we share the scripts for steps 2 and 3, as used for all evaluations in our paper. 

#### Frame extraction:
Run the provided bash script as follows:
```
./extract_frames_all_datasets.sh videos_dir dest_frames_dir 
```

After the script is done running, you will observe the following directory structure:
```
|--dest_frames_dir
            |--vid1_name
                       |--frame1.png
                       |--frame2.png
                       |--...
            |--vid2_name
                       |--frame1.png
                       |--frame2.png
                       |--...
            |--...
```
#### Face extraction:
After the above frame extraction, run the provided python script as follows:

```
python face_extract.py --videos_frame_path frames_dir --dest_faces_path dest_faces_dir
```

After the script is done running, you will observe the following directory structure: 

```
|--dest_faces_dir
            |--vid1_name
                       |--frame-1_face_0.png
                       |--frame-1_face_1.png
                       |--frame-2_face_0.png
                       |--...
            |--vid2_name
                       |--frame-1_face_0.png
                       |--frame-1_face_1.png
                       |--frame-2_face_0.png
                       |--...
            |--...
```

Happy detecting!