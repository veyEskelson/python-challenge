# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 18:57:21 2018

@author: mvesk
"""
#Dependencies
import csv as csv
import os as os

#Variable names
greatest_max = 0
greatest_min = 0
total_Bal = 0
avg_change = 0
totalDates = 0
differ = 0
counter = 0
leader = 0

#File paths
csv_path = os.path.join("budget_data.csv")

#open the cvsfile
with open(csv_path, 'r', ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    for row in csvreader:      
        total_Bal += int(row[1])
        if counter > 0:
            differ = (int(row[1]) - leader)
            avg_change = differ + avg_change        
            leader = int(row[1])            
            if differ > greatest_max:
                greatest_max = differ
                rowMax = row
            if differ < greatest_min:             
                greatest_min = differ
                rowMin = row
        else:
            leader = int(row[1])
        counter += 1
avg_change = avg_change / (counter - 1)  


print("Financial Analysis")
print("------------------------")
print(f"Total Months: {counter}")        
print(f"Total: ${total_Bal}")
print(f"Average change: ${avg_change}")
print(f"Greatest Increase in Profits: {rowMax[0]} (${greatest_max})")
print(f"Greatest Decrease in Profits: {rowMin[0]} (${greatest_min})")

# Writing to file
output_path = os.path.join("results.txt")

# Open the text file using writing mode. Use "w"
with open(output_path, 'w') as txtFile:
    
#print to text file
    print(f"Total Months: {totalDates}", file = txtFile)        
    print(f"Total: ${total_Bal}", file = txtFile)
    print(f"Average change: ${avg_change}", file = txtFile)
    print(f"Greates Increase in profits: {rowMax[0]} (${greatest_max})", file = txtFile)
    print(f"Greates Decrease in profits: {rowMin[0]} (${greatest_min})", file = txtFile)