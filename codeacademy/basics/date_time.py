from datetime import datetime

now = datetime.now()

# Get current date and time
print (now)

# Get current year
print( now.year )

# Get current month
print (now.month)

# Get current day
print( now.day )

# print today’s date in the format mm/dd/yyyy
print ('%02d-%02d-%04d' % (now.month, now.day, now.year))

# print current time in the format hh:mm:ss
print ('%02d:%02d:%02d' % (now.hour, now.minute, now.second))

# print today’s date, followed by current time, in the format mm/dd/yyyy hh:mm:ss
print ('%02d/%02d/%04d %02d:%02d:%02d ' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
