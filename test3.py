import json

# Create a list to store the JSON data objects
json_data_list = []

# JSON data object 1
json_data1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Add JSON data object 1 to the list
json_data_list.append(json_data1)

# JSON data object 2
json_data2 = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}

# Add JSON data object 2 to the list
json_data_list.append(json_data2)
json_data = json.dumps(json_data_list)
print(json_data_list)
# Write the list of JSON data objects to the file
# with open('output.json', 'w') as file:
#     json.dump(json_data_list, file)
