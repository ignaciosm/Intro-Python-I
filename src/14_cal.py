"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

print(sys.argv)
args = []

if len(sys.argv) > 2:
  args.append(int(sys.argv[2]))
else: 
  args.append(datetime.today().year)


if len(sys.argv) > 1:
  args.append(int(sys.argv[1]))
else:
  args.append(datetime.today().month)

# If more than 2 extra args given, print warning and exit
if len(sys.argv) > 3:
    print('Too many arguments. 14_cal.py expects either to be called with no arguments, \n\
    with a numeric month, or with a numeric month followed by a year')
    sys.exit()

# if 2 additional arguments passed in, set year to year argument
if len(args) == 2:
    year = args[0]

# if at least 1 additional argument passed in, set month to month argument
if len(args) > 1:
    month = int(args[1])

# initialize calendar and print month
c = calendar.TextCalendar(calendar.SUNDAY)

c.prmonth(theyear=year, themonth=month)