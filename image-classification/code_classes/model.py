import tensorflow as tf

class ModelCreate():


    def create():
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Input(shape = (150,150,3)))
        model.add(tf.keras.layers.SeparableConv2D(filters = 32, kernel_size = (3,3), padding = 'same', activation = 'relu'))
        model.add(tf.keras.layers.MaxPooling2D())
        model.add(tf.keras.layers.SeparableConv2D(filters = 32, kernel_size = (3,3), padding = 'same', activation = 'relu'))
        model.add(tf.keras.layers.MaxPooling2D())
        model.add(tf.keras.layers.SeparableConv2D(filters = 16, kernel_size = (3,3), padding = 'same', activation = 'relu'))
        model.add(tf.keras.layers.MaxPooling2D())
        model.add(tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu'))