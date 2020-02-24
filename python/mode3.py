## License: Apache 2.0. See LICENSE file in root directory.
## Copyright(c) 2015-2017 Intel Corporation. All Rights Reserved.

###############################################
##      Open CV and Numpy integration        ##
###############################################

# import sys
# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import os
import pyrealsense2 as rs
import numpy as np
import cv2
import time
from PIL import Image
from object_detection_model import *
from keras.models import load_model


def startRsPipeline():

# Configure depth and color streams
	pipeline = rs.pipeline()
	config = rs.config()
	config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
	config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
	# Start streaming
	pipeline.start(config)
	return pipeline


def initializeNet():
	classNames = { 0: 'background',
	1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
	5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
	10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
	14: 'motorbike', 15: 'person', 16: 'pottedplant',
	17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor' }
	net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt",
		"MobileNetSSD_deploy.caffemodel")
	return net, classNames

def detectObject(net, classNames, frame, depth_frame):
	frame_resized = cv2.resize(frame,(300,300))
	blob = cv2.dnn.blobFromImage(frame_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5), False)
	#Set to network the input blob 
	net.setInput(blob)
	#Prediction of network
	detections = net.forward()
	# print(detections)
	#Size of frame resize (300x300)
	cols = frame_resized.shape[1] 
	rows = frame_resized.shape[0]
	#For get the class and location of object detected, 
	# There is a fix index for class, location and confidence
	# value in @detections array .
	for i in range(detections.shape[2]):
		confidence = detections[0, 0, i, 2] #Confidence of prediction 
		if confidence > 0.8: # Filter prediction 
			class_id = int(detections[0, 0, i, 1]) # Class label
			# Object location 
			xLeftBottom = int(detections[0, 0, i, 3] * cols) 
			yLeftBottom = int(detections[0, 0, i, 4] * rows)
			xRightTop   = int(detections[0, 0, i, 5] * cols)
			yRightTop   = int(detections[0, 0, i, 6] * rows)

			# Factor for scale to original size of frame
			heightFactor = frame.shape[0]/300.0  
			widthFactor = frame.shape[1]/300.0 
			# Scale object detection to frame
			xLeftBottom = int(widthFactor * xLeftBottom) 
			yLeftBottom = int(heightFactor * yLeftBottom)
			xRightTop   = int(widthFactor * xRightTop)
			yRightTop   = int(heightFactor * yRightTop)
			# Draw location of object  
			cv2.rectangle(frame, (xLeftBottom, yLeftBottom), (xRightTop, yRightTop),
						  (0, 255, 0))

			xCenter = int((xRightTop - xLeftBottom)/2)
			yCenter = int((yRightTop - yLeftBottom)/2)

			depth = depth_frame.get_distance(xCenter, yCenter)

			# Draw label and confidence of prediction in frame resized
			if class_id in classNames:
				label = classNames[class_id] + ": " + str(int(confidence*100)) + "% " + str(int(depth*100)/100) + "m away"
				labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
				yLeftBottom = max(yLeftBottom, labelSize[1])
				cv2.rectangle(frame, (xLeftBottom, yLeftBottom - labelSize[1]),
									 (xLeftBottom + labelSize[0], yLeftBottom + baseLine),
									 (255, 255, 255), cv2.FILLED)
				cv2.putText(frame, label, (xLeftBottom, yLeftBottom),
							cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
				print(label) #print class and confidence 
				obj = classNames[class_id]
				# os.system("spd-say {l}".format(l=obj))
				# break


	return frame

def loop(pipeline):
# Wait for a coherent pair of frames: depth and color
	frames = pipeline.wait_for_frames()
	depth_frame = frames.get_depth_frame()
	color_frame = frames.get_color_frame()
	if not depth_frame or not color_frame:
		return
	# Convert images to numpy arrays
	depth_image = np.asanyarray(depth_frame.get_data())
	color_image = np.asanyarray(color_frame.get_data())

	# Apply colormap on depth image (image must be converted to 8-bit per pixel first)
	depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

	# Stack both images horizontally
	# images = np.hstack((color_image, depth_colormap))
	
	frame = detectObject(net, classNames, color_image, depth_frame)

	# Show images
	cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
	cv2.imshow('RealSense', frame)

def main(pipeline=None):
	# l = "You are now in descriptive mode"
	# os.system("spd-say {l}".format(l=l))
	# time.sleep(1)

	if pipeline == None:
		pipeline = startRsPipeline()

	net, classNames = initializeNet()
	try:
		while True:
			loop(pipeline)
			key = cv2.waitKey(1) & 0xFF
			if key == ord('q'):
				break

	finally:

		# Stop streaming
		pipeline.stop()

if __name__ == "__main__":

	main()

