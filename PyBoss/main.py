import os
import csv
import datetime as dt

#Used to determine Runtime
startime=dt.datetime.now()

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

filename=os.path.join("./","employee_data.csv")

with open(filename, "r",newline="") as csv_in:
    PII_Data=csv.reader(csv_in, delimiter=",")
    next(PII_Data)
    for row in PII_Data:
        Emp_ID.append(row[0])
        Name.append(row[1])
        DOB.append(dt.date.fromisoformat(row[2]))
        SSN.append(row[3])
        state.append(us_state_abbrev[row[4]])

#format things



new_DOB=[day.strftime("%m/%d/%Y") for day in DOB]
new_DOB.insert(0,"DOB")
new_SSN=["***-**-"+sn.split("-")[2] for sn in SSN]
new_SSN.insert(0,"SSN")
state.insert(0,"State")