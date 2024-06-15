
def palindromeNumber(x):
    num = str(x)
    reverse_num = ""
    for i in num[::-1]: # reverse it
        reverse_num += i
        print(i)
    if num == reverse_num:
        return True
    else:
        return False
    

print(palindromeNumber(-121))
