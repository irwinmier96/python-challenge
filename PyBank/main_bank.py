import os

import csv

total_sum = []

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline = '') as csvfile:

    csvreader =csv.reader(csvfile, delimiter = ',')

    for month in csvreader:
        #line_num is a built-in csv function that counts all the rows in 
        #a csv file. Need the total amount of months = total amount of rows
        #excluding the header.
        month = csvreader.line_num - 1

    print(f"Total Months: {month}")
    
    for row in csvreader:
        values = row.strip().split(',')
        total_sum.append(int(values[1]))
        total_values = sum(total_sum)

        print(total_sum)


        