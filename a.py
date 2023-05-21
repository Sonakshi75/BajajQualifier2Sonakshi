
import json
import pandas as pd
import re
with open('DataEngineeringQ2.json') as file:
    data = json.load(file)
col = ['appointmentId', 'phoneNumber', 'patientDetails.firstName', 'patientDetails.lastName',
           'patientDetails.gender', 'patientDetails.birthDate', 'consultationData.medicines']
selected_data = []
for item in data:
    selected_item = {}
    for i in col:
        keys = i.split('.')
        value = item
        try:
            for key in keys:
                value = value.get(key)
            selected_item[i] = value
        except (KeyError, TypeError):
            selected_item[i] = None
    selected_data.append(selected_item)

df = pd.DataFrame(selected_data)

df['patientDetails.gender'] = df['patientDetails.gender'].map({'M': 'male', 'F': 'female'}).fillna('others')

df = df.rename(columns={'patientDetails.birthDate': 'DOB'})

print(df)



