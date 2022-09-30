# Written by Lex Whalen

import cv2
from pose_estimator import PoseEstimator
from frame_operations import FrameOperations
from google.colab.patches import cv2_imshow
class VideoImgManager():

    def __init__(self):
        self.POSE_ESTIMATOR = PoseEstimator()
        self.FRAME_OPS = FrameOperations()

        self.FIRST = True

    def estimate_vid(self,webcam_id=0):
        """reads webcam, applies pose estimation on webcam"""
        cap = cv2.VideoCapture(webcam_id)

        while(True):
            has_frame, frame = cap.read()

            if self.FIRST:
                self.WEB_CAM_H,self.WEB_CAM_W = frame.shape[0:2]
                self.FIRST = False

            frame = self.POSE_ESTIMATOR.get_pose_key_angles(frame)

            cv2_imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    def estimate_img(self,img_path):
        """applies pose estimation on img"""

        img = cv2.imread(img_path,cv2.IMREAD_UNCHANGED)

        img = self.POSE_ESTIMATOR.get_pose_key_angles(img)


        cv2_imshow("Image Pose Estimation",img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

