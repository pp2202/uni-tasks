import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# def import_dataset():
#     (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
#     print('Train: x=%s, y=%s' % (x_train.shape, y_train.shape))
#     print('Test: x=%s, y=%s' % (x_test.shape, y_test.shape))
class Dataset():
    def import_dataset():

        paths = [os.getcwd() + '/image-classification\dataset/intel-image-classification/seg_train/',
        os.getcwd() + '/image-classification\dataset/intel-image-classification/seg_test/']

        classes = [] 
        for folder in os.listdir(paths[0]):
            classes.append(folder)
        print(classes)
        
        for i in classes:
            print(f'Total {i} training images: {len(os.listdir(paths[0] + i))}')
            print(f'Total {i} test images: {len(os.listdir(paths[1] + i))}')


        train_split = tf.keras.utils.image_dataset_from_directory(paths[0],
        seed = 1337)

        test_split = tf.keras.utils.image_dataset_from_directory(paths[1],
        seed = 1337)

        plt.figure(figsize=(10, 10))
        for images, labels in train_split.take(3):
            for i in range(6):
                ax = plt.subplot(2, 3, i + 1)
                plt.imshow(images[i].numpy().astype("uint8"))
                plt.title(classes[labels[i]])
                plt.axis("off") 
        plt.show()
