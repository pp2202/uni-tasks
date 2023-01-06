import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os
from random import randrange


class dataSet():

    def read_class_info(path):
        list = []
        with open('class_info.txt') as f:
            for line in f:
                list.append(line.rstrip())
        return list

    def save_class_info(c):
        with open('class_info.txt', 'w') as f:
            for i in c:
                f.write(f"{i}\n")

    def gather_class_info(list_name, paths):
        for folder in os.listdir(paths[0]):
            list_name.append(folder)
        print(list_name)

    def list_dataset_details(classes, paths):
        for i in classes:
            print(f'Total {i} training images: {len(os.listdir(paths[0] + i))}')
            print(f'Total {i} test images: {len(os.listdir(paths[1] + i))}')

    def define_split(paths, i):
        split  = tf.keras.utils.image_dataset_from_directory(paths[i],
            seed = randrange(10,2000))
        return split

class Display():

    def display_examples(datagroup_name, classes):
        plt.figure(figsize=(10, 10))
        for images, labels in datagroup_name.take(3):
            for i in range(6):
                ax = plt.subplot(2, 3, i + 1)
                plt.imshow(images[i].numpy().astype('uint8'))
                plt.title(classes[labels[i]])
                plt.axis('off') 
        plt.show()

    def plot_history(training_history):
            acc = training_history.history['accuracy']
            val_acc = training_history.history['val_accuracy']
            loss = training_history.history['loss']
            val_loss = training_history.history['val_loss']
            epochs = np.arange(len(acc)) + 1
            
            fig = plt.figure(figsize=(12, 4))

            ax1 = fig.add_subplot(121)    
            ax1.plot(epochs, loss, c='g', label='Train')
            ax1.plot(epochs, val_loss, c='r', label='Valid')
            ax1.set_title('Loss')
            ax1.legend(loc='lower left');
            ax1.grid(True)
            
            ax2 = fig.add_subplot(122)    
            ax2.plot(epochs, acc, c='g', label='Train')
            ax2.plot(epochs, val_acc, c='r', label='Valid')
            ax2.set_title('Accuracy')
            ax2.grid(True)
                
            plt.show()

class modelRelated():

    def read_model(path):
        return tf.keras.models.load_model(path)

    def set_callback(c_pat, c_mode, c_delta):
        callback = tf.keras.callbacks.EarlyStopping(monitor = 'val_loss', patience = c_pat, mode = c_mode, min_delta = c_delta)
        return callback

    def augment_data(data_source):
        data_augmentation = tf.keras.Sequential([
            tf.keras.layers.RandomFlip('horizontal_and_vertical'),
            tf.keras.layers.RandomContrast(factor = (0.3,0.5)),
            tf.keras.layers.RandomRotation(0.1),
        ])
        return data_source.map(lambda x,y: (data_augmentation(x, training = True), y), num_parallel_calls = tf.data.AUTOTUNE)

    def class_check(input_path, model, classes):

        img = tf.keras.utils.load_img(input_path,target_size=(256,256))
        img = tf.keras.utils.img_to_array(img)
        img = img/255.0
        img = tf.expand_dims(img, 0)               
        
        pred=model.predict(img)
        img_class = tf.math.argmax(pred[0], axis=-1)

        result_list = ''
        for inside in pred:
            inside_s = np.split(inside, 6, axis=0)
            b = 0
            for number in inside_s:
                a = number[0]
                result_list = result_list+(f'{classes[b]:>10}{str(round(a*100,2)):>30}% \n')
                b+=1

        header = str('Correct class: '+input_path.split("/")[-2]+'\nEstimated class: '+classes[img_class])

        im = plt.imread(input_path)
        plt.title(header)
        plt.imshow(im)
        plt.axis('off')
        plt.figtext(0.05, 0.05, str('Probability for every class in the model:'+'\n'+result_list), horizontalalignment='left', verticalalignment='bottom', fontsize=8)
        plt.show()
        

        