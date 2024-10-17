
def validAnagram(s,t):
    if len(s) != len(t):
        return False
    elif sorted(s) == sorted(t):
        return True
    return False

print(validAnagram("car","rat"))
