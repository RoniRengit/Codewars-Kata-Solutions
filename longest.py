def longest(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    string1= ''
    string2 = ''
    for string in s1:
        string1+= ' ' + string
    for string in s2:
        string2 += ' ' + string
    string = string1 + string2
    string = string.split()
    string.sort()
    value = [ya for ya in set(string)]
    print(''.join(value))


longest("aretheyhere", "yestheyarehere")