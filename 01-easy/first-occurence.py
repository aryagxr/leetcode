# problem 28

# Given two strings needle and haystack, 
# return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.


def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    else:
        for i in range(len(haystack)-len(needle)+1):
            if needle == haystack[i:i+len(needle)]:
                print(i)
                return i
         

strStr("butsad","sad")