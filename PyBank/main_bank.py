import os

import csv

csvpath = os.path.join('budget_data.csv')

total_sum = []

profitLossAverage = []

changeAmount = []

sumChangeAmount = 0

with open(csvpath, newline = '') as csvfile:

    csvreader =csv.reader(csvfile, delimiter = ',')

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

    increase_max = 0
    increase_max_date = ""
    decrease_max = 0
    decrease_max_date = ""

    before = 0
    
    for row in csvreader:
        #Finding the sum of all the rows in the file
         total_sum.append(int(row[1]))
        #Finding the average change of each rows in the file
        #This formula helps in finding the greatest increase
        #as well as the greatest decrease
         changeAmount = int(row[1]) - int(before)
        #Make a new list to put the values of the differences
        #between the rows
         profitLossAverage.append(row[1])
         if changeAmount > int(increase_max):
            increase_max_date = row[0]
            increase_max = changeAmount
         elif changeAmount < int(decrease_max):
            decrease_max_date = row[0]
            decrease_max = changeAmount
         before = row[1]
         
    lengthofProfitLoss = len(profitLossAverage) - 1 
    firstIndexProfitLoss = profitLossAverage[0]
    #need to index lengthofProfitLoss because we want the value in that specific index, 
    # which is the last value on the list
    ProfitLossAvg = (int(profitLossAverage[int(lengthofProfitLoss)]) - int(firstIndexProfitLoss))/int(lengthofProfitLoss)


 

    print(f"Total: ${sum(total_sum)}")
    print(f"Average Change: {ProfitLossAvg}")
    print(f"Greatest Increase: {increase_max_date} (${increase_max})")
    print(f"Greatest Decrease: {decrease_max_date} (${decrease_max})")

  

  
   