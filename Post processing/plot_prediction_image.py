import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import os
import PIL
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class_names = sorted([os.path.basename(os.path.dirname(f)) for f in glob('./processed/train/*/')])

def plot_predicted_image(img_pre):
    plt.figure(figsize=(7, 2))
    img_pre = np.expand_dims(img, axis=0)
    # Get the prediction
    preds = model.pred(img_pre)
    predicted_lbl = np.argmax(preds)
    predicted_prob = np.max(preds)
    # Get predicted image
    predicted_file = np.random.choice(glob('./processed/train/' + class_names[predicted_lbl] + '/*'))
    predicted_obj = PIL.Image.open(predicted_file).convert('RGB')
    predicted_arr = np.asarray(predicted_obj)

    plt.subplot(5, 2, 2)
    plt.title('Prediction {} ({:.2f}%)'.format(class_names[predicted_lbl], predicted_prob*100))
    plt.imshow(predicted_arr)
    plt.axis('off')