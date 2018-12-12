# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 22:59:31 2018

@author: mvesk
"""
#Dependencies
import os
import csv

#the only path file reference that works for me. note to self find out why.
csvpath = os.path.join("election_data.csv")
candidate = []

#with open to read election_data.csv file
with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  reader=next(csvreader)

  for row in csvreader:
      candidate.append(row[2])

# display print statements
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(len(candidate)))
print("----------------------------")

# percentages math for the candidates
# should have made a loop for this but wanted to walk arond of lights in the heights so...lame version
Khan = candidate.count("Khan")
khan_WINNING_percent = int((Khan) / len(candidate) * 100)
print("Khan: " + str(khan_WINNING_percent) + "% (" + str(Khan) + ")")

Correy = candidate.count("Correy")
correy_WINNING_percent = int((Correy) / len(candidate) * 100)
print("Corry: " + str(correy_WINNING_percent) + "% (" + str(Correy) + ")")

Li = candidate.count("Li")
Li_WINNING_percent = int((Li) / len(candidate) * 100)
print("Li: " + str(Li_WINNING_percent) + "% (" + str(Li) + ")")

OTooley = candidate.count("O'Tooley")
OTooley_WINNING_percent = int((OTooley) / len(candidate) * 100)
print("O'Tooley " + str(OTooley_WINNING_percent) + "% (" + str(OTooley) + ")")

print("----------------------------")

#50% to win
if khan_WINNING_percent > .50:
	print("Winner: Khan")
elif correy_WINNING_percent > .50:
	print("Winner: Correy")
elif Li_WINNING_percent > .50:
	print("Winner: Li")
else:
	print("Winner: O'Tooley")	#ergo		

# open a write file and write to it
#didn't add the line seperaters/'----' since it would be in the way if someone was wanting to use it.
    #uh i needed to add a \n for the text to end up on the next line
f = open("election_result.txt","w")   
f.write("Khan: " + str(khan_WINNING_percent) + "% (" + str(Khan) + ")\n")
f.write("Corry: " + str(correy_WINNING_percent) + "% (" + str(Correy) + ")\n")
f.write("Li: " + str(Li_WINNING_percent) + "% (" + str(Li) + ")\n")
f.write("O'Tooley " + str(OTooley_WINNING_percent) + "% (" + str(OTooley) + ")\n")
f.close()			#closing file object