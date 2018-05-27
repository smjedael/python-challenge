#PyBoss Script
#Import modules
import os
import csv

#Request path and filename of data file
csvpath = input('Please enter path and filename of data file (e.g. "datafolder/datafile.csv"): ')

#Declare variables to store data
emp_id = []
first_name = []
last_name = []
ssn = []
dob = []
state = []

#Dictionary for state abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Open CSV file and perform operations
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)    
    
    for row in csvreader:
        emp_id.append(row[0])
        
        #Split full name into parts
        full_name = row[1].split(' ')
        first_name.append(full_name[0])
        last_name.append(full_name[1])
        
        #Reformat date of birth
        orig_dob = row[2].split('-')
        dob.append(f'{orig_dob[1]}/{orig_dob[2]}/{orig_dob[0]}')
        
        #Mask first five digits of SSN
        orig_ssn = row[3].split('-')
        ssn.append(f'***-**-{orig_ssn[2]}')
        
        #Convert state name to abbreviation
        state.append(us_state_abbrev[row[4]])

#Create reformated Employee Table
employees = zip(emp_id, first_name, last_name, dob, ssn, state)

#Request filename for CSV file
outputfile = input('Please type filename of new employee file (e.g. "employee_table.csv"): ')

#Write Employee Table to new CSV file
with open(outputfile, 'w', newline = "") as table:
    writer = csv.writer(table)
    
    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write in zipped rows
    writer.writerows(employees)

