def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))


def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif 90 > grade >= 80:
        return "B"
    elif 80 > grade >= 70:
        return "C"
    elif 70 > grade >= 65:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print( grade_converter(92))

# This should print a "C"
print (grade_converter(70))

# This should print an "F"
print (grade_converter(61))