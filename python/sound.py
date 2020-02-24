from gtts import gTTS
import pygame
from pygame import mixer
def text_to_speech(my_text):
	"""
	:param my_text:
	:return:
	"""
	pygame.init()
	language = 'en'
	output = gTTS(text=my_text, lang=language, slow=False)
	output.save("output.mp3")

	pygame.display.set_mode((200,100))
	pygame.mixer.music.load("output.mp3")
	pygame.mixer.music.play(0)
	clock = pygame.time.Clock()
	clock.tick(10)
	while pygame.mixer.music.get_busy():
	    pygame.event.poll()
	    clock.tick(10)

	# mixer.init()
	# mixer.music.load("output.mp3")
	# mixer.music.play()
	# print(my_text)

if __name__ == "__main__":
	text_to_speech("Hello 1 2 3 4 5 6 8 my name is Hi")