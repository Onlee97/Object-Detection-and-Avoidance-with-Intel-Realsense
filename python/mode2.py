## License: Apache 2.0. See LICENSE file in root directory.
## Copyright(c) 2015-2017 Intel Corporation. All Rights Reserved.

###############################################
##      Open CV and Numpy integration        ##
###############################################

# import sys
# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

import pyrealsense2 as prs
import numpy as np
import cv2
import pyaudio
import speech_recognition as sr
from gtts import gTTS
import os
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



def startRsPipeline():
# Configure depth and color streams
    pipeline = prs.pipeline()
    config = prs.config()
    config.enable_stream(prs.stream.depth, 640, 480, prs.format.z16, 30)
    config.enable_stream(prs.stream.color, 640, 480, prs.format.bgr8, 30)
    # Start streaming
    pipeline.start(config)
    return pipeline


def initializeNet():
    net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt",
        "MobileNetSSD_deploy.caffemodel")
    return net

def beeps(duration):
    freq = 440
    duration = 0.2
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    # os.system('spd-say "left"')
    # time.sleep(delayTime)


def detectObject(net, classNames, frame, depth_frame, objectToDetect, counter):
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
            if class_id in classNames and classNames[class_id] == objectToDetect:
                label = classNames[class_id] + " is " + str(int(depth*100)/100) + "meters away " 
                # label = classNames[class_id] + " is " + str(int(depth*100)/100) + "meters away " + str(int(confidence*100)) + "% " 
                labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
                yLeftBottom = max(yLeftBottom, labelSize[1])
                cv2.rectangle(frame, (xLeftBottom, yLeftBottom - labelSize[1]),
                                     (xLeftBottom + labelSize[0], yLeftBottom + baseLine),
                                     (255, 255, 255), cv2.FILLED)
                cv2.putText(frame, label, (xLeftBottom, yLeftBottom),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
                if counter == 0:
                    # annount_tts = gTTS(text = "label")
                    # annount_tts.save("announce.mp3")
                    # os.system("mpg123 " + "announce.mp3")
                    text_to_speech("Found " + label)
                    print(label) 
                    counter += 1
                else:
                    beeps(depth)
                # print(label) #print class and confidence   
    return frame, counter

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def getObjectToDetect(classList):
    PROMPT_LIMIT = 5
    # question_file = "/home/duy/Desktop/Eye-for-Blind/mode2/question.mp3"
    # sad_response = "/home/duy/Desktop/Eye-for-Blind/mode2/sad_response.mp3"
    # final_response_dir = "final_response.mp3"
    # # os.system("mpg123 " + question_file)
    # playsound(question_file)
    # print("What do you want to find?")
    text_to_speech("What do you want to find")
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    #time.sleep(2)
    objectToDetect = None
    while not objectToDetect:
        for j in range(PROMPT_LIMIT):
            answer = recognize_speech_from_mic(recognizer, microphone)
            if answer['transcription']:
                break
            if not answer['success']:
                break
            text_to_speech("I did not register any object")

        answer_list = answer['transcription'].split(" ")
        print(answer_list)
        for _, word in enumerate(answer_list):
            print(word)
            if word in classList:
                objectToDetect = word
                break
    
    final_tts = gTTS(text = "Finding  " + objectToDetect)
    final_tts.save("final_response.mp3")
    text_to_speech("Finding  " + objectToDetect)
    return objectToDetect    

def loop(pipeline, net, classNames, objectToDetect, counter):
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
    
    frame, counter = detectObject(net, classNames, color_image, depth_frame, objectToDetect, counter)

    # Show images
    return frame, counter

def main(pipeline = None, net = None):
    if pipeline == None:    
        pipeline = startRsPipeline()

    if net == None:
        net = initializeNet()
        
    classNames = { 0: 'background',
    1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
    5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
    10: 'cow', 11: 'table', 12: 'dog', 13: 'horse',
    14: 'motorbike', 15: 'person', 16: 'potted plant',
    17: 'sheep', 18: 'sofa', 19: 'train', 20: 'monitor' }
    classList = list(classNames.values())
    objectToDetect = getObjectToDetect(classList)
    net = initializeNet()
    counter = 0
    try:
        while True:

            # Wait for a coherent pair of frames: depth and color
            frame, counter = loop(pipeline, net, classNames, objectToDetect, counter)
            cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('RealSense', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break

    finally:

        # Stop streaming
        pipeline.stop()

if __name__ == "__main__":
    main()