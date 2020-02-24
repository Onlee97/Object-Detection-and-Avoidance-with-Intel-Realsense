import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import mode1
import mode2
# import mode3
import view
import speech_recognition as sr
import os
import cv2
# from gtts import gTTS 
from gtts import gTTS
import pygame
from pygame import mixer

pygame.init()
def text_to_speech(my_text):
	"""
	:param my_text:
	:return:
	"""
	language = 'en'
	output = gTTS(text=my_text, lang=language, slow=False)
	output.save("output.mp3")

	pygame.mixer.music.load("output.mp3")
	pygame.mixer.music.play(0)
	clock = pygame.time.Clock()
	clock.tick(10)
	while pygame.mixer.music.get_busy():
		pygame.event.poll()
		clock.tick(10)

def main():
	#set up pipeline
	pipeline = mode2.startRsPipeline()
	net = mode2.initializeNet()
	# Initial Definition
	pygame.init()
	left_mouse_down = False
	right_mouse_down = False
	left_click_frame = 0  # keeps track of how long the left button has been down
	right_click_frame = 0  # keeps track of how long the right button has been down
	left_right_action_once = True  # perform the combo action only once
	left_action_once = True  # perform the left action only once
	right_action_once = True  # perform the right action only once
	max_frame = 2  # The frames to wait to see if the other mouse button is pressed (can be tinkered with)
	performing_left_right_action = False  # prevents the off chance one of the single button actions running on top of the combo action
	screen = pygame.display.set_mode((2000, 1000)) #Define the clicking screen


	mode = 0

	just_run_mode2 = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				screen.exit()
		mouse_pressed = pygame.mouse.get_pressed()
		if mouse_pressed[0]:  # left click
			left_click_frame += 1
			left_mouse_down = True
		else:
			left_action_once = True
			left_mouse_down = False
			left_click_frame = 0
		if mouse_pressed[2]:  # right click
			right_click_frame += 1
			right_mouse_down = True
		else:
			right_action_once = True
			right_mouse_down = False
			right_click_frame = 0
		if not mouse_pressed[0] and not mouse_pressed[2]:
			left_right_action_once = True
			performing_left_right_action = False

		if left_mouse_down and right_mouse_down and abs(left_click_frame - right_click_frame) <= max_frame:
			if left_right_action_once:
				print("performing right/left action")
				left_right_action_once = False
				performing_left_right_action = True

		elif left_mouse_down and left_click_frame > max_frame and not performing_left_right_action and not right_mouse_down:
			if left_action_once:
				print("perform single left click action")
				mode += 1
				left_action_once = False
		elif right_mouse_down and right_click_frame > max_frame and not performing_left_right_action and not left_mouse_down:
			if right_action_once:
				print("perform single right click action")
				mode -= 1
				right_action_once = False

		if mode < 0:
			mode = 2
		elif mode > 2:
			mode = 0

		# print(mode)

		if mode == 0:
			mode1.loop(pipeline)
			images = view.loop(pipeline)
			just_run_mode2 = 0
		elif mode == 1:
			mode1.loop(pipeline)
			just_run_mode2 = 0
		elif mode == 2:
			if just_run_mode2 == 0:
				classNames = { 0: 'background',
				1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
				5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
				10: 'cow', 11: 'table', 12: 'dog', 13: 'horse',
				14: 'motorbike', 15: 'person', 16: 'potted plant',
				17: 'sheep', 18: 'sofa', 19: 'train', 20: 'monitor' }
				classList = list(classNames.values())
				objectToDetect = mode2.getObjectToDetect(classList)
				counter = 0
				just_run_mode2 = 1
			if just_run_mode2 != 0:
				# model2.loop(pipeline, net)
				images, counter = mode2.loop(pipeline, net, classNames, objectToDetect, counter)

		cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
		cv2.imshow('RealSense', images)
		cv2.waitKey(1)	



if __name__ == "__main__":
	main()
