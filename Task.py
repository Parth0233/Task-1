#Creating a List.
my_list = [3,23,33,10,6]

#Adding an Eliment.
my_list.append(1)

#Removing an Eliment.
my_list.remove(23)

#Modifiying an Eliment.
my_list[2] = 2006

print("Updated List:" , my_list)



#Creating a Set.
my_set = {3,23,33,10,6}

#Adding.
my_set.add(1)

#Removing.
my_set.remove(23)

#Modifiying.
my_set.discard(3)
my_set.add(7)

print("Updated Set:" , my_set)



#Creating a Dictionary.
my_dict = {'Name': 'Gojo', 'Age': 23, 'City': 'Shibuya', 'Domain': 'Unlimited Void'}

#Adding.
my_dict['Gender'] = 'Male'

#Removing,
del my_dict['Domain']

#Modifiying.
my_dict['City'] = 'Tokyo'

print("Updated Dictionary:" , my_dict)
