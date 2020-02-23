## License: Apache 2.0. See LICENSE file in root directory.
## Copyright(c) 2015-2017 Intel Corporation. All Rights Reserved.

#####################################################
## librealsense tutorial #1 - Accessing depth data ##
#####################################################


# First import the library
import pyrealsense2 as rs
import cv2
import numpy as np
import os
import time

def main(pipeline = None):
	if pipeline == None:
		pipeline = startRsPipeline()

	delayTime = 0.5
	def beepLeft(duration):
		freq = 440
		#os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
		os.system('spd-say "left"')
		time.sleep(delayTime)

	def beepRight(duration):
		freq = 1000
		#os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
		os.system('spd-say "right"')
		time.sleep(delayTime)

	width = 640
	height = 360
	
	try:
		# Create a context object. This object owns the handles to all connected realsense devices

		while True:
			# This call waits until a new coherent set of frames is available on a device
			# Calls to get_frame_data(...) and get_frame_timestamp(...) on a device will return stable values until wait_for_frames(...) is called
			frames = pipeline.wait_for_frames()
			depth_frame = frames.get_depth_frame()
			color_frame = frames.get_color_frame()
			if not depth_frame or not color_frame:
				continue

			# Print a simple text-based representation of the image, by breaking it into 10x20 pixel regions and approximating the coverage of pixels within one meter
			coverage = [0]*64

			#Left search
			minDepthLeft = width
			minXLeft = 0
			step = 5

			leftThreshold = int(width/5)

			for x in range(leftThreshold,int(width/2),step):			
				for y in range(0,int(height), step):
					dist = depth_frame.get_distance(x, y)
					if (dist != 0 and dist < minDepthLeft):
						minDepthLeft = dist
						minXLeft = x

			#Right search
			minDepthRight = width
			minXRight = 0

			rightThreshold = int(width*4/5)
			for x in range(int(width/2),rightThreshold, step):			
				for y in range(0,int(height), step):
					dist = depth_frame.get_distance(x, y)
					if (dist != 0 and dist < minDepthRight):
						minDepthRight = dist
						minXRight = x

			depthThreshold = 0.5
			# print(minDepthRight, minDepthLeft)
			# if minDepthRight < depthThreshold and minDepthRight < depthThreshold:
			# 	print("Right: ", minDepthRight, " | Left: ", minDepthLeft)
			if minDepthRight < depthThreshold:
				print("Right: ", minDepthRight)
				beepRight(minDepthRight)
			if minDepthLeft < depthThreshold:
				print("Left: ", minDepthLeft)
				beepLeft(minDepthLeft)
			# depth_image = np.asanyarray(depth_frame.get_data())
			# color_image = np.asanyarray(color_frame.get_data())

			# # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
			# depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

			# # Stack both images horizontally
			# # images = np.hstack((color_image, depth_colormap))
			# images = depth_colormap
			# # Show images
			# # cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
			# cv2.imshow('RealSense', images)
			# cv2.waitKey(1)


		exit(0)
	#except rs.error as e:
	#    # Method calls agaisnt librealsense objects may throw exceptions of type pylibrs.error
	#    print("pylibrs.error was thrown when calling %s(%s):\n", % (e.get_failed_function(), e.get_failed_args()))
	#    print("    %s\n", e.what())
	#    exit(1)
	except Exception as e:
		pipeline.stop()
		print(e)
		pass
