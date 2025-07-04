# pip install opencv-python numpy

import cv2
import numpy as np

# Load pre-trained colorization model
prototxt = "colorization_deploy_v2.prototxt"
model = "colorization_release_v2.caffemodel"
points = "pts_in_hull.npy"

net = cv2.dnn.readNetFromCaffe(prototxt, model)
pts = np.load(points)