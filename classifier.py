import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree

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

# _________ BELOW HERE IS AN ALTERNATIVE TRAINING FILE WITH ALL ROWS,
# --------- NOT JUST TOP 50 GENES ----------------------------------

training_data_all = pd.read_csv("training_data_all.csv")
training_data_all = training_data_all.drop(columns=['Accession'], axis=1)
training_data_all = training_data_all.transpose()
training_features_all = list(training_data_all) # we will train on these features
training_data_all['target'] = training_labels

# __________ READ PROCESSED TESTING DATA INTO DATAFRAME _____________

testing_data = pd.read_csv("testing_data_top_50_pvals.csv")
testing_data = testing_data.drop(columns=['Accession', 'P-value'], axis=1)
testing_data = testing_data.transpose()
testing_features = list(testing_data)
testing_data['target'] = testing_labels

# ___________ BELOW WE WILL TRAIN ON THE ABOVE FEATURES AND TARGET _____

X_train_all = training_data_all[training_features_all]
y_train_all = training_data_all['target']

X_train = training_data[training_features]
y_train = training_data['target']

X_test = testing_data[testing_features]
y_test = testing_data['target']

# ____________ CREATE AND TRAIN OUR CLASSIFIER _____________

classifier = KNeighborsClassifier(algorithm='auto', leaf_size=30,
                           metric='minkowski', metric_params=None, n_jobs=3,
                           n_neighbors=1, p=2, weights='uniform')

classifier.fit(X_train, y_train)

# ________ GET OUTPUT METRICS _______________

train_predicted = classifier.predict(X_train)

print("\n___ KNN CLASSIFICATION RESULTS ___\n")

print("\nTraining Predictions: ", train_predicted)
print("Test Accuracy:", accuracy_score(y_train, train_predicted))

test_predicted = classifier.predict(X_test)

print("\nTest Predictions:", test_predicted)
print("Test Accuracy:", accuracy_score(y_test, test_predicted))

print("\n")

print("___ DECISION TREE CLASSIFICATION RESULTS ___\n")

c = tree.DecisionTreeClassifier(min_samples_split=2)

dt = c.fit(X_train, y_train)

y_pred = dt.predict(X_test)

print("Test Predictions: ", y_pred)
print("Test Accuracy:", accuracy_score(y_test, y_pred))
print("\n")
