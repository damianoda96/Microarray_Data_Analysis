import sys
import numpy as np

data_table = []
i = 0

with open("ALL_vs_AML_train_set_38_sorted.res", "r") as file:
	for line in file:
		cells = line.split()
		data_table.append(cells)

for i in data_table[0]:
	print(i)
		
