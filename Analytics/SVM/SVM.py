import numpy
import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

# Parameters
# Size of window segment in values, each one here is 0.01 seconds
StepSize = 3
# Control Overlapping, because svm isn't convering
SkipSize = StepSize

Nominal = pandas.read_csv('nominal180.csv', header=None, names=['X', 'Y', 'Z'])
Loose = pandas.read_csv('loose180.csv', header=None, names=['X', 'Y', 'Z'])
Damaged = pandas.read_csv('damaged180.csv', header=None, names=['X', 'Y', 'Z'])


# Convert data into sequences with label, Overlapping as we go!
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

X_train_scaled = Scaler.transform(X_train)
X_test_scaled = Scaler.transform(X_test)

print("StandardScaler Successfully Fitted the Data! Proceeding to fit")
print("Shape of our features: "+str(X_train_scaled.shape))

# Define and fit our model
SVM = SVC(kernel='rbf', C=1, gamma='scale', random_state=42, tol=1e-3)

SVM.fit(X_train_scaled, y_train)

y_pred = SVM.predict(X_test_scaled)

print("Shape of our test features: "+str(X_test_scaled.shape))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Summary, this is a success! We see that if we don't consider temporal data, SVM can only achieve an 80% acc
# However, the moment we take acount of temperal data, we get 90-95% accuracy depending on adjustments
