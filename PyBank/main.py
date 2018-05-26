#Import modules
import os
import csv

#Request path and filename of data file
csvpath = input('Please enter path and filename of data file (e.g. "datafolder/datafile.csv"): ')

#Open CSV file and perform operations
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #Declare and initialize variables to store data
    total_revenue = 0
    prev_revenue = 0
    sum_revenue_chg = 0
    max_revenue_chg = 0
    max_revenue_dt = ""                           #Date of max revenue increase
    min_revenue_chg = 0
    min_revenue_dt = ""                           #Date of max revenue decrease
    revenue_chg = []                              #List to store revenue change values
    
    for row in csvreader:
        total_revenue = total_revenue + int(row[1])          #Add revenue value to cumulative total
        
        cur_revenue_chg = int(row[1]) - prev_revenue
        
        if cur_revenue_chg > max_revenue_chg:                #Update max revenue increase
            max_revenue_chg = cur_revenue_chg
            max_revenue_dt = row[0]
        
        if cur_revenue_chg < min_revenue_chg:                #Update min revenue increase
            min_revenue_chg = cur_revenue_chg
            min_revenue_dt = row[0]
            
        revenue_chg.append(cur_revenue_chg)                  #Store revenue change
        
        prev_revenue = int(row[1])                           #Set prior revenue to current revenue value
        
    
    total_months = len(revenue_chg)
    
    for x in range(1, total_months):                         #Ignore revenue change of first entry
        sum_revenue_chg = sum_revenue_chg + revenue_chg[x]
   
    avg_revenue_chg = round(sum_revenue_chg/(total_months - 1), 2)     #Calculate avg revenue change, ignoring first entry
    
#Create Budget Summary
budget_summary = [f'Financial Analysis',
                  f'-----------------------------------',
                  f'Total Months: {total_months}',
                  f'Total Revenue: ${total_revenue}',
                  f'Average Revenue Change: ${avg_revenue_chg}',
                  f'Greatest Increase in Revenue: {max_revenue_dt} (${max_revenue_chg})',
                  f'Greatest Decrease in Revenue: {min_revenue_dt} (${min_revenue_chg})'
                 ]

#Print Budget Summary in terminal
for item in budget_summary:
    print(item)
    
#Request filename for text file
outputfile = input('Please type filename of new report file (e.g. "budget_report.txt"): ')

#Write Budget Summary to text file
with open(outputfile, 'w', newline = "") as report:
    
    for item in budget_summary:
        report.write(item + "\r")
    

