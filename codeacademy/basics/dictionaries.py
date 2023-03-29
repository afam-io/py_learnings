# Assigning a dictionary with three key-value pairs to residents:
''' Instructions: Print the values stored under the 'Sloth' and 'Burmese Python' keys.
Accessing dictionary values by key is just like accessing list values by index:'''

residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print (residents['Puffin']) # Prints Puffin's room number

# Your code here!
print (residents['Sloth'])
print (residents['Burmese Python'])

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print( menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!
menu['Salad']= 9.50
menu['Salmon Salad'] = 13.50
menu['Pizza'] = 10.00

print( "There are " + str(len(menu)) + " items on the menu.")
print (menu)

'''Instructions: Delete the 'Sloth' and 'Bengal Tiger' items from zoo_animals using del.

Set the value associated with 'Rockhopper Penguin' to anything other than 'Arctic Exhibit'.

'''
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Bengal Tiger']
del zoo_animals['Sloth']
zoo_animals['Rockhopper Penguin'] = 'Open Air Exhibit'



print (zoo_animals)