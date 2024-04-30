# parameter passed is string
# return int

def romanToInt(s):
    my_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    int_value = 0
    prev = 0
    for i in s[::-1]: #reverse the string
        value = my_dict[i]
        if value < prev:
            int_value -= value
        else:
            int_value += value
        prev = value

    return int_value
            

# print(ord('V'))
# print(ord('I'))


print(romanToInt("XV"))
# s = "python"
# print(s[1])