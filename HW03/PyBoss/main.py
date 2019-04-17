import os
import csv
import datetime as dt

#Used to determine Runtime
#start_time=dt.datetime.now()

#input and output files
filename=os.path.join(".","employee_data.csv")
outputfile=os.path.join(".","modified_employee_data.csv")
#Initial lists
Emp_ID=[]
Name=[]
SSN=[]
DOB=[]
state=[]

# Dictionary for state conversion
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


#This reads the csv file into separate lists
with open(filename, "r",newline="") as csv_in:
    PII_Data=csv.reader(csv_in, delimiter=",")
    next(PII_Data)
    for row in PII_Data:
        Emp_ID.append(row[0])
        Name.append(row[1])
        #Date of birth is converted to datetime object
        DOB.append(dt.date.fromisoformat(row[2]))
        SSN.append(row[3])
        #state is looked up in the dictionary
        state.append(us_state_abbrev[row[4]])

#format things and add row headers
Emp_ID.insert(0,"Emp ID")
first_name=[name.split(" ")[0] for name in Name]
first_name.insert(0,"First Nane")
last_name=[name.split(" ")[1] for name in Name]
last_name.insert(0,"Last Name")
new_DOB=[day.strftime("%m/%d/%Y") for day in DOB]
new_DOB.insert(0,"DOB")
new_SSN=["***-**-"+sn.split("-")[2] for sn in SSN]
new_SSN.insert(0,"SSN")
state.insert(0,"State")

#zip em up and move em out
outputlist=zip(Emp_ID,first_name,last_name,new_DOB,new_SSN,state)

with open(outputfile, "w") as csv_out:
    writer=csv.writer(csv_out)
    writer.writerows(outputlist)

#this is for QAing runtime
#runtime=(dt.datetime.now()-start_time).total_seconds()
#print(runtime)