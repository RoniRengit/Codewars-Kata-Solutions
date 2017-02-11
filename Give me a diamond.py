"""
Program Name: Give me a Diamond
Author: Roni Rengit

This kata is to practice simple string output. Jamie is a programmer, and James' girlfriend.
She likes diamonds, and wants a diamond string from James.
Since James doesn't know how to make this happen, he needs your help.

Task:

You need to return a string that displays a diamond shape on the screen
using asterisk ("*") characters. Please see provided test cases for exact
output format.

The shape that will be returned from print method resembles a diamond,
where the number provided as input represents the number of *’s printed on
the middle line. The line above and below will be centered and will have 2
less *’s than the middle line. This reduction by 2 *’s for each line continues
until a line with a single * is printed at the top and bottom of the figure.

Return null if input is even number or negative (as it is not possible to
print diamond with even number or negative number).

Please see provided test case(s) for examples.

Python Note

Since print is a reserved word in Python, Python students must implement
the diamond(n) method instead, and return None for invalid input.
"""
##def diamond(n):
##    # Make some diamonds!
##    if n<=1 or n%2 == 0:
##        return None
##    else:
##        middle = n//2 + 1
##        for i in reversed(range(0, middle)):
##            print(i * ' ' + (n - 2 * i) * '*' + '\n', end ='')
##        for i in range(1, middle):
##            print(i * ' ' + (n - 2 * i) * '*' + '\n', end = '')

def diamond(n):
    # Make some diamonds!
    if n<=1 or n%2 == 0:
        return None
    else:
        middle = n//2 + 1
        upper = [(i * ' ' + (n - 2 * i) * '*' + '\n') for i in reversed(range(0, middle))]
        lower = [ (i * ' ' + (n - 2 * i) * '*' + '\n')for i in range(1, middle)]
        return ''.join(upper)+ ''.join(lower)

print(diamond(103))
