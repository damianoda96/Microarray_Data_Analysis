import sys
import pandas as pd # pandas is used to export csv

data_table = []
i = 0

with open("ALL_vs_AML_train_set_38_sorted.res", "r") as file:
	for line in file:
		cells = line.split("\t")
		data_table.append(cells)

data_frame = pd.DataFrame(data_table)
data_frame.columns = data_table[0]
data_frame = data_frame.drop(data_frame.index[[0,1,2]]) # drop all unnecessary rows
data_frame.to_csv('training_data.csv', index=False) # export csv of data

# TODO: remove rows as stated by the project instructions
	
		
