import matplotlib.pyplot as plt 

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