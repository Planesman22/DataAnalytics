import tensorflow as tf
import pandas
import numpy
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Dense, Flatten, Dropout
from tensorflow.keras.optimizers import Adam

#Paramters
SequenceLength = 5

# Set gpu memory growth
tf.config.experimental.set_memory_growth(tf.config.list_physical_devices('GPU')[0], True)

# Push data into memory
Nominal = pandas.read_csv('nominal180.csv', header=None, names=['X', 'Y', 'Z'])
Loose = pandas.read_csv('loose180.csv', header=None, names=['X', 'Y', 'Z'])
Damaged = pandas.read_csv('damaged180.csv', header=None, names=['X', 'Y', 'Z'])
Nominal['label'] = 0
Loose['label'] = 1
Damaged['label'] = 2

# Put them together
Sequences = numpy.concatenate((Nominal, Loose, Damaged), axis=0)
Labels = Sequences[:, -1]
Sequences = Sequences[:, :-1]



Model = Sequential([
    Conv1D(32, kernel_size=3, activation='relu', input_shape=(SequenceLength, 3)),
    MaxPooling1D(pool_size=2),
    Conv1D(64, kernel_size=3, activation='relu'),
    MaxPooling1D(pool_size=2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(3, activation='softmax')
])

Model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

Model.summary()

History = Model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=20, batch_size=32)

