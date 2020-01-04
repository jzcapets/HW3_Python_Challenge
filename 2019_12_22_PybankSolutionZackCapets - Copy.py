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
    dat_month = ""
    big_loss = float(0)
    why_bother= ""
    avg_delta = float(0)
    
    #go through data line by line
    for row in data:
        #find first date in file
        if total_months == 1:
            startdate = row[0]        
        
        #increment counters
        total_months += 1
        total_profit += float(row[1])
        
        #check monthly P/L against vars that hold "high scores". If value is more extreme, it becomes the new high score
        if float(row[1]) > big_gain:
            dat_month = str(row[0])
            big_gain = float(row[1])
            
        if float(row[1]) < float(big_loss):
            why_bother = str(row[0])
            big_loss = float(row[1])
        
        #inefficient but effective way of storing the last date in the range. Note: Inaccurate if dates aren't sorted chronologically but making that edge case work is WAY out of scope
        enddate = row[0]
        
    #calculate things
    avg_delta = total_profit / total_months
    
    #print results to the terminal
    print(f'("Number of months of budget data: {total_months}')
    print(f'("Total profit over time period analyzed: {round(total_profit,2)}')
    print(f'("Biggest profit over time period analyzed: {round(big_gain,2)} ({dat_month})')
    print(f'("Biggest loss over time period analyzed: {round(big_loss,2)} ({why_bother})')
    print(f'("Average P/L over time period analyzed: {round(avg_delta,2)}')

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
   
    # Write the first row (column headers)
    csvwriter.writerow(['Total Months of Data', 'Total Profit', 'Biggest Monthly Gain','Biggest Monthly Loss','Average Monthly Change'])
    csvwriter.writerow([total_months,total_profit,big_gain,big_loss,avg_delta])
    
print(f'Your file analysis is complete, your results are here: {outputpath}')     