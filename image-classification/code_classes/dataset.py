import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import mlmodel as ml
from random import randrange

paths = [os.getcwd() + '/image-classification\dataset/intel-image-classification/seg_train/',
os.getcwd() + '/image-classification\dataset/intel-image-classification/seg_test/']

classes = [] 

def gatherClassInfo(list_name):
    for folder in os.listdir(paths[0]):
        list_name.append(folder)
    print(list_name)
    
def listDatasetDetails():
    for i in classes:
        print(f'Total {i} training images: {len(os.listdir(paths[0] + i))}')
        print(f'Total {i} test images: {len(os.listdir(paths[1] + i))}')    

def displayExamples(datagroup_name):
    plt.figure(figsize=(10, 10))
    for images, labels in datagroup_name.take(3):
        for i in range(6):
            ax = plt.subplot(2, 3, i + 1)
            plt.imshow(images[i].numpy().astype('uint8'))
            plt.title(classes[labels[i]])
            plt.axis('off') 
    plt.show()

def augmentData(data_source):
    data_augmentation = tf.keras.Sequential([
        tf.keras.layers.RandomFlip('horizontal_and_vertical'),
        tf.keras.layers.RandomContrast(factor = (0.3,0.5)),
        tf.keras.layers.RandomRotation(0.2),
    ])
    return data_source.map(lambda x,y: (data_augmentation(x, training = True), y), num_parallel_calls = tf.data.AUTOTUNE)



train_split = tf.keras.utils.image_dataset_from_directory(paths[0],
seed = randrange(10,2000))
test_split = tf.keras.utils.image_dataset_from_directory(paths[1],
seed = randrange(10,2000))

model = ml.ModelCreation()

gatherClassInfo(classes)

listDatasetDetails()

displayExamples(train_split)

augmented_train_split = augmentData(train_split)

displayExamples(augmented_train_split)

history = model.createModel().fit(augmented_train_split, validation_data = test_split, epochs = 32)










