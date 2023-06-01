import json

data_list1 = ['eip: 1', 'title: EIP Purpose and Guidelines', 'status: Living', 'type: Meta', 'author: Martin Becze <mb@ethereum.org>, Hudson Jameson <hudson@ethereum.org>, et al.', 'created: 2015-10-27']

data_list2 = ['eip: 2', 'title: EIP Title', 'status: Draft', 'type: Standard', 'author: John Doe', 'created: 2022-01-01']

# Create a list to store the dictionaries
data_dict_list = []

# Convert data_list1 to dictionary
data_dict1 = {}
for item in data_list1:
    key, value = item.split(': ', 1)
    key = key.strip()
    value = value.strip()
    data_dict1[key] = value

# Append data_dict1 to the list
data_dict_list.append(data_dict1)

# Convert data_list2 to dictionary
data_dict2 = {}
for item in data_list2:
    key, value = item.split(': ', 1)
    key = key.strip()
    value = value.strip()
    data_dict2[key] = value

# Append data_dict2 to the list
data_dict_list.append(data_dict2)

# Convert the list of dictionaries to JSON
json_data = json.dumps(data_dict_list)
print(json_data)
# # Write the JSON data to a file
# with open('output.json', 'w') as file:
#     file.write(json_data)
