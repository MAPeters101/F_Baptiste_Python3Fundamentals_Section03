"""
Exercise 2
Assume you have some variable elapsed that contains elapsed time in seconds.

Create three new variables: hours, minutes and seconds, that represent the
number of hours, minutes and seconds represented by elapsed.

For example, if elapsed = 7835, then hours = 2, minutes = 10 and seconds = 35
"""


elapsed = 7835
hours = elapsed // (60*60)
"""minutes = (elapsed-(hours*60*60)) // 60
#seconds = elapsed % (60*60)
seconds = elapsed - (hours * 60*60 + minutes * 60)
"""
minutes = (elapsed % 3600) // 60
seconds = (elapsed % 3600) % 60



print(f"{elapsed} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")
