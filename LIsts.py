my_list = ['wood' 'metal', 'plastic', 'glass']
print (my_list[0])
my_list.append('ceramic')
my_list[1] = 'aluminum'
print(my_list)
print(my_list[2:4])
print(len(my_list))
print(my_list[-1])  # Accessing the last element
print(my_list[1:3])  # Slicing from index 1 to 2
print(my_list[1:])  # Slicing from index 1 to the end
print(my_list[:3])  # Slicing from the start to index 2
print(my_list[::2])  # Slicing with a step of 2