import tensorflow as tf


class modelCreation():
    def create_model():

            model = tf.keras.Sequential()
            model.add(tf.keras.layers.Input(shape = (256,256,3)))
            model.add(tf.keras.layers.Conv2D(filters = 128, strides = (2,2), kernel_size = 3, padding='valid', activation='relu',
             kernel_regularizer = tf.keras.regularizers.l2(0.01), bias_regularizer = tf.keras.regularizers.l2(0.01)))
            model.add(tf.keras.layers.SeparableConv2D(filters = 128, kernel_size = 3, padding = 'same', activation = 'relu',
             bias_regularizer = tf.keras.regularizers.l2(0.01)))
            model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
            model.add(tf.keras.layers.SeparableConv2D(filters = 128, kernel_size = 3, padding = 'same', activation = 'relu',
             bias_regularizer = tf.keras.regularizers.l2(0.02)))
            model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
            model.add(tf.keras.layers.BatchNormalization(axis = 1))
            model.add(tf.keras.layers.Dropout(0.2))
            model.add(tf.keras.layers.AveragePooling2D())
            model.add(tf.keras.layers.SeparableConv2D(filters = 256, kernel_size = 2, strides = (1,1), padding = 'same',
             activation = 'relu'))
            model.add(tf.keras.layers.Dropout(0.2))
            model.add(tf.keras.layers.SeparableConv2D(filters = 96, kernel_size = 2, strides = (1,1), padding = 'same',
             activation = 'relu', bias_regularizer = tf.keras.regularizers.l2(0.01)))
            model.add(tf.keras.layers.Conv2D(filters = 128, kernel_size = 2, strides = (1,1), padding = 'same', activation = 'relu',
             kernel_regularizer = tf.keras.regularizers.l2(0.01), bias_regularizer = tf.keras.regularizers.l2(0.01)))
            model.add(tf.keras.layers.Flatten())
            model.add(tf.keras.layers.Dropout(0.45))
            model.add(tf.keras.layers.Dense(6, activation = 'softmax'))

            model.compile(optimizer='nadam', loss='SparseCategoricalCrossentropy', metrics='accuracy')
            model.summary()

            return model

        

