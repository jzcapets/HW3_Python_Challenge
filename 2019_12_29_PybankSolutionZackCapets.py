#this is Zack Capets' HW#3 PyBank Python Homework
#this script is intended to run from the homework folder inside a 'solutions' folder, however the code allows the user to choose where to find the file they analyzed and where to put the results file

import os
import csv

#prompt user to choose how they want to find the file to analyze (since TA's may have the file in a different directory...)
inputchoice = input("Do you want to use the default path to the Accounting CSV? y/n: ")

#set path to csvfile -- assign a default value to the file location (up 1 level from cwd, down into resources folder)
if  inputchoice.lower() == "y":
    csvpath = os.path.join("../","PyBank/Resources/budget_data.csv")
else:
    csvpath = input(f"Input the absolute path of the budget data file. No spaces allowed!")

#open the csv using the path we got above
with open(csvpath, newline = '') as budgetdata:
    data = csv.reader(budgetdata, delimiter = ',')
    
    #obligatory skip over the headerrow when reading the data
    csv_header = next(data)
    
    #initialize stat trackers that keep running totals of things, potentially unnecessary typecasting but hey, you can never be too careful...
    startdate = ""
    enddate = ""
    total_months = 0
    total_profit = float(0)
    big_gain = float(0)
    great_month = ""
    big_loss = float(0)
    bad_month= ""
    avg_delta = float(0)
    thismonth = float(0)
    lastmonth = float(0)
    delta = float(0)
    total_delta = float(0)
    
    #go through data line by line
    for row in data:
        
        #set this month's profit value to the profit for the row we're working in
        thismonth = float(row[1])   
        
        #subtract
        delta = thismonth-lastmonth        
        
        #find first date in file
        if total_months == 0:
            startdate = row[0]
            delta = 0       
        
        #increment counters
        total_months += 1
        total_delta += delta
        total_profit += thismonth
        
        
        #check month-over-month P/L change against vars that hold "high scores". If value is more extreme, it becomes the new high score
        if delta > big_gain:
            great_month = str(row[0])
            big_gain = delta
            
        if delta < float(big_loss):
            bad_month = str(row[0])
            big_loss = delta
        
        #get the last date in range
        enddate = row[0]
        
        lastmonth = thismonth
    
    #calculate things
    avg_delta = total_delta / (total_months-1)
    
    #print results to the terminal
    print(f'("Number of months of budget data: {total_months}')
    print(f'("Total profit over time period analyzed: ${round(total_profit,2)}')
    print(f'("Biggest profit over time period analyzed: ${round(big_gain,2)} ({great_month})')
    print(f'("Biggest loss over time period analyzed: ${round(big_loss,2)} ({bad_month})')
    print(f'("Average P/L over time period analyzed: ${round(avg_delta,2)}')

#write this data to a csv    
#prompt user to choose where to save data with default to save in cwd
outputchoice = input("Do you want to use the default data output path? y/n: ")

#set path to csvfile -- default save location is cwd because convenience
if  outputchoice.lower() == "y":
    outputpath = str("Budget_Data_Analyis_" + startdate + "-" + enddate + ".csv")

#let the user choose where to put their output file
else:
    alt = input(f"Input the absolute path of the folder you'd like to store the output file in. No spaces allowed!")
    outputpath = os.path.join(str(alt), str("Budget_Data_Analyis_" + startdate + "-" + enddate + ".csv"))
    
# Open the file using "write" mode. Specify the variable to hold the contents
with open(outputpath, 'w', newline='') as results:
    
    #Initialize csv.writer
    csvwriter = csv.writer(results, delimiter=',')
   
    #write the results in the format requested
    csvwriter.writerow(["Number of months of budget data: ", total_months])
    csvwriter.writerow(["Total profit over time period analyzed:", '${:,.2f}'.format(round(total_profit,2))])
    csvwriter.writerow(["Biggest monthly increase in profit:", round(big_gain,2), great_month])
    csvwriter.writerow(["Biggest monthly decrease in profit:", round(big_loss,2), bad_month])
    csvwriter.writerow(["Average P/L over time period:", round(avg_delta,2)])
    
print(f'Your file analysis is complete, your results are here: {outputpath}')     