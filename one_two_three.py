"""
Description:

There are no explanations. You have to create the code that gives the following results in Python and Ruby:

one_two_three(0) == [0, 0]
one_two_three(1) == [1, 1]
one_two_three(2) == [2, 11]
one_two_three(3) == [3, 111]
one_two_three(19) == [991, 1111111111111111111]

Author: Roni Rengit
"""

def one_two_three(n):
    """String repetition"""

    if n == 0: return [n, n]
    rem = n % 9
    div = (n - rem) // 9
    if len(str(n)) > 1 and rem != 0:
        return [int(div * '9' + str(rem)), int(n * '1')]
    elif len(str(n)) > 1 and rem == 0:
        return [int(div * '9'), int(n * '1')]
    else:
        return [n, int(n * '1')]