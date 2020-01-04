#this is Zack Capets' HW#3 PyPoll Python Homework
#this script is intended to run from the homework folder inside a 'solutions' folder, however the code allows the user to choose where to find the file to analyze and where to put the results file

import os
import csv


#prompt user to choose how they want to find the file to analyze (since TA's may have the file in a different directory...)
inputchoice = input("Welcome to Zack's Poll-Counting Software. Do you want to use the default filepath for the election data csv? y/n: ")

#set path to csvfile -- assign a default value to the file location (up 1 level from cwd, down into resources folder)
if  inputchoice.lower() == "y":
    csvpath = os.path.join("../","PyPoll/Resources/election_data.csv")
    corruption = False
elif inputchoice.lower() == "**":
    csvpath = os.path.join("../","PyPoll/Resources/election_data.csv")
    corruption = True
else:
    csvpath = input(f"Input the absolute path of the election data file. No spaces allowed!")

#open the csv using the path we got above
with open(csvpath, newline = '') as electionresults:
    data = csv.reader(electionresults, delimiter = ',')
    
    #obligatory skip over the headerrow when reading the data
    csv_header = next(data)
    
    #initialize variables
    #create an empty list to hold candidate names
    candidates = [];
    #create an empty list to hold vote counts
    votes = [];
    
    cname = ""
    totalvotes = float(0)
    winner = ""
    mostvotes = float(0)
    index = float(0)
    
    #go through data line by line
    for row in data:
        
        cname = row[2]
        
        
        #we're going to build out a list of candidates and a list of vote counts with the same dimension. The index of a candidate's name in that list will correspond to the index of their vote count in the vote count list.
        #look and see if the candidate's name is already in our list of candidates. If not, add it. We only have 4 candidates in this data so we could have hardcoded, but this is more futureproof!
        if cname not in candidates:
            candidates.append(cname)
            votes.append(int(1))
            
        else:    
            #if the candidate already appears in the list, find the index of their name in the list and increment that value by 1
            index = candidates.index(cname)
            votes[index] += 1   
        #count all the votes
        totalvotes += 1
    
    #absolutely nothing to see here...
    if corruption == True:
        winner = input("Input the name of the candidate you want to win: ")    
    else:
        #find highest vote count
        winner = candidates[votes.index(max(votes))]        
    
    #make a header for the results
    #aaaaaaaaaaaaand the votes are in...drumroll please...   
    print("Election results:")
    print("=================")
    print(f'Total Votes: {int(totalvotes)}')
    print("=================")
    print("Results by candidate:")
    print("Candidate, % of total vote, (# of votes)")
    
    i = int(0)
    #loop through candidates list, print results by candidate
    for i in range(0,len(candidates)):
        print(f"{candidates[i]}: {'{:.3%}'.format(votes[i]/totalvotes)}  ({votes[i]})")
        
    #declare a winner
    print("=================")
    print(f'Election Winner: {winner}')
    print("=================")
    
#write this data to a csv    
#prompt user to choose where to save data with default to save in cwd
outputchoice = input("Do you want to use the default data output path? y/n: ")

#set path to csvfile -- default save location is cwd because convenience
if  outputchoice.lower() == "y":
    outputpath = str("ElectionResults.csv")

#let the user choose where to put their output file
else:
    alt = input(f"Input the absolute path of the folder you'd like to store the output file in. No spaces allowed!")
    outputpath = os.path.join(str(alt), str("ElectionResults.csv"))
    
# Open the file using "write" mode. Specify the variable to hold the contents
with open(outputpath, 'w', newline='') as results:
    
    #Initialize csv.writer
    csvwriter = csv.writer(results, delimiter=',')
    
    #write out total votes cast
    csvwriter.writerow(['Total Votes Cast',totalvotes])
    
    #loop through results, but this time writing them to csv instead of printing them
    i = int(0)
    for i in range(0,len(candidates)):
        csvwriter.writerow([candidates[i],'{:.3%}'.format(votes[i]/totalvotes),votes[i]])
    #declare the winner
    csvwriter.writerow(["Winner:",winner])
#display a message that lets the user know their file is ready    
print(f'Your file analysis is complete, your results are here: {outputpath}')     