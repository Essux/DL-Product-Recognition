from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import ReduceLROnPlateau
from tensorflow.keras.preprocessing.image import ImageDataGenerator

EPOCHS = 100
BATCH_SIZE = 32
MODEL_FILE = 'filename.model'

reduce_lr = ReduceLROnPlateau(monitor='val_acc', factor=0.8,
                              patience=5, min_lr=0.0001)

history = model.fit_generator(
    train_generator,
    epochs=EPOCHS,
    validation_data=validation_generator,
    callbacks = [reduce_lr])
