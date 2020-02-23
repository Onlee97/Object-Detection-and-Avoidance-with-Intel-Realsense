import os
import sys
import matplotlib.pyplot as plt
from evaluator import Evaluator
from generator import Generator
# from keras.callbacks import CSVLogger
# from keras.callbacks import ModelCheckpoint
# from keras.callbacks import ReduceLROnPlateau
from models import NIC
from data_manager import DataManager
from keras.models import load_model

sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2

plt.rcParams['figure.figsize'] = (18, 18)
plt.rcParams['image.interpolation'] = 'nearest'

num_epochs = 500
batch_size = 256
PARENT_PATH = r"/home/duy/Eye_for_Blind/neural_image_captioning-master/neural_image_captioning-master/"
root_path = os.path.join(PARENT_PATH, r"datasets/IAPR_2012")
captions_filename = os.path.join(root_path, 'IAPR_2012_captions.txt')
data_manager = DataManager(data_filename=captions_filename,
                            max_caption_length=30,
                            word_frequency_threshold=2,
                            extract_image_features=False,
                            cnn_extractor='inception',
                            image_directory=os.path.join(root_path, "iaprtc12"),
                            split_data=True,
                            dump_path=os.path.join(root_path + "reprocessed_data")
                          )

data_manager.preprocess()
print(data_manager.captions[0])
print(data_manager.word_frequencies[0:20])

preprocessed_data_path = os.path.join(root_path, "preprocessed_data")
print(root_path)
print(preprocessed_data_path)
generator = Generator(data_path=preprocessed_data_path,
                      batch_size=batch_size)

num_training_samples =  generator.training_dataset.shape[0]
num_validation_samples = generator.validation_dataset.shape[0]
print('Number of training samples:', num_training_samples)
print('Number of validation samples:', num_validation_samples)


model = NIC(max_token_length=generator.MAX_TOKEN_LENGTH,
            vocabulary_size=generator.VOCABULARY_SIZE,
            rnn='gru',
            num_image_features=generator.IMG_FEATS,
            hidden_size=256,
            embedding_size=256)

model.compile(loss='categorical_crossentropy',
              optimizer = 'adam',
              metrics=['accuracy'])

print(model.summary())
print('Number of parameters:', model.count_params())

#image = plt.imread(os.path.join(PARENT_PATH, "images/NIC.png"))
#plt.imshow(image)
#plt.axis('off')
#plt.show()

print(PARENT_PATH)
root_path = os.path.join(PARENT_PATH, "datasets/IAPR_2012")
data_path = os.path.join(root_path, 'preprocessed_data')
images_path = os.path.join(root_path)
model_filename = os.path.join(PARENT_PATH, "trained_models/IAPR_2012/iapr_weights.90-1.99.hdf5")
print(model_filename)
#model = load_model(model_filename)
#evaluator = Evaluator(model, data_path, images_path)

#evaluator.display_caption()

key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
	try:
		check, frame = webcam.read()
		print(check) #prints true as long as the webcam is running
		print(frame) #prints matrix values of each framecd 
		cv2.imshow("Capturing", frame)
		key = cv2.waitKey(1)
		if key == ord('s'): 
			cv2.imwrite(filename='saved_img.jpg', img=frame)
			webcam.release()
			img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
			img_new = cv2.imshow("Captured Image", img_new)
			cv2.waitKey(1650)
			cv2.destroyAllWindows()
			print("Processing image...")
			img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
			print("Converting RGB image to grayscale...")
			gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
			print("Converted RGB image to grayscale...")
			print("Resizing image to 28x28 scale...")
			img_ = cv2.resize(gray,(28,28))
			print("Resized...")
			img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
			print("Image save")
			model = load_model(model_filename)
			evaluator = Evaluator(model, data_path, images_path)

			evaluator.display_caption()

        
			break
		elif key == ord('q'):
			print("Turning off camera.")
			webcam.release()
			print("Camera off.")
			print("Program ended.")
			cv2.destroyAllWindows()
			break
        
	except(KeyboardInterrupt):
		print("Turning off camera.")
		webcam.release()
		print("Camera off.")
		print("Program ended.")
		cv2.destroyAllWindows()
		break
