def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False
  
def is_int(x):
  if int(x) == float(x) and x == int(x):
    return True
  else:
    return False

'''Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number’s digits. For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4. 
(Assume that the number you are given will always be positive.)'''
def digit_sum(n):
  a = str(n)
  total = 0
  for num in a:
    total += int(num)
  return total

# calculate the factorial of a +ve number
def factorial(x):
  count = x
  total = 1
  while count > 0:
    total *= count
    count -= 1
  return total

# check if a number is prime
def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

'''Define a function called reverse that takes a string textand returns that string in reverse. 
For example: reverse("abcd") should return "dcba".
You may not use reversed or [::-1] to help you with this.
You may get a string containing special characters (for example, !, @, or #).
'''
def reverse(text):
  count = len(text) -1
  rev_list = []
  for char in text:
    rev_list.append(text[count])
    count -= 1
  rev_str = ''.join(rev_list)
  return rev_str

# remove vowels from a string
def anti_vowel(text):
  vowels = ['a','A','e','E','i','I','O','o','u','U']
  new_list = []
  for char in text:
    if char in vowels:
      continue
    else:
      new_list.append(char)
  result = ''.join(new_list)
  return result

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def scrabble_score(word):
  total = 0
  for char in word:
    total += score[char.lower()]
  return total


# censor a word in a string
def censor(text, word):
  lst = []
  lngth = len(word)
  wrd_list = text.split()
  for wrd in wrd_list:
    if word == wrd:
      lst.append('*' * lngth)
    else:
      lst.append(wrd)
  return ' '.join(lst)

# count the number of times an item appears in a list
def count(sequence, item):
  total = 0
  for i in sequence:
      if i == item:
        total += 1
  return total

# remove odd numbers from a list
def purify(lst):
  result = []
  for i in lst:
    if i % 2 == 0:
      result.append(i)
  return result 

def remove_duplicates(lst):
  result = []
  for i in lst:
    if i in result:
      continue
    else:
      result.append(i)
  return result

def median(lst):
  lst.sort()
  if len(lst) % 2 == 0:
    return (lst[len(lst)/2] + lst[len(lst)/2 - 1]) / 2.0
  else:
    return lst[len(lst)/2]