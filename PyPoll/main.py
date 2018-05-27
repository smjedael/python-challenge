#Import modules
import os
import csv

#Request path and filename of data file
csvpath = input('Please enter path and filename of data file (e.g. "datafolder/datafile.csv"): ')

#Declare and initialize variables to store data
candidate_list = []                                 #Stores the list of candidates for each election
candidate_votes = []                                #Stores the total votes for each candidate
election_results = []                               #Stores election results
total_votes = []                                    #Stores total votes from datafile
vote_pct = []                                       #Stores candidate vote percentages
win_votes = 0

#Open CSV file and perform operations
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #Store votes for all candidates
    for row in csvreader:
        total_votes.append(row[2])

#Create candidate list
for candidate in total_votes:
    if (candidate in candidate_list) == False:
        candidate_list.append(candidate)
        
#Count votes and percentages for each candidate and determine a winner
for candidate in candidate_list:
    votes = 0
    for vote in total_votes:
        if vote == candidate:
            votes = votes + 1
    if votes > win_votes:
        win_votes = votes
    candidate_votes.append(votes)
    vote_pct.append(round((votes/len(total_votes)) * 100, 1))

winner = candidate_list[candidate_votes.index(win_votes)]

#Create Election Results table
election_header = [f'Election Results',
                   f'-----------------------------------',
                   f'Total Votes: {len(total_votes)}',
                   f'-----------------------------------'
                  ]

for candidate in candidate_list:
    election_results.append(f'{candidate}: {vote_pct[candidate_list.index(candidate)]}% ({candidate_votes[candidate_list.index(candidate)]})')

election_footer = [f'-----------------------------------',
                   f'Winner: {winner}',
                   f'-----------------------------------'
                  ]
election_summary = election_header + election_results + election_footer

#Print Election Results in terminal
for item in election_summary:
    print(item)

#Request filename for text file
outputfile = input('Please type filename of new report file (e.g. "election_results.txt"): ')

#Write Election Results to text file
with open(outputfile, 'w', newline = "") as report:
    
    for item in election_summary:
        report.write(item + "\r")

