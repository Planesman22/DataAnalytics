import pandas
import numpy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MaxAbsScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Dense, Flatten, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical


#Paramters
SequenceLength = 5
# Size of window segment in values, each one here is 0.01 seconds
StepSize = SequenceLength
# Control Overlapping
SkipSize = StepSize
# Set gpu memory growth
tf.config.experimental.set_memory_growth(tf.config.list_physical_devices('GPU')[0], True)


# Push data into memory
Nominal = pandas.read_csv('nominal180.csv', header=None, names=['X', 'Y', 'Z'])
Loose = pandas.read_csv('loose180.csv', header=None, names=['X', 'Y', 'Z'])
Damaged = pandas.read_csv('damaged180.csv', header=None, names=['X', 'Y', 'Z'])

# Convert data into sequences with label, overlapping is optional
def getSequence(Data, Step, Skip, Label):
    Sequences = []
    Labels = []
    for I in range(0, len(Data) - Step + 1, Skip):
        Sequences.append(Data.iloc[I:I + Step, :])
        Labels.append(Label)
    return numpy.array(Sequences), numpy.array(Labels)

# Our labels 0 = Normal, 1 = Loose, 2 = Damaged
NominalSeqs, NominalLabs = getSequence(Nominal, StepSize, SkipSize, 0)
LooseSeqs, LooseLabs = getSequence(Loose, StepSize, SkipSize, 1)
DamagedSeqs, DamagedLabs = getSequence(Damaged, StepSize, SkipSize, 2)

# Combine our sequences
Sequences = numpy.concatenate((NominalSeqs, DamagedSeqs, LooseSeqs), axis=0)
Labels = numpy.concatenate((NominalLabs, LooseLabs, DamagedLabs), axis=0)

# Scale the data
scaler = MaxAbsScaler()
Sequences = scaler.fit_transform(Sequences.reshape(-1, 3)).reshape(Sequences.shape)

# Encode labels using one-hot encoding
Labels = to_categorical(Labels, num_classes=3)

# Shuffle and split, then reshape
X_train, X_test, y_train, y_test = train_test_split(Sequences, Labels, test_size=0.2, random_state=42)

Model = Sequential([
    Conv1D(32, kernel_size=3, activation='relu', input_shape=(SequenceLength, 3)),
    MaxPooling1D(pool_size=2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(3, activation='softmax')
])

Model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

Model.summary()

History = Model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=32)

