#PyBank Script
#Import modules
import os
import csv

#Request path and filename of data file
csvpath = input('Please enter path and filename of data file (e.g. "datafolder/datafile.csv"): ')

#Declare and initialize variables to store data
total_revenue = 0
prev_revenue = 0
sum_revenue_chg = 0
max_revenue_chg = 0
max_revenue_dt = ""                           #Date of max revenue increase
min_revenue_chg = 0
min_revenue_dt = ""                           #Date of max revenue decrease
revenue_chg = []                              #List to store revenue change values

#Open CSV file and perform operations
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)    
    
    for row in csvreader:

        #Add revenue value to cumulative total
        total_revenue = total_revenue + int(row[1])          
        
        #Calculate current change in revenue
        cur_revenue_chg = int(row[1]) - prev_revenue
        
        #Update max revenue increase
        if cur_revenue_chg > max_revenue_chg:                
            max_revenue_chg = cur_revenue_chg
            max_revenue_dt = row[0]
        
        #Update min revenue increase
        if cur_revenue_chg < min_revenue_chg:                
            min_revenue_chg = cur_revenue_chg
            min_revenue_dt = row[0]

        #Store revenue change
        revenue_chg.append(cur_revenue_chg)                  
        
        #Set prior revenue to current revenue value
        prev_revenue = int(row[1])                           
        
    
    total_months = len(revenue_chg)

    #Ignore revenue change of first entry
    for x in range(1, total_months):                         
        sum_revenue_chg = sum_revenue_chg + revenue_chg[x]
   
    #Calculate avg revenue change, ignoring first entry
    avg_revenue_chg = round(sum_revenue_chg/(total_months - 1), 2)     
    
#Create Budget Summary
budget_summary = [f'',
                  f'Financial Analysis',
                  f'-----------------------------------',
                  f'Total Months: {total_months}',
                  f'Total Revenue: ${total_revenue}',
                  f'Average Revenue Change: ${avg_revenue_chg}',
                  f'Greatest Increase in Revenue: {max_revenue_dt} (${max_revenue_chg})',
                  f'Greatest Decrease in Revenue: {min_revenue_dt} (${min_revenue_chg})',
                  f''
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
    

