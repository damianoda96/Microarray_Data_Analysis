import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# _________ READ IN TARGET COLUMN ___________

label_file = open("ALL_vs_AML_train_set_38_sorted.cls", "r")
labels = label_file.readlines()
labels = labels[1].split()
for i in range(len(labels)):
	labels[i] = int(labels[i])

# __________ READ PREPROCESSED TRAINING DATA INTO DATAFRAME ____________

training_data = pd.read_csv("training_data_top_50_pvals.csv")
#training_labels.remove("Accession") # Remove unneccesary columns
#training_labels.remove("P-value")
training_data = training_data.drop(columns=['Accession', 'P-value'], axis=1)
training_data = training_data.transpose()
training_features = list(training_data) # we will train on these features
training_data['target'] = labels # this is our target column

# ___________________

#X_train, X_test, y_train, y_test = train_test_split(training_data, training_labels, test_size=0.0)  
#training_data = training_data.drop(columns='P-value')



#print(training_data)

#training_data = pd.to_numeric(training_labels, errors='ignore')

'''testing_data = pd.read_csv("testing_data_top_50_pvals.csv")
testing_labels = list(testing_data)
testing_labels.remove("Accession") # Remove unneccesary columns
testing_labels.remove("P-value")


model = KNeighborsClassifier(algorithm='auto', metrics= 'minkowski', n_neighbors = 5)'''

# Train the model on our training sets
#model.fit(X_train, y_train)

# Predict Output
#predicted = model.predict(train or test)
