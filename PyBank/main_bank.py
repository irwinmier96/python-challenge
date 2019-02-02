import os

import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline = '') as csvfile:

    csvreader =csv.reader(csvfile, delimiter = ',')
    
    sum_profit = 0
    sum_loss = 0
    profit = 0
    total_profit = 0

    for month in csvreader:
        #line_num is a built-in csv function that counts all the rows in 
        #a csv file. Need the total amount of months = total amount of rows
        #excluding the header.
        month = csvreader.line_num - 1

    print(f"Total Months: {month}")

    #reset the file pointer the csvreader 
    #is associated with so that you can iterate over it again.
    csvfile.seek(0)
    next(csvreader)
    
    for row in csvreader:
        profit = int(row[1])
        if profit > 0:
            sum_profit = sum_profit + profit
        elif profit < 0:
            sum_loss = sum_loss + profit
    
    total_profit = sum_profit + sum_loss
    average = total_profit/len(int(profit))
    print(f"Total: ${total_profit}")
    print(f"Average: ${average}")

   