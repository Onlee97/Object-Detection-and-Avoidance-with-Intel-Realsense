import os
import matplotlib.pyplot as plt
from evaluator import Evaluator
from generator import Generator
# from keras.callbacks import CSVLogger
# from keras.callbacks import ModelCheckpoint
# from keras.callbacks import ReduceLROnPlateau
from models import NIC
from data_manager import DataManager
from keras.models import load_model

plt.rcParams['figure.figsize'] = (18, 18)
plt.rcParams['image.interpolation'] = 'nearest'

num_epochs = 500
batch_size = 256
PARENT_PATH = r"C:\Users\nomie\Desktop\neural_image_captioning-master\neural_image_captioning-master"
root_path = os.path.join(PARENT_PATH, r"datasets\IAPR_2012")
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

image = plt.imread(os.path.join(PARENT_PATH, "images/NIC.png"))
plt.imshow(image)
plt.axis('off')
plt.show()

print(PARENT_PATH)
root_path = os.path.join(PARENT_PATH, "datasets/IAPR_2012")
data_path = os.path.join(root_path, 'preprocessed_data')
images_path = os.path.join(root_path, 'iaprtc12')
model_filename = os.path.join(PARENT_PATH, "trained_models/IAPR_2012/iapr_weights.90-1.99.hdf5")
print(model_filename)
model = load_model(model_filename)
evaluator = Evaluator(model, data_path, images_path)

evaluator.display_caption()