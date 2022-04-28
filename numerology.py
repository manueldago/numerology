#Imports
from calendar import month
from datetime import datetime, date, timedelta

#Initial values
show_info_in_year = 2022
birthday_year= 1974
birthday_month= 6
birthday_day= 28

#Functions
def calculate_sum_of_digits(n):       
    s = 0
    while n:
        s += n % 10
        n //= 10    
    if ( s > 9):
        return calculate_sum_of_digits(s)
    else:
        return s        

def get_birthday_magic_number(year,month,day):
    final_number = calculate_sum_of_digits(year + month + day)
    return str(final_number)

def my_birthday(year,month,day):
  return int(get_birthday_magic_number(year,month,day))

def get_all_sundays_in_year(year,month,day):
    
   d = date(year, month, day)                    # January 1st
   d += timedelta(days = 6 - d.weekday())  # First Sunday
   while d.year == year:
      yield d
      d += timedelta(days = 7)

def show_header_message():
    print ("******************************************************************************************")
    print ("YOUR NUMBER IS: " + str(my_birthday(birthday_year,birthday_month,birthday_day)))
    print ("******************************************************************************************")

def show_sundays_info(year,my_birthday):
    goodluck_in_year= 0    
    for d in get_all_sundays_in_year(year,1,1):
        final_number =int(get_birthday_magic_number(d.year,d.month,d.day))    
        if (final_number == my_birthday):
            print('\033[94m' + "Sunday " + str(d) + " is magic: YES")
            goodluck_in_year += 1
        else:
            print('\33[37m' +  "Sunday " + str(d) +  " is magic: NOT" )
    return goodluck_in_year;

def show_footer_message(days_with_lucky):
    if (days_with_lucky > 0):
        print ("******************************************************************************************")
        print ("You have ".upper() + str(days_with_lucky) + " days for take your opportunity !!!".upper())
        print ("******************************************************************************************")

def initialize():    
    birthday= my_birthday(birthday_year,birthday_month,birthday_day)
    show_header_message()    
    days_with_lucky= show_sundays_info(show_info_in_year,birthday)
    show_footer_message(days_with_lucky)


#Start script here
initialize()

        
