import sys
import pandas as pd # pandas is used to create csv

data_table = []
i = 0

with open("ALL_vs_AML_train_set_38_sorted.res", "r") as file:
	for line in file:
		cells = line.split("\t")
		data_table.append(cells)

data_frame = pd.DataFrame(data_table)
data_frame.columns = data_table[0] # set row zero as our column names
data_frame = data_frame.drop(data_frame.index[[0,1,2]]) # drop all unnecessary rows

# TODO:: REMOVE THE FOLLOWING FROM OUR DATA SET
# - (endogenous) control genes

column_name_list = list(data_frame) # get a list of our column headers

# below removes all rows that contain an 'A'

data_frame = data_frame[~(data_frame[column_name_list] == 'A').any(axis=1)]

# - genes with A's across the experiments
# - genes with less than two fold change across the experiments (max/min <2);
# TODO:: REPLACE EXPR VALUES BELIOW THRESHHOLD WITH THRESHHOLD VALUE
# TODO:: REORGANIZE REMAINING DATA TO ONLY SHOW EXPR VALUES




data_frame.to_csv('training_data.csv', index=False) # export csv of data

# TODO: remove rows as stated by the project instructions
	
		
