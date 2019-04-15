import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt  
from sklearn.neighbors import KNeighborsClassifier

# Some framework for the classifier

training_data = pd.read_csv("training_data_top_50_pvals.csv")
training_labels = list(training_data)
training_labels.remove("Accession") # Remove unneccesary columns
training_labels.remove("P-value")

#testing_data = pd.read_csv("")
#testing_labels = list(testing_data)

print(training_labels)

# model = KNeighborsClassifier(n_neighbors = 3)

# Train the model on our training sets
# model.fit(features, label

# Predict Output
#predicted = model.predict([[]])