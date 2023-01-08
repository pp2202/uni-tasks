import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

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
    #changing the colour value skewes the results by a large margin 
    #img = img/255.0
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
    plt.figtext(0.05, 0.05, str('Probability for every class in the model:'+'\n'+result_list), horizontalalignment='left', verticalalignment='bottom', fontsize=12)
    plt.show()