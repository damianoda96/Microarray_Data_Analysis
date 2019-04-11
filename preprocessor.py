import sys
import pandas as pd # pandas is used to create csv

data_table = []

THRESHOLD = 20

with open("ALL_vs_AML_train_set_38_sorted.res", "r") as file:
	for line in file:
		cells = line.split("\t")
		data_table.append(cells)

# - replace all values below THRESHOLD with THRESHOLD

for i in range(len(data_table)):
	for j in range(len(data_table[i])):
		if(data_table[i][j].isdigit()):
			if int(data_table[i][j]) < THRESHOLD:
				data_table[i][j] = str(THRESHOLD)

# create data_frame

data_frame = pd.DataFrame(data_table)
data_frame.columns = data_table[0] # set row zero as our column names
data_frame = data_frame.drop(data_frame.index[[0,1,2]]) # drop all unnecessary rows

column_name_list = list(data_frame) # get a list of our column headers

# - remove all genes with A's across the experiments

data_frame = data_frame[~(data_frame[column_name_list] == 'A').any(axis=1)]

# - remove all endogenous control genes

data_frame = data_frame[~data_frame.Description.str.contains("endogenous control")]

# TODO:: remove genes with less than two fold change across the experiments (max/min <2);
# (not sure what this means yet)

# drop all columns with no headers (will elimate p's)

#data_frame = data_frame[data_frame.columns.dropna()]

column_name_list.remove("Description")
exp_list = column_name_list
exp_list.remove("Accession")
for i in exp_list:
	if i == '':
		exp_list.remove(i)

del data_frame['Description'] # delete description column as it is uneccessary

data_frame.to_csv('training_data.csv', index=False) # export csv of data

# TODO: remove rows as stated by the project instructions
	
		
