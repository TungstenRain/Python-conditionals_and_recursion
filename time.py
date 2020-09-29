"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    Copyright 2015 Allen B. Downey
    License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

    This is to test out the turtle module from Chapter 5: Conditionals and Recursion in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.8.5
"""

import time

# Get the epoch and the current time
epoch = time.time()
current_time = time.ctime()

# Constants
seconds_in_a_day = 24 * 60 * 60
seconds_in_an_hour = 60 * 60
seconds_in_a_minute = 60

# Convert days, hours, minutes, and seconds from the epoch
epoch_days = int(epoch // seconds_in_a_day)
epoch_hours = int((epoch % seconds_in_a_day) // seconds_in_an_hour + 8)
epoch_minutes = int((epoch % seconds_in_a_day) % seconds_in_an_hour // seconds_in_a_minute)
epoch_seconds = (epoch % seconds_in_a_day) % seconds_in_an_hour % seconds_in_a_minute

# Print results
print("The current time is: " + current_time)
print("%s days: %s hours: %s minutes: %s seconds since the epoch" %(str(epoch_days), str(epoch_hours), str(epoch_minutes), str(epoch_seconds)))