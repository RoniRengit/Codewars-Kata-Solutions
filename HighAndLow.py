"""
Description:
In this little assignment you are given a string of space separated numbers, 
and have to return the highest and lowest number.
Author: Roni Rengit
"""

# My Final Solution
def high_and_low(numbers):
    """Function to get min and max from list"""
    
    tmp = [int(i) for i in numbers.split(' ')] # Create a list of integers
    return str(max(tmp)) + ' ' +  str(min(tmp))

# Another Solution
def high_and_low(numbers):
    tmp = numbers.split(' ')
    tmp = [int(i) for i in tmp]
    tmp.sort()
    print(tmp)
    string = str(tmp.pop()) + ' '
    string += str(tmp.pop(0))
    return string

# Test Case
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
