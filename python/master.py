import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import mode1
import mode2
import mode3
import view
import speech_recognition as sr
import os
import pygame
# from gtts import gTTS 

def main():
	pipeline = mode2.startRsPipeline()
	while(True):
		mode1.loop(pipeline)


if __name__ == "__main__":
	main()