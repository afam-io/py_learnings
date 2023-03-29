
import math

# Uses math module sqrt function
print (math.sqrt(25))

def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  # function calling another function
  return one_good_turn(n) + 2



''' Instructions: First, def a function called cube that takes an argument called number. Don’t forget the parentheses and the colon!
Make that function return the cube of that number (i.e. that number multiplied by itself and multiplied by itself once again).
Define a second function called by_three that takes an argument called number.
if that number is divisible by 3, by_three should call cube(number) and return its result. Otherwise, by_three should return False.
Don’t forget that if and else statements need a : at the end of that line!'''

def cube(number):
  return number ** 3

def by_three(number):
  if number % 3 == 0:
      return cube(number)
  else:
      return False      
  
""" Instructions: First, def a function, shut_down, that takes one argument s. Don’t forget the parentheses or the colon!
Then, if the shut_down function receives an s equal to "yes", it should return "Shutting down"
Alternatively, elif s is equal to "no", then the function should return "Shutdown aborted".
Finally, if shut_down gets anything other than those inputs, the function should return "Sorry"""
def shut_down(s):
    if s == 'yes':
      return 'Shutting down'
    elif s == 'no':
      return 'Shutdown aborted'
    else:
      return 'Sorry' 
    

''' Instructions: First, def a function called distance_from_zero, with one argument (choose any argument name you like).
If the type of the argument is either int or float, the function should return the absolute value of the function input.
Otherwise, the function should return "Nope"
'''

def distance_from_zero(n):
  if type(n) == int or type(n) == float:
    return abs(n)
  else:
    return 'Nope'


# Vacation cost functions
def hotel_cost(nights):
  return nights * 140

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost 

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

print( trip_cost('Los Angeles', 5, 600))