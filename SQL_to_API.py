# we will essentially need to pull the same report 
# from OtterbotCbsPopulationView
# for grad years = current year, and current year + 1, 
# and upload all the data  to the Otterbot

import json
import os
import requests
import pandas as pd
import pyodbc
import numpy as np
import datetime
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Environment and Connection
drivername = 'mssql+pyodbc'
server = 'sqldatamart'
database = 'datamart'
api_token = 'btg9Jd5HhpPfyH15cSGfvUhA_kWVa9ec4uhomzFjwxDg2DgiSOTCApnt1Pr5Djk7MSAmdo7Cg7_pM9IZYE2ZMg'
driver = 'ODBC Driver 17 for SQL Server'
trusted_connection = 'yes'

# url = "https://api.admithub.com/contacts/5555556"
# headers = {'content-type': 'application/json',
# 'Authorization': 'APIToken ' + api_token}

# response = requests.get(url, headers=headers).json()

# print(json.dumps(response))



#   1. CONNECT TO THE DATABASE ( DATAMART )
# Create connection URL
connect_url = URL.create(
    drivername = drivername,
    host = server,
    database = database,
    query = dict(trusted_connection = trusted_connection, driver = driver))

#   2. API parameters to load multiple contacts into the Otterbot
url = 'https://api.admithub.com/contacts/bulk/'
params = {'include_nonpermitted_contacts': 'true'}
headers = {'content-type': 'application/json', 
           'Authorization': 'APIToken ' + api_token}

if server is None or database is None or api_token is None:
    print("SERVER and DATABASE variables are requried")
    exit(1)

#   3. Connect to the database and get the table result, load into dataframe
dbEngine = create_engine(connect_url)
connection = dbEngine.connect()
if (connection):
    print ('Connection to the database was succesful')


# SQL -- Connect to the DB and get the result of SELECT query
# get the first row from the table
tableResultSQL = pd.read_sql(" SELECT top 200 * from OtterbotCBSPopulationView WHERE GradYear IN ('2022-2023')",  connection )
# tableResultSQL = pd.read_sql("SELECT * from OtterbotCBSPopulationView " + 
#                              "WHERE GradYear IN ('2022-2023') " +
#                              "EXCEPT  " +
#                              "select * from OtterbotCBSPopulationView_UPLOADED " +
#                              "WHERE GradYear IN ('2022-2023')",  connection) 
#print (tableResult)
df = pd.DataFrame(tableResultSQL)

# replace nulls in LastReportedGPA column with 0.0
#df["LastReportedGPA"].fillna("0.0", inplace=True)

# drop rows with nulls in LastReportedGPA column
#df.dropna(subset=["LastReportedGPA"], inplace=True)

#df.drop(columns=["CBSPledgeID"], inplace=True) # TODO - is that OKAY?

# drop duplicates in the 'OtterbotContactID' column
# duplicates in the 'phone' column are not allowed - they break the import
df.drop_duplicates(subset=["Phone"], inplace=True)

#   4. REMAP COLUMNS
conv_dict = {
    'OtterbotContactID':'admithub_id',
    'CBSPledgeID': 'crm_id',
    'EnrollmentID': 'enrollment_id',
    'StudentFirstName': 'first_name',
    'StudentLastName': 'last_name',
    'Channel': 'channel',
    'Phone': 'phone',
    'Email': 'email',
    'DateAdded': 'created',
    'IsActive': 'permitted_user_status',
    'OptOutStatus': 'texting_status',
    'LastIncomingMessageDate': 'last_incoming_message_at',
    'LastOutgoingMessageDate': 'last_outgoing_message_at',
    'CBStatus': 'custom.CB Status',
    'Cohort': 'custom.Cohort',
    'CompletionStatus': 'custom.CompletionStatus',
    'DOB': 'custom.DOB',
    'FamiliarWithCollegeBound': 'custom.FamiliarWithCollegeBound',
    'Grade': 'custom.Grade',
    'GradYear': 'custom.GradYear',
    'HighSchool': 'custom.High School',
    'IsEligibleFoster': 'custom.IsEligibleFoster',
    'LastReportedDistrictCode': 'custom.LastReportedDistrictCode',
    'LastReportedDistrictName': 'custom.LastReportedDistrictName',
    'LastReportedESD': 'custom.LastReportedESD',
    'LastReportedSchoolCode': 'custom.LastReportedSchoolCode',
    'LastReportedSchoolName': 'custom.LastReportedSchoolNamev',
    'SelectedForVerification': 'custom.SelectedForVerification',
    'CollegeInTheHighSchool': 'custom.CollegeInTheHighSchool',
    'CteDualCredit': 'custom.CteDualCredit',
    'Gender': 'custom.Gender',
    'LanguageIndex': 'custom.LanguageIndex',
    'LastReportedGPA': 'custom.LastReportedGPA',
    'LastReportedOSPIRaceEthnicity': 'custom.LastReportedOSPIRace/Ethnicity',
    'RunningStart': 'custom.RunningStart',
    'StudentResearchId': 'custom.StudentResearchID',
    'SelfReportedCBStatus': 'custom.Self-reported CB Status'
}
# rename columns to match the API
df.rename(columns=conv_dict, inplace=True)

# make sure there's no NaN values in the dataframe - API would reject them
df = df.astype(object).replace(np.nan, 'None')

print (df)
# records to get separate objects
data = df.to_dict('records')
print ("Getting into dictionary replacement")

output = list()
for d in data:
    temp = dict()
    temp["custom"] = dict()
    for key, value in d.items():
        if "custom" not in key.lower():
            # check for NaN values needed?
            temp[key] = value
        else:            
            temp["custom"][key[7:]] = value # key[7:] is to get rid of "custom." portion of keys
    output.append(temp)  
print ("After for loop:")

# output is a list of dict (with ' instead of " )
# json.dumps() creates a proper json object, that is double-quoted "
#print (json.dumps(output))    

# 5. LOAD INTO THE API
url = "https://api.admithub.com/contacts/bulk/"
headers = {"Content-type": "application/json",
"Authorization": "APIToken " + api_token}

response = requests.post(url, headers=headers, json=output)
# 6. IF THE LOAD WAS SUCCESSFUL, COPY THE TABLE INTO THE 'UPLOADED' TABLE
print (response)
if (response.ok):
    print ("Data has been loaded")
    # we need to make sure that the data is replaced in the 'uploaded' table
    # so that we don't upload the same data again next week
    # execute a SQL statement
    cursor = connection.cursor()
    cursor.execute("DROP TABLE OtterbotCBSPopulationView_UPLOADED")
    cursor.execute("SELECT * INTO OtterbotCBSPopulationView_UPLOADED " +            
    "FROM OtterbotCBSPopulationView")
    print ("Data has been copied to the 'UPLOADED' table")
