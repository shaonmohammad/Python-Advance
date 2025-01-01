# -------------------------------------------------
# json.dumps - for convert dict to json
# json.dump - for import dict data in file as json
# json.loads - to convert json data to python dict
# ----------------------------------------------------

import json
user_data = {'name': 'afat', 'age': 23, 'is_male': True}
print(user_data)

user_data_json = json.dumps(user_data)
print(user_data_json)

with open('user_data.txt', 'w') as file:
    json.dump(user_data, file, indent=4)
