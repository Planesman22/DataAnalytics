import numpy
import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# Parameters
# Size of window segment in values, each one here is 0.01 seconds
StepSize = 4
# Control Overlapping
SkipSize = 4
#KNN Stuff
Neighbors = 4

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

# Shuffle and split, then reshape
X_train, X_test, y_train, y_test = train_test_split(Sequences, Labels, test_size=0.2, random_state=42)
X_train = X_train.reshape(X_train.shape[0], -1)
X_test = X_test.reshape(X_test.shape[0], -1)

# Scale our data because of SVM
Scaler = StandardScaler()
Scaler.fit(X_train)
X_train = Scaler.transform(X_train)
X_test = Scaler.transform(X_test)

KNN = KNeighborsClassifier(n_neighbors=Neighbors)
KNN.fit(X_train, y_train)
y_pred = KNN.predict(X_test)

# Calculate the accuracy, is like cheating!
knn_accuracy = accuracy_score(y_test, y_pred)
print("KNN :"+str(round(knn_accuracy, 2))+"%\n")
print(str(confusion_matrix(y_test, y_pred))+"\n")
print(str(classification_report(y_test, y_pred))+"\n")
