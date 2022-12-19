import tensorflow as tf

class ModelCreate():


    def create():
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Input(shape = (150,150,3)))
        model.add(tf.keras.layers.Conv2D(filters = 32, strides = (2,2), padding='same', activation='relu'))
        model.add(tf.keras.layers.SeparableConv2D(filters = 32, kernel_size = (3,3), padding = 'same', activation = 'relu'))
        model.add(tf.keras.layers.MaxPooling2D())
        model.add(tf.keras.layers.SeparableConv2D(filters = 32, kernel_size = (3,3), padding = 'same', activation = 'relu'))
        model.add(tf.keras.layers.MaxPooling2D())
        model.add(tf.keras.layers.SeparableConv2D(filters = 16, kernel_size = (3,3), padding = 'same', activation = 'relu'))
        model.add(tf.keras.layers.MaxPooling2D())
        model.add(tf.keras.layers.SeparableConv2D(filters = 32, kernel_size = (3,3), padding = 'same', activation = 'relu'))
        model.add(tf.keras.layers.Dropout(0.2))
        model.add(tf.keras.layers.AveragePooling2D())
        model.add(tf.keras.layers.SeparableConv2D(filters = 64, kernel_size = (3,3), padding = 'same', activation = 'relu'))
        model.add(tf.keras.layers.MaxPooling2D())
        model.add(tf.keras.layers.Conv2D(filters = 64, strides = (2,2), padding='same', activation='relu', kernel_regularizer ='l2'))
        model.add(tf.keras.layers.BatchNormalization(axis = 1))
        model.add(tf.keras.layers.MaxPooling2D())
        model.add(tf.keras.layers.SeparableConv2D(filters = 64, kernel_size = (4,4), strides = (1,1), padding = 'same', activation = 'relu'))
        model.add(tf.keras.layers.Dropout(0.2))
        model.add(tf.keras.layers.AveragePooling2D())
        model.add(tf.keras.layers.SeparableConv2D(filters = 128, kernel_size = (4,4), strides = (1,1), padding = 'same', activation = 'relu'))
        model.add(tf.keras.layers.MaxPooling2D())
        model.add(tf.keras.layers.Conv2D(filters = 128, kernel_size = (4,4), strides = (1,1), padding = 'same', activation = 'relu', kernel_regularizer ='l2'))
        model.add(tf.keras.layers.BatchNormalizatio(naxis = 1))
        model.add(tf.keras.layers.Dropout(0.4))
        model.add(tf.keras.layers.Dense(6, activation = 'softmax'))

        model.compile(optimizer='AdamW', loss='categorical_crossentropy', metrics='accuracy')

        model.summary()

        

        

