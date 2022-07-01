import cv2
from cv2 import circle
from mtcnn import MTCNN
import os
path_of_the_directory= '/home/sourav/Documents/Face Detection using mtcnn/images/images_helmat'
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    cap = cv2.imread(f)
    detector = MTCNN()

    
    output = detector.detect_faces(cap)
    
    for i in output:
        x,y,width, height = i['box']
        left_eye_x, left_eye_y = i['keypoints']['left_eye']
        right_eye_x, right_eye_y = i['keypoints']['right_eye']
        nose_x, nose_y = i['keypoints']['nose']
        mouth_left_x, mouth_left_y = i['keypoints']['mouth_left']
        mouth_left_x, mouth_left_y = i['keypoints']['mouth_right']


        cv2.rectangle(cap, pt1=(x,y), pt2=(x+width, y+height), color=(255,0,0), thickness = 3)
        cv2.circle(cap, center=(left_eye_x,left_eye_y), color=(255,0,0), thickness=3, radius=2)
        cv2.circle(cap, center=(right_eye_x,right_eye_y), radius=2, thickness=3, color=(245,0,0))
        cv2.circle(cap, center=(nose_x, nose_y), radius=2, thickness=3, color=(245,0,0))
        cv2.circle(cap, center=(mouth_left_x, mouth_left_y), radius=2, thickness=3, color=(245,0,0))
        cv2.circle(cap, center=(mouth_left_x, mouth_left_y), radius=2, thickness=3, color=(245,0,0))
    cv2.imshow("window",cap)
    cv2.waitKey(2000)