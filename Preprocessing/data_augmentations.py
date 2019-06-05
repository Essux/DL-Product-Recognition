import tensorflow.keras.applications.inception_v3 as inception_v3
from tensorflow.keras.preprocessing.image import ImageDataGenerator

BATCH_SIZE = 32
TRAIN_DIR = './processed/train'
VALIDATION_DIR = './processed/dev'
TEST_DIR = './processed/test'

# Initialize data generators and data augmentation for training
train_datagen = ImageDataGenerator(
    preprocessing_function=inception_v3.preprocess_input,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=20,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

validation_datagen = ImageDataGenerator(
    preprocessing_function=inception_v3.preprocess_input)

test_datagen = ImageDataGenerator(
    preprocessing_function=inception_v3.preprocess_input)

# Set directories and batch sizes for data generators
train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    batch_size=BATCH_SIZE,
    class_mode='categorical')
    
validation_generator = validation_datagen.flow_from_directory(
    VALIDATION_DIR,
    batch_size=BATCH_SIZE,
    class_mode='categorical', shuffle=False)

test_generator = test_datagen.flow_from_directory(
    TEST_DIR,
    batch_size = 1,
    class_mode='categorical', shuffle=False)