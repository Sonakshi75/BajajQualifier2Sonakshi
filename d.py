import json
import pandas as pd
import re
import hashlib
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
    # Part b
    selected_item['fullName'] = f"{selected_item['patientDetails.firstName']} {selected_item['patientDetails.lastName']}"
    selected_data.append(selected_item)

    phone_number = selected_item['phoneNumber']

    phone_number = re.sub(r'\D', '', phone_number)

    # Check if the phone number meets the length criteria
    if len(phone_number) == 10:
        # Check if the phone number falls within the valid range
        if 6000000000 <= int(phone_number) <= 9999999999:
            selected_item['isValidMobile'] = True
            phone_number_bytes = str.encode(re.sub(r'\D', '', phone_number))
            # Hash the phone number using SHA256
            hash_value = hashlib.sha256(phone_number_bytes).hexdigest()
            selected_item['phonrNumberHash'] = hash_value
        else:
            selected_item['isValidMobile']=False
            selected_item['phonrNumberHash']=None
    else:
        selected_item['isValidMobile']=False
        selected_item['phonrNumberHash']=None

df = pd.DataFrame(selected_data)

df['patientDetails.gender'] = df['patientDetails.gender'].map({'M': 'male', 'F': 'female'}).fillna('others')

df = df.rename(columns={'patientDetails.birthDate': 'DOB'})

print(df)
