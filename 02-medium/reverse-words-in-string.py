# leetcode 75
# Given an input string s, reverse the order of the words.


# initial attempt
def reverseWords(s):
    s = " ".join(s.split())  # Remove extra whitespace
    reversed_string = ""
    j = len(s)
    for i in range(len(s)-1, -1, -1):
        if s[i] == " " and i != 0:
            reversed_string += s[i+1:j]
            reversed_string += " "
            j = i
        elif i == 0:
            reversed_string += s[:j]
    return reversed_string
        

# so much better
def reverseWords2(s):
    s=s.split()
    return " ".join(s[: : -1])


print(reverseWords2("   the     sky  is   blue "))
