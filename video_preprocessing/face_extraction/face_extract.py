import cv2, os, dlib, sys
import numpy as np
from py_utils.face_utils import lib
from concurrent.futures import ProcessPoolExecutor

seed = 100
# Employ dlib to extract face area and landmark points
pwd = os.path.dirname(os.path.abspath(__file__))
front_face_detector = dlib.get_frontal_face_detector()
lmark_predictor = dlib.shape_predictor(pwd + '/dlib_model/shape_predictor_68_face_landmarks.dat')


def extract_faces_img(im, dest):
    face_info = lib.align(im[:, :, (2, 1, 0)], front_face_detector, lmark_predictor)
    print(len(face_info))
    for i, face in enumerate(face_info):
        _, point = face
        roi, _ = lib.cut_head([im], point, seed)
        cv2.imwrite(dest + "_face_" + str(i) + ".png", roi[0])


def extract_faces_video(extraction_cmd_args):
    frames_path, faces_path = extraction_cmd_args
    # dont repeat videos if we're picking up on a prev run..
    if os.path.isdir(faces_path):
        return
    os.makedirs(faces_path)
    for img_name in os.listdir(frames_path):
        img = cv2.imread(os.path.join(frames_path, img_name))
        extract_faces_img(img, os.path.join(faces_path, get_filename_only(img_name)))


def get_filename_only(full_path):
    filename_with_extension = os.path.basename(full_path)
    filename = ''.join(filename_with_extension.split(".")[:-1])
    return filename


def extract_faces_videos(videos_path, dest_faces_path):
    extraction_cmd_args = [
        (os.path.join(videos_path, os.path.basename(video)), os.path.join(dest_faces_path, os.path.basename(video)))
        for video in
        os.listdir(videos_path)]
    # print(extraction_cmd_args)
    with ProcessPoolExecutor(50) as executor:
        executor.map(extract_faces_video, extraction_cmd_args)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--videos_frame_path', type=str, default='', required = True, help='The folder path contains extracted frames of videos')
    parser.add_argument('--dest_faces_path', type=str, default='', required = True, help='The folder path where extracted faces will be saved')
    opt = parser.parse_args()
    # print(opt)
    ## extract faces for bilibili: extract_faces_videos("folder-path-of-bilibili-video-frames", "folder-path-of-bilibili-extracted-faces")
    extract_faces_videos(args.videos_frame_path, args.dest_faces_path)

    ## extract faces for youtube: extract_faces_videos("folder-path-of-youtube-video-frames", "folder-path-of-youtube-extracted-faces")
    # extract_faces_videos(args.videos_frame_path, args.dest_faces_path) 

if __name__ == '__main__':
    main()
