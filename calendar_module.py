import calendar
import datetime
import time

print(calendar.weekheader(3))
print()
print(calendar.firstweekday())
print()
print(calendar.month(2020, 5))
print(calendar.month(2020, 5, 3, 3))
# Returns a matrix representing a month’s calendar. Each row represents a week; days outside of the month a represented by zeros. Each week begins with Monday unless set by setfirstweekday().
print(calendar.monthcalendar(2020, 5))

print(calendar.calendar(2020))

year_matrix = []
x = 1
while x < 13:
    year_matrix.append(calendar.monthcalendar(2020, x))
    x = x+1


# Returns a 3 dimensional matrix representing a year of matrices of a month’s calendar. Each row is represented by a month and within each month each row represents a week; days outside of the month a represented by zeros. Each week begins with Monday unless set by setfirstweekday().
print(year_matrix)

day_of_the_week = calendar.weekday(2020, 5, 24)
print(day_of_the_week)
is_leap_year = calendar.isleap(2020)
print(is_leap_year)
how_many_leap_days = calendar.leapdays(2020, 2021)
print(how_many_leap_days)
