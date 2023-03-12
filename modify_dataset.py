#!/usr/bin/python3

# Import pandas library as they only like bamboo
import pandas as pd

# Reads data from csv file
resco = pd.read_csv('orig_data.csv')
# Creates a unique list of names from 'Created by' column
uniques = resco['Created by'].unique()
num = 0
for i in uniques:
    # Iterates through list of names and replaces name with number
    resco.loc[resco['Created by'] == i, ['Name']] = num
    num += 1
resco.to_csv('modified_data.csv', index=False)

# Reads data from other csv file and performs same function on that dataset
resco = pd.read_csv('other_orig_data.csv')
uniques = resco['Created by'].unique()
num = 0
for i in uniques:
    resco.loc[resco['Created by'] == i, ['Name']] = num
    num += 1
resco.to_csv('other_modified_data.csv', index=False)
