suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = suitcase[2:4] 

# The last two items (index four and five)
last =  suitcase[4:6]


animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index('duck') # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, 'cobra')

print (animals )# Observe what prints after the insert operation


'''
Instructions: Write a for-loop that iterates over start_list and .append()s each number squared (x ** 2) to square_list.

Then sort square_list
'''
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number ** 2)

square_list.sort()

# remove dagger
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')


print (square_list)

''' Instructions:
Add a key to inventory called 'pocket'

Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'

.sort() the items in the list stored under the 'backpack' key

Then .remove('dagger') from the list of items stored under the 'backpack' key

Add 50 to the number stored under the 'gold' key

'''

inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry','lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50