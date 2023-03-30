# Challenge to create functions for grading students and loop throught nested lists.

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [ 75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

for student in students:
  print (student['name'])
  print (student['homework'])
  print (student['quizzes'])
  print (student['tests'])


def average(numbers):
  total = float(sum(numbers))
  return total / len(numbers)

# returns weighted average of student scores
def get_average(student):
  homework = average(student['homework'])
  quizzes = average(student['quizzes'])
  tests = average(student['tests'])
  return 0.1 * homework + 0.3 * quizzes + tests * 0.6

# returns letter grades given a number score
def get_letter_grade(score):
  if score >= 90:
    return 'A'
  elif score >= 80:
    return 'B'
  elif score >= 70:
    return 'C'
  elif score >= 60:
    return 'D'
  else:
    return 'F'
  
print( 'lloyds grade was %s' % get_letter_grade(get_average(lloyd)))

# Returns average grade of a list of students
def get_class_average(class_list):
  results = []
  for student in class_list:
    results.append(get_average(student))
  return average(results)


class_average = get_class_average(students)
print ('class average numerical grade was %s' % class_average)
print ('class average numerical grade was %s' % get_letter_grade(class_average))