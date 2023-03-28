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



print (square_list)