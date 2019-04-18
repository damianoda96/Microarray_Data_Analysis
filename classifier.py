import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# _________ READ IN TARGET COLUMN FOR TRAINING DATA___________

training_label_file = open("ALL_vs_AML_train_set_38_sorted.cls", "r")
training_labels = training_label_file.readlines()
training_labels = training_labels[1].split()
for i in range(len(training_labels)):
	training_labels[i] = int(training_labels[i])

# ________ READ IN TARGET COLUMN FOR TESTING DATA ______________

testing_label_file = open("Leuk_ALL_AML.test.cls", "r")
testing_labels = testing_label_file.readlines()
testing_labels = testing_labels[1].split()
for i in range(len(testing_labels)):
	testing_labels[i] = int(testing_labels[i])

# __________ READ PREPROCESSED TRAINING DATA INTO DATAFRAME ____________

training_data = pd.read_csv("training_data_top_50_pvals.csv")
training_data = training_data.drop(columns=['Accession', 'P-value'], axis=1)
training_data = training_data.transpose()
training_features = list(training_data) # we will train on these features
training_data['target'] = training_labels # this is our target column

# __________ READ PROCESSED TESTING DATA INTO DATAFRAME _____________

testing_data = pd.read_csv("testing_data_top_50_pvals.csv")
testing_data = testing_data.drop(columns=['Accession', 'P-value'], axis=1)
testing_data = testing_data.transpose()
testing_features = list(testing_data)
testing_data['target'] = testing_labels

# ___________ BELOW WE WILL TRAIN ON THE ABOVE FEATURES AND TARGET _____

X_train = training_data[training_features]
y_train = training_data['target']

X_test = testing_data[testing_features]
y_test = testing_data['target']

classifier = KNeighborsClassifier(algorithm='auto', n_neighbors = 5)

classifier.fit(X_train, y_train)

# Predict Output
#predicted = model.predict(train or test)
