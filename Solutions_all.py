"""
Exercise 1
Given two floats a and b, and some tolerance tol, write an expression that
will test whether a and b are within tol of each other.

We essentially want to make sure that the distance between a and b is bounded
by some tolerance tol.

We can use the abs() function to calculate the absolute value of some value,
so:

abs(a-b)

essentially calculates the distance between a and b.

Our solution is then:

abs(a - b) < tol
a = 0.1 + 0.1 + 0.1
b = 0.3
As we know these two numbers will not compare True:

a == b
False
However, using a tolerance we can see if they are "close enough":

tol = 0.0001
abs(a - b) < tol
True



Exercise 2
Assume you have some variable elapsed that contains elapsed time in seconds.

Create three new variables: hours, minutes and seconds, that represent the
number of hours, minutes and seconds represented by elapsed.

For example, if elapsed = 7835, then hours = 2, minutes = 10 and seconds = 35

We are going to take this step by step first, and later simplify things if we
can.

Let's start with some value for elapsed:

elapsed = 7835
The number of seconds in an hour is 60 * 60.

The number of seconds in a minute is 60.

Given that elapsed is in seconds, we can calculate the number of (whole) hours
in elapsed using integer division:

hours = elapsed // (60 * 60)
print('hours =', hours)
hours = 2
The remaining number of seconds could be calculated this way:

remaining_seconds = elapsed - hours * (60 * 60)
print('remaining_seconds = ', remaining_seconds)
remaining_seconds =  635
But it's actually simpler to use %:

remaining_seconds = elapsed % (60 * 60)
print('remaining_seconds = ', remaining_seconds)
remaining_seconds =  635
Next we need to calculate the number of (whole) minutes in those remaining
seconds:

minutes = remaining_seconds // 60
print('minutes = ', minutes)
minutes =  10
And the remaining number of seconds is now:

seconds = remaining_seconds % 60
print('seconds = ', seconds)
seconds =  35
Let's put everything together and see what we have:

elapsed = 7835
hours = elapsed // (60 * 60)
remaining_seconds = elapsed % (60 * 60)
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(hours, minutes, seconds)
2 10 35
If we wanted to we could get rid of the temporary variable remaining_seconds.

(I call it temporary because once we're done with our calculation we don't
need it anymore - our result is stored in the variables hours, minutes and
seconds)

elapsed = 7835
hours = elapsed // (60 * 60)
minutes = elapsed % (60 * 60) // 60
seconds = elapsed % (60 * 60) % 60

print(hours, minutes, seconds)
2 10 35
Now operator precedence worked for us here, but I don't consider the above
very "safe" or easy to understand how the operations are grouped, so I would
prefer this:

elapsed = 7835
hours = elapsed // (60 * 60)
minutes = (elapsed % (60 * 60)) // 60
seconds = (elapsed % (60 * 60)) % 60

print(hours, minutes, seconds)
2 10 35
One last thing we could do is use 3600 instead of (60 * 60):

elapsed = 7835
hours = elapsed // 3600
minutes = (elapsed % 3600) // 60
seconds = (elapsed % 3600) % 60

print(hours, minutes, seconds, sep=':')
2:10:35
Notice how I specified sep in the print function - by default the separator
used is a space, but here we can override that, so I chose : as the separator
character.

"""