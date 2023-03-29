names = ["Adam","Alex","Mariah","Martine","Columbus"]
for name in names:
  print (name)

webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for key in webster:
  print( webster[key])
  #Value order not guaranteed.

# print even numbers in a
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
  if number % 2 == 0:
    print (number)

# Function that counts the number of times fizz appears in a list
def fizz_count(x):
  count = 0
  for item in x:
    if item == 'fizz':
      count += 1
  return count

# Shopping market stock function managers perspective
prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

total = 0

for key in prices:
  print( key)
  print ("price: %s" % prices[key])
  print ("stock: %s" % stock[key])

for key in prices:
 value = prices[key] * stock[key]
 print (value)
 total += value

print (total)


# Shopping market stock function customers perspective

shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0: 
      total += prices[item]
      stock[item] -= 1
  return total

