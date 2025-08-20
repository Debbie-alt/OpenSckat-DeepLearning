my_dict= {
    'name': 'Sam',
    "age": 30,
    'city': 'New York',
}
c = my_dict['city']
my_dict['age'] = 31

for x in my_dict:
    print(my_dict[x])

if 'age' in my_dict:
    print('yes')    

len(my_dict)  # Get the number of key-value pairs
print(my_dict.get('name'))  # Accessing value by key
print(my_dict.get('country', 'Not Found'))  # Accessing a non-existent key
print(my_dict.keys())  # Get all keys
print(my_dict.values())  # Get all values
print(my_dict.items())  # Get all key-value pairs
my_dict.pop('city')  # Remove a key-value pair
print(my_dict)  # Display the updated dictionary
my_dict.clear()  # Clear the dictionary
print(my_dict)  # Display the empty dictionary  

del my_dict  # Delete the dictionary