import os

import cv2
import numpy as np
import math

import time

cam = cv2.VideoCapture(0)
check, frame = cam.read()
cv2.imshow("frame", frame)
print(frame.shape)
cv2.waitKey(0)
