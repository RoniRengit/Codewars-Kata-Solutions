def high_and_low(numbers):
    tmp = numbers.split(' ')
    tmp = [int(i) for i in tmp]
    tmp.sort()
    print(tmp)
    string = str(tmp.pop()) + ' '
    string += str(tmp.pop(0))
    return string

def high_and_low(numbers):
    tmp = numbers.split(' ')
    tmp = [int(i) for i in tmp]
    tmp = str(min(tmp)) + ' ' +  str(max(tmp))
    return tmp

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))